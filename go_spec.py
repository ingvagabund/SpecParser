from __future__ import print_function
import re
from copy import deepcopy
import json


from abstract_model import SpecfileClass, BlockTypes, keys_list
from metastring import Metastring
from model_2_methods import list_of_blocks


GoSpecfile = SpecfileClass('GO spec')
Specfile2_from_GoSpec = SpecfileClass('Specfile 2.0')
ExcludeArch = []
PredicateList = []


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
                        for (single_field_index, single_field) in enumerate(single_record):
                            if single_field['block_type'] == BlockTypes.HeaderTagType and re.match(r'(?i)requires', single_field['key']) is not None:
                                reduced_block_list[1][index] = append_dependency(reduced_block_list[1][index], 'runtime', single_field)
                                to_be_removed.append([index, single_field_index])
                            elif single_field['block_type'] == BlockTypes.HeaderTagType and re.match(r'(?i)buildrequires', single_field['key']) is not None:
                                append_dependency(reduced_block_list[1][index], 'buildtime', single_field)
                                to_be_removed.append([index, single_field_index])
                            elif single_field['block_type'] == BlockTypes.HeaderTagType and re.match(r'(?i)excludearch', single_field['key']) is not None:
                                append_dependency(reduced_block_list[1], 'excludearch', single_field)
                                to_be_removed.append([index, single_field_index])
                            else:
                                reduced_block_list[1][index][single_field_index] = gospecfile_to_print(single_field)
                                
                        for record in reversed(sorted(to_be_removed)):
                            del reduced_block_list[1][record[0]][record[1]]
                            if reduced_block_list[1][record[0]] == []:
                                del reduced_block_list[1][record[0]]
                else:
                    if 'block_type' not in single_record:
                        for keyword in single_record:
                            if 'block_type' not in single_record[keyword]:
                                for inner_keyword in single_record[keyword]:
                                    if single_record[keyword][inner_keyword] is not None:
                                        if 'block_type' in single_record[keyword][inner_keyword]:
                                            reduced_block_list[1][index][keyword][inner_keyword] = gospecfile_to_print(block_list[1][index][keyword][inner_keyword])

                    else:
                        if single_record['block_type'] == BlockTypes.HeaderTagType and re.match(r'(?i)requires', single_record['key']) is not None:
                            setattr(reduced_GoSpecfile, reduced_block_list[0], append_dependency(reduced_block_list[1], 'runtime', single_record))
                            del reduced_block_list[1][index]
                        elif single_record['block_type'] == BlockTypes.HeaderTagType and re.match(r'(?i)buildrequires', single_record['key']) is not None:
                            setattr(reduced_GoSpecfile, reduced_block_list[0], append_dependency(reduced_block_list[1], 'buildtime', single_record))
                            del reduced_block_list[1][index]
                        elif single_record['block_type'] == BlockTypes.HeaderTagType and re.match(r'(?i)excludearch', single_record['key']) is not None:
                            setattr(reduced_GoSpecfile, reduced_block_list[0], append_dependency(reduced_block_list[1], 'excludearch', single_record))
                            del reduced_block_list[1][index]
                        else:
                            reduced_block_list[1][index] = gospecfile_to_print(block_list[1][index])

        elif isinstance(block_list[1], dict):
            if block_list[1] != {}:
                reduced_GoSpecfile.history = gospecfile_to_print(block_list[1])

    return reduced_GoSpecfile


def append_dependency(current_unit, keyword, header_tag):

    if current_unit == []:
        if keyword == 'excludearch':
            current_unit = {keyword:[header_tag['content']]}
        else:        
            current_unit = {keyword:{'dependencies':[{'name':header_tag['content']}]}}
    else:
        found = False
        for single_record in current_unit:
            if keyword in single_record:
                found = True
                if keyword == 'excludearch':
                    single_record[keyword].append(header_tag['content'])
                else:
                    if 'dependencies' in single_record[keyword]:
                        single_record[keyword]['dependencies'].append({'name':header_tag['content']})
                    else:
                        single_record[keyword]['dependencies'] = [{'name':header_tag['content']}]

        if found is False:
            if keyword == 'excludearch':
                current_unit.append({keyword:[header_tag['content']]})
            else:
                current_unit.append({keyword:{'dependencies':[{'name':header_tag['content']}]}})

    return current_unit


