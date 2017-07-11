from __future__ import print_function
import sys, re
from yapps import runtime
import argparse, json, io

from abstract_model import SpecfileClass, BlockTypes


class Block(object):

    def __init__(self, type):
        self.block_type = type


Specfile = SpecfileClass('Parser')


def open_file(input_filepath):
    
    if input_filepath == None:
        input_filepath = raw_input("Enter path to a specfile or json file: ")

    try:
        input_file = io.open(input_filepath, mode='r', encoding="utf-8")
        input_data = input_file.read()
        input_file.close()
        return input_data
    except IOError:
        print('ERROR: Cannot open input file ' + input_filepath + '!')
        sys.exit(3)



# Begin -- grammar generated by Yapps
class SpecfileParserScanner(runtime.Scanner):
    patterns = [
        ('END', re.compile('\\s*$')),
        ('BEGINNING', re.compile('\\s*')),
        ('TAG_KEY', re.compile('(?i)(NAME|VERSION|RELEASE|SUMMARY|LICENSE|URL|BUILDREQUIRES(\\(\\S+\\))?|REQUIRES(\\(\\S+\\))?|PREFIX|GROUP|BUILDROOT|EXCLUDEARCH|EXCLUSIVEARCH|CONFLICTS|BUILDARCH|PROVIDES|PREP|PRE|PREUN|POST|POSTUN)\\s*|(SOURCE|PATCH)\\d*\\s*')),
        ('COLON', re.compile('\\:')),
        ('TAG_VALUE', re.compile('.*\\s*')),
        ('COMMENT', re.compile('\\#.+\\s*')),
        ('PERCENT_SIGN', re.compile('%')),
        ('DASH', re.compile('\\-')),
        ('PARAMETERS', re.compile('\\S+[ \\t\\r\\f\\v]*')),
        ('NAME', re.compile('(?!\\-)\\S+[ \\t\\r\\f\\v]*')),
        ('NEWLINE', re.compile('\\n')),
        ('MACRO_DEF_KEYWORD', re.compile('(?i)(define|global)\\s*')),
        ('MACRO_UNDEF_KEYWORD', re.compile('(?i)undefine\\s*')),
        ('MACRO_NAME', re.compile('\\S+?(?=[\\(|\\:|\\s])\\s*')),
        ('MACRO_OPTIONS', re.compile('\\(.*?\\)\\s*')),
        ('MACRO_BODY', re.compile('(?!\\().*\\s*')),
        ('MACRO_CONDITION_BODY', re.compile('(?!\\().*(?=\\}\\s*)')),
        ('LEFT_PARENTHESIS', re.compile('\\{')),
        ('RIGHT_PARENTHESIS', re.compile('\\}')),
        ('EXCLAMATION_MARK', re.compile('\\!')),
        ('QUESTION_MARK', re.compile('\\?')),
        ('WHITESPACE', re.compile('[ \\t\\n\\r\\f\\v]*')),
        ('CONDITION_BEG_KEYWORD', re.compile('(?i)(if|ifarch|ifos|ifnarch|ifnos)\\s*')),
        ('CONDITION_ELSE_KEYWORD', re.compile('(?i)else\\s*')),
        ('CONDITION_EXPRESSION', re.compile('.*\\s*')),
        ('CONDITION_BODY', re.compile('(?!(endif|if|else))[\\W\\w]*?(?=%(else|endif|if))')),
        ('CONDITION_END_KEYWORD', re.compile('(?i)endif\\s*')),
        ('SECTION_KEY', re.compile('(?i)(DESCRIPTION|PREP|PREUN|PRE|POSTUN|POST|FILES)[ \\t\\r\\f\\v]*')),
        ('SECTION_KEY_NOPARSE', re.compile('(?i)(BUILD|CHECK|INSTALL|CLEAN)[ \\t\\r\\f\\v]*')),
        ('SECTION_CONTENT', re.compile('(?i)(?!(NAME|VERSION|RELEASE|SUMMARY|LICENSE|URL|SOURCE|PATCH|BUILDREQUIRES|REQUIRES|PREFIX|GROUP|BUILDROOT|EXCLUDEARCH|EXCLUSIVEARCH|CONFLICTS|BUILDARCH|PROVIDES)\\:|%(DESCRIPTION|PREP|BUILD|CHECK|INSTALL|FILES|PACKAGE|CHANGELOG|PRE|PREUN|POST|POSTUN)|%(define|global|undefine)|%(if|ifarch|ifos|ifnarch|ifnos|else|endif))[\\w\\W]+?(?=(NAME|VERSION|RELEASE|SUMMARY|LICENSE|URL|SOURCE|PATCH|BUILDREQUIRES|REQUIRES|PREFIX|GROUP|BUILDROOT|EXCLUDEARCH|EXCLUSIVEARCH|CONFLICTS|BUILDARCH|PROVIDES)\\:|%(DESCRIPTION|PREP|BUILD|CHECK|INSTALL|FILES|PACKAGE|CHANGELOG|PRE|PREUN|POST|POSTUN)|%(define|global|undefine)|%(if|ifarch|ifos|ifnarch|ifnos|else|endif)|%\\{!\\?|%\\{\\?|$)\\s*')),
        ('SECTION_CONTENT_NOPARSE', re.compile('(?i)(?!(NAME|VERSION|RELEASE|SUMMARY|LICENSE|URL|SOURCE|PATCH|BUILDREQUIRES|REQUIRES|PREFIX|GROUP|BUILDROOT|EXCLUDEARCH|EXCLUSIVEARCH|CONFLICTS|BUILDARCH|PROVIDES)\\:|%(DESCRIPTION|PREP|BUILD|CHECK|INSTALL|FILES|PACKAGE|CHANGELOG|PRE|PREUN|POST|POSTUN))[\\w\\W]+?(?=(NAME|VERSION|RELEASE|SUMMARY|LICENSE|URL|SOURCE|PATCH|BUILDREQUIRES|REQUIRES|PREFIX|GROUP|BUILDROOT|EXCLUDEARCH|EXCLUSIVEARCH|CONFLICTS|BUILDARCH|PROVIDES)\\:|%(DESCRIPTION|PREP|BUILD|CHECK|INSTALL|FILES|PACKAGE|CHANGELOG|PRE|PREUN|POST|POSTUN)|$)\\s*')),
        ('CHANGELOG_KEYWORD', re.compile('(?i)CHANGELOG\\s*')),
        ('SINGLE_LOG', re.compile('\\*[\\W\\w]*?(?=\\*|$)')),
        ('PACKAGE_KEYWORD', re.compile('(?i)PACKAGE[ \\t\\r\\f\\v]*')),
        ('PACKAGE_CONTENT', re.compile('(?i)[\\W\\w]*?(?=%(PACKAGE|PREP|BUILD|INSTALL|CHECK|PRE|PREUN|POST|POSTUN)|$)\\s*')),
    ]
    def __init__(self, str,*args,**kw):
        runtime.Scanner.__init__(self,None,{},str,*args,**kw)

