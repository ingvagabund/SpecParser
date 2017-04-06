class HeaderTags(object):

    def __init__(self):
        self.keys = {}

    def __repr__(self):
        return "HeaderTags(%r)" % ([x in self.keys])



class Sections(object):

    def __init__(self):
        self.section_dict = {}
        
    def __repr__(self):
        return "Section(%r)" % (self.section_dict)



class Comments(object):

    def __init__(self):
        self.content = []
        
    def __repr__(self):
        return "Comments(%r)" % (self.content)



class Macros(object):

    def __init__(self):
        self.macro_definitions = {}
        self.macro_undefs = {}
        
    def __repr__(self):
        return "MacroDefinitions(%r)" % (self.macro_definitions)


class Conditions(object):

    def __init__(self):
        self.condition_list = []

    def __repr__(self):
        return "Conditions(%r)" % (self.condition_list)


HeaderTags = HeaderTags()
Sections = Sections()
Comments = Comments()
Macros = Macros()
Conditions = Conditions()

SpecfileSections = {"HeaderTags": HeaderTags, "Sections": Sections, "Comments": Comments, "Macros": Macros, "Conditions": Conditions}


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
parser Specfile:
    #option:    "context-insensitive-scanner"

    ignore: ' \t'

    token END: "$"
    token TAG_KEY: __HeaderDirectives
    token COLON: "\:"
    token TAG_VALUE: __match_tag_content
    token COMMENT: r'\#.+'
    token PERCENT_SIGN: '%'
    token MACRO_DEF_KEYWORD: __MacroDefDirectives
    token MACRO_UNDEF_KEYWORD: __MacroUndefDirectives
    token MACRO_NAME: r'\S+'
    token MACRO_BODY: match_section_content
    token CONDITION_BEG_KEYWORD: __ConditionBegDirectives
    token CONDITION_EXPRESSION: 
    token CONDITION_BODY: 
    token CONDITION_END_KEYWORD: __ConditionEndDirectives
    token SECTION_KEY: __SectionDirectives
    token SECTION_CONTENT: match_section_content


    rule goal:         specfile END                     {{ return SpecfileSections }}


    rule specfile:     header rest
                                                        

    rule header:       tag                              
                    |  tag header


    rule tag:          header_tag                       {{ HeaderTags.keys.update(header_tag) }}
                    |  commentary                       {{ Comments.content.update(commentary) }}
                    |  PERCENT_SIGN macro_definition    {{ Macros.macro_definitions.update(macro_definition) }}


    rule header_tag:   TAG_KEY COLON TAG_VALUE          {{ return {TAG_KEY: TAG_VALUE} }}


    rule rest:      PERCENT_SIGN (
                       section                          {{ Sections.section_dict.update(section) }}             
                    |  section rest                     {{ Sections.section_dict.update(section) }}
                    |  macro_definition                 {{ Macros.macro_definitions.update(macro_definition) }}
                    |  macro_definition rest            {{ Macros.macro_definitions.update(macro_definition) }}
                    |  macro_undefine                   {{ Macros.macro_undefs.update(macro_undefine) }}
                    |  macro_undefine rest              {{ Macros.macro_undefs.update(macro_undefine) }}
                    |  condition_definition             {{ Conditions.condition_list.append(condition_definition) }}
                    |  condition_definition rest        {{ Conditions.condition_list.append(condition_definition) }}
                    )
                    |  commentary                       {{ Comments.content.update(commentary) }}
                    |  commentary rest                  {{ Comments.content.update(commentary) }}


    rule macro_definition: MACRO_DEF_KEYWORD MACRO_NAME MACRO_BODY      {{ return {MACRO_NAME: [MACRO_DEF_KEYWORD, MACRO_BODY]} }}


    rule commentary:  COMMENT                                           {{ return COMMENT }}


    rule condition_definition: CONDITION_KEYWORD CONDITION_EXPRESSION CONDITION_BODY PERCENT_SIGN CONDITION_END_KEYWORD 
                                        {{ return [CONDITION_KEYWORD, CONDITION_EXPRESSION, CONDITION_BODY] }}


    rule section:           SECTION_KEY SECTION_CONTENT                 {{ return {SECTION_KEY: SECTION_CONTENT} }}
                                                                       

    rule macro_undefine:    MACRO_UNDEF_KEYWORD MACRO_NAME              {{ return {MACRO_NAME: MACRO_UNDEF_KEYWORD} }}


%%
if __name__ == '__main__':
    
    print('Parsing started!')
    try: 
        s = raw_input('')
    except EOFError: 
        break

    parse('goal', s)
    print('Parsed!')
