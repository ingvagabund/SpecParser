from __future__ import print_function
import json
import sys

from abstract_model import *


Specfile2 = SpecfileClass('Specfile 2.0')
list_of_blocks = []

number_of_blocktypes = len([a for a in dir(BlockTypes) if not a.startswith('__')])
for i in range(number_of_blocktypes):
    list_of_blocks.append([])


def add_blocks_to_specfile():

    Specfile2.HeaderTags = list_of_blocks[0]
    Specfile2.SectionTags = list_of_blocks[1]
    Specfile2.MacroDefinitions = list_of_blocks[2]
    Specfile2.MacroConditions = list_of_blocks[3]
    Specfile2.MacroUndefinitions = list_of_blocks[4]
    Specfile2.Comments = list_of_blocks[5]
    Specfile2.Conditions = list_of_blocks[6]


def create_blocks_from_specfile():
    
    list_of_blocks = []

    list_of_blocks.append(Specfile2.HeaderTags)  
    list_of_blocks.append(Specfile2.SectionTags)
    list_of_blocks.append(Specfile2.MacroDefinitions) 
    list_of_blocks.append(Specfile2.MacroConditions)
    list_of_blocks.append(Specfile2.MacroUndefinitions) 
    list_of_blocks.append(Specfile2.Comments)
    list_of_blocks.append(Specfile2.Conditions) 


def transform_spec1_to_spec2(Specfile1):
    
    metastring_list = Specfile1.metastring.split('#')

    Specfile2.metastring = metastring_list[0]

    for block, metastring1 in zip(Specfile1.block_list, metastring_list[1:]):
        block_metastring_list = metastring1.split('%')
        Specfile2.metastring += '#' + str(block['block_type']) + str(len(list_of_blocks[block['block_type']]))
        list_of_blocks[block['block_type']].append(block)
        Specfile2.metastring += block_metastring_list[0] + metastring1

    add_blocks_to_specfile()


def transform_spec2_to_spec1(Specfile2):

    create_blocks_from_specfile()
    Specfile1 = SpecfileClass('Specfile 1.0')
    metastring_list = Specfile2.metastring.split('#')
    Specfile1.metastring = metastring_list[0]

    for metastring1 in metastring_list[1:]:
        Specfile1.metastring += '#' + metastring1[metastring1.find('%'):]
        Specfile1.block_list.append(list_of_blocks[int(metastring1[0])][int(metastring1[1:metastring1.find('%')])])

    return Specfile1


def create_spec_2_model(Specfile1):

    transform_spec1_to_spec2(Specfile1)
    Specfile1 = transform_spec2_to_spec1(Specfile2)
    print(json.dumps(Specfile1, default=lambda o: o.__dict__, sort_keys=True))

    sys.exit(0)
