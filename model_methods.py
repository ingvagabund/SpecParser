from __future__ import print_function
from specparser import BlockTypes



def print_specfile(intern_specfile):
    print(str(intern_specfile.beginning["content"]), end='')

    if intern_specfile.beginning["next"] != None:
        print_field(intern_specfile.beginning["next"])

    return



def print_field(intern_field):

    if intern_field != None:
        if intern_field["block_type"] == BlockTypes.HeaderTagType:
            print(str(intern_field["key"]) + ":" + str(intern_field["content"]), end='')

        elif intern_field["block_type"] == BlockTypes.SectionTagType:
            print("%" + str(intern_field["keyword"]), end='')

            if "changelog" in intern_field["keyword"]:
                for single_log in intern_field["content"]:
                    print(str(single_log), end='')
            # elif "package" in intern_field["keyword"]: # TODO
            else:
                print(str(intern_field["content"]), end='')

        elif intern_field["block_type"] == BlockTypes.CommentType:
            print(str(intern_field["content"]), end='')

        elif intern_field["block_type"] == BlockTypes.MacroDefinitionType:
            print("%" + str(intern_field["keyword"]) + str(intern_field["name"]) + str(intern_field["options"]) + str(intern_field["body"]), end='')

        elif intern_field["block_type"] == BlockTypes.MacroConditionType:
            print("%" + str(intern_field["name"]) + str(intern_field["condition"]) + str(intern_field["content"]), end='')

        elif intern_field["block_type"] == BlockTypes.ConditionType:
            print("%" + str(intern_field["keyword"]) + str(intern_field["expression"]), end='')
            print_field(intern_field["content"])
            print("%endif\n\n", end='')         # TODO



        if intern_field["next"] != None:
            print_field(intern_field["next"])

    return
