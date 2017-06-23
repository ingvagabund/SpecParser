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
