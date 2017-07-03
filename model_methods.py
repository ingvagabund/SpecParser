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
                            metastring += get_whitespace(record, i)
                            single_block[key][j] = record.strip()

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
    global previous_node_next_pointer
    global next_field

    for single_block in json_containing_parsed_spec:
        single_block['next'] = None
        
        if predicate_list != []:
            single_block['AP'] = predicate_list

        # Header Tag
        if single_block['block_type'] == BlockTypes.HeaderTagType:
            Specfile.headerTags.append(remove_blocktype(create_metastring(single_block, single_block['block_type'])))
            next_field = Specfile.headerTags[-1]

        # Section Tag
        elif single_block['block_type'] == BlockTypes.SectionTagType:
            if 'package' not in single_block['keyword']:
                Specfile.sectionTags.append(remove_blocktype(create_metastring(single_block, single_block['block_type'])))
                next_field = Specfile.sectionTags[-1]
            else:
                content = single_block['content']
                del single_block['content']
                point_package_to_ptr = previous_node_next_pointer
                if content != []:
                    tmp = {'next': None}
                    previous_node_next_pointer = tmp
                    json_to_specfile_class(content, predicate_list)
                    single_block['content'] = tmp['next']
                created_block = remove_blocktype(create_metastring(single_block, single_block['block_type']))
                created_block['metastring'] += '%4'
                Specfile.sectionTags.append(created_block)
                Specfile.sectionTags.append(create_metastring(single_block, single_block['block_type']))
                next_field = Specfile.sectionTags[-1]
                previous_node_next_pointer = point_package_to_ptr

        # Macro Definition
        elif single_block['block_type'] == BlockTypes.MacroDefinitionType:
            Specfile.macroDefinitions.append(remove_blocktype(create_metastring(single_block, single_block['block_type'])))
            next_field = Specfile.macroDefinitions[-1]

        # Macro Condition
        elif single_block['block_type'] == BlockTypes.MacroConditionType:
            Specfile.macroConditions.append(remove_blocktype(create_metastring(single_block, single_block['block_type'])))
            next_field = Specfile.macroConditions[-1]
        
        # Macro Undefinition
        elif single_block['block_type'] == BlockTypes.MacroUndefinitionType:
            Specfile.macroUndefinitions.append(remove_blocktype(create_metastring(single_block, single_block['block_type'])))
            next_field = Specfile.macroUndefinitions[-1]

        # Commentary
        elif single_block['block_type'] == BlockTypes.CommentType:
            Specfile.comments.append(remove_blocktype(create_metastring(single_block, single_block['block_type'])))
            next_field = Specfile.comments[-1]
        
        # Condition
        elif single_block['block_type'] == BlockTypes.ConditionType:
            content = single_block['content']
            else_body = single_block['else_body']
            point_condition_to_ptr = previous_node_next_pointer
            if content != []:
                tmp = {'next': None}
                previous_node_next_pointer = tmp
                json_to_specfile_class(content, predicate_list + [[single_block['expression'], 1]])
                single_block['content'] = tmp['next']
            if else_body != []:
                tmp = {'next': None}
                previous_node_next_pointer = tmp
                json_to_specfile_class(else_body, predicate_list + [[single_block['expression'], 0]])
                single_block['else_body'] = tmp['next']                
            Specfile.conditions.append(remove_blocktype(create_metastring(single_block, single_block['block_type'])))
            next_field = Specfile.conditions[-1]
            previous_node_next_pointer = point_condition_to_ptr

        previous_node_next_pointer.update({'next': next_field})
        previous_node_next_pointer = next_field

Specfile = SpecfileClass('AbstractModel')
previous_node_next_pointer = None

def create_abstract_model(input_filepath):

    global previous_node_next_pointer
        
    json_containing_parsed_spec = json.loads(parse_file(input_filepath))

    if isinstance(json_containing_parsed_spec['beginning'], basestring):
        Specfile.beginning = {'content': json_containing_parsed_spec['beginning'], 'next': None}
    else:
        Specfile.beginning = {'content': json_containing_parsed_spec['beginning']['content'], 'next': json_containing_parsed_spec['beginning']['next']}        
    Specfile.end = json_containing_parsed_spec['end'];

    next_field = None
    previous_node_next_pointer = Specfile.beginning

    if 'block_list' in json_containing_parsed_spec:
        json_to_specfile_class(json_containing_parsed_spec['block_list'], [])

    else:
        extern_json_to_specfile_class(json_containing_parsed_spec)

    return Specfile


