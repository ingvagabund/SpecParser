from __future__ import print_function
import json
from copy import deepcopy

from abstract_model import BlockTypes, SpecfileClass, keys_list
from specparser import parse_file, open_file


def extern_json_to_specfile_class(json_containing_parsed_spec):

    for key in json_containing_parsed_spec:
        if key != 'beginning' and key != 'end':
            setattr(Specfile, key, json_containing_parsed_spec[key])

    return


def remove_blocktype(single_block):
    
    # del single_block['block_type']
    return single_block


def get_whitespace(current_string, order):

    if not isinstance(current_string, basestring):
        return ""

    if current_string.isspace():
        return "%" + str(order) + current_string
    
    metastring = current_string[:len(current_string) - len(current_string.lstrip())]
    metastring += "%" + str(order)
    metastring += current_string[len(current_string.rstrip()):]

    return metastring


def create_metastring(single_block, block_type):

    metastring = ""

    for i, key in enumerate(keys_list[block_type]):

        if key in single_block:

            if isinstance(single_block[key], dict):
                create_metastring(single_block[key], single_block[key]['block_type'])

                if 'keyword' in single_block and single_block['keyword'] == 'package':
                    metastring += '%' + str(i)

            else:
                if isinstance(single_block[key], list):
                    if single_block[key] != []:
                        for j, record in enumerate(single_block[key]):
                            if isinstance(record, basestring):
                                metastring += get_whitespace(record, i)
                                single_block[key][j] = record.strip()
                    metastring = metastring
                else:
                    if single_block[key] is not None:
                        metastring += get_whitespace(single_block[key], i)
                        single_block[key] = single_block[key].strip()

                if 'metastring' in single_block and len(single_block['metastring']) > len(metastring):
                    return single_block

                single_block['metastring'] = metastring

    return single_block


def json_to_specfile_class(json_containing_parsed_spec, predicate_list):
    
    global Specfile

    if json_containing_parsed_spec is None:
        return

    for single_block in json_containing_parsed_spec:
        if predicate_list != []:
            single_block['AP'] = predicate_list

        # Header Tag
        if single_block['block_type'] == BlockTypes.HeaderTagType:
            Specfile.block_list.append(remove_blocktype(create_metastring(single_block, single_block['block_type'])))

        # Section Tag
        elif single_block['block_type'] == BlockTypes.SectionTagType:
            if 'package' not in single_block['keyword']:
                Specfile.block_list.append(remove_blocktype(create_metastring(single_block, single_block['block_type'])))
            else:
                if single_block['content'] != []:
                    count = len(Specfile.block_list)
                    json_to_specfile_class(single_block['content'], predicate_list)
                    Specfile.block_list = Specfile.block_list[:count]
                created_block = remove_blocktype(create_metastring(single_block, single_block['block_type']))
                created_block['metastring'] += '%4'
                Specfile.block_list.append(created_block)

        # Macro Definition
        elif single_block['block_type'] == BlockTypes.MacroDefinitionType:
            Specfile.block_list.append(remove_blocktype(create_metastring(single_block, single_block['block_type'])))

        # Macro Condition
        elif single_block['block_type'] == BlockTypes.MacroConditionType:
            Specfile.block_list.append(remove_blocktype(create_metastring(single_block, single_block['block_type'])))
        
        # Macro Undefinition
        elif single_block['block_type'] == BlockTypes.MacroUndefinitionType:
            Specfile.block_list.append(remove_blocktype(create_metastring(single_block, single_block['block_type'])))

        # Commentary
        elif single_block['block_type'] == BlockTypes.CommentType:
            Specfile.block_list.append(remove_blocktype(create_metastring(single_block, single_block['block_type'])))
        
        # Condition
        elif single_block['block_type'] == BlockTypes.ConditionType:
            Specfile.block_list.append(remove_blocktype(create_metastring(single_block, single_block['block_type'])))
            count = len(Specfile.block_list)
            if 'content' in single_block and single_block['content'] != []:
                json_to_specfile_class(single_block['content'], predicate_list + [[single_block['expression'], 1]])
            if 'else_body' in single_block and single_block['else_body'] != []:
                json_to_specfile_class(single_block['else_body'], predicate_list + [[single_block['expression'], 0]])
            Specfile.block_list = Specfile.block_list[:count]
            
Specfile = SpecfileClass()


def create_abstract_model(input_filepath):

    global Specfile
        
    json_containing_parsed_spec = json.loads(parse_file(input_filepath))

    if isinstance(json_containing_parsed_spec['beginning'], basestring):
        Specfile.beginning = json_containing_parsed_spec['beginning']
    else:
        Specfile.beginning = {'content': json_containing_parsed_spec['beginning']['content']}        
    Specfile.end = json_containing_parsed_spec['end'];

    if 'block_list' in json_containing_parsed_spec:
        json_to_specfile_class(json_containing_parsed_spec['block_list'], [])

    else:
        extern_json_to_specfile_class(json_containing_parsed_spec)

    return Specfile