class SpecfileParser(runtime.Parser):
    Context = runtime.Context
    def goal(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'goal', [])
        begin = self.begin(_context)
        spec_file = self.spec_file(_context)
        END = self._scan('END', context=_context)
        Specfile.end = END

    def begin(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'begin', [])
        BEGINNING = self._scan('BEGINNING', context=_context)
        Specfile.beginning = BEGINNING

    def spec_file(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'spec_file', [])
        header = self.header(_context)
        if self._peek('PERCENT_SIGN', 'END', 'COMMENT', 'TAG_KEY', context=_context) in ['PERCENT_SIGN', 'COMMENT']:
            rest = self.rest(_context)

    def header(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'header', [])
        while self._peek('PERCENT_SIGN', 'END', 'COMMENT', 'TAG_KEY', context=_context) != 'END':
            tag = self.tag(_context)

    def tag(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'tag', [])
        _token = self._peek('PERCENT_SIGN', 'TAG_KEY', 'COMMENT', context=_context)
        if _token == 'TAG_KEY':
            header_tag = self.header_tag(_context)
            Specfile.block_list.append(header_tag)
        elif _token == 'COMMENT':
            commentary = self.commentary(_context)
            Specfile.block_list.append(commentary)
        else: # == 'PERCENT_SIGN'
            PERCENT_SIGN = self._scan('PERCENT_SIGN', context=_context)
            keyword = self.keyword(_context)

    def header_tag(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'header_tag', [])
        TAG_KEY = self._scan('TAG_KEY', context=_context)
        COLON = self._scan('COLON', context=_context)
        TAG_VALUE = self._scan('TAG_VALUE', context=_context)
        block = Block(BlockTypes.HeaderTagType)
        if TAG_KEY.find('(') == -1: block.key = TAG_KEY; block.option = None
        else: block.key = TAG_KEY[:TAG_KEY.find('(')]; block.option = TAG_KEY[TAG_KEY.find('(')+1:-1]
        block.content = TAG_VALUE
        return block

    def rest(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'rest', [])
        _token = self._peek('PERCENT_SIGN', 'COMMENT', context=_context)
        if _token == 'PERCENT_SIGN':
            PERCENT_SIGN = self._scan('PERCENT_SIGN', context=_context)
            keyword = self.keyword(_context)
        else: # == 'COMMENT'
            commentary = self.commentary(_context)
            Specfile.block_list.append(commentary)

    def keyword(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'keyword', [])
        _token = self._peek('LEFT_PARENTHESIS', 'SECTION_KEY', 'SECTION_KEY_NOPARSE', 'PACKAGE_KEYWORD', 'CHANGELOG_KEYWORD', 'MACRO_DEF_KEYWORD', 'MACRO_UNDEF_KEYWORD', 'CONDITION_BEG_KEYWORD', context=_context)
        if _token not in ['LEFT_PARENTHESIS', 'MACRO_DEF_KEYWORD', 'MACRO_UNDEF_KEYWORD', 'CONDITION_BEG_KEYWORD']:
            section = self.section(_context)
            Specfile.block_list.append(section)
        elif _token == 'MACRO_DEF_KEYWORD':
            macro_definition = self.macro_definition(_context)
            Specfile.block_list.append(macro_definition)
        elif _token == 'MACRO_UNDEF_KEYWORD':
            macro_undefine = self.macro_undefine(_context)
            Specfile.block_list.append(macro_undefine)
        elif _token == 'CONDITION_BEG_KEYWORD':
            condition_definition = self.condition_definition(_context)
            Specfile.block_list.append(condition_definition)
        else: # == 'LEFT_PARENTHESIS'
            LEFT_PARENTHESIS = self._scan('LEFT_PARENTHESIS', context=_context)
            macro_condition = self.macro_condition(_context)
            RIGHT_PARENTHESIS = self._scan('RIGHT_PARENTHESIS', context=_context)
            WHITESPACE = self._scan('WHITESPACE', context=_context)
            macro_condition.ending = WHITESPACE
            Specfile.block_list.append(macro_condition)

    def macro_definition(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'macro_definition', [])
        MACRO_DEF_KEYWORD = self._scan('MACRO_DEF_KEYWORD', context=_context)
        MACRO_NAME = self._scan('MACRO_NAME', context=_context)
        if self._peek('MACRO_OPTIONS', 'MACRO_BODY', context=_context) == 'MACRO_OPTIONS':
            MACRO_OPTIONS = self._scan('MACRO_OPTIONS', context=_context)
        MACRO_BODY = self._scan('MACRO_BODY', context=_context)
        block = Block(BlockTypes.MacroDefinitionType)
        block.name = MACRO_NAME
        block.keyword = MACRO_DEF_KEYWORD
        if 'MACRO_OPTIONS' in locals(): block.options = MACRO_OPTIONS
        else: block.options = None
        block.body = MACRO_BODY
        return block

    def macro_condition(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'macro_condition', [])
        if self._peek('EXCLAMATION_MARK', 'QUESTION_MARK', context=_context) == 'EXCLAMATION_MARK':
            EXCLAMATION_MARK = self._scan('EXCLAMATION_MARK', context=_context)
        QUESTION_MARK = self._scan('QUESTION_MARK', context=_context)
        MACRO_NAME = self._scan('MACRO_NAME', context=_context)
        COLON = self._scan('COLON', context=_context)
        MACRO_CONDITION_BODY = self._scan('MACRO_CONDITION_BODY', context=_context)
        block = Block(BlockTypes.MacroConditionType)
        block.name = MACRO_NAME
        if 'EXCLAMATION_MARK' in locals(): block.condition = EXCLAMATION_MARK + QUESTION_MARK
        else: block.condition = QUESTION_MARK
        block.content = MACRO_CONDITION_BODY
        return block

    def commentary(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'commentary', [])
        COMMENT = self._scan('COMMENT', context=_context)
        block = Block(BlockTypes.CommentType)
        block.content = COMMENT
        return block

    def changelog(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'changelog', [])
        SINGLE_LOG = self._scan('SINGLE_LOG', context=_context)
        return SINGLE_LOG

    def condition_definition(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'condition_definition', [])
        CONDITION_BEG_KEYWORD = self._scan('CONDITION_BEG_KEYWORD', context=_context)
        CONDITION_EXPRESSION = self._scan('CONDITION_EXPRESSION', context=_context)
        CONDITION_BODY = self._scan('CONDITION_BODY', context=_context)
        PERCENT_SIGN = self._scan('PERCENT_SIGN', context=_context)
        block = Block(BlockTypes.ConditionType)
        block.keyword = CONDITION_BEG_KEYWORD
        block.expression = CONDITION_EXPRESSION
        block.content = []
        count = len(Specfile.block_list)
        parse('spec_file', CONDITION_BODY)
        if Specfile.block_list[count:] not in block.content: block.content += Specfile.block_list[count:]
        Specfile.block_list = Specfile.block_list[:count]
        block.else_body = []
        while self._peek('CONDITION_ELSE_KEYWORD', 'CONDITION_END_KEYWORD', 'CONDITION_BEG_KEYWORD', 'CONDITION_BODY', context=_context) in ['CONDITION_BEG_KEYWORD', 'CONDITION_BODY']:
            _token = self._peek('CONDITION_BEG_KEYWORD', 'CONDITION_BODY', context=_context)
            if _token == 'CONDITION_BEG_KEYWORD':
                condition_definition = self.condition_definition(_context)
                if block.content[-1].block_type == BlockTypes.SectionTagType and 'package' in block.content[-1].keyword and condition_definition not in block.content[-1].content: block.content[-1].content.append(condition_definition)
                elif condition_definition not in block.content: block.content.append(condition_definition)
            else: # == 'CONDITION_BODY'
                body = self.body(_context)
                count = len(Specfile.block_list)
                parse('spec_file', body)
                if block.content[-1].block_type == BlockTypes.SectionTagType and 'package' in block.content[-1].keyword and Specfile.block_list[count:] not in block.content[-1].content: block.content[-1].content += Specfile.block_list[count:]
                elif Specfile.block_list[count:] not in block.content: block.content += Specfile.block_list[count:]
                Specfile.block_list = Specfile.block_list[:count]
            if self._peek('PERCENT_SIGN', 'CONDITION_ELSE_KEYWORD', 'CONDITION_BEG_KEYWORD', 'CONDITION_BODY', 'CONDITION_END_KEYWORD', context=_context) == 'PERCENT_SIGN':
                PERCENT_SIGN = self._scan('PERCENT_SIGN', context=_context)
        if self._peek('CONDITION_ELSE_KEYWORD', 'CONDITION_END_KEYWORD', 'CONDITION_BEG_KEYWORD', 'CONDITION_BODY', context=_context) == 'CONDITION_ELSE_KEYWORD':
            CONDITION_ELSE_KEYWORD = self._scan('CONDITION_ELSE_KEYWORD', context=_context)
            condition_else_body = self.condition_else_body(_context)
            PERCENT_SIGN = self._scan('PERCENT_SIGN', context=_context)
            if 'condition_else_body' in locals(): count = len(Specfile.block_list); parse('spec_file', condition_else_body); block.else_body += Specfile.block_list[count:]; Specfile.block_list = Specfile.block_list[:count]; del condition_else_body
            while self._peek('CONDITION_BEG_KEYWORD', 'CONDITION_BODY', 'CONDITION_END_KEYWORD', context=_context) != 'CONDITION_END_KEYWORD':
                _token = self._peek('CONDITION_BEG_KEYWORD', 'CONDITION_BODY', context=_context)
                if _token == 'CONDITION_BEG_KEYWORD':
                    condition_else_inner = self.condition_else_inner(_context)
                else: # == 'CONDITION_BODY'
                    else_body = self.else_body(_context)
                if 'else_body' in locals(): count = len(Specfile.block_list); parse('spec_file', else_body); block.else_body += Specfile.block_list[count:]; Specfile.block_list = Specfile.block_list[:count]; del else_body
                if 'condition_else_inner' in locals() and condition_else_inner not in block.else_body: block.else_body.append(condition_else_inner); del condition_else_inner
                if self._peek('PERCENT_SIGN', 'CONDITION_BEG_KEYWORD', 'CONDITION_BODY', 'CONDITION_END_KEYWORD', context=_context) == 'PERCENT_SIGN':
                    PERCENT_SIGN = self._scan('PERCENT_SIGN', context=_context)
        CONDITION_END_KEYWORD = self._scan('CONDITION_END_KEYWORD', context=_context)
        block.end_keyword = CONDITION_END_KEYWORD
        if 'CONDITION_ELSE_KEYWORD' in locals(): block.else_keyword = CONDITION_ELSE_KEYWORD
        else: block.else_keyword = None
        return block

    def condition_else_body(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'condition_else_body', [])
        CONDITION_BODY = self._scan('CONDITION_BODY', context=_context)
        return CONDITION_BODY

    def condition_else_inner(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'condition_else_inner', [])
        condition_definition = self.condition_definition(_context)
        return condition_definition

    def else_body(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'else_body', [])
        CONDITION_BODY = self._scan('CONDITION_BODY', context=_context)
        return CONDITION_BODY

    def body(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'body', [])
        CONDITION_BODY = self._scan('CONDITION_BODY', context=_context)
        return CONDITION_BODY

    def section(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'section', [])
        _token = self._peek('SECTION_KEY', 'SECTION_KEY_NOPARSE', 'PACKAGE_KEYWORD', 'CHANGELOG_KEYWORD', context=_context)
        if _token == 'SECTION_KEY':
            SECTION_KEY = self._scan('SECTION_KEY', context=_context)
            if self._peek('DASH', 'NAME', 'NEWLINE', context=_context) == 'NAME':
                option = self.option(_context)
            if self._peek('DASH', 'NAME', 'NEWLINE', context=_context) == 'DASH':
                DASH = self._scan('DASH', context=_context)
                PARAMETERS = self._scan('PARAMETERS', context=_context)
            if self._peek('NAME', 'NEWLINE', context=_context) == 'NAME':
                NAME = self._scan('NAME', context=_context)
            NEWLINE = self._scan('NEWLINE', context=_context)
            SECTION_CONTENT = self._scan('SECTION_CONTENT', context=_context)
            block = Block(BlockTypes.SectionTagType)
            block.keyword = SECTION_KEY
            block.content = NEWLINE + SECTION_CONTENT
            if 'PARAMETERS' in locals(): block.parameters = PARAMETERS
            else: block.parameters = None
            if 'NAME' in locals(): block.subname = NAME
            else: block.subname = None
            if 'option' in locals(): block.name = option
            else: block.name = None
            return block
        elif _token == 'SECTION_KEY_NOPARSE':
            SECTION_KEY_NOPARSE = self._scan('SECTION_KEY_NOPARSE', context=_context)
            if self._peek('DASH', 'NAME', 'NEWLINE', context=_context) == 'NAME':
                option = self.option(_context)
            if self._peek('DASH', 'NAME', 'NEWLINE', context=_context) == 'DASH':
                DASH = self._scan('DASH', context=_context)
                PARAMETERS = self._scan('PARAMETERS', context=_context)
            if self._peek('NAME', 'NEWLINE', context=_context) == 'NAME':
                NAME = self._scan('NAME', context=_context)
            NEWLINE = self._scan('NEWLINE', context=_context)
            SECTION_CONTENT_NOPARSE = self._scan('SECTION_CONTENT_NOPARSE', context=_context)
            block = Block(BlockTypes.SectionTagType)
            block.keyword = SECTION_KEY_NOPARSE
            block.content = NEWLINE + SECTION_CONTENT_NOPARSE
            if 'PARAMETERS' in locals(): block.parameters = PARAMETERS
            else: block.parameters = None
            if 'NAME' in locals(): block.subname = NAME
            else: block.subname = None
            if 'option' in locals(): block.name = option
            else: block.name = None
            return block
        elif _token == 'PACKAGE_KEYWORD':
            count = len(Specfile.block_list)
            PACKAGE_KEYWORD = self._scan('PACKAGE_KEYWORD', context=_context)
            if self._peek('DASH', 'NAME', 'NEWLINE', context=_context) == 'DASH':
                DASH = self._scan('DASH', context=_context)
                PARAMETERS = self._scan('PARAMETERS', context=_context)
            if self._peek('NAME', 'NEWLINE', context=_context) == 'NAME':
                NAME = self._scan('NAME', context=_context)
            NEWLINE = self._scan('NEWLINE', context=_context)
            PACKAGE_CONTENT = self._scan('PACKAGE_CONTENT', context=_context)
            block = Block(BlockTypes.SectionTagType)
            block.keyword = PACKAGE_KEYWORD
            if 'NAME' in locals(): block.subname = NAME + NEWLINE
            else: block.subname = NEWLINE
            if 'PARAMETERS' in locals(): block.parameters = PARAMETERS
            else: block.parameters = None
            parse('spec_file', PACKAGE_CONTENT)
            block.content = Specfile.block_list[count:]
            Specfile.block_list = Specfile.block_list[:count]
            return block
        else: # == 'CHANGELOG_KEYWORD'
            block = Block(BlockTypes.SectionTagType)
            block.content = []
            CHANGELOG_KEYWORD = self._scan('CHANGELOG_KEYWORD', context=_context)
            while self._peek('SINGLE_LOG', 'PERCENT_SIGN', 'TAG_KEY', 'COMMENT', 'END', context=_context) == 'SINGLE_LOG':
                changelog = self.changelog(_context)
                block.content.append(changelog)
            block.keyword = CHANGELOG_KEYWORD
            return block

    def option(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'option', [])
        NAME = self._scan('NAME', context=_context)
        return NAME

    def macro_undefine(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'macro_undefine', [])
        MACRO_UNDEF_KEYWORD = self._scan('MACRO_UNDEF_KEYWORD', context=_context)
        MACRO_NAME = self._scan('MACRO_NAME', context=_context)
        block = Block(BlockTypes.MacroUndefinitionType)
        block.keyword = MACRO_UNDEF_KEYWORD
        block.name = MACRO_NAME
        return block


def parse(rule, text):
    P = SpecfileParser(SpecfileParserScanner(text))
    return runtime.wrap_error_reporter(P, rule)

# End -- grammar generated by Yapps


def parse_file(input_filepath):

    inputfile_content = open_file(input_filepath)

    try:
        json_object = json.loads(inputfile_content)
        return inputfile_content
    except ValueError, e:
        parse('goal', inputfile_content)
        return json.dumps(Specfile, default=lambda o: o.__dict__, sort_keys=True)