def gospecfile_to_print(single_record):

    predicate_list = []

    if 'AP' in single_record and single_record['AP'] != '':
        for single_predicate in single_record['AP']:
            single_condition = ''
            if single_predicate[2] != None:
                single_condition += single_predicate[2] + ' '
            if single_predicate[1] == 0:
                single_condition += 'NOT '
            predicate_list.append(single_condition + single_predicate[0])

    if single_record['block_type'] == BlockTypes.HeaderTagType:
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
                for idx, single_log in enumerate(single_record['content']):
                    single_record[length - idx] = parse_changelog(single_log)
                    Metastring.create_metastring(single_record[length - idx], BlockTypes.ChangelogTagType)
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

    if predicate_list != []:
        if isinstance(single_record, dict):
            single_record.update({'condition':predicate_list})
        elif isinstance(single_record, unicode):
            single_record = (single_record, {'condition':predicate_list})

    return single_record


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

    for index, single_record in enumerate(GoSpecfile.unit_list):
        if 'subname' in single_record and single_record['subname'] != None:
            GoSpecfile.metastring = Metastring.change_metastring(GoSpecfile.metastring, index, len(processed_unit_list[used_unit_names.index(single_record['subname']) + 1]), used_unit_names.index(single_record['subname']) + 1)
            processed_unit_list[used_unit_names.index(single_record['subname']) + 1].append(single_record)
        elif 'name' in single_record and single_record['name'] != None:
            GoSpecfile.metastring = Metastring.change_metastring(GoSpecfile.metastring, index, len(processed_unit_list[used_unit_names.index(single_record['name']) + 1]), used_unit_names.index(single_record['name']) + 1)
            processed_unit_list[used_unit_names.index(single_record['name']) + 1].append(single_record)
        elif 'package' in single_record and single_record['package'] != None:
            GoSpecfile.metastring = Metastring.change_metastring(GoSpecfile.metastring, index, len(processed_unit_list[used_unit_names.index(single_record['package']) + 1]), used_unit_names.index(single_record['package']) + 1)
            processed_unit_list[used_unit_names.index(single_record['package']) + 1].append(single_record)
        elif single_record['block_type'] != BlockTypes.HeaderTagType:
            GoSpecfile.metastring = Metastring.change_metastring(GoSpecfile.metastring, index, len(processed_unit_list[0]), 0)
            processed_unit_list[0].append(single_record)

    GoSpecfile.unit_list = processed_unit_list

    return


def add_excludearch_tags():

    if GoSpecfile.unit_list != []:
        for single_unit in GoSpecfile.unit_list:
            single_unit.append(ExcludeArch[0:])
    else:
        for excludearch_tag in ExcludeArch:
            GoSpecfile.main_unit = GoSpecfile.main_unit[:excludearch_tag[0]] + [excludearch_tag[1]] + GoSpecfile.main_unit[excludearch_tag[0]:]