# specfile class to specfile reconstruction - main
def class_to_specfile(intern_specfile, pretty): # TODO pretty print
    
    if not pretty:
        print(str(intern_specfile.beginning["content"]), end='')

        if intern_specfile.beginning["next"] != None:
            print_field(intern_specfile.beginning["next"])
    
        print(str(intern_specfile.end), end='')

    else:
        if intern_specfile.beginning["next"] != None:
            print_field(intern_specfile.beginning["next"])        
            # print_pretty_field(intern_specfile.beginning["next"]) TODO        

    return


# specfile class to specfile reconstruction - subprocedure
def print_field(intern_field):

    if intern_field != None:
        metastring_list = intern_field['metastring'].split('%')
        print(metastring_list[0], end='')

        if intern_field['block_type'] == BlockTypes.HeaderTagType:
            for metastring in metastring_list[1:]:
                if int(metastring[0]) == 1:
                    print('(', end='')

                print(intern_field[keys_list[intern_field['block_type']][int(metastring[0])]], end='')

                if int(metastring[0]) == 0 and intern_field['option'] == None:
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



        # if intern_field["block_type"] == BlockTypes.HeaderTagType:
        #     print(str(intern_field["key"]), end='')
        #     if "option" in intern_field and intern_field["option"] is not None:
        #         print('(' + str(intern_field["option"]) + ')', end='')
        #     print(":" + str(intern_field["content"]), end='')

        # elif intern_field["block_type"] == BlockTypes.SectionTagType:
        #     print("%" + str(intern_field["keyword"]), end='')

        #     if "changelog" in intern_field["keyword"]:
        #         for single_log in intern_field["content"]:
        #             print(str(single_log), end='')
        #     elif "files" in intern_field["keyword"]:
        #         if "name" in intern_field and intern_field["name"] is not None:            
        #             print(str(intern_field["name"]), end='')            
        #         if "parameters" in intern_field and intern_field["parameters"] is not None:
        #             print('-' + str(intern_field["parameters"]), end='')
        #         if "subname" in intern_field and intern_field["subname"] is not None:
        #             print(str(intern_field["subname"]), end='')
        #         if "content" in intern_field and intern_field["content"] is not None:
        #             print(str(intern_field["content"]), end='')                        
                    
        #     else:
        #         if "parameters" in intern_field and intern_field["parameters"] is not None:
        #             print('-' + str(intern_field["parameters"]), end='')
        #         if "name" in intern_field and intern_field["name"] is not None:            
        #             print(str(intern_field["name"]), end='')            
        #         if "subname" in intern_field and intern_field["subname"] is not None:
        #             print(str(intern_field["subname"]), end='')

        #         if "package" in intern_field["keyword"]:
        #             print_field(intern_field["content"])
        #         else:
        #             if "content" in intern_field and intern_field["content"] is not None:
        #                 print(str(intern_field["content"]), end='')                        

        # elif intern_field["block_type"] == BlockTypes.CommentType:
        #     print(str(intern_field["content"]), end='')

        # elif intern_field["block_type"] == BlockTypes.MacroDefinitionType:
        #     print("%" + str(intern_field["keyword"]) + str(intern_field["name"]), end='')
        #     if intern_field["options"] is not None:
        #         print(str(intern_field["options"]), end='')
        #     print(str(intern_field["body"]), end='')

        # elif intern_field["block_type"] == BlockTypes.MacroConditionType:
        #     print("%{" + str(intern_field["condition"]) + str(intern_field["name"]) + ':' + str(intern_field["content"]) + '}' + str(intern_field["ending"]), end='')

        # elif intern_field["block_type"] == BlockTypes.ConditionType:
        #     if intern_field["keyword"] is not None and intern_field["expression"] is not None:
        #         print("%" + str(intern_field["keyword"]) + str(intern_field["expression"]), end='')
        #     print_field(intern_field["content"])
        #     if intern_field["else_keyword"] is not None and intern_field["else_body"] is not None:
        #         print("%" + str(intern_field["else_keyword"]), end='')
        #         print_field(intern_field["else_body"])
        #     print("%" + str(intern_field["end_keyword"]), end='')

        if intern_field["next"] != None:
            print_field(intern_field["next"])
    
    return


def remove_empty_fields(Specfile):
    
    reduced_Specfile = deepcopy(Specfile)

    for attr, value in Specfile.__dict__.iteritems():
        if value == []:
            delattr(reduced_Specfile, attr)

    return reduced_Specfile


def process_config_file(Specfile, config_path):

    config_data = open_file(config_path)
    # TODO config form and make it work
    return
