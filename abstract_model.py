from __future__ import print_function
import json
from specparser import parse_specfile, SpecfileClass, BlockTypes
from pprint import pprint


def remove_blocktype(single_block):
    
    del single_block['block_type']
    return single_block


def json_to_specfile_class(json_containing_parsed_spec):
    
    global counter
    global Specfile

    for single_block in json_containing_parsed_spec:
        single_block['position'] = counter
        
        if single_block['block_type'] == BlockTypes.HeaderTagType:
            Specfile.headerTags.append(remove_blocktype(single_block))
        elif single_block['block_type'] == BlockTypes.SectionTagType:
            if 'package' not in single_block['key']:
                Specfile.sectionTags.append(remove_blocktype(single_block))
            else:
                content = single_block['content']
                del single_block['content']
                Specfile.sectionTags.append(remove_blocktype(single_block))
                counter += 1
                if content != []:
                    json_to_specfile_class(content)
                counter -= 1         
        elif single_block['block_type'] == BlockTypes.MacroDefinitionType:
            Specfile.macroDefinitions.append(remove_blocktype(single_block))
        elif single_block['block_type'] == BlockTypes.MacroConditionType:
            Specfile.macroConditions.append(remove_blocktype(single_block))
        elif single_block['block_type'] == BlockTypes.MacroUndefinitionType:
            Specfile.macroUndefinitions.append(remove_blocktype(single_block))
        elif single_block['block_type'] == BlockTypes.CommentType:
            Specfile.comments.append(remove_blocktype(single_block))
        elif single_block['block_type'] == BlockTypes.ConditionType:
            content = single_block['content']
            else_body = single_block['else_body']
            del single_block['content']
            del single_block['else_body']
            Specfile.conditions.append(remove_blocktype(single_block))
            counter += 1
            if content != []:
                json_to_specfile_class(content)
            if else_body != []:
                json_to_specfile_class(else_body)   
            counter -= 1         

        counter += 1


json_containing_parsed_spec = json.loads(parse_specfile())

Specfile = SpecfileClass('AbstractModel')
Specfile.beginning = json_containing_parsed_spec['beginning']
counter = 0

json_to_specfile_class(json_containing_parsed_spec['block_list'])

print(json.dumps(Specfile, default=lambda o: o.__dict__, sort_keys=True))

# print(json_containing_parsed_spec)
# pprint(json_containing_parsed_spec)
