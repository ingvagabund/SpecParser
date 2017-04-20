import argparse, sys, re, json


class BlockTypes(object):

    HeaderTagType = 0
    SectionTagType = 1
    MacroDefinitionType = 2
    MacroConditionType = 3
    MacroUndefinitionType = 3
    CommentType = 4
    ConditionType = 5



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
    help="input file containing information about computation")


def open_specfile(filename):

    try:
        input_file = open(filename, mode='r', encoding="utf-8")
        input_data = input_file.read()
        input_file.close()
        return input_data
    except IOError:
        print('ERROR: Cannot find specfile!')
        sys.exit(1)


__HeaderDirectives = r'(NAME|VERSION|RELEASE|SUMMARY|LICENSE|URL|'\
r'SOURCE|PATCH|BUILDREQUIRES|REQUIRES|PREFIX|GROUP|BUILDROOT|EXCLUDEARCH)'
__SectionDirectives = r'(?i)(DESCRIPTION|PREP|BUILD|CHECK|INSTALL|FILES|'\
r'PACKAGE|DOC|CHANGELOG)'
__MacroDefDirectives = r'(define|global)'
__MacroUndefDirectives = 'undefine'
__ConditionBegDirectives = r'(if|ifarch|ifos|ifnarch|ifnos|else)'
__ConditionEndDirectives = 'endif'


__match_tag_content = r'(?i)(?!' + self.__HeaderDirectives + '\:|%' + self.__SectionDirectives + \
r'|%' + self.__MacroDirectives + '|%' + self.__ConditionDirectives + ').+?(?=\n\S+\:|%' + \
self.__SectionDirectives + r'|%' + self.__MacroDirectives + '|%' + self.__ConditionDirectives + '|$)'


__match_section_content = r'(?i)(?!' + self.__HeaderDirectives + '\:|%' + self.__SectionDirectives + \
r'|%' + self.__MacroDirectives + '|%' + self.__ConditionDirectives + ')\s[\w\W]+?(?=\n\S+\:|%' + \
self.__SectionDirectives + r'|%' + self.__MacroDirectives + '|%' + self.__ConditionDirectives + '|$)'


%%
parser SpecfileParser:

    token END: "$"
    token BEGINNING: r'\s*'
    token TAG_KEY: r'(NAME|VERSION|RELEASE|SUMMARY|LICENSE|URL|SOURCE|PATCH|BUILDREQUIRES|REQUIRES|PREFIX|GROUP|BUILDROOT|EXCLUDEARCH)'
    token COLON: "\:"
    token TAG_VALUE: r'(?i)(?!(NAME|VERSION|RELEASE|SUMMARY|LICENSE|URL|SOURCE|PATCH|BUILDREQUIRES|REQUIRES|PREFIX|GROUP|BUILDROOT|EXCLUDEARCH)\:|%(DESCRIPTION|PREP|BUILD|CHECK|INSTALL|FILES|PACKAGE|CHANGELOG)|%(define|global|undefine)|%' + self.__ConditionDirectives + ').+?(?=\n\S+\:|%' + \
