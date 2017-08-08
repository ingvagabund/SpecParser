from __future__ import print_function
import json
import re
from copy import deepcopy


from abstract_model import SpecfileClass, BlockTypes, keys_list
from model_methods import create_metastring


GoSpecfile = SpecfileClass('GO spec')


def reduce_gospecfile():

    global GoSpecfile

    reduced_GoSpecfile = deepcopy(GoSpecfile)

    for (block_list, reduced_block_list) in zip(sorted(GoSpecfile.__dict__.iteritems()), sorted(reduced_GoSpecfile.__dict__.iteritems())):
        if block_list[1] is None or block_list[1] == [[]] or block_list[1] == [] or block_list[1] == {} or block_list[1] == '' or block_list[0] in ['metastring', 'comments']:
            delattr(reduced_GoSpecfile, block_list[0])
        elif isinstance(block_list[1], list):
            for (index, single_record) in enumerate(block_list[1]):
                if isinstance(single_record, list):
                    for (neco, neco2) in enumerate(single_record):
                        single_record[index][neco] = gospecfile_to_print(neco2)
                else:
                    if 'block_type' not in single_record:
                        for keyword in single_record:
                            if 'block_type' not in single_record[keyword]:
                                for inner_keyword in single_record[keyword]:
                                    if 'block_type' in single_record[keyword][inner_keyword]:
                                        reduced_block_list[1][index][keyword][inner_keyword] = gospecfile_to_print(block_list[1][index][keyword][inner_keyword]) 
                            else:
                                print("NOT DICT: " + str(keyword) + " : "  + str(single_record[keyword]))

                    else:
                        reduced_block_list[1][index] = gospecfile_to_print(block_list[1][index])

        elif isinstance(block_list[1], dict):
            if block_list[1] != {}:
                reduced_GoSpecfile.history = gospecfile_to_print(block_list[1])

    return reduced_GoSpecfile


def gospecfile_to_print(single_record):

    global GoSpecfile

    if single_record['block_type'] == BlockTypes.HeaderTagType:
        single_record = {single_record['key']:single_record['content']}

    elif single_record['block_type'] == BlockTypes.MacroDefinitionType:
        if 'name' in single_record and 'body' in single_record:
            single_record['name'] = '%' + single_record['name']
            single_record = {single_record['name']:single_record['body']}

    elif single_record['block_type'] == BlockTypes.SectionTagType:
        if 'keyword' in single_record and 'content' in single_record:
            if single_record['keyword'] == 'changelog':
                length = len(single_record['content']) - 1
                for idx, single_log in enumerate(single_record['content']):
                    single_record[length - idx] = parse_changelog(single_log)
                    create_metastring(single_record[length - idx], BlockTypes.ChangelogTagType)
                    if 'keyword' in single_record:
                        del single_record['keyword']
                    if 'content' in single_record:
                        del single_record['content']
                single_record['block_type'] = BlockTypes.ChangelogTagType
                single_record = gospecfile_to_print(single_record)

            else:
                if single_record['content'] == '':
                    single_record['content'] = None
                single_record = {single_record['keyword']:single_record['content']}

    elif single_record['block_type'] == BlockTypes.ChangelogTagType:
        del single_record['block_type']
        for record_index in single_record:
            for field in keys_list[BlockTypes.ChangelogTagType]:
                if field in single_record[record_index] and single_record[record_index][field] == '':
                    single_record[record_index][field] = None
                # else:
                #     single_record[record_index][field] = single_record[record_index][field]

    return single_record


def replace_field_number(prev_section_count, replacing):

    global GoSpecfile

    to_be_replaced_list = re.findall(r'#' + str(replacing[0]) + r'\d*', GoSpecfile.metastring)
    for replace_record in to_be_replaced_list:
        GoSpecfile.metastring = GoSpecfile.metastring.replace(replace_record, '#!' + str(replacing[1]) + str(prev_section_count))


def parse_changelog(changelog):

    parsed_changelog = {}
    first_line = changelog[:changelog.find('\n')+1]

    parsed_changelog['comment'] = changelog[changelog.find('\n')+1:]
    parsed_changelog['date'] = first_line[first_line.find('*')+1:first_line.find('20')+4]
    parsed_changelog['mark'] = re.findall(r'[\d\s\.-]*', first_line)[-2]
    parsed_changelog['author'] = first_line[first_line.find(parsed_changelog['date'])+(len(parsed_changelog['date'])):first_line.rfind(parsed_changelog['mark'])]

    return parsed_changelog


def append_dependency(keyword, header_tag):

    if GoSpecfile.main_unit == []:
        GoSpecfile.main_unit.append({keyword:{'dependencies':[{'name':header_tag['content']}]}})
    else:
        found = False
        for single_record in GoSpecfile.main_unit:
            if keyword in single_record:
                found = True
                if 'dependencies' in single_record[keyword]:
                    single_record[keyword]['dependencies'].append({'name':header_tag['content']})
                else:
                    single_record[keyword]['dependencies'] = [{'name':header_tag['content']}]

        if found is False:
            GoSpecfile.main_unit.append({keyword:{'dependencies':[{'name':header_tag['content']}]}})
    return


def process_unit_list():

    used_unit_names = []
    for single_unit in GoSpecfile.unit_list:
        if single_unit['subname'] not in used_unit_names:
            used_unit_names.append(single_unit['subname'])
        # else:
        #     pos = find_appropriate_unit()
        #     append_to_appropriate_unit
        #     remove_original_record()

    return


def create_go_spec_model(Specfile2):

    global GoSpecfile
    GoSpecfile.metastring = Specfile2.metastring

    prev_section_count = 0

    if Specfile2.HeaderTags:
        for index, header_tag in enumerate(Specfile2.HeaderTags):
            if re.match(r'(?i)requires', header_tag['key']) is not None:
                append_dependency('runtime', header_tag)
                replace_field_number(prev_section_count, ["0" + str(index), 1])
                prev_section_count += 1

            elif re.match(r'(?i)buildrequires', header_tag['key']) is not None:
                append_dependency('buildtime', header_tag)
                replace_field_number(prev_section_count, ["0" + str(index), 1])
                prev_section_count += 1

            elif 'AP' not in header_tag or header_tag['AP'] == '':
                GoSpecfile.metadata.append(header_tag)

    if Specfile2.MacroDefinitions:
        for index in range(len(Specfile2.MacroDefinitions)):
            replace_field_number(len(GoSpecfile.metadata) + index, ["2" + str(index), 0])
        GoSpecfile.metadata += Specfile2.MacroDefinitions

    if Specfile2.SectionTags:
        for index, single_section in enumerate(Specfile2.SectionTags):
            if single_section['keyword'] == 'changelog':
                GoSpecfile.history = single_section
                replace_field_number(0, ["1" + str(index),3])
                prev_section_count += 1

            elif('subname' in single_section and single_section['subname'] is not None):
                # TODO find appropriate unit if it exists
                GoSpecfile.unit_list.append(single_section)

            elif ('AP' not in single_section or single_section['AP'] == ''):
                GoSpecfile.main_unit.append(single_section)
                replace_field_number(prev_section_count, ["1" + str(index),1])
                prev_section_count += 1

    if Specfile2.Comments:
        for index in range(len(Specfile2.Comments)):
            replace_field_number(index, [5, 4])
        prev_section_count += len(Specfile2.Comments)
        GoSpecfile.comments = Specfile2.Comments

    process_unit_list()
    GoSpecfile.metastring = GoSpecfile.metastring.replace('#!', '#')
