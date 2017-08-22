from __future__ import print_function
import re
from copy import deepcopy


from abstract_model import SpecfileClass, BlockTypes, keys_list
from model_methods import create_metastring
from model_2_methods import list_of_blocks


GoSpecfile = SpecfileClass('GO spec')


def reduce_gospecfile():

    reduced_GoSpecfile = deepcopy(GoSpecfile)

    for (block_list, reduced_block_list) in zip(sorted(GoSpecfile.__dict__.iteritems()), sorted(reduced_GoSpecfile.__dict__.iteritems())):
        if block_list[1] is None or block_list[1] == [[]] or block_list[1] == [] or block_list[1] == {} or block_list[1] == '':
            delattr(reduced_GoSpecfile, block_list[0])
        elif isinstance(block_list[1], list):
            for (index, single_record) in reversed(list(enumerate(block_list[1]))):
                if isinstance(single_record, list):
                    if single_record == []:
                        del reduced_block_list[1][index]
                    else:
                        to_be_removed = []
                        for (neco, neco2) in enumerate(single_record):
                            if neco2['block_type'] == BlockTypes.HeaderTagType and re.match(r'(?i)requires', neco2['key']) is not None:
                                reduced_block_list[1][index] = append_dependency(reduced_block_list[1][index], 'runtime', neco2)
                                to_be_removed.append([index, neco])
                            elif neco2['block_type'] == BlockTypes.HeaderTagType and re.match(r'(?i)buildrequires', neco2['key']) is not None:
                                append_dependency(reduced_block_list[1][index], 'buildtime', neco2)
                                to_be_removed.append([index, neco])
                            else:
                                reduced_block_list[1][index][neco] = gospecfile_to_print(neco2)
                        for record in reversed(sorted(to_be_removed)):
                            del reduced_block_list[1][record[0]][record[1]]
                else:
                    if 'block_type' not in single_record:
                        for keyword in single_record:
                            if 'block_type' not in single_record[keyword]:
                                for inner_keyword in single_record[keyword]:
                                    if single_record[keyword][inner_keyword] is not None:
                                        if 'block_type' in single_record[keyword][inner_keyword]:
                                            reduced_block_list[1][index][keyword][inner_keyword] = gospecfile_to_print(block_list[1][index][keyword][inner_keyword])
                            else:
                                print("NOT DICT: " + str(keyword) + " : "  + str(single_record[keyword]))

                    else:
                        if single_record['block_type'] == BlockTypes.HeaderTagType and re.match(r'(?i)requires', single_record['key']) is not None:
                            setattr(reduced_GoSpecfile, reduced_block_list[0], append_dependency(reduced_block_list[1], 'runtime', single_record))
                            del reduced_block_list[1][index]
                        elif single_record['block_type'] == BlockTypes.HeaderTagType and re.match(r'(?i)buildrequires', single_record['key']) is not None:
                            setattr(reduced_GoSpecfile, reduced_block_list[0], append_dependency(reduced_block_list[1], 'buildtime', single_record))
                            del reduced_block_list[1][index]
                                # reduced_block_list[1] = append_dependency(reduced_block_list[1], 'buildtime', single_record)
                                # to_be_removed.append([index, neco])
                        else:
                            reduced_block_list[1][index] = gospecfile_to_print(block_list[1][index])

        elif isinstance(block_list[1], dict):
            if block_list[1] != {}:
                reduced_GoSpecfile.history = gospecfile_to_print(block_list[1])

    return reduced_GoSpecfile


def append_dependency(current_unit, keyword, header_tag):

    if current_unit == []:
        current_unit = {keyword:{'dependencies':[{'name':header_tag['content']}]}}
    else:
        found = False
        for single_record in current_unit:
            if keyword in single_record:
                found = True
                if 'dependencies' in single_record[keyword]:
                    single_record[keyword]['dependencies'].append({'name':header_tag['content']})
                else:
                    single_record[keyword]['dependencies'] = [{'name':header_tag['content']}]

        if found is False:
            current_unit.append({keyword:{'dependencies':[{'name':header_tag['content']}]}})

    return current_unit


