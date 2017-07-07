from __future__ import print_function
from pprint import pprint
import ctypes



prettyprint_headervalue_position = 16
prettyprint_macroname_position = 20


class BlockTypes(object):

    HeaderTagType = 0
    SectionTagType = 1
    MacroDefinitionType = 2
    MacroConditionType = 3
    MacroUndefinitionType = 4
    CommentType = 5
    ConditionType = 6



keys_list = [
    ['key', 'option', 'content'], 
    ['keyword', 'name', 'parameters', 'subname', 'content'], 
    ['keyword', 'name', 'options', 'body'], 
    ['condition', 'name', 'content', 'ending'],
    ['keyword', 'name'], 
    ['content'], 
    ['keyword', 'expression', 'content', 'else_keyword', 'else_body', 'end_keyword']
]



class SpecfileClass(object):

    def __init__(self):
        self.beginning = ""
        self.end = ""
        self.block_list = []
        self.metastring = ""