def create_go_spec_model(Specfile2_json_representation):

    global Specfile2
    global ExcludeArch

    Specfile2 = json.loads(Specfile2_json_representation)
    GoSpecfile.metastring = Specfile2['metastring']

    prev_section_count = 0

    if 'HeaderTags' in Specfile2:
        for index, header_tag in enumerate(list_of_blocks[0]):
            if 'package' not in header_tag or header_tag['package'] == '':
                if re.match(r'(?i)excludearch', header_tag['key']) is not None or \
                    re.match(r'(?i)requires', header_tag['key']) is not None or \
                    re.match(r'(?i)buildrequires', header_tag['key']) is not None:
                    GoSpecfile.main_unit.append(header_tag)
                    GoSpecfile.metastring = Metastring.replace_field_number(GoSpecfile.metastring, str(prev_section_count) + '[' + str(index) + ']', ['0' + str(index), 1])
                    prev_section_count += 1

                elif 'AP' not in header_tag or header_tag['AP'] == '':
                    GoSpecfile.metadata.append(header_tag)

                    to_be_replaced_list = re.findall(r'#' + str('0' + str(index)) + '%', GoSpecfile.metastring)
                    for replace_record in to_be_replaced_list:
                        GoSpecfile.metastring = GoSpecfile.metastring.replace(replace_record, '#!' + str('0' + str(len(GoSpecfile.metadata) - 1) + '[' + str(index) + ']') + '%')
            else:
                GoSpecfile.unit_list.append(header_tag)

                to_be_replaced_list = re.findall(r'#' + str('0' + str(index)) + '%', GoSpecfile.metastring)
                for replace_record in to_be_replaced_list:
                    GoSpecfile.metastring = GoSpecfile.metastring.replace(replace_record, '#!' + str('2' + str(len(GoSpecfile.unit_list) - 1) + '[' + str(index) + ']') + '%')

    if 'MacroDefinitions' in Specfile2:
        for index, macro_definition in enumerate(list_of_blocks[2]):
            GoSpecfile.metadata.append(macro_definition)
            GoSpecfile.metastring = Metastring.replace_field_number(GoSpecfile.metastring, len(GoSpecfile.metadata) - 1, ['2' + str(index), 0])

    if 'SectionTags' in Specfile2:
        for index, single_section in enumerate(Specfile2['SectionTags']):
            if single_section['keyword'] == 'changelog':
                GoSpecfile.history = single_section
                GoSpecfile.metastring = Metastring.replace_field_number(GoSpecfile.metastring, 0, ['1' + str(index), 3])

            elif single_section['keyword'] == 'package':
                GoSpecfile.unit_list.append(single_section)

                to_be_replaced_list = re.findall(r'#' + str('1' + str(index)) + '%', GoSpecfile.metastring)
                for replace_record in to_be_replaced_list:
                    GoSpecfile.metastring = GoSpecfile.metastring.replace(replace_record, '#!' + str('2' + str(len(GoSpecfile.unit_list) - 1) + '[' + str(index) + ']') + '%')

            elif single_section['keyword'] == 'files' and 'name' in single_section and single_section['name'] != '' and single_section['name'] != None:
                GoSpecfile.unit_list.append(single_section)

                to_be_replaced_list = re.findall(r'#' + str('1' + str(index)) + '%', GoSpecfile.metastring)
                for replace_record in to_be_replaced_list:
                    GoSpecfile.metastring = GoSpecfile.metastring.replace(replace_record, '#!' + str('2' + str(len(GoSpecfile.unit_list) - 1) + '[' + str(index) + ']') + '%')

            elif ('name' in single_section and single_section['name'] is not None) \
            or ('subname' in single_section and single_section['subname'] is not None
            and 'parameters' in single_section and 'n' in single_section['parameters']): # TODO subname?
                GoSpecfile.unit_list.append(single_section)

                to_be_replaced_list = re.findall(r'#' + str('1' + str(index)) + '%', GoSpecfile.metastring)
                for replace_record in to_be_replaced_list:
                    GoSpecfile.metastring = GoSpecfile.metastring.replace(replace_record, '#!' + str('2' + str(len(GoSpecfile.unit_list) - 1) + '[' + str(index) + ']') + '%')

            elif 'subname' in single_section and single_section['subname'] is not None:
                GoSpecfile.main_unit.append(single_section)

                to_be_replaced_list = re.findall(r'#' + str('1' + str(index)) + '%', GoSpecfile.metastring)
                for replace_record in to_be_replaced_list:
                    GoSpecfile.metastring = GoSpecfile.metastring.replace(replace_record, '#!' + str('1' + str(len(GoSpecfile.main_unit) - 1) + '[' + str(index) + ']') + '%')

            elif 'AP' not in single_section or single_section['AP'] == '':
                GoSpecfile.main_unit.append(single_section)
                to_be_replaced_list = re.findall(r'#' + str('1' + str(index)) + '%', GoSpecfile.metastring)
                for replace_record in to_be_replaced_list:
                    GoSpecfile.metastring = GoSpecfile.metastring.replace(replace_record, '#!' + str('1' + str(len(GoSpecfile.main_unit) - 1) + '[' + str(index) + ']') + '%')
            prev_section_count += 1

    if 'Comments' in Specfile2:
        for index in range(len(Specfile2['Comments'])):
            GoSpecfile.metastring = Metastring.replace_field_number(GoSpecfile.metastring, index, [str(5) + str(index), 4])
        prev_section_count += len(Specfile2['Comments'])
        GoSpecfile.comments = Specfile2['Comments']

    if 'MacroConditions' in Specfile2:
        for index in range(len(Specfile2['MacroConditions'])):
            GoSpecfile.metastring = Metastring.replace_field_number(GoSpecfile.metastring, index, [str(3) + str(index), str(7)])
    
    process_unit_list()
    if ExcludeArch != []:
        add_excludearch_tags()
    GoSpecfile.metastring = GoSpecfile.metastring.replace('#!', '#')