def gospecfile_to_print(single_record):

    predicate_list = []

    if 'AP' in single_record and single_record['AP'] != '':
        for single_predicate in single_record['AP']:
            if single_predicate[1] == 1:
                predicate_list.append(single_predicate[0])
            else:
                predicate_list.append('NOT ' + single_predicate[0])

    if single_record['block_type'] == BlockTypes.HeaderTagType:
        if re.match(r'(?i)requires', single_record['key']) is not None:
            GoSpecfile.main_unit = append_dependency(GoSpecfile.main_unit, 'runtime', single_record)
        elif re.match(r'(?i)buildrequires', single_record['key']) is not None:
            GoSpecfile.main_unit = append_dependency(GoSpecfile.main_unit, 'buildtime', single_record)
        else:
            single_record = {single_record['key']:single_record['content']}

    elif single_record['block_type'] == BlockTypes.MacroDefinitionType:
        if 'name' in single_record and 'body' in single_record:
            single_record['name'] = '%' + single_record['name']
            single_record = {single_record['name']:single_record['body']}

    elif single_record['block_type'] == BlockTypes.SectionTagType:
        if 'keyword' in single_record and single_record['keyword'] == 'package':
            single_record = {'name':single_record['subname']}

        elif 'keyword' in single_record and 'content' in single_record:
            if single_record['keyword'] == 'changelog':
                length = len(single_record['content']) - 1
                for idx, single_log in enumerate(single_record['content']):         # TODO reversed???
                    single_record[length - idx] = parse_changelog(single_log)
                    create_metastring(single_record[length - idx], BlockTypes.ChangelogTagType)
                    if 'keyword' in single_record:
                        del single_record['keyword']
                    if 'content' in single_record:
                        del single_record['content']
                single_record['block_type'] = BlockTypes.ChangelogTagType
                single_record = gospecfile_to_print(single_record)

            elif single_record['keyword'] == 'files':
                parsed_record = {}
                if 'subname' in single_record and single_record['subname'] is not None:
                    parsed_record.update({'meta':{'file':single_record['subname']}})
                parsed_record.update({'list':single_record['content']})
                single_record = {'files':parsed_record}

            else:
                if single_record['content'] == '':
                    single_record['content'] = None
                single_record = {single_record['keyword']:single_record['content']}

    elif single_record['block_type'] == BlockTypes.CommentType:
        single_record = single_record['content']

    elif single_record['block_type'] == BlockTypes.ChangelogTagType:
        del single_record['block_type']
        for record_index in single_record:
            for field in keys_list[BlockTypes.ChangelogTagType]:
                if field in single_record[record_index] and single_record[record_index][field] == '':
                    single_record[record_index][field] = None
                # else:
                #     single_record[record_index][field] = single_record[record_index][field]

    if predicate_list != []:
        if isinstance(single_record, dict):
            single_record.update({'condition':predicate_list})
        elif isinstance(single_record, unicode):
            single_record = (single_record, {'condition':predicate_list})

    return single_record


def replace_field_number(prev_section_count, replacing):

    to_be_replaced_list = re.findall(r'#' + str(replacing[0]), GoSpecfile.metastring)
    for replace_record in to_be_replaced_list:
        GoSpecfile.metastring = GoSpecfile.metastring.replace(replace_record, '#!' + str(replacing[1]) + str(prev_section_count))


def parse_changelog(changelog):

    parsed_changelog = {}
    first_line = changelog[:changelog.find('\n')+1]

    parsed_changelog['comment'] = changelog[changelog.find('\n')+1:]
    parsed_changelog['date'] = first_line[first_line.find('*')+1:first_line.find('20')+4]
    parsed_changelog['mark'] = re.findall(r'\s+\-\s[\s\S]*', first_line)
    if parsed_changelog['mark'] == []:
        parsed_changelog['mark'] = re.findall(r'[\d\.\s-]*', first_line)
        if parsed_changelog['mark'] == []:
            parsed_changelog['mark'] = ''
        else:
            parsed_changelog['mark'] = parsed_changelog['mark'][-2]
    else:
        parsed_changelog['mark'] = parsed_changelog['mark'][0]

    parsed_changelog['author'] = first_line[first_line.find(parsed_changelog['date'])+(len(parsed_changelog['date'])):first_line.rfind(parsed_changelog['mark'])]

    return parsed_changelog



def process_unit_list():

    used_unit_names = []

    for single_record in GoSpecfile.unit_list:
        for keyword in ['subname', 'name']:
            if keyword in single_record and single_record[keyword] != None:
                if single_record[keyword] not in used_unit_names:
                    used_unit_names.append(single_record[keyword])

    if used_unit_names == []:
        return

    processed_unit_list = []
    for _ in range(len(used_unit_names) + 1):
        processed_unit_list.append([])

    for single_record in GoSpecfile.unit_list:
        if 'subname' in single_record and single_record['subname'] != None:
            processed_unit_list[used_unit_names.index(single_record['subname']) + 1].append(single_record)
        elif 'name' in single_record and single_record['name'] != None:
            processed_unit_list[used_unit_names.index(single_record['name']) + 1].append(single_record)
        elif 'package' in single_record and single_record['package'] != None:
            processed_unit_list[used_unit_names.index(single_record['package']) + 1].append(single_record)
        elif single_record['block_type'] != BlockTypes.HeaderTagType:
            processed_unit_list[0].append(single_record)

    GoSpecfile.unit_list = processed_unit_list

    return


