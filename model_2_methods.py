from __future__ import print_function
import json
import sys

from abstract_model import *


Specfile2 = SpecfileClass('Specfile 2.0')
list_of_blocks = []
metastring_list = []


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


def transform_spec1_to_spec2(Specfile1_block_list, metastring_list):

    for block, metastring1 in zip(Specfile1_block_list, metastring_list):
        block_metastring_list = metastring1.split('%')
        Specfile2.metastring += '#' + str(block['block_type']) + str(len(list_of_blocks[block['block_type']]))
        list_of_blocks[block['block_type']].append(block)

        if 'content' in block and block['block_type'] in [6]:
            if not 'else_body' in block or block['else_body'] == []:
                Specfile2.metastring += metastring1[:metastring1.find('%5')]
                metastring1 = '#' + str(block['block_type']) + str(len(list_of_blocks[block['block_type']])-1) + metastring1[metastring1.find('%5'):]
            else:
                Specfile2.metastring += metastring1[:metastring1.find('%3')]
                metastring1 = '#' + str(block['block_type']) + str(len(list_of_blocks[block['block_type']])-1) + metastring1[metastring1.find('%3'):]                

            transform_spec1_to_spec2(block['content'], metastring_list[1:])
            del block['content']

        if 'else_body' in block and block['else_body'] != []:
            Specfile2.metastring += metastring1[:metastring1.find('%5')]
            metastring1 = '#' + str(block['block_type']) + str(len(list_of_blocks[block['block_type']])-1) + metastring1[metastring1.find('%5'):]
            transform_spec1_to_spec2(block['else_body'], metastring_list[1:])
            del block['else_body']

        Specfile2.metastring += block_metastring_list[0] + metastring1
        metastring_list = metastring_list[1:]

    add_blocks_to_specfile()


def process_inner_blocks(): # remove?
    
    global metastring_list

    block_list = []
    metastring1 = ""
    print("\n\n"+ str(metastring_list))

    for metastring2 in metastring_list:
        if int(metastring2[0]) == 6 and int(metastring2[metastring2.find('%') + 1]) == 0:
            (list_of_blocks[int(metastring2[0])][int(metastring2[1:metastring2.find('%')])]['content'], metastring1) = process_inner_blocks()            
        elif int(metastring2[0]) == 6:
             break

        metastring_list = metastring_list[1:]
        metastring1 += '#' + metastring2[metastring2.find('%'):]
        block_list.append(list_of_blocks[int(metastring2[0])][int(metastring2[1:metastring2.find('%')])])

    print(str(block_list)+ "\n\n")

    return (block_list, metastring1)



def get_outer_block_pos(block_list, wanted_block):
    
    count = 0

    for block in block_list:
        if block == wanted_block:
            return count
        count += 1
    return -1


def process_blocks(outer_block_id):

    global metastring_list

    block_list = []
    metastring1 = ""

    for metastring2 in metastring_list:
        # if int(metastring2[0]) == 6 and int(metastring2[:metastring2.find('%')]) == outer_block_id:
        #     break
    
        metastring_list = metastring_list[1:]
        metastring1 += '#' + metastring2[metastring2.find('%'):]

        if int(metastring2[0]) == 6 and int(metastring2[metastring2.find('%') + 1]) == 5:
            pos = get_outer_block_pos(block_list, list_of_blocks[int(metastring2[0])][int(metastring2[1:metastring2.find('%')])])
            list_of_blocks[int(metastring2[0])][int(metastring2[1:metastring2.find('%')])]['content'] = block_list[pos+1:]
            block_list = block_list[:pos-1]

        # if int(metastring2[0]) == 6 and int(metastring2[metastring2.find('%') + 1]) == 0:
        #     (list_of_blocks[int(metastring2[0])][int(metastring2[1:metastring2.find('%')])]['content'], metastring1) = process_blocks(metastring2[:metastring2.find('%')])
        
        # elif int(metastring2[0]) == 6 and int(metastring2[metastring2.find('%') + 1]) == 3:
        #     (list_of_blocks[int(metastring2[0])][int(metastring2[1:metastring2.find('%')])]['else_body'], metastring1) = process_blocks(metastring2[:metastring2.find('%')])
        #     # list_of_blocks[int(metastring2[0])][int(metastring2[1:metastring2.find('%')])]['content']

        block_list.append(list_of_blocks[int(metastring2[0])][int(metastring2[1:metastring2.find('%')])])

    return (block_list, metastring1)


def transform_spec2_to_spec1(Specfile2):

    global metastring_list

    create_blocks_from_specfile()
    Specfile1 = SpecfileClass('Specfile 1.0')
    metastring_list = Specfile2.metastring.split('#')
    Specfile1.metastring = metastring_list[0]
    metastring_list = metastring_list[1:]

    (Specfile1.block_list, Specfile1.metastring) = process_blocks(None)
    # print(json.dumps(Specfile1, default=lambda o: o.__dict__, sort_keys=True))

    return Specfile1


def create_spec_2_model(Specfile1):

    global list_of_blocks
    metastring_list = Specfile1.metastring.split('#')

    Specfile2.metastring += metastring_list[0]

    transform_spec1_to_spec2(Specfile1.block_list, metastring_list[1:])
    # Specfile1 = transform_spec2_to_spec1(Specfile2)
    # print(json.dumps(Specfile2.metastring, default=lambda o: o.__dict__, sort_keys=True))

    # sys.exit(0)