def add_section_to_position(position, section_record):

    global Specfile2_from_GoSpec

    if len(Specfile2_from_GoSpec.SectionTags) > position:
        Specfile2_from_GoSpec.SectionTags[position] = section_record
        return
    if len(Specfile2_from_GoSpec.SectionTags) < position:
        for _ in range(position - len(Specfile2_from_GoSpec.SectionTags)):
            Specfile2_from_GoSpec.SectionTags.append('')
    Specfile2_from_GoSpec.SectionTags.append(section_record)


def process_single_record(metarecord, attribute, index, pos_in_unit):

    global Specfile2_from_GoSpec, PredicateList

    if not isinstance(metarecord, list):
        if metarecord['block_type'] == 0:
            if attribute == 'metadata':
                pattern = r'#0' + str(index) + '\[\d+\]'
            elif attribute == 'main_unit':
                pattern = r'#1' + str(index) + '\[\d+\]'
            else:
                pattern = r'#2<' + str(index) + '>' + str(pos_in_unit) + '\[\d+\]'
            
            condition_position = Metastring.check_for_conditions(Specfile2_from_GoSpec.metastring, pattern)
            if condition_position != None and condition_position != -1:
                PredicateList[condition_position] = metarecord['AP']
            elif condition_position != None and condition_position == -1:
                PredicateList.append(metarecord['AP'])

            metastring_id = re.search(pattern, Specfile2_from_GoSpec.metastring).group()
            former_field_id = int(metastring_id[metastring_id.find('[') + 1:-1])
            Specfile2_from_GoSpec.HeaderTags = Specfile2_from_GoSpec.HeaderTags[:former_field_id] + [metarecord] + Specfile2_from_GoSpec.HeaderTags[former_field_id:]
            Specfile2_from_GoSpec.metastring = Specfile2_from_GoSpec.metastring.replace(metastring_id, '#!0' + str(former_field_id))

            if attribute == 'main_unit':
                to_be_replaced = re.findall(r'#1\d+%', Specfile2_from_GoSpec.metastring)
                for single_replace in sorted(to_be_replaced):
                    Specfile2_from_GoSpec.metastring = re.sub(single_replace, r'#1' + str(int(single_replace[2:-1]) - 1) + '%', Specfile2_from_GoSpec.metastring)

        elif metarecord['block_type'] == 1:
            if ('keyword' in metarecord and metarecord['keyword'] == 'package') or ('package' in metarecord \
            and metarecord['package'] != None) or ('subname' in metarecord and metarecord['subname'] != None \
            and ('parameters' not in metarecord or 'n' in metarecord['parameters'])) \
            or ('name' in metarecord and metarecord['name'] != None):
                condition_position = Metastring.check_for_conditions(Specfile2_from_GoSpec.metastring, r'#2<' + str(index) + '>' + str(pos_in_unit) + '\[\d+\]')
                if condition_position != None and condition_position != -1:
                    PredicateList[condition_position] = metarecord['AP']
                elif condition_position != None and condition_position == -1:
                    PredicateList.append(metarecord['AP'])
                package_section_id = re.search(r'#2<' + str(index) + '>' + str(pos_in_unit) + '\[\d+\]', Specfile2_from_GoSpec.metastring).group()
                former_field_id = int(package_section_id[package_section_id.find('[') + 1:-1])
                Specfile2_from_GoSpec.metastring = Specfile2_from_GoSpec.metastring.replace(package_section_id, '#!1' + package_section_id[package_section_id.find('[') + 1:-1])
                add_section_to_position(former_field_id, metarecord)
            elif 'subname' in metarecord and metarecord['subname'] != None:
                condition_position = Metastring.check_for_conditions(Specfile2_from_GoSpec.metastring, r'#1' + str(index) + r'\[\d+\]')
                if condition_position != None and condition_position != -1:
                    PredicateList[condition_position] = metarecord['AP']
                elif condition_position != None and condition_position == -1:
                    PredicateList.append(metarecord['AP'])                
                main_unit_section_id = re.search(r'#1' + str(index) + r'\[\d+\]', Specfile2_from_GoSpec.metastring).group()
                former_section_id = int(main_unit_section_id[main_unit_section_id.find('[') + 1:-1])
                Specfile2_from_GoSpec.metastring = Specfile2_from_GoSpec.metastring.replace(main_unit_section_id, '#!1' + main_unit_section_id[main_unit_section_id.find('[') + 1:-1])
                add_section_to_position(former_section_id, metarecord)
            elif 'keyword' in metarecord and metarecord['keyword'] == 'changelog':
                condition_position = Metastring.check_for_conditions(Specfile2_from_GoSpec.metastring, '#30')
                if condition_position != None and condition_position != -1:
                    PredicateList[condition_position] = metarecord['AP']
                elif condition_position != None and condition_position == -1:
                    PredicateList.append(metarecord['AP'])                
                Specfile2_from_GoSpec.SectionTags.append(metarecord)
                Specfile2_from_GoSpec.metastring = Specfile2_from_GoSpec.metastring.replace('#30', '#!1' + str(len(Specfile2_from_GoSpec.SectionTags) - 1))
            else:
                condition_position = Metastring.check_for_conditions(Specfile2_from_GoSpec.metastring, r'#1' + str(index) + r'\[\d+\]')
                if condition_position != None and condition_position != -1:
                    PredicateList[condition_position] = metarecord['AP']
                elif condition_position != None and condition_position == -1:
                    PredicateList.append(metarecord['AP'])                
                section_id = re.search(r'#1' + str(index) + r'\[\d+\]', Specfile2_from_GoSpec.metastring).group()
                former_section_id = int(section_id[section_id.find('[') + 1:-1])
                add_section_to_position(former_section_id, metarecord)
                Specfile2_from_GoSpec.metastring = Specfile2_from_GoSpec.metastring.replace(section_id, '#!1' + section_id[section_id.find('[') + 1:-1])

        elif metarecord['block_type'] == 2:
            Specfile2_from_GoSpec.MacroDefinitions.append(metarecord)
            index = len(Specfile2_from_GoSpec.HeaderTags) + len(Specfile2_from_GoSpec.MacroDefinitions) - 1
            condition_position = Metastring.check_for_conditions(Specfile2_from_GoSpec.metastring, r'#0' + str(index))
            if condition_position != None and condition_position != -1:
                PredicateList[condition_position] = metarecord['AP']
            elif condition_position != None and condition_position == -1:
                PredicateList.append(metarecord['AP'])
            Specfile2_from_GoSpec.metastring = re.sub(r'#0' + str(index), r'#!2' + str(index - len(Specfile2_from_GoSpec.HeaderTags)), Specfile2_from_GoSpec.metastring)
                
        elif metarecord['block_type'] == 5:
            condition_position = Metastring.check_for_conditions(Specfile2_from_GoSpec.metastring, r'#5' + str(index))
            if condition_position != None and condition_position != -1:
                PredicateList[condition_position] = metarecord['AP']
            elif condition_position != None and condition_position == -1:
                PredicateList.append(metarecord['AP'])
            Specfile2_from_GoSpec.Comments.append(metarecord)

    else:
        for offset, unit_field in enumerate(metarecord):
            process_single_record(unit_field, attribute, index, offset)



