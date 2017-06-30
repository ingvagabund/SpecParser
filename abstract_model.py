from __future__ import print_function
from pprint import pprint
import ctypes



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

    def __init__(self, type):
        self.beginning = ""

        if type == 'Parser':
            self.block_list = []

        elif type == 'AbstractModel':
            self.headerTags = []
            self.sectionTags = []
            self.macroDefinitions = []
            self.macroConditions = []
            self.macroUndefinitions = []
            self.comments = []
            self.conditions = []
