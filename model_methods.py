from __future__ import print_function
import json

from abstract_model import BlockTypes, SpecfileClass
from specparser import parse_specfile



def remove_blocktype(single_block):
    
    # del single_block['block_type']
    return single_block


def json_to_specfile_class(json_containing_parsed_spec):
    
    global Specfile
    global previous_node_next_pointer
    global next_field

    for single_block in json_containing_parsed_spec:
        single_block['next'] = None

        # Header Tag
        if single_block['block_type'] == BlockTypes.HeaderTagType:
            Specfile.headerTags.append(remove_blocktype(single_block))
            next_field = Specfile.headerTags[-1]

        # Section Tag
        elif single_block['block_type'] == BlockTypes.SectionTagType:
            if 'package' not in single_block['keyword']:
                Specfile.sectionTags.append(remove_blocktype(single_block))
                next_field = Specfile.sectionTags[-1]
            else:
                content = single_block['content']
                del single_block['content']
                point_package_to_ptr = previous_node_next_pointer
                if content != []:
                    tmp = {'next': None}
                    previous_node_next_pointer = tmp
                    json_to_specfile_class(content)
                    single_block['content'] = tmp['next']
                Specfile.sectionTags.append(remove_blocktype(single_block))
                next_field = Specfile.sectionTags[-1]
                previous_node_next_pointer = point_package_to_ptr

        # Macro Definition
        elif single_block['block_type'] == BlockTypes.MacroDefinitionType:
            Specfile.macroDefinitions.append(remove_blocktype(single_block))
            next_field = Specfile.macroDefinitions[-1]

        # Macro Condition
        elif single_block['block_type'] == BlockTypes.MacroConditionType:
            Specfile.macroConditions.append(remove_blocktype(single_block))
            next_field = Specfile.macroConditions[-1]
        
        # Macro Undefinition
        elif single_block['block_type'] == BlockTypes.MacroUndefinitionType:
            Specfile.macroUndefinitions.append(remove_blocktype(single_block))
            next_field = Specfile.macroUndefinitions[-1]

        # Commentary
        elif single_block['block_type'] == BlockTypes.CommentType:
            Specfile.comments.append(remove_blocktype(single_block))
            next_field = Specfile.comments[-1]
        
        # Condition
        elif single_block['block_type'] == BlockTypes.ConditionType:
            content = single_block['content']
            else_body = single_block['else_body']
            point_condition_to_ptr = previous_node_next_pointer
            if content != []:
                tmp = {'next': None}
                previous_node_next_pointer = tmp
                json_to_specfile_class(content)
                single_block['content'] = tmp['next']
            if else_body != []:
                tmp = {'next': None}
                previous_node_next_pointer = tmp
                json_to_specfile_class(else_body)
                single_block['else_body'] = tmp['next']                
            Specfile.conditions.append(remove_blocktype(single_block))
            next_field = Specfile.conditions[-1]
            previous_node_next_pointer = point_condition_to_ptr

        previous_node_next_pointer.update({'next': next_field})
        previous_node_next_pointer = next_field

Specfile = SpecfileClass('AbstractModel')
previous_node_next_pointer = None

def create_abstract_model(input_filepath):

    global previous_node_next_pointer

    json_containing_parsed_spec = json.loads(parse_specfile(input_filepath))
    Specfile.beginning = {'content': json_containing_parsed_spec['beginning'], 'next': None}
    Specfile.end = json_containing_parsed_spec['end'];

    next_field = None
    previous_node_next_pointer = Specfile.beginning

    json_to_specfile_class(json_containing_parsed_spec['block_list'])

    return Specfile


# specfile class to specfile reconstruction - main
def class_to_specfile(intern_specfile):
    
    print(str(intern_specfile.beginning["content"]), end='')

    if intern_specfile.beginning["next"] != None:
        print_field(intern_specfile.beginning["next"])
    
    print(str(intern_specfile.end), end='')

    return


# specfile class to specfile reconstruction - subprocedure
def print_field(intern_field):

    if intern_field != None:
        if intern_field["block_type"] == BlockTypes.HeaderTagType:
            print(str(intern_field["key"]), end='')
            if "option" in intern_field and intern_field["option"] is not None:
                print('(' + str(intern_field["option"]) + ')', end='')
            print(":" + str(intern_field["content"]), end='')

        elif intern_field["block_type"] == BlockTypes.SectionTagType:
            print("%" + str(intern_field["keyword"]), end='')

            if "changelog" in intern_field["keyword"]:
                for single_log in intern_field["content"]:
                    print(str(single_log), end='')
            elif "files" in intern_field["keyword"]:
                if "name" in intern_field and intern_field["name"] is not None:            
                    print(str(intern_field["name"]), end='')            
                if "parameters" in intern_field and intern_field["parameters"] is not None:
                    print('-' + str(intern_field["parameters"]), end='')
                if "subname" in intern_field and intern_field["subname"] is not None:
                    print(str(intern_field["subname"]), end='')
                if "content" in intern_field and intern_field["content"] is not None:
                    print(str(intern_field["content"]), end='')                        
                    
            else:
                if "parameters" in intern_field and intern_field["parameters"] is not None:
                    print('-' + str(intern_field["parameters"]), end='')
                if "name" in intern_field and intern_field["name"] is not None:            
                    print(str(intern_field["name"]), end='')            
                if "subname" in intern_field and intern_field["subname"] is not None:
                    print(str(intern_field["subname"]), end='')

                if "package" in intern_field["keyword"]:
                    # print(str(intern_field["name"]), end='')
                    print_field(intern_field["content"])
                else:
                    if "content" in intern_field and intern_field["content"] is not None:
                        print(str(intern_field["content"]), end='')                        

        elif intern_field["block_type"] == BlockTypes.CommentType:
            print(str(intern_field["content"]), end='')

        elif intern_field["block_type"] == BlockTypes.MacroDefinitionType:
            print("%" + str(intern_field["keyword"]) + str(intern_field["name"]), end='')
            if intern_field["options"] is not None:
                print(str(intern_field["options"]), end='')
            print(str(intern_field["body"]), end='')

        elif intern_field["block_type"] == BlockTypes.MacroConditionType:
            print("%{" + str(intern_field["condition"]) + str(intern_field["name"]) + ':' + str(intern_field["content"]) + '}' + str(intern_field["ending"]), end='')

        elif intern_field["block_type"] == BlockTypes.ConditionType:
            if intern_field["keyword"] is not None and intern_field["expression"] is not None:
                print("%" + str(intern_field["keyword"]) + str(intern_field["expression"]), end='')
            print_field(intern_field["content"])
            if intern_field["else_keyword"] is not None and intern_field["else_body"] is not None:
                print("%" + str(intern_field["else_keyword"]), end='')
                print_field(intern_field["else_body"])
            print("%" + str(intern_field["end_keyword"]), end='')

        if intern_field["next"] != None:
            print_field(intern_field["next"])
    
    return
