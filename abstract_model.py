from __future__ import print_function
import json
from specparser import parse_specfile, SpecfileClass, BlockTypes
from pprint import pprint


json_containing_parsed_spec = json.loads(parse_specfile())

Specfile = SpecfileClass()
Specfile.beginning = json_containing_parsed_spec['beginning']



for single_block in json_containing_parsed_spec['block_list']:
    print(single_block['block_type'])



# print(json_containing_parsed_spec)
# pprint(json_containing_parsed_spec)
