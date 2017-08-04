from __future__ import print_function
import json
import re
import ruamel.yaml
from copy import deepcopy

from abstract_model import SpecfileClass, BlockTypes
from model_methods import reduce_inner_block


GoSpecfile = SpecfileClass('GO spec')


def reduce_gospecfile():

    global GoSpecfile

    reduced_GoSpecfile = deepcopy(GoSpecfile)

    for (block_list, reduced_block_list) in zip(GoSpecfile.__dict__.iteritems(), reduced_GoSpecfile.__dict__.iteritems()):
        if block_list[1] is None or block_list[1] == [[]] or block_list[1] == [] or block_list[1] == "" or block_list[0] == 'metastring':
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
                                    if 'block_type' not in single_record[keyword][inner_keyword]:
                                        print("DICT: " + str(inner_keyword) + " : "  + str(single_record[keyword][inner_keyword]))
                                    else:
                                        reduced_block_list[1][index][keyword][inner_keyword] = gospecfile_to_print(reduced_block_list[1][index][keyword][inner_keyword]) 
                            else:
                                print("NOT DICT: " + str(keyword) + " : "  + str(single_record[keyword]))
                    
                    else:
                        reduced_block_list[1][index] = gospecfile_to_print(reduced_block_list[1][index])

    return reduced_GoSpecfile


def gospecfile_to_print(single_record):

    if single_record['block_type'] == BlockTypes.HeaderTagType:
        single_record = {single_record['key']:single_record['content']}

    elif single_record['block_type'] == BlockTypes.MacroDefinitionType:
        if 'name' in single_record and 'body' in single_record:
            single_record['name'] = '%' + single_record['name']
            single_record = {single_record['name']:single_record['body']}

    elif single_record['block_type'] == BlockTypes.SectionTagType:
        if 'keyword' in single_record and 'content' in single_record:
            if single_record['keyword'] == 'changelog':
                for idx, single_log in enumerate(single_record['content']):
                    single_record[idx] = parse_changelog(single_log)
                    if 'keyword' in single_record:
                        del single_record['keyword']
                    if 'block_type' in single_record:
                        del single_record['block_type']
                    if 'content' in single_record:
                        del single_record['content']

            else:
                single_record = {single_record['keyword']:single_record['content']}

    return single_record


def replace_field_number(prev_section_count, replacing):

    global GoSpecfile

    to_be_replaced_list = re.findall(r'#' + str(replacing[0]) + '\d+', GoSpecfile.metastring)
    for replace_record in to_be_replaced_list:
        GoSpecfile.metastring = GoSpecfile.metastring.replace(replace_record, '#' + str(replacing[1]) + str(int(replace_record[2:]) + prev_section_count))


def parse_changelog(changelog):

    parsed_changelog = {}
    first_line = changelog[:changelog.find('\n')+1]

    parsed_changelog['comment'] = changelog[changelog.find('\n')+1:]
    parsed_changelog['date'] = first_line[first_line.find('*')+1:first_line.find('20')+4]
    parsed_changelog['mark'] = re.findall(r'[\d\s\.-]*', first_line)[-2]
    parsed_changelog['author'] = first_line[first_line.find(parsed_changelog['date'])+(len(parsed_changelog['date'])):first_line.rfind(parsed_changelog['mark'])]

    return parsed_changelog


def create_go_spec_model(Specfile2):

    global GoSpecfile
    GoSpecfile.metastring = Specfile2.metastring

    if Specfile2.HeaderTags:
        for header_tag in Specfile2.HeaderTags:
            if re.match(r'(?i)requires', header_tag['key']) is not None:
                if 'runtime' in GoSpecfile.main_unit:
                    if 'dependencies' in GoSpecfile.main_unit['runtime']:
                        GoSpecfile.main_unit['runtime']['dependencies'].append(header_tag)                    
                    else:
                        GoSpecfile.main_unit['runtime']['dependencies'] = header_tag
                else:
                    GoSpecfile.main_unit.append({'runtime':{'dependencies':header_tag}})

            elif re.match(r'(?i)buildrequires', header_tag['key']) is not None:
                if 'buildtime' in GoSpecfile.main_unit:
                    if 'dependencies' in GoSpecfile.main_unit['buildtime']:
                        GoSpecfile.main_unit['buildtime']['dependencies'].append(header_tag)                    
                    else:
                        GoSpecfile.main_unit['buildtime']['dependencies'] = header_tag
                else:            
                    GoSpecfile.main_unit.append({'buildtime':{'dependencies':header_tag}})

            elif 'AP' not in header_tag or header_tag['AP'] == '':
                GoSpecfile.metadata.append(header_tag)

    if Specfile2.MacroDefinitions:
        GoSpecfile.metadata += Specfile2.MacroDefinitions
        replace_field_number(len(Specfile2.HeaderTags), [2,0])

    prev_section_count = 0
    # unit_list = []  # TODO make a dict instead?

    if Specfile2.SectionTags:
        
        for single_section in Specfile2.SectionTags:
            if single_section['keyword'] == 'changelog':
                GoSpecfile.history.append(single_section)
                replace_field_number(prev_section_count, [1,1])
                prev_section_count += 1

            elif ('AP' not in single_section or single_section['AP'] == ''):
                GoSpecfile.main_unit.append(single_section)
                replace_field_number(prev_section_count, [1,1])
                prev_section_count += 1

    # if Specfile2.Comments:
    #     GoSpecfile.main_unit += Specfile2.Comments
    #     GoSpecfile.metastring = replace_field_number(GoSpecfile.metastring, prev_section_count, [5,1])
    #     prev_section_count += len(Specfile2.Comments)

    # GoSpecfile.unit_list.append(unit_list)
    
    # print(ruamel.yaml.dump(ruamel.yaml.safe_load(json.dumps(reduce_gospecfile(GoSpecfile), default=lambda o: o.__dict__, sort_keys=True))))
    print(ruamel.yaml.round_trip_dump(ruamel.yaml.safe_load(
        json.dumps(reduce_gospecfile(), default=lambda o: o.__dict__, sort_keys=True)),
                                      default_flow_style=False, indent=4, block_seq_indent=2, width=80))
    # print("\n\n"+str(GoSpecfile.metastring))
