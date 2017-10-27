from __future__ import print_function
import json
from abstract_model import RawSpecFile, BlockTypes

class Block(object):

    def _filter(self, data):
        return {k:v for k,v in data.items() if v != None and v != []}

class HeaderTagBlock(Block):
    def __init__(self, key, content, option=None):
        self.block_type = BlockTypes.HeaderTagType
        self.key = key
        self.option = option
        self.content = content
        self.AP = None

    def to_json(self):
        return self._filter({
          "AP": self.AP,
          "block_type": self.block_type,
          "key": self.key,
          "option": self.option,
          "content": self.content,
        })

class SectionBlock(Block):
    def __init__(self, keyword, parameters, name, subname, content):
        self.block_type = BlockTypes.SectionTagType
        self.keyword = keyword
        self.content = content
        self.parameters = parameters
        self.subname = subname
        self.name = name
        self.AP = None

    def to_json(self):
        return self._filter({
          "AP": self.AP,
          "block_type": self.block_type,
          "keyword": self.keyword,
          # TODO(jchaloup): Make sure the content of a general section is always a string
          "content": self.content if isinstance(self.content, basestring) else map(lambda l: l.to_json(), self.content),
          "parameters": self.parameters,
          "subname": self.subname,
          "name": self.name
        })

class PackageBlock(Block):
    def __init__(self, keyword, parameters, subname, content):
        self.block_type = BlockTypes.SectionTagType
        self.keyword = keyword
        self.content = content
        self.parameters = parameters
        self.subname = subname
        self.name = None
        self.AP = None

    def to_json(self):
        return self._filter({
          "AP": self.AP,
          "block_type": self.block_type,
          "keyword": self.keyword,
          "content": map(lambda l: l.to_json(), self.content),
          "parameters": self.parameters,
          "subname": self.subname
        })

class ChangelogBlock(Block):
    def __init__(self, keyword, content):
        self.block_type = BlockTypes.SectionTagType
        self.keyword = keyword
        self.content = content
        self.AP = None

    def to_json(self):
        return self._filter({
          "AP": self.AP,
          "block_type": self.block_type,
          "keyword": self.keyword,
          "content": self.content
        })

class MacroDefinitionBlock(Block):
    def __init__(self, name, keyword, options, body):
        self.block_type = BlockTypes.MacroDefinitionType
        self.name = name
        self.keyword = keyword
        self.options = options
        self.body = body
        self.AP = None

    def to_json(self):
        return self._filter({
          "AP": self.AP,
          "block_type": self.block_type,
          "name": self.name,
          "keyword": self.keyword,
          "options": self.options,
          "body": self.body,
        })

class MacroUndefinitionBlock(Block):
    def __init__(self, name, keyword):
        self.block_type = BlockTypes.MacroUndefinitionType
        self.name = name
        self.keyword = keyword
        self.AP = None

    def to_json(self):
        return self._filter({
          "AP": self.AP,
          "block_type": self.block_type,
          "name": self.name,
          "keyword": self.keyword
        })

class MacroConditionBlock(Block):
    def __init__(self, name, condition, content, ending = None):
        self.block_type = BlockTypes.MacroConditionType
        self.name = name
        self.condition = condition
        self.content = content
        self.ending = ending
        self.AP = None

    def to_json(self):
        return self._filter({
          "AP": self.AP,
          "block_type": self.block_type,
          "name": self.name,
          "condition": self.condition,
          "content": map(lambda l: l.to_json(), self.content),
          "ending": self.ending,
        })

class CommentBlock(Block):
    def __init__(self, content):
        self.block_type = BlockTypes.CommentType
        self.content = content
        self.AP = None

    def to_json(self):
        return self._filter({
          "AP": self.AP,
          "block_type": self.block_type,
          "content": self.content,
        })

class ConditionBlock(Block):
    def __init__(self, keyword, expression, content, else_body, end_keyword, else_keyword):
        self.block_type = BlockTypes.ConditionType
        self.keyword = keyword
        self.expression = expression
        self.content = content
        self.else_body = else_body
        self.end_keyword = end_keyword
        # If else keyword is None, the else_body is ignored
        self.else_keyword = else_keyword
        self.AP = None

    def to_json(self):
        return self._filter({
          "AP": self.AP,
          "block_type": self.block_type,
          "keyword": self.keyword,
          "expression": self.expression,
          "content": map(lambda l: l.to_json(), self.content),
          "else_keyword": self.else_keyword,
          "else_body": map(lambda l: l.to_json(), self.else_body),
          "end_keyword": self.end_keyword,
        })