# specfile class to specfile reconstruction - main
def class_to_specfile(intern_specfile, pretty): # TODO pretty print
    
    if not pretty:
        print(str(intern_specfile.beginning), end='')

        if intern_specfile.block_list != []:
            print_field(intern_specfile.block_list)
    
        print(str(intern_specfile.end), end='')

    else:
        if intern_specfile.block_list != []:
            print_field(intern_specfile.block_list)        
            # print_pretty_field(intern_specfile.block_list) TODO        

    return


# specfile class to specfile reconstruction - subprocedure
def print_field(block_list):

    if block_list is None:
        return

    for intern_field in block_list:
        if intern_field != None:
            metastring_list = intern_field['metastring'].split('%')
            print(metastring_list[0], end='')

            if intern_field['block_type'] == BlockTypes.HeaderTagType:
                for metastring in metastring_list[1:]:
                    if int(metastring[0]) == 1:
                        print('(', end='')

                    print(intern_field[keys_list[intern_field['block_type']][int(metastring[0])]], end='')

                    if int(metastring[0]) == 0 and ('option' not in intern_field or intern_field['option'] == None):
                        print(':', end='')
                    elif int(metastring[0]) == 1:
                        print('):', end='')

                    print(metastring[1:], end='')

            elif intern_field['block_type'] == BlockTypes.SectionTagType:
                counter = 0

                for metastring in metastring_list[1:]:
                    if int(metastring[0]) == 0:
                        print('%', end='')
                    elif int(metastring[0]) == 2:
                        print('-', end='')
                    elif int(metastring[0]) == 4 and 'keyword' in intern_field and intern_field['keyword'] == 'package':
                        print_field(intern_field['content'])
                        break

                    if isinstance(intern_field[keys_list[intern_field['block_type']][int(metastring[0])]], list):
                        print(intern_field[keys_list[intern_field['block_type']][int(metastring[0])]][counter], end='')
                        counter += 1
            
                    else:
                        print(intern_field[keys_list[intern_field['block_type']][int(metastring[0])]], end='')
                    print(metastring[1:], end='')
        
            elif intern_field['block_type'] == BlockTypes.MacroDefinitionType:
                for metastring in metastring_list[1:]:
                    if int(metastring[0]) == 0:
                        print('%', end='')

                    print(intern_field[keys_list[intern_field['block_type']][int(metastring[0])]], end='')
                    print(metastring[1:], end='')

            elif intern_field['block_type'] == BlockTypes.MacroConditionType:
                for metastring in metastring_list[1:]:
                    if int(metastring[0]) == 0:
                        print('%{', end='')
                    elif int(metastring[0]) == 2:
                        print(':', end='')
                    elif int(metastring[0]) == 3:
                        print('}', end='')

                    print(intern_field[keys_list[intern_field['block_type']][int(metastring[0])]], end='')
                    print(metastring[1:], end='')

            elif intern_field['block_type'] == BlockTypes.MacroUndefinitionType:
                for metastring in metastring_list[1:]:
                    if int(metastring[0]) == 0:
                        print('%', end='')

                    print(intern_field[keys_list[intern_field['block_type']][int(metastring[0])]], end='')
                    print(metastring[1:], end='')

            elif intern_field['block_type'] == BlockTypes.CommentType:
                for metastring in metastring_list[1:]:
                    print(intern_field[keys_list[intern_field['block_type']][int(metastring[0])]], end='')
                    print(metastring[1:], end='')

            elif intern_field['block_type'] == BlockTypes.ConditionType:
                for metastring in metastring_list[1:]:
                    if int(metastring[0]) in [0, 3, 5]:
                        print('%', end='')

                    print(intern_field[keys_list[intern_field['block_type']][int(metastring[0])]], end='')
                    print(metastring[1:], end='')

                    if int(metastring[0]) == 1:
                        print_field(intern_field['content'])
                
                    elif int(metastring[0]) == 3:
                        print_field(intern_field['else_body'])

    return


def reduce_inner_block(single_block):
    
    reduced_single_block = deepcopy(single_block)
    
    if isinstance(single_block, dict):
        for (attr, value), (reduced_attr, reduced_value) in zip(single_block.iteritems(), reduced_single_block.iteritems()):
            if value is None or value == []:
                reduced_single_block.pop(reduced_attr, None)
            elif (isinstance(value, dict) or isinstance(value, list)) and attr != 'AP':
                reduce_inner_block(value)

    return reduced_single_block               


def remove_empty_fields(Specfile):
    
    reduced_Specfile = deepcopy(Specfile)

    for (single_block, reduced_single_block) in zip(Specfile.block_list, reduced_Specfile.block_list):
        for (attr, value), (reduced_attr, reduced_value) in zip(single_block.iteritems(), reduced_single_block.iteritems()):
            if value == None or value == []:
                reduced_single_block.pop(attr, None)
            elif isinstance(value, dict):
                reduced_single_block = reduce_inner_block(single_block)
            elif isinstance(value, list):
                for (single_record, reduced_single_record) in zip(value, reduced_value):
                    reduced_single_record = reduce_inner_block(single_record)
                    

    return reduced_Specfile


def process_config_file(Specfile, config_path):

    config_data = open_file(config_path)
    # TODO config form and make it work
    return
