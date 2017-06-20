from __future__ import print_function
import json
from specparser import parse_specfile, SpecfileClass, BlockTypes
from pprint import pprint
import ctypes


def remove_blocktype(single_block):
    
    # del single_block['block_type']
    return single_block


def json_to_specfile_class(json_containing_parsed_spec):
    
    global Specfile
    global previous_node_next_pointer
    global next_field

    for single_block in json_containing_parsed_spec:
        single_block['next'] = None

        if single_block['block_type'] == BlockTypes.HeaderTagType:
            Specfile.headerTags.append(remove_blocktype(single_block))
            next_field = Specfile.headerTags[-1]
        elif single_block['block_type'] == BlockTypes.SectionTagType:
            if 'package' not in single_block['keyword']:
                Specfile.sectionTags.append(remove_blocktype(single_block))
                next_field = Specfile.sectionTags[-1]
            else:
                content = single_block['content']
                del single_block['content']
                point_package_to_ptr = previous_node_next_pointer
                Specfile.sectionTags.append(remove_blocktype(single_block))
                if content != []:
                    tmp = {'next': None}
                    previous_node_next_pointer = tmp
                    json_to_specfile_class(content)
                    single_block['content'] = tmp['next']
                Specfile.conditions.append(remove_blocktype(single_block))
                next_field = Specfile.sectionTags[-1]
                previous_node_next_pointer = point_package_to_ptr
        elif single_block['block_type'] == BlockTypes.MacroDefinitionType:
            Specfile.macroDefinitions.append(remove_blocktype(single_block))
            next_field = Specfile.macroDefinitions[-1]
        elif single_block['block_type'] == BlockTypes.MacroConditionType:
            Specfile.macroConditions.append(remove_blocktype(single_block))
            next_field = Specfile.macroConditions[-1]
        elif single_block['block_type'] == BlockTypes.MacroUndefinitionType:
            Specfile.macroUndefinitions.append(remove_blocktype(single_block))
            next_field = Specfile.macroUndefinitions[-1]
        elif single_block['block_type'] == BlockTypes.CommentType:
            Specfile.comments.append(remove_blocktype(single_block))
            next_field = Specfile.comments[-1]
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
            # previous_node_next_pointer.update({'next': point_condition_to_ptr})
            previous_node_next_pointer = point_condition_to_ptr

        previous_node_next_pointer.update({'next': next_field})
        previous_node_next_pointer = next_field


json_containing_parsed_spec = json.loads(parse_specfile())
Specfile = SpecfileClass('AbstractModel')
Specfile.beginning = {'content': json_containing_parsed_spec['beginning'], 'next': None}

next_field = None
previous_node_next_pointer = Specfile.beginning

json_to_specfile_class(json_containing_parsed_spec['block_list'])

print(json.dumps(Specfile, default=lambda o: o.__dict__, sort_keys=True))

# print(ctypes.cast(previous_node_next_pointer, ctypes.py_object))
# pprint(json_containing_parsed_spec)
