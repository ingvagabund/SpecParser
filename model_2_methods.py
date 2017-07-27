from __future__ import print_function
import json
import sys
import re

from abstract_model import *


Specfile2 = SpecfileClass('Specfile 2.0')
list_of_blocks = []
metastring_list = []
Specfile1_metastring_list = []


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

    global list_of_blocks

    list_of_blocks = []

    list_of_blocks.append(Specfile2.HeaderTags)
    list_of_blocks.append(Specfile2.SectionTags)
    list_of_blocks.append(Specfile2.MacroDefinitions)
    list_of_blocks.append(Specfile2.MacroConditions)
    list_of_blocks.append(Specfile2.MacroUndefinitions)
    list_of_blocks.append(Specfile2.Comments)
    list_of_blocks.append(Specfile2.Conditions)


def transform_spec1_to_spec2(Specfile1_block_list):

    global Specfile1_metastring_list

    for block in Specfile1_block_list:
        metastring1 = Specfile1_metastring_list[0]
        Specfile1_metastring_list = Specfile1_metastring_list[1:]
        block_metastring_list = metastring1.split('%')
        sequence_number = len(list_of_blocks[block['block_type']])
        Specfile2.metastring += '#' + str(block['block_type']) + str(sequence_number)
        list_of_blocks[block['block_type']].append(block)

        if 'content' in block and block['block_type'] in [6]:
            if not 'else_body' in block or block['else_body'] == []:
                number_of_next_item = 5
            else:
                number_of_next_item = 3

            Specfile2.metastring += metastring1[:metastring1.find('%' + str(number_of_next_item))]
            metastring1 = '#' + str(block['block_type']) + str(sequence_number) + metastring1[metastring1.find('%' + str(number_of_next_item)):]                

            transform_spec1_to_spec2(block['content'])
            del block['content']

        if 'else_body' in block and block['else_body'] != []:
            Specfile2.metastring += metastring1[:metastring1.find('%5')]
            metastring1 = '#' + str(block['block_type']) + str(sequence_number) + metastring1[metastring1.find('%5'):]
            
            transform_spec1_to_spec2(block['else_body'])
            del block['else_body']
        
        if 'keyword' in block and block['keyword'] == 'package':
            Specfile2.metastring += metastring1[:metastring1.find('%4')]
            metastring1 = '#' + str(block['block_type']) + str(sequence_number) + metastring1[metastring1.find('%4'):]
            
            transform_spec1_to_spec2(block['content'])
            del block['content']
        
        # if 'end_keyword' in block and block['end_keyword'] != "":
        #     Specfile1_metastring_list = Specfile1_metastring_list[1:]

        Specfile2.metastring += block_metastring_list[0] + metastring1

    add_blocks_to_specfile()


def get_outer_block_pos(block_list, wanted_block):

    count = 0

    for block in block_list:
        if block == wanted_block:
            return count
        count += 1
    return -1


def process_blocks():

    global metastring_list

    block_list = []
    metastring1 = ""

    for metastring2 in metastring_list:

        if int(metastring2[0]) == 6 and int(metastring2[metastring2.find('%') + 1]) != 0:
            pos_of_next_field = metastring1.find('#', metastring1.find('#' + metastring2[:metastring2.find('%')]) + 1)
            metastring1 = metastring1[:pos_of_next_field] + metastring2[metastring2.find('%'):] + metastring1[pos_of_next_field:]
        elif int(metastring2[0]) == 1 and list_of_blocks[int(metastring2[0])][int(metastring2[1:metastring2.find('%')])]['keyword'] == 'package':
            # pos_of_next_field = metastring2.find('#', metastring2.find('#' + metastring2[:metastring2.find('%')]) + 1)
            if int(metastring2[metastring2.find('%') + 1]) == 0:
                metastring1 += "#" + metastring2#[:pos_of_next_field] TODO += ????
            else:
                pos_of_next_field = metastring1.find('#', metastring1.find('#' + metastring2[:metastring2.find('%')]) + 1)            
                metastring1 = metastring1[:pos_of_next_field] + metastring2[metastring2.find('%'):] + metastring1[pos_of_next_field:]
        else:
            metastring1 += '#' + metastring2

        if int(metastring2[0]) == 1 and list_of_blocks[int(metastring2[0])][int(metastring2[1:metastring2.find('%')])]['keyword'] == 'package':
            pos = get_outer_block_pos(block_list, list_of_blocks[int(metastring2[0])][int(metastring2[1:metastring2.find('%')])])
            list_of_blocks[int(metastring2[0])][int(metastring2[1:metastring2.find('%')])]['content'] = block_list[pos+1:]
            block_list = block_list[:pos]

        elif int(metastring2[0]) == 6:
            if int(metastring2[metastring2.find('%') + 1]) == 3 or (int(metastring2[metastring2.find('%') + 1]) == 5 and 'content' not in list_of_blocks[int(metastring2[0])][int(metastring2[1:metastring2.find('%')])]):
                pos = get_outer_block_pos(block_list, list_of_blocks[int(metastring2[0])][int(metastring2[1:metastring2.find('%')])])
                list_of_blocks[int(metastring2[0])][int(metastring2[1:metastring2.find('%')])]['content'] = block_list[pos+1:]
                block_list = block_list[:pos]

            elif int(metastring2[metastring2.find('%') + 1]) == 5:
                pos = get_outer_block_pos(block_list, list_of_blocks[int(metastring2[0])][int(metastring2[1:metastring2.find('%')])])
                list_of_blocks[int(metastring2[0])][int(metastring2[1:metastring2.find('%')])]['else_body'] = block_list[pos+1:]
                block_list = block_list[:pos]

        block_list.append(list_of_blocks[int(metastring2[0])][int(metastring2[1:metastring2.find('%')])])

    return (block_list, metastring1)



def remove_block_ids(metastring):

    return re.sub(r'#\d+%', '#%', metastring)



def transform_spec2_to_spec1(Specfile2):

    global metastring_list

    create_blocks_from_specfile()
    Specfile1 = SpecfileClass('Specfile 1.0')
    metastring_list = Specfile2.metastring.split('#')
    Specfile1.metastring = metastring_list[0]
    metastring_list = metastring_list[1:]

    (Specfile1.block_list, Specfile1.metastring) = process_blocks()
    Specfile1.metastring = remove_block_ids(Specfile1.metastring)

    return Specfile1


def create_spec_2_model(Specfile1):

    global list_of_blocks
    global Specfile1_metastring_list

    metastring_list = Specfile1.metastring.split('#')
    Specfile2.metastring += metastring_list[0]
    Specfile1_metastring_list = metastring_list[1:]
    transform_spec1_to_spec2(Specfile1.block_list)
