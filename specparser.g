import argparse, sys, re, json, io


class BlockTypes(object):

    HeaderTagType = 0
    SectionTagType = 1
    MacroDefinitionType = 2
    MacroConditionType = 3
    MacroUndefinitionType = 4
    CommentType = 5
    ConditionType = 6



class Specfile(object):

    def __init__(self):
        self.beginning = ""
        self.block_list = []



class Block(object):

    def __init__(self, type):
        self.block_type = type


Specfile = Specfile()


def parse_arguments():

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-i', '--input', dest="input", type=str,
    help="path to input specfile")

    return arg_parser.parse_args()


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

    token END: "$"
    token BEGINNING: r'\s*'
    token TAG_KEY: r'(?i)(NAME|VERSION|RELEASE|SUMMARY|LICENSE|URL|BUILDREQUIRES|REQUIRES|PREFIX|GROUP|BUILDROOT|EXCLUDEARCH|EXCLUSIVEARCH|CONFLICTS|BUILDARCH)\s*|(SOURCE|PATCH)\d*\s*'
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
    token SECTION_KEY: r'(?i)(DESCRIPTION|PREP|BUILD|CHECK|INSTALL|PRE|FILES)[ \t\r\f\v]*'
    token SECTION_CONTENT: r'(?i)(?!(NAME|VERSION|RELEASE|SUMMARY|LICENSE|URL|SOURCE|PATCH|BUILDREQUIRES|REQUIRES|PREFIX|GROUP|BUILDROOT|EXCLUDEARCH|EXCLUSIVEARCH|CONFLICTS|BUILDARCH)\:|%(DESCRIPTION|PREP|BUILD|CHECK|INSTALL|FILES|PACKAGE|CHANGELOG|PRE)|%(define|global|undefine)|%(if|ifarch|ifos|ifnarch|ifnos|else|endif))[\w\W]+?(?=(NAME|VERSION|RELEASE|SUMMARY|LICENSE|URL|SOURCE|PATCH|BUILDREQUIRES|REQUIRES|PREFIX|GROUP|BUILDROOT|EXCLUDEARCH|EXCLUSIVEARCH|CONFLICTS|BUILDARCH)\:|%(DESCRIPTION|PREP|BUILD|CHECK|INSTALL|FILES|PACKAGE|CHANGELOG|PRE)|%(define|global|undefine)|%(if|ifarch|ifos|ifnarch|ifnos|else|endif)|%\{!\?|%\{\?|$)'
    token CHANGELOG_KEYWORD: r'changelog\s*'
    token SINGLE_LOG: r'\*[\W\w]*?(?=\*|$)'
    token PACKAGE_KEYWORD: r'package[ \t\r\f\v]*'
    token PACKAGE_CONTENT: '(?i)[\W\w]*?(?=%(PACKAGE|PREP|BUILD|INSTALL|CHECK|PRE)|$)'


    rule goal:         begin spec_file END


    rule begin:        BEGINNING                        {{ Specfile.beginning = BEGINNING }} 


    rule spec_file:    header rest?
                                                        

    rule header:       tag*



    rule tag:          header_tag                       {{ Specfile.block_list.append(header_tag) }}
                    |  commentary                       {{ Specfile.block_list.append(commentary) }}
                    |  PERCENT_SIGN keyword



    rule header_tag:   TAG_KEY COLON TAG_VALUE          {{ block = Block(BlockTypes.HeaderTagType) }}
                                                        {{ block.key = TAG_KEY }}
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
                                        {{ content = CONDITION_BODY }}
                        ((condition_definition 
                        | (CONDITION_ELSE_KEYWORD condition_else_body PERCENT_SIGN (condition_else_inner else_body PERCENT_SIGN)?) 
                        | body ) PERCENT_SIGN?)*
                        CONDITION_END_KEYWORD
                                        {{ if 'condition_else_inner' in locals(): block.content.append(condition_else_inner) }}
                                        {{ block.end_keyword = CONDITION_END_KEYWORD }}
                                        {{ count = len(Specfile.block_list) }} 
                                        {{ parse('spec_file', content) }}
                                        {{ block.content += Specfile.block_list[count:] }}
                                        {{ Specfile.block_list = Specfile.block_list[:count] }}
                                        {{ if 'CONDITION_ELSE_KEYWORD' in locals(): block.else_keyword = CONDITION_ELSE_KEYWORD }}
                                        {{ else: block.else_keyword = None }}
                                        {{ to_parse = "" }}
                                        {{ if 'condition_else_body' in locals(): to_parse += condition_else_body }} 
                                        {{ if 'else_body' in locals(): to_parse += else_body }}
                                        {{ if 'condition_else_body' in locals(): count = len(Specfile.block_list); parse('spec_file', to_parse); block.else_body = Specfile.block_list[count:]; Specfile.block_list = Specfile.block_list[:count] }}
                                        {{ else: block.else_body = None }}
                                        {{ return block }}



    rule condition_else_body:       CONDITION_BODY                      {{ return CONDITION_BODY }}                     



    rule condition_else_inner:      condition_definition                {{ return condition_definition }}



    rule else_body:                 CONDITION_BODY                      {{ return CONDITION_BODY }}



    rule body:                      CONDITION_BODY                      {{ return CONDITION_BODY }}



    rule section:           SECTION_KEY (DASH PARAMETERS)? NAME? NEWLINE SECTION_CONTENT
                                                                        {{ block = Block(BlockTypes.SectionTagType) }}
                                                                        {{ block.key = SECTION_KEY }}
                                                                        {{ block.content = NEWLINE + SECTION_CONTENT }}
                                                                        {{ if 'PARAMETERS' in locals(): block.parameters = PARAMETERS }}
                                                                        {{ else: block.parameters = None }}
                                                                        {{ if 'NAME' in locals(): block.name = NAME }}
                                                                        {{ else: block.name = None }}
                                                                        {{ return block }}
                        |                                               {{ count = len(Specfile.block_list) }}
                            PACKAGE_KEYWORD (DASH PARAMETERS)? NAME? NEWLINE PACKAGE_CONTENT
                                                                        {{ block = Block(BlockTypes.SectionTagType) }}
                                                                        {{ block.key = PACKAGE_KEYWORD }}
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
                            CHANGELOG_KEYWORD changelog*                {{ block.content.append(changelog) }}
                                                                        {{ block.keyword = CHANGELOG_KEYWORD }}
                                                                        {{ return block }}



    rule macro_undefine:    MACRO_UNDEF_KEYWORD MACRO_NAME              {{ block = Block(BlockTypes.MacroUndefinitionType) }}
                                                                        {{ block.keyword = MACRO_UNDEF_KEYWORD }}
                                                                        {{ block.name = MACRO_NAME }}
                                                                        {{ return block }}


%%
if __name__ == '__main__':

    args = parse_arguments()

    parse('goal', open_specfile(args.input))

    print(json.dumps(Specfile, default=lambda o: o.__dict__, sort_keys=True))