# Begin -- grammar generated by Yapps

import sys, re
from yapps import runtime

class SpecfileParserScanner(runtime.Scanner):
    patterns = [
        ('END', re.compile('\\s*$')),
        ('BEGINNING', re.compile('\\s*')),
        ('TAG_KEY', re.compile('(?i)(NAME|VERSION|RELEASE|SUMMARY|LICENSE|URL|BUILDREQUIRES(\\(\\S+\\))?|REQUIRES(\\(\\S+\\))?|GROUP|BUILDROOT|EXCLUDEARCH|EXCLUSIVEARCH|CONFLICTS|BUILDARCH|PROVIDES|PRE|PREUN|POST|POSTUN)\\s*|(SOURCE|PATCH)\\d*\\s*')),
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
        ('SECTION_CONTENT', re.compile('(?i)(?!(NAME|VERSION|RELEASE|SUMMARY|LICENSE|URL|SOURCE|PATCH|BUILDREQUIRES|REQUIRES|GROUP|BUILDROOT|EXCLUDEARCH|EXCLUSIVEARCH|CONFLICTS|BUILDARCH|PROVIDES)\\:|%(DESCRIPTION|BUILD|CHECK|INSTALL|FILES|PACKAGE|CHANGELOG|PRE|PREUN|POST|POSTUN)|%(define|global|undefine)|%(if|ifarch|ifos|ifnarch|ifnos|else|endif))[\\w\\W]+?(?=(NAME|VERSION|RELEASE|SUMMARY|LICENSE|URL|SOURCE|PATCH|BUILDREQUIRES|REQUIRES|GROUP|BUILDROOT|EXCLUDEARCH|EXCLUSIVEARCH|CONFLICTS|BUILDARCH|PROVIDES)\\:|%(DESCRIPTION|PREP|BUILD|CHECK|INSTALL|FILES|PACKAGE|CHANGELOG|PRE|PREUN|POST|POSTUN)|%(define|global|undefine)|%(if|ifarch|ifos|ifnarch|ifnos|else|endif)|%\\{!\\?|%\\{\\?|$)\\s*')),
        ('SECTION_CONTENT_NOPARSE', re.compile('(?i)(?!(NAME|VERSION|RELEASE|SUMMARY|LICENSE|URL|SOURCE|PATCH|BUILDREQUIRES|REQUIRES|GROUP|BUILDROOT|EXCLUDEARCH|EXCLUSIVEARCH|CONFLICTS|BUILDARCH|PROVIDES)\\:|%(DESCRIPTION|BUILD|CHECK|INSTALL|FILES|PACKAGE|CHANGELOG|PRE|PREUN|POST|POSTUN))[\\w\\W]+?(?=(NAME|VERSION|RELEASE|SUMMARY|LICENSE|URL|SOURCE|PATCH|BUILDREQUIRES|REQUIRES|GROUP|BUILDROOT|EXCLUDEARCH|EXCLUSIVEARCH|CONFLICTS|BUILDARCH|PROVIDES)\\:|%(DESCRIPTION|PREP|BUILD|CHECK|INSTALL|FILES|PACKAGE|CHANGELOG|PRE|PREUN|POST|POSTUN)|$)\\s*')),
        ('CHANGELOG_KEYWORD', re.compile('(?i)CHANGELOG\\s*')),
        ('SINGLE_LOG', re.compile('\\*[\\W\\w]*?(?=\\*|$)')),
        ('PACKAGE_KEYWORD', re.compile('(?i)PACKAGE[ \\t\\r\\f\\v]*')),
        ('PACKAGE_CONTENT', re.compile('(?i)[\\W\\w]*?(?=%(PACKAGE|PREP|BUILD|INSTALL|CHECK|PRE|PREUN|POST|POSTUN|FILES)|$)\\s*')),
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
        self._rawSpecFile.end = END

    def begin(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'begin', [])
        BEGINNING = self._scan('BEGINNING', context=_context)
        self._rawSpecFile.beginning = BEGINNING

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
            self._rawSpecFile.block_list.append(header_tag)
        elif _token == 'COMMENT':
            commentary = self.commentary(_context)
            self._rawSpecFile.block_list.append(commentary)
        else: # == 'PERCENT_SIGN'
            PERCENT_SIGN = self._scan('PERCENT_SIGN', context=_context)
            keyword = self.keyword(_context)

    def header_tag(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'header_tag', [])
        TAG_KEY = self._scan('TAG_KEY', context=_context)
        COLON = self._scan('COLON', context=_context)
        TAG_VALUE = self._scan('TAG_VALUE', context=_context)
        if TAG_KEY.find('(') == -1: key = TAG_KEY; option = None
        else: key = TAG_KEY[:TAG_KEY.find('(')]; option = TAG_KEY[TAG_KEY.find('(')+1:-1]
        return HeaderTagBlock(key, TAG_VALUE, option)

    def rest(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'rest', [])
        _token = self._peek('PERCENT_SIGN', 'COMMENT', context=_context)
        if _token == 'PERCENT_SIGN':
            PERCENT_SIGN = self._scan('PERCENT_SIGN', context=_context)
            keyword = self.keyword(_context)
        else: # == 'COMMENT'
            commentary = self.commentary(_context)
            self._rawSpecFile.block_list.append(commentary)

    def keyword(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'keyword', [])
        _token = self._peek('LEFT_PARENTHESIS', 'SECTION_KEY', 'SECTION_KEY_NOPARSE', 'PACKAGE_KEYWORD', 'CHANGELOG_KEYWORD', 'MACRO_DEF_KEYWORD', 'MACRO_UNDEF_KEYWORD', 'CONDITION_BEG_KEYWORD', context=_context)
        if _token not in ['LEFT_PARENTHESIS', 'MACRO_DEF_KEYWORD', 'MACRO_UNDEF_KEYWORD', 'CONDITION_BEG_KEYWORD']:
            section = self.section(_context)
            self._rawSpecFile.block_list.append(section)
        elif _token == 'MACRO_DEF_KEYWORD':
            macro_definition = self.macro_definition(_context)
            self._rawSpecFile.block_list.append(macro_definition)
        elif _token == 'MACRO_UNDEF_KEYWORD':
            macro_undefine = self.macro_undefine(_context)
            self._rawSpecFile.block_list.append(macro_undefine)
        elif _token == 'CONDITION_BEG_KEYWORD':
            condition_definition = self.condition_definition(_context)
            self._rawSpecFile.block_list.append(condition_definition)
        else: # == 'LEFT_PARENTHESIS'
            LEFT_PARENTHESIS = self._scan('LEFT_PARENTHESIS', context=_context)
            macro_condition = self.macro_condition(_context)
            RIGHT_PARENTHESIS = self._scan('RIGHT_PARENTHESIS', context=_context)
            WHITESPACE = self._scan('WHITESPACE', context=_context)
            macro_condition.ending = WHITESPACE
            self._rawSpecFile.block_list.append(macro_condition)

    def macro_definition(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'macro_definition', [])
        MACRO_DEF_KEYWORD = self._scan('MACRO_DEF_KEYWORD', context=_context)
        MACRO_NAME = self._scan('MACRO_NAME', context=_context)
        if self._peek('MACRO_OPTIONS', 'MACRO_BODY', context=_context) == 'MACRO_OPTIONS':
            MACRO_OPTIONS = self._scan('MACRO_OPTIONS', context=_context)
        MACRO_BODY = self._scan('MACRO_BODY', context=_context)
        if 'MACRO_OPTIONS' in locals(): options = MACRO_OPTIONS
        else: options = None
        return MacroDefinitionBlock(MACRO_NAME, MACRO_DEF_KEYWORD, options, MACRO_BODY)

    def macro_condition(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'macro_condition', [])
        if self._peek('EXCLAMATION_MARK', 'QUESTION_MARK', context=_context) == 'EXCLAMATION_MARK':
            EXCLAMATION_MARK = self._scan('EXCLAMATION_MARK', context=_context)
        QUESTION_MARK = self._scan('QUESTION_MARK', context=_context)
        MACRO_NAME = self._scan('MACRO_NAME', context=_context)
        COLON = self._scan('COLON', context=_context)
        MACRO_CONDITION_BODY = self._scan('MACRO_CONDITION_BODY', context=_context)
        if 'EXCLAMATION_MARK' in locals(): condition = EXCLAMATION_MARK + QUESTION_MARK
        else: condition = QUESTION_MARK
        _, rawSpecFile = parseByRule('spec_file', MACRO_CONDITION_BODY)
        return MacroConditionBlock(MACRO_NAME, condition, rawSpecFile.block_list)

    def commentary(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'commentary', [])
        COMMENT = self._scan('COMMENT', context=_context)
        return CommentBlock(COMMENT)

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
        block_content = []
        _, rawSpecFile = parseByRule('spec_file', CONDITION_BODY)
        block_content = rawSpecFile.block_list
        block_else_body = []
        while self._peek('CONDITION_ELSE_KEYWORD', 'CONDITION_END_KEYWORD', 'CONDITION_BEG_KEYWORD', 'CONDITION_BODY', context=_context) in ['CONDITION_BEG_KEYWORD', 'CONDITION_BODY']:
            _token = self._peek('CONDITION_BEG_KEYWORD', 'CONDITION_BODY', context=_context)
            if _token == 'CONDITION_BEG_KEYWORD':
                condition_definition = self.condition_definition(_context)
                if block_content[-1].block_type == BlockTypes.SectionTagType and 'package' in block_content[-1].keyword and condition_definition not in block_content[-1].content: block_content[-1].content.append(condition_definition)
                elif condition_definition not in block_content: block_content.append(condition_definition)
            else: # == 'CONDITION_BODY'
                body = self.body(_context)
                _, rawSpecFile = parseByRule('spec_file', body)
                if block_content[-1].block_type == BlockTypes.SectionTagType and 'package' in block_content[-1].keyword: block_content[-1].content += rawSpecFile.block_list
                else: block_content += rawSpecFile.block_list
            if self._peek('PERCENT_SIGN', 'CONDITION_ELSE_KEYWORD', 'CONDITION_BEG_KEYWORD', 'CONDITION_BODY', 'CONDITION_END_KEYWORD', context=_context) == 'PERCENT_SIGN':
                PERCENT_SIGN = self._scan('PERCENT_SIGN', context=_context)
        if self._peek('CONDITION_ELSE_KEYWORD', 'CONDITION_END_KEYWORD', 'CONDITION_BEG_KEYWORD', 'CONDITION_BODY', context=_context) == 'CONDITION_ELSE_KEYWORD':
            CONDITION_ELSE_KEYWORD = self._scan('CONDITION_ELSE_KEYWORD', context=_context)
            condition_else_body = self.condition_else_body(_context)
            PERCENT_SIGN = self._scan('PERCENT_SIGN', context=_context)
            if 'condition_else_body' in locals(): _, rawSpecFile = parseByRule('spec_file', condition_else_body); block_else_body += rawSpecFile.block_list; del condition_else_body
            while self._peek('CONDITION_BEG_KEYWORD', 'CONDITION_BODY', 'CONDITION_END_KEYWORD', context=_context) != 'CONDITION_END_KEYWORD':
                _token = self._peek('CONDITION_BEG_KEYWORD', 'CONDITION_BODY', context=_context)
                if _token == 'CONDITION_BEG_KEYWORD':
                    condition_else_inner = self.condition_else_inner(_context)
                else: # == 'CONDITION_BODY'
                    else_body = self.else_body(_context)
                if 'else_body' in locals(): _, rawSpecFile = parseByRule('spec_file', else_body); block_else_body += rawSpecFile.block_list; del else_body
                if 'condition_else_inner' in locals() and condition_else_inner not in block_else_body: block_else_body.append(condition_else_inner); del condition_else_inner
                if self._peek('PERCENT_SIGN', 'CONDITION_BEG_KEYWORD', 'CONDITION_BODY', 'CONDITION_END_KEYWORD', context=_context) == 'PERCENT_SIGN':
                    PERCENT_SIGN = self._scan('PERCENT_SIGN', context=_context)
        CONDITION_END_KEYWORD = self._scan('CONDITION_END_KEYWORD', context=_context)
        if 'CONDITION_ELSE_KEYWORD' in locals(): block_else_keyword = CONDITION_ELSE_KEYWORD
        else: block_else_keyword = None
        return ConditionBlock(CONDITION_BEG_KEYWORD, CONDITION_EXPRESSION, block_content, block_else_body, CONDITION_END_KEYWORD, block_else_keyword)

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
            parameters = None
            subname = None
            name = None
            if 'PARAMETERS' in locals(): parameters = PARAMETERS
            if 'NAME' in locals(): subname = NAME
            if 'option' in locals(): name = option
            return SectionBlock(SECTION_KEY, parameters, name, subname, NEWLINE + SECTION_CONTENT)
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
            parameters = None
            subname = None
            name = None
            if 'PARAMETERS' in locals(): parameters = PARAMETERS
            if 'NAME' in locals(): subname = NAME
            if 'option' in locals(): name = option
            return SectionBlock(SECTION_KEY_NOPARSE, parameters, name, subname, NEWLINE + SECTION_CONTENT_NOPARSE)
        elif _token == 'PACKAGE_KEYWORD':
            PACKAGE_KEYWORD = self._scan('PACKAGE_KEYWORD', context=_context)
            if self._peek('DASH', 'NAME', 'NEWLINE', context=_context) == 'DASH':
                DASH = self._scan('DASH', context=_context)
                PARAMETERS = self._scan('PARAMETERS', context=_context)
            if self._peek('NAME', 'NEWLINE', context=_context) == 'NAME':
                NAME = self._scan('NAME', context=_context)
            NEWLINE = self._scan('NEWLINE', context=_context)
            PACKAGE_CONTENT = self._scan('PACKAGE_CONTENT', context=_context)
            parameters = None
            name = None
            if 'NAME' in locals(): subname = NAME + NEWLINE
            else: subname = NEWLINE
            if 'PARAMETERS' in locals(): parameters = PARAMETERS
            _, rawSpecFile = parseByRule('spec_file', PACKAGE_CONTENT)
            return PackageBlock(PACKAGE_KEYWORD, parameters, subname, rawSpecFile.block_list)
        else: # == 'CHANGELOG_KEYWORD'
            content = []
            CHANGELOG_KEYWORD = self._scan('CHANGELOG_KEYWORD', context=_context)
            while self._peek('SINGLE_LOG', 'PERCENT_SIGN', 'TAG_KEY', 'COMMENT', 'END', context=_context) == 'SINGLE_LOG':
                changelog = self.changelog(_context)
                content.append(changelog)
            return ChangelogBlock(CHANGELOG_KEYWORD, content)

    def option(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'option', [])
        NAME = self._scan('NAME', context=_context)
        return NAME

    def macro_undefine(self, _parent=None):
        _context = self.Context(_parent, self._scanner, 'macro_undefine', [])
        MACRO_UNDEF_KEYWORD = self._scan('MACRO_UNDEF_KEYWORD', context=_context)
        MACRO_NAME = self._scan('MACRO_NAME', context=_context)
        return MacroUndefinitionBlock(MACRO_UNDEF_KEYWORD, MACRO_NAME)


def parse(rule, text):
    P = SpecfileParser(SpecfileParserScanner(text))
    return runtime.wrap_error_reporter(P, rule)

# End -- grammar generated by Yapps



def parseByRule(goal, text):
    P = SpecfileParser(SpecfileParserScanner(text))
    P._rawSpecFile = RawSpecFile()
    e = runtime.wrap_error_reporter(P, goal)
    return e, P._rawSpecFile

class RawSpecFileParser(object):

  def __init__(self, specfile):
    self._specfile = specfile
    self._rawSpecfile = None

  def parse(self):
     _, self._rawSpecfile = parseByRule("goal", self._specfile)
     return self

  def json(self):
     return json.loads(json.dumps(self._rawSpecfile, default=lambda o: o.__dict__, sort_keys=True))

  def raw(self):
    return self._rawSpecfile
