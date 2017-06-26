import argparse, json, io

from abstract_model import SpecfileClass, BlockTypes


class Block(object):

    def __init__(self, type):
        self.block_type = type


Specfile = SpecfileClass('Parser')


def open_specfile(filename):

    try:
        input_file = io.open(filename, mode='r', encoding="utf-8")
        input_data = input_file.read()
        input_file.close()
        return input_data
    except IOError:
        print('ERROR: Cannot find specfile!')
        sys.exit(1)


%%
parser SpecfileParser:

    token END: "\s*$"
    token BEGINNING: r'\s*'
    token TAG_KEY: r'(?i)(NAME|VERSION|RELEASE|SUMMARY|LICENSE|URL|BUILDREQUIRES(\(\S+\))?|REQUIRES(\(\S+\))?|PREFIX|GROUP|BUILDROOT|EXCLUDEARCH|EXCLUSIVEARCH|CONFLICTS|BUILDARCH|PROVIDES|PREP|PRE|PREUN|POST|POSTUN)\s*|(SOURCE|PATCH)\d*\s*'
    token COLON: "\:"
    token TAG_VALUE: r'.*\s*'
    token COMMENT: r'\#.+\s*'
    token PERCENT_SIGN: '%'
    token DASH: r'\-'
    token PARAMETERS: r'\S+[ \t\r\f\v]*'
    token NAME: r'(?!\-)\S+[ \t\r\f\v]*'
    token NEWLINE: r'\n'
    token MACRO_DEF_KEYWORD: r'(define|global)\s*'
    token MACRO_UNDEF_KEYWORD: r'undefine\s*'
    token MACRO_NAME: r'\S+?(?=[\(|\:|\s])\s*'
    token MACRO_OPTIONS: r'\(.*?\)\s*'
    token MACRO_BODY: r'(?!\().*\s*'
    token MACRO_CONDITION_BODY: r'(?!\().*(?=\}\s*)'
    token LEFT_PARENTHESIS: r'\{'
    token RIGHT_PARENTHESIS: r'\}'
    token EXCLAMATION_MARK: r'\!'
    token QUESTION_MARK: r'\?'
    token WHITESPACE: r'[ \t\n\r\f\v]*'
    token CONDITION_BEG_KEYWORD: r'(if|ifarch|ifos|ifnarch|ifnos)\s*'
    token CONDITION_ELSE_KEYWORD: r'else\s*'
    token CONDITION_EXPRESSION: r'.*\s*'
    token CONDITION_BODY: r'(?!(endif|if|else))[\W\w]*?(?=%(else|endif|if))'
    token CONDITION_END_KEYWORD: r'endif\s*'
    token SECTION_KEY: r'(?i)(DESCRIPTION|PREP|PREUN|PRE|POSTUN|POST|FILES)[ \t\r\f\v]*'
    token SECTION_KEY_NOPARSE: r'(?i)(BUILD|CHECK|INSTALL)[ \t\r\f\v]*'
    token SECTION_CONTENT: r'(?i)(?!(NAME|VERSION|RELEASE|SUMMARY|LICENSE|URL|SOURCE|PATCH|BUILDREQUIRES|REQUIRES|PREFIX|GROUP|BUILDROOT|EXCLUDEARCH|EXCLUSIVEARCH|CONFLICTS|BUILDARCH|PROVIDES)\:|%(DESCRIPTION|PREP|BUILD|CHECK|INSTALL|FILES|PACKAGE|CHANGELOG|PRE|PREUN|POST|POSTUN)|%(define|global|undefine)|%(if|ifarch|ifos|ifnarch|ifnos|else|endif))[\w\W]+?(?=(NAME|VERSION|RELEASE|SUMMARY|LICENSE|URL|SOURCE|PATCH|BUILDREQUIRES|REQUIRES|PREFIX|GROUP|BUILDROOT|EXCLUDEARCH|EXCLUSIVEARCH|CONFLICTS|BUILDARCH|PROVIDES)\:|%(DESCRIPTION|PREP|BUILD|CHECK|INSTALL|FILES|PACKAGE|CHANGELOG|PRE|PREUN|POST|POSTUN)|%(define|global|undefine)|%(if|ifarch|ifos|ifnarch|ifnos|else|endif)|%\{!\?|%\{\?|$)\s*'
    token SECTION_CONTENT_NOPARSE: r'(?i)(?!(NAME|VERSION|RELEASE|SUMMARY|LICENSE|URL|SOURCE|PATCH|BUILDREQUIRES|REQUIRES|PREFIX|GROUP|BUILDROOT|EXCLUDEARCH|EXCLUSIVEARCH|CONFLICTS|BUILDARCH|PROVIDES)\:|%(DESCRIPTION|PREP|BUILD|CHECK|INSTALL|FILES|PACKAGE|CHANGELOG|PRE|PREUN|POST|POSTUN))[\w\W]+?(?=(NAME|VERSION|RELEASE|SUMMARY|LICENSE|URL|SOURCE|PATCH|BUILDREQUIRES|REQUIRES|PREFIX|GROUP|BUILDROOT|EXCLUDEARCH|EXCLUSIVEARCH|CONFLICTS|BUILDARCH|PROVIDES)\:|%(DESCRIPTION|PREP|BUILD|CHECK|INSTALL|FILES|PACKAGE|CHANGELOG|PRE|PREUN|POST|POSTUN)|$)\s*'
    token CHANGELOG_KEYWORD: r'changelog\s*'
    token SINGLE_LOG: r'\*[\W\w]*?(?=\*|$)'
    token PACKAGE_KEYWORD: r'package[ \t\r\f\v]*'
    token PACKAGE_CONTENT: '(?i)[\W\w]*?(?=%(PACKAGE|PREP|BUILD|INSTALL|CHECK|PRE|PREUN|POST|POSTUN)|$)\s*'


    rule goal:         begin spec_file END              {{ Specfile.end = END }}


    rule begin:        BEGINNING                        {{ Specfile.beginning = BEGINNING }} 


    rule spec_file:    header rest?
                                                        

    rule header:       tag*



    rule tag:          header_tag                       {{ Specfile.block_list.append(header_tag) }}
                    |  commentary                       {{ Specfile.block_list.append(commentary) }}
                    |  PERCENT_SIGN keyword



    rule header_tag:   TAG_KEY COLON TAG_VALUE          {{ block = Block(BlockTypes.HeaderTagType) }}
                                                        {{ if TAG_KEY.find('(') == -1: block.key = TAG_KEY; block.option = None }}
                                                        {{ else: block.key = TAG_KEY[:TAG_KEY.find('(')]; block.option = TAG_KEY[TAG_KEY.find('(')+1:-1] }}
                                                        {{ block.content = TAG_VALUE }}
                                                        {{ return block }}



    rule rest:      PERCENT_SIGN keyword
                    |  commentary                       {{ Specfile.block_list.append(commentary) }}

    

    rule keyword:      section                          {{ Specfile.block_list.append(section) }}
                    |  macro_definition                 {{ Specfile.block_list.append(macro_definition) }}
                    |  macro_undefine                   {{ Specfile.block_list.append(macro_undefine) }}
                    |  condition_definition             {{ Specfile.block_list.append(condition_definition) }}
                    |  LEFT_PARENTHESIS macro_condition RIGHT_PARENTHESIS WHITESPACE
                                                        {{ macro_condition.ending = WHITESPACE }}
                                                        {{ Specfile.block_list.append(macro_condition) }}



    rule macro_definition: MACRO_DEF_KEYWORD MACRO_NAME MACRO_OPTIONS? MACRO_BODY      
                                                                        {{ block = Block(BlockTypes.MacroDefinitionType) }}
                                                                        {{ block.name = MACRO_NAME }}
                                                                        {{ block.keyword = MACRO_DEF_KEYWORD }}
                                                                        {{ if 'MACRO_OPTIONS' in locals(): block.options = MACRO_OPTIONS }}
                                                                        {{ else: block.options = None }}
                                                                        {{ block.body = MACRO_BODY }}
                                                                        {{ return block }}


    rule macro_condition:   EXCLAMATION_MARK? QUESTION_MARK MACRO_NAME COLON MACRO_CONDITION_BODY
                                                                        {{ block = Block(BlockTypes.MacroConditionType) }}
                                                                        {{ block.name = MACRO_NAME }}
                                                                        {{ if 'EXCLAMATION_MARK' in locals(): block.condition = EXCLAMATION_MARK + QUESTION_MARK }}
                                                                        {{ else: block.condition = QUESTION_MARK }}
                                                                        {{ block.content = MACRO_CONDITION_BODY }}
                                                                        {{ return block }}



    rule commentary:  COMMENT                                           {{ block = Block(BlockTypes.CommentType) }}
                                                                        {{ block.content = COMMENT }}
                                                                        {{ return block }}



    rule changelog:     SINGLE_LOG                                      {{ return SINGLE_LOG }}



    rule condition_definition:  CONDITION_BEG_KEYWORD CONDITION_EXPRESSION CONDITION_BODY PERCENT_SIGN
                                        {{ block = Block(BlockTypes.ConditionType) }}
                                        {{ block.keyword = CONDITION_BEG_KEYWORD }}
                                        {{ block.expression = CONDITION_EXPRESSION }}
                                        {{ block.content = [] }}
                                        {{ count = len(Specfile.block_list) }} 
                                        {{ parse('spec_file', CONDITION_BODY) }}
                                        {{ if Specfile.block_list[count:] not in block.content: block.content += Specfile.block_list[count:] }}
                                        {{ Specfile.block_list = Specfile.block_list[:count] }}
                                        {{ block.else_body = [] }}
                        ((condition_definition              
                                        {{ if block.content[-1].block_type == BlockTypes.SectionTagType and 'package' in block.content[-1].keyword and condition_definition not in block.content[-1].content: block.content[-1].content.append(condition_definition) }}
                                        {{ elif condition_definition not in block.content: block.content.append(condition_definition) }}
                        | body          {{ count = len(Specfile.block_list) }} 
                                        {{ parse('spec_file', body) }}
                                        {{ if block.content[-1].block_type == BlockTypes.SectionTagType and 'package' in block.content[-1].keyword and Specfile.block_list[count:] not in block.content[-1].content: block.content[-1].content += Specfile.block_list[count:] }}
                                        {{ elif Specfile.block_list[count:] not in block.content: block.content += Specfile.block_list[count:] }}
                                        {{ Specfile.block_list = Specfile.block_list[:count] }}
                        ) PERCENT_SIGN?)*
                        (CONDITION_ELSE_KEYWORD condition_else_body PERCENT_SIGN
                                        {{ if 'condition_else_body' in locals(): count = len(Specfile.block_list); parse('spec_file', condition_else_body); block.else_body += Specfile.block_list[count:]; Specfile.block_list = Specfile.block_list[:count]; del condition_else_body }} 
                        ((condition_else_inner | else_body)
                                        {{ if 'else_body' in locals(): count = len(Specfile.block_list); parse('spec_file', else_body); block.else_body += Specfile.block_list[count:]; Specfile.block_list = Specfile.block_list[:count]; del else_body }}
                                        {{ if 'condition_else_inner' in locals() and condition_else_inner not in block.else_body: block.else_body.append(condition_else_inner); del condition_else_inner }}
                        PERCENT_SIGN?)*)?
                        CONDITION_END_KEYWORD
                                        {{ block.end_keyword = CONDITION_END_KEYWORD }}
                                        {{ if 'CONDITION_ELSE_KEYWORD' in locals(): block.else_keyword = CONDITION_ELSE_KEYWORD }}
                                        {{ else: block.else_keyword = None }}
                                        {{ return block }}



    rule condition_else_body:       CONDITION_BODY                      {{ return CONDITION_BODY }}                     



    rule condition_else_inner:      condition_definition                {{ return condition_definition }}



    rule else_body:                 CONDITION_BODY                      {{ return CONDITION_BODY }}



    rule body:                      CONDITION_BODY                      {{ return CONDITION_BODY }}



    rule section:           SECTION_KEY option? (DASH PARAMETERS)? NAME? NEWLINE SECTION_CONTENT
                                                                        {{ block = Block(BlockTypes.SectionTagType) }}
                                                                        {{ block.keyword = SECTION_KEY }}
                                                                        {{ block.content = NEWLINE + SECTION_CONTENT }}
                                                                        {{ if 'PARAMETERS' in locals(): block.parameters = PARAMETERS }}
                                                                        {{ else: block.parameters = None }}
                                                                        {{ if 'NAME' in locals(): block.subname = NAME }}
                                                                        {{ else: block.subname = None }}
                                                                        {{ if 'option' in locals(): block.name = option }}
                                                                        {{ else: block.name = None }}
                                                                        {{ return block }}
                        |   SECTION_KEY_NOPARSE option?  (DASH PARAMETERS)? NAME? NEWLINE SECTION_CONTENT_NOPARSE
                                                                        {{ block = Block(BlockTypes.SectionTagType) }}
                                                                        {{ block.keyword = SECTION_KEY_NOPARSE }}
                                                                        {{ block.content = NEWLINE + SECTION_CONTENT_NOPARSE }}
                                                                        {{ if 'PARAMETERS' in locals(): block.parameters = PARAMETERS }}
                                                                        {{ else: block.parameters = None }}
                                                                        {{ if 'NAME' in locals(): block.subname = NAME }}
                                                                        {{ else: block.subname = None }}
                                                                        {{ if 'option' in locals(): block.name = option }}
                                                                        {{ else: block.name = None }}
                                                                        {{ return block }}
                        |                                               {{ count = len(Specfile.block_list) }}
                            PACKAGE_KEYWORD (DASH PARAMETERS)? NAME? NEWLINE PACKAGE_CONTENT
                                                                        {{ block = Block(BlockTypes.SectionTagType) }}
                                                                        {{ block.keyword = PACKAGE_KEYWORD }}
                                                                        {{ if 'NAME' in locals(): block.name = NAME + NEWLINE }}
                                                                        {{ else: block.name = NEWLINE }}
                                                                        {{ if 'PARAMETERS' in locals(): block.parameters = PARAMETERS }}
                                                                        {{ else: block.parameters = None }}                                                                        
                                                                        {{ parse('spec_file', PACKAGE_CONTENT) }}
                                                                        {{ block.content = Specfile.block_list[count:] }}
                                                                        {{ Specfile.block_list = Specfile.block_list[:count] }}
                                                                        {{ return block }}
                        |                                               {{ block = Block(BlockTypes.SectionTagType) }}
                                                                        {{ block.content = [] }}
                            CHANGELOG_KEYWORD (
                                changelog                               {{ block.content.append(changelog) }}
                            )*
                                                                        {{ block.keyword = CHANGELOG_KEYWORD }}
                                                                        {{ return block }}



    rule option:            NAME                                        {{ return NAME }}



    rule macro_undefine:    MACRO_UNDEF_KEYWORD MACRO_NAME              {{ block = Block(BlockTypes.MacroUndefinitionType) }}
                                                                        {{ block.keyword = MACRO_UNDEF_KEYWORD }}
                                                                        {{ block.name = MACRO_NAME }}
                                                                        {{ return block }}


%%
def parse_specfile(input_filepath):

    if input_filepath == None:
        input_filepath = raw_input("Enter path to the specfile: ")

    parse('goal', open_specfile(input_filepath))

    return json.dumps(Specfile, default=lambda o: o.__dict__, sort_keys=True)
