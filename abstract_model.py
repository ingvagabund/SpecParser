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
    ChangelogTagType = 7



keys_list = [
    ['key', 'option', 'content'],
    ['keyword', 'name', 'parameters', 'subname', 'content'],
    ['keyword', 'name', 'options', 'body'],
    ['condition', 'name', 'content', 'ending'],
    ['keyword', 'name'],
    ['content'],
    ['keyword', 'expression', 'content', 'else_keyword', 'else_body', 'end_keyword'],
    ['author', 'date', 'mark', 'comment']
]



class SpecfileClass(object):

    def __init__(self, class_type):

        if class_type == 'Specfile 2.0':
            self.HeaderTags = []
            self.SectionTags = []
            self.MacroDefinitions = []
            self.MacroConditions = []
            self.MacroUndefinitions = []
            self.Comments = []
            self.Conditions = []
            self.metastring = ""
            return

        elif class_type == 'GO spec':
            self.metadata = []
            self.main_unit = []
            self.unit_list = []
            self.history = {}
            self.comments = []
            self.metastring = ""
            return

        self.block_list = []
        self.metastring = ""

        if class_type == 'Parser':
            self.beginning = ""
            self.end = ""
            