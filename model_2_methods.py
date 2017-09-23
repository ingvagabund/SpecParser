from __future__ import print_function
import re
from copy import deepcopy

from abstract_model import SpecfileClass, BlockTypes
from model_methods import create_metastring

Specfile2 = SpecfileClass('Specfile 2.0')
list_of_blocks = []
metastring_list = []
Specfile1_metastring_list = []


number_of_blocktypes = len([a for a in dir(BlockTypes) if not a.startswith('__')])
for _ in range(number_of_blocktypes):
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


def transform_spec1_to_spec2(Specfile1_block_list, package_name):

    global Specfile1_metastring_list

    for block in Specfile1_block_list:
        if package_name is not None:
            block['package'] = package_name
        metastring1 = Specfile1_metastring_list[0]
        Specfile1_metastring_list = Specfile1_metastring_list[1:]
        block_metastring_list = metastring1.split('%')
        sequence_number = len(list_of_blocks[block['block_type']])
        Specfile2.metastring += '#' + str(block['block_type']) + str(sequence_number)
        list_of_blocks[block['block_type']].append(block)

        if 'content' in block and block['block_type'] in [3]:
            Specfile2.metastring += metastring1[:metastring1.find('%3')]
            metastring1 = '#' + str(block['block_type']) + str(sequence_number) + metastring1[metastring1.find('%3'):]
            
            transform_spec1_to_spec2(block['content'], None)
            del block['content']

        elif 'content' in block and block['block_type'] in [6]:
            if not 'else_body' in block or block['else_body'] == []:
                number_of_next_item = 5
            else:
                number_of_next_item = 3

            Specfile2.metastring += metastring1[:metastring1.find('%' + str(number_of_next_item))]
            metastring1 = '#' + str(block['block_type']) + str(sequence_number) + metastring1[metastring1.find('%' + str(number_of_next_item)):]

            transform_spec1_to_spec2(block['content'], None)
            del block['content']

        if 'else_body' in block:
            if block['else_body'] != []:
                Specfile2.metastring += metastring1[:metastring1.find('%5')]
                metastring1 = '#' + str(block['block_type']) + str(sequence_number) + metastring1[metastring1.find('%5'):]

                transform_spec1_to_spec2(block['else_body'], None)
            del block['else_body']

        if 'keyword' in block and block['keyword'] == 'package':
            Specfile2.metastring += metastring1[:metastring1.find('%4')]
            metastring1 = '#' + str(block['block_type']) + str(sequence_number) + metastring1[metastring1.find('%4'):]

            transform_spec1_to_spec2(block['content'], block['subname'])
            del block['content']

        elif 'keyword' in block and block['keyword'] == 'files':    # TODO
            block['content'] = re.findall(r'.*\s*', block['content'])
            used_file_fields = 0
            metastring = ''
            to_be_removed = []
            first = False

            for idx, single_file in enumerate(block['content']):
                if single_file == '':
                    to_be_removed.append(idx)
                elif single_file[0] == '#':
                    metastring += '#5' + str(len(list_of_blocks[5]))
                    list_of_blocks[5].append({'block_type': 5, 'content': block['content'][idx], 'files': block['name'], 'position': idx})
                    metastring += create_metastring(list_of_blocks[5][-1], list_of_blocks[5][-1]['block_type'])
                    to_be_removed.append(idx)
                    first = True
                else:
                    if first:
                        metastring += '#' + str(block['block_type']) + str(sequence_number)
                        first = False
                    metastring += block['content'][idx][:len(block['content'][idx]) - len(block['content'][idx].lstrip())]
                    metastring += '%4' + str(used_file_fields)
                    metastring += block['content'][idx][len(block['content'][idx].rstrip()):]
                    block['content'][idx] = block['content'][idx][len(block['content'][idx]) - len(block['content'][idx].lstrip()):len(block['content'][idx].rstrip())]
                    used_file_fields += 1

            for record in reversed(to_be_removed):
                del block['content'][record]

            metastring1 = metastring1.replace('%4', metastring)

        # if 'end_keyword' in block and block['end_keyword'] != '':
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


def get_files_block_pos(block_list, wanted_block):

    count = 0
    for block in block_list:
        if 'keyword' in block and block['keyword'] == 'files':
            if wanted_block['files'] is None:
                if (('name' in block and block['name'] is None) or 'name' not in block) and \
                (('subname' in block and block['subname'] is None) or 'subname' not in block):
                    return count
            elif ('name' in block and block['name'] == wanted_block['files']) or ('name' not in block and 'files' not in wanted_block):
                return count
        count += 1
    return -1