self.__SectionDirectives + r'|%(define|global|undefine)|%(if|ifarch|ifos|ifnarch|ifnos|else|endif)|$)'
    token COMMENT: r'\#.+'
    token PERCENT_SIGN: '%'
    token MACRO_DEF_KEYWORD: r'(define|global)'
    token MACRO_UNDEF_KEYWORD: 'undefine'
    token DASH: r'\-'
    token MACRO_NAME: r'\S+\s*'
    token MACRO_BODY: match_section_content
    token CONDITION_BEG_KEYWORD: r'(if|ifarch|ifos|ifnarch|ifnos)'
    token CONDITION_ELSE_KEYWORD: 'else'
    token CONDITION_EXPRESSION: 
    token CONDITION_BODY: 
    token CONDITION_END_KEYWORD: 'endif'
    token SECTION_KEY: r'(?i)(DESCRIPTION|PREP|BUILD|CHECK|INSTALL|PRE)'
    token SECTION_CONTENT: match_section_content
    token FILES_KEYWORD: 'files'
    token CHANGELOG_KEYWORD: 'changelog'
    token PACKAGE_KEYWORD: 'package'


    rule goal:         begin spec_file END


    rule begin:        BEGINNING                        {{ Specfile.beginning = BEGINNING }} 


    rule spec_file:    header rest
                                                        

    rule header:       tag*


    rule tag:          header_tag                       {{ Specfile.block_list.append(header_tag) }}
                    |  commentary                       {{ Specfile.block_list.append(commentary) }}
                    |  PERCENT_SIGN macro_definition    {{ Macros.macro_definitions.update(macro_definition) }}


    rule header_tag:   TAG_KEY COLON TAG_VALUE          {{ block = Block(BlockTypes.HeaderTagType) }}
                                                        {{ block.key = TAG_KEY }}
                                                        {{ block.content = TAG_VALUE }}
                                                        {{ return block }}


    rule rest:      PERCENT_SIGN (
                       section                          {{ Sections.section_dict.update(section) }}             
                    |  macro_definition                 {{ Macros.macro_definitions.update(macro_definition) }}
                    |  macro_undefine                   {{ Macros.macro_undefs.update(macro_undefine) }}
                    |  condition_definition             {{ Conditions.condition_list.append(condition_definition) }}
                    )
                    |  commentary                       {{ Comments.content.update(commentary) }}


    rule macro_definition: MACRO_DEF_KEYWORD MACRO_NAME MACRO_BODY      {{ block = Block(MacroDefinitionType) }}
                                                                        {{ block.name = MACRO_NAME }}
                                                                        {{ block.keyword = MACRO_DEF_KEYWORD }}
                                                                        {{ block.body = MACRO_BODY }}
                                                                        {{ return block }}


    rule commentary:  COMMENT                                           {{ block = Block(BlockTypes.CommentType) }}
                                                                        {{ block.content = COMMENT }}
                                                                        {{ return block }}


    rule condition_definition:          {{ count = len(Specfile.block_list) }} 
                        CONDITION_KEYWORD CONDITION_EXPRESSION CONDITION_BODY condition_rest 
                                        {{ block = Block(BlockTypes.ConditionType) }}
                                        {{ block.keyword = CONDITION_KEYWORD }}
                                        {{ block.expression = CONDITION_EXPRESSION }}
                                        {{ parse('spec_file', CONDITION_BODY) }}
                                        {{ block.content = Specfile.block_list[count:] }}
                                        {{ Specfile.block_list[count:] }}
                                        {{ return block }}

    rule condition_rest:    (PERCENT_SIGN CONDITION_ELSE_KEYWORD CONDITION_BODY)? PERCENT_SIGN CONDITION_END_KEYWORD



    rule section:           SECTION_KEY (DASH PARAMETERS)? NAME? SECTION_CONTENT
                                                                        {{ block = Block(BlockTypes.SectionTagType) }}
                                                                        {{ block.key = SECTION_KEY }}
                                                                        {{ if 'PARAMETERS' in locals(): block.parameters = PARAMETERS }}
                                                                        {{ else: block.parameters = None }}
                                                                        {{ if 'NAME' in locals(): block.name = NAME }}
                                                                        {{ else: block.name = None }}
                                                                        {{ return block }}
                                                                       

    rule macro_undefine:    MACRO_UNDEF_KEYWORD MACRO_NAME              {{ block = Block(BlockTypes.MacroUndefinitionType) }}
                                                                        {{ block.name = MACRO_NAME }}
                                                                        {{ return block }}


%%
if __name__ == '__main__':

    args = parse_arguments()

    parse('goal', open_specfile(args.input))

    print(json.dumps(Specfile.__dict__, sort_keys=True, indent=4))
