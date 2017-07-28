from __future__ import print_function
import json
import re

from abstract_model import SpecfileClass


def replace_field_number(metastring, prev_section_count, replacing):

    to_be_replaced_list = re.findall(r'#' + str(replacing[0]) + '\d+', metastring)
    for replace_record in to_be_replaced_list:
        metastring = metastring.replace(replace_record, '#' + str(replacing[1]) + str(int(replace_record[2:]) + prev_section_count))

    return metastring


def create_go_spec_model(Specfile2):

    GoSpecfile = SpecfileClass('GO spec')
    GoSpecfile.metastring = Specfile2.metastring

    if Specfile2.HeaderTags:
        GoSpecfile.metadata += Specfile2.HeaderTags

    if Specfile2.MacroDefinitions:
        GoSpecfile.metadata += Specfile2.MacroDefinitions
        GoSpecfile.metastring = replace_field_number(GoSpecfile.metastring, len(Specfile2.HeaderTags), [2,0])

    if not Specfile2.Conditions:
        prev_section_count = 0
        unit_list = []

        if Specfile2.SectionTags:
            unit_list += Specfile2.SectionTags
            GoSpecfile.metastring = replace_field_number(GoSpecfile.metastring, prev_section_count, [1,1])
            prev_section_count += len(Specfile2.SectionTags)

        if Specfile2.Comments:
            unit_list += Specfile2.Comments
            GoSpecfile.metastring = replace_field_number(GoSpecfile.metastring, prev_section_count, [5,1])
            prev_section_count += len(Specfile2.Comments)

        GoSpecfile.unit_list.append(unit_list)

    print(json.dumps(GoSpecfile, default=lambda o: o.__dict__, sort_keys=True))