def process_blocks():

    global metastring_list
    block_list = []
    metastring1 = ''

    for idx, metastring2 in enumerate(metastring_list):
        processed_already = False

        if int(metastring2[0]) == 6 and int(metastring2[metastring2.find('%') + 1]) != 0:
            pos_of_next_field = metastring1.find('#', metastring1.find('#' + metastring2[:metastring2.find('%')]) + 1)
            metastring1 = metastring1[:pos_of_next_field] + metastring2[metastring2.find('%'):] + metastring1[pos_of_next_field:]
        elif int(metastring2[0]) == 1 and list_of_blocks[int(metastring2[0])][int(metastring2[1:metastring2.find('%')])]['keyword'] == 'package':
            if int(metastring2[metastring2.find('%') + 1]) == 0:
                metastring1 += '#' + metastring2
            else:
                pos_of_next_field = metastring1.find('#', metastring1.find('#' + metastring2[:metastring2.find('%')]) + 1)
                metastring1 = metastring1[:pos_of_next_field] + metastring2[metastring2.find('%'):] + metastring1[pos_of_next_field:]
        elif int(metastring2[0]) == 3 and int(metastring2[metastring2.find('%') + 1]) != 0:
            pos_of_next_field = metastring1.find('#', metastring1.find('#' + metastring2[:metastring2.find('%')]) + 1)
            metastring1 = metastring1[:pos_of_next_field] + metastring2[metastring2.find('%'):] + metastring1[pos_of_next_field:]

            pos = get_outer_block_pos(block_list, list_of_blocks[int(metastring2[0])][int(metastring2[1:metastring2.find('%')])])
            list_of_blocks[int(metastring2[0])][int(metastring2[1:metastring2.find('%')])]['content'] = [block_list[pos+1]]
            block_list = block_list[:pos] + block_list[pos + 2:]
        else:
            metastring1 += '#' + metastring2

        if 'package' in list_of_blocks[int(metastring2[0])][int(metastring2[1:metastring2.find('%')])]:
            del list_of_blocks[int(metastring2[0])][int(metastring2[1:metastring2.find('%')])]['package']

        if int(metastring2[0]) == 1 and list_of_blocks[int(metastring2[0])][int(metastring2[1:metastring2.find('%')])]['keyword'] == 'package':
            if int(metastring2[metastring2.find('%') + 1]) == 4:
                pos = get_outer_block_pos(block_list, list_of_blocks[int(metastring2[0])][int(metastring2[1:metastring2.find('%')])])
                list_of_blocks[int(metastring2[0])][int(metastring2[1:metastring2.find('%')])]['content'] = deepcopy(block_list[pos+1:])
                block_list = block_list[:pos]

        elif int(metastring2[0]) == 1 and list_of_blocks[int(metastring2[0])][int(metastring2[1:metastring2.find('%')])]['keyword'] == 'files':
            merged_content = ''

            if isinstance(list_of_blocks[int(metastring2[0])][int(metastring2[1:metastring2.find('%')])]['content'], list):
                last_field_id = len(list_of_blocks[int(metastring2[0])][int(metastring2[1:metastring2.find('%')])]['content']) - 1
            else:
                last_field_id = 1 
            file_records = re.findall(r'%4[^%]*', metastring2)
            first_record = True
            original_files_line_id = 0
            files_line_id = 0
            processed_already = False
            subtract = 0

            for single_file in file_records:
                files_line_id = int(re.match(r'\d+', single_file[2:]).group())
                original_files_line_id = files_line_id

                if first_record and files_line_id != 0:
                    subtract = files_line_id - 1
                    processed_already = True
                files_line_id -= subtract

                if first_record:
                    first_record = False

                if len(list_of_blocks[int(metastring2[0])][int(metastring2[1:metastring2.find('%')])]['content']) - 1 >= files_line_id:
                    merged_content += list_of_blocks[int(metastring2[0])][int(metastring2[1:metastring2.find('%')])]['content'][files_line_id]

                if files_line_id != last_field_id:
                    merged_content += single_file[len(str(original_files_line_id)) + 2:]
                else:
                    metastring1 += single_file[len(str(original_files_line_id)) + 2:]

                if files_line_id == 0:
                    metastring1 = metastring1.replace(single_file, '%4')
                elif processed_already and files_line_id == last_field_id:
                    metastring1 = metastring1.replace(re.search(r'\s*#\d+' + single_file, metastring1).group(), '')
                else:
                    metastring1 = metastring1.replace(single_file, '')

            if not processed_already:
                del list_of_blocks[int(metastring2[0])][int(metastring2[1:metastring2.find('%')])]['content'][0:files_line_id]
                list_of_blocks[int(metastring2[0])][int(metastring2[1:metastring2.find('%')])]['content'][0] = merged_content
            else:
                del list_of_blocks[int(metastring2[0])][int(metastring2[1:metastring2.find('%')])]['content'][1:files_line_id + 1]
                list_of_blocks[int(metastring2[0])][int(metastring2[1:metastring2.find('%')])]['content'][0] += merged_content

            if len(list_of_blocks[int(metastring2[0])][int(metastring2[1:metastring2.find('%')])]['content']) == 1:
                list_of_blocks[int(metastring2[0])][int(metastring2[1:metastring2.find('%')])]['content'] = list_of_blocks[int(metastring2[0])][int(metastring2[1:metastring2.find('%')])]['content'][0]

        elif int(metastring2[0]) == 5 and 'files' in list_of_blocks[int(metastring2[0])][int(metastring2[1:metastring2.find('%')])]:

            processed_already = True

            pos = get_files_block_pos(block_list, list_of_blocks[int(metastring2[0])][int(metastring2[1:metastring2.find('%')])])
            if pos != -1:
                comment_metastring = re.findall(r'\s*#5' + metastring2[1:metastring2.find('%')] + r'[^#]*', metastring1)[0]
                pre_comment_whitespace = re.findall(r'[^#]*', comment_metastring)[0]
                post_comment_whitespace = re.search(r'\s*$', comment_metastring).group() #comment_metastring[comment_metastring.find(r'\s*$'):]

                # due to some unicode assignment failures
                tmp = []
                if isinstance(block_list[pos]['content'], list):
                    tmp.append(block_list[pos]['content'][0] + pre_comment_whitespace + list_of_blocks[int(metastring2[0])][int(metastring2[1:metastring2.find('%')])]['content'] + post_comment_whitespace)
                    tmp += block_list[pos]['content'][1:]
                else:
                    tmp.append(block_list[pos]['content'] + pre_comment_whitespace + list_of_blocks[int(metastring2[0])][int(metastring2[1:metastring2.find('%')])]['content'])

                del block_list[pos]['content']
                block_list[pos]['content'] = tmp
                # block_list[pos]['content'][0] += pre_comment_whitespace
                # block_list[pos]['content'][0] += list_of_blocks[int(metastring2[0])][int(metastring2[1:metastring2.find('%')])]['content']
                # block_list[pos]['content'][0] += post_comment_whitespace
                if len(block_list[pos]['content']) == 1:
                    block_list[pos]['content'] = block_list[pos]['content'][0]
                    metastring1 = metastring1.replace(comment_metastring, post_comment_whitespace)
                else:
                    metastring1 = metastring1.replace(comment_metastring, '')

        elif int(metastring2[0]) == 6:
            if int(metastring2[metastring2.find('%') + 1]) == 3 or (int(metastring2[metastring2.find('%') + 1]) == 5 and 'content' not in list_of_blocks[int(metastring2[0])][int(metastring2[1:metastring2.find('%')])]):
                pos = get_outer_block_pos(block_list, list_of_blocks[int(metastring2[0])][int(metastring2[1:metastring2.find('%')])])
                list_of_blocks[int(metastring2[0])][int(metastring2[1:metastring2.find('%')])]['content'] = block_list[pos+1:]
                block_list = block_list[:pos]

            elif int(metastring2[metastring2.find('%') + 1]) == 5:
                pos = get_outer_block_pos(block_list, list_of_blocks[int(metastring2[0])][int(metastring2[1:metastring2.find('%')])])
                list_of_blocks[int(metastring2[0])][int(metastring2[1:metastring2.find('%')])]['else_body'] = block_list[pos+1:]
                block_list = block_list[:pos]

        if not processed_already:
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

    global Specfile1_metastring_list

    metastring_list = Specfile1.metastring.split('#')
    Specfile2.metastring += metastring_list[0]
    Specfile1_metastring_list = metastring_list[1:]
    transform_spec1_to_spec2(Specfile1.block_list, None)