def get_existing_condition_position(wanted_expression):

    global Specfile2_from_GoSpec

    for index, single_condition in enumerate(Specfile2_from_GoSpec.Conditions):
        if single_condition['expression'] == wanted_expression:
            return index



def add_packages_to_conditions():

    global Specfile2_from_GoSpec

    for section_index in range(len(Specfile2_from_GoSpec.SectionTags)):
        section_index_metastring = Specfile2_from_GoSpec.metastring[Specfile2_from_GoSpec.metastring.find(r'#1' + str(section_index) + '%0'):Specfile2_from_GoSpec.metastring.rfind(r'#1' + str(section_index) + '%4')]
        if section_index_metastring != '' and \
        Specfile2_from_GoSpec.SectionTags[int(section_index_metastring[2:int(section_index_metastring.find('%'))])]['keyword'] == 'package':
            condition_records_list = re.findall(r'#6\d+\%0', section_index_metastring)
            for single_condition_record in condition_records_list:
                Specfile2_from_GoSpec.Conditions[int(single_condition_record[2:single_condition_record.find('%')])]['package'] = Specfile2_from_GoSpec.SectionTags[int(section_index_metastring[2:int(section_index_metastring.find('%'))])]['subname']



def recreate_conditions():

    global Specfile2_from_GoSpec

    used_conditions = []

    for single_predicate in PredicateList:
        if single_predicate == '':
            break
        
        single_condition = {}

        if len(single_predicate) > 1:
            single_condition['AP'] = single_predicate[:-1]
            single_predicate = [single_predicate[-1]]

        if single_predicate[0][2] != None:
            if int(single_predicate[0][1]) == 0:
                index = get_existing_condition_position(single_predicate[0][0])
                Specfile2_from_GoSpec.Conditions[index]['else_keyword'] = 'else'
            else:
                single_condition['block_type'] = BlockTypes.ConditionType
                single_condition['else_keyword'] = None
                single_condition['end_keyword'] = 'endif'
                single_condition['keyword'] = single_predicate[0][2]
                single_condition['expression'] = single_predicate[0][0]
                Specfile2_from_GoSpec.Conditions.append(single_condition)

        else:
            single_condition['block_type'] = BlockTypes.MacroConditionType
            single_condition['name'] = single_predicate[0][0]
            single_condition['ending'] = ''
            if (single_predicate[0][1]) == 0:
                single_condition['condition'] = '!?'
            else:
                single_condition['condition'] = '?'
            Specfile2_from_GoSpec.MacroConditions.append(single_condition)
            Specfile2_from_GoSpec.metastring = Specfile2_from_GoSpec.metastring.replace('#7', '#3')

    add_packages_to_conditions()


def init_PredicateList():

    global PredicateList

    condition_list = re.findall(r'#6[^%]*?%0', GoSpecfile.metastring)
    for _ in condition_list:
        PredicateList.append('')


def transform_gospec_to_spec2(go_specfile):

    global PredicateList

    GoSpecfile = json.loads(go_specfile)

    init_PredicateList()
    Specfile2_from_GoSpec.metastring = GoSpecfile['metastring']
    Specfile2_from_GoSpec.metastring = Specfile2_from_GoSpec.metastring.replace('#4', '#5')

    for attribute in ['metadata', 'main_unit', 'unit_list', 'history', 'comments']:
        if isinstance(GoSpecfile[attribute], list) and GoSpecfile[attribute] != []:
            for index, single_field in enumerate(GoSpecfile[attribute]):
                process_single_record(single_field, attribute, index, None)

        elif isinstance(GoSpecfile[attribute], dict) and GoSpecfile[attribute] != {}:
            process_single_record(GoSpecfile[attribute], attribute, None, None)

    Specfile2_from_GoSpec.metastring = Specfile2_from_GoSpec.metastring.replace('#!', '#')
    recreate_conditions()

    return json.dumps(Specfile2_from_GoSpec, default=lambda o: o.__dict__, sort_keys=True)