def create_go_spec_model(Specfile2):

    GoSpecfile.metastring = Specfile2.metastring

    prev_section_count = 0

    if Specfile2.HeaderTags:
        for index, header_tag in enumerate(list_of_blocks[0]):
            if 'package' not in header_tag or header_tag['package'] == '':
                if re.match(r'(?i)requires', header_tag['key']) is not None:
                    GoSpecfile.main_unit.append(header_tag)
                    replace_field_number(prev_section_count, ["0" + str(index), 1])
                    prev_section_count += 1

                elif re.match(r'(?i)buildrequires', header_tag['key']) is not None:
                    replace_field_number(prev_section_count, ["0" + str(index), 1])
                    prev_section_count += 1
                    GoSpecfile.main_unit.append(header_tag)

                # elif re.match(r'(?i)excludearch', header_tag['key']) is not None:     # TODO
                #     replace_field_number(prev_section_count, ["0" + str(index), 1])
                #     prev_section_count += 1
                #     GoSpecfile.main_unit.append(header_tag)

                elif 'AP' not in header_tag or header_tag['AP'] == '':
                    GoSpecfile.metadata.append(header_tag)
            else:
                GoSpecfile.unit_list.append(header_tag)

    if Specfile2.MacroDefinitions:
        for index, macro_definition in enumerate(list_of_blocks[2]):
            # if 'AP' not in macro_definition or macro_definition['AP'] == '':
            GoSpecfile.metadata.append(macro_definition)
            replace_field_number(len(GoSpecfile.metadata) - 1, ["2" + str(index), 0])
            # else:           # TODO
            #     GoSpecfile.metadata.append(macro_definition)
            #     replace_field_number(len(GoSpecfile.metadata) - 1, ["2" + str(index), 0])

    if Specfile2.SectionTags:
        # to_be_removed = []
        for index, single_section in enumerate(Specfile2.SectionTags):
            if single_section['keyword'] == 'changelog':
                GoSpecfile.history = single_section
                replace_field_number(0, ["1" + str(index), 3])

            elif single_section['keyword'] == 'package':
                GoSpecfile.unit_list.append(single_section)
                # crop the part of metastring describing fields inside package section
                # [3:-4] - remove identification of the package section
                # split('#')[1:] - divide inner sections, remove the first describing only package section itself

                # inner_sections = re.search(r'#1' + str(int(len(GoSpecfile.unit_list) - 1)) + r'%[\s\S]*#1' + str(int(len(GoSpecfile.unit_list) - 1)) + r'%', GoSpecfile.metastring)
                # if inner_sections is not None:
                #     inner_sections = inner_sections.group()
                #     inner_sections = inner_sections.replace('!', '')
                #     if '#' in inner_sections:
                #         inner_sections = inner_sections[3:-4].split('#')[1:]

                # if inner_sections is not None:
                #     for single_inner_section in reversed(inner_sections):
                #         if single_inner_section != '':
                #             if len(list_of_blocks[int(single_inner_section[0])]) > int(single_inner_section[1:single_inner_section.find('%')]):
                #                 if list_of_blocks[int(single_inner_section[0])][int(single_inner_section[1:single_inner_section.find('%')])]['block_type'] == BlockTypes.HeaderTagType:
                #                     list_of_blocks[int(single_inner_section[0])][int(single_inner_section[1:single_inner_section.find('%')])]['name'] = single_section['subname']
                #                     GoSpecfile.unit_list.append(list_of_blocks[int(single_inner_section[0])][int(single_inner_section[1:single_inner_section.find('%')])])
                #             to_be_removed.append([int(single_inner_section[0]), int(single_inner_section[1:single_inner_section.find('%')])])

            elif ('name' in single_section and single_section['name'] is not None) \
            or ('subname' in single_section and single_section['subname'] is not None \
            and 'parameters' in single_section and 'n' in single_section['parameters']): # TODO subname?
                GoSpecfile.unit_list.append(single_section)

            elif 'AP' not in single_section or single_section['AP'] == '':
                GoSpecfile.main_unit.append(single_section)
                replace_field_number(prev_section_count, ["1" + str(index), 1])
            prev_section_count += 1

        # for record in reversed(sorted(to_be_removed)):
        #     if record[0] == 0:
        #         del GoSpecfile.metadata[record[1]]
        #     else:
        #         print(record)
        #         print(str(GoSpecfile.main_unit))
        #         del GoSpecfile.main_unit[record[1]]

    if Specfile2.Comments:
        for index in range(len(Specfile2.Comments)):
            replace_field_number(index, [str(5) + str(index), 4])
        prev_section_count += len(Specfile2.Comments)
        GoSpecfile.comments = Specfile2.Comments

    # if Specfile2.MacroConditions:   # TODO + parse content
    #     print(str(Specfile2.MacroConditions))

    process_unit_list()
    GoSpecfile.metastring = GoSpecfile.metastring.replace('#!', '#')
