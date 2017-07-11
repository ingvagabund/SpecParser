# SpecParser


Runnable with commands:

- make (runs specfile parsing, the path to specfile is prompted in the command line)
- make SPEC="path_to_specfile" (runs specfile parsing on the file 'path_to_specfile')
- make test (runs available tests on the implementation of the specfile parser)
- python specparser.py (same as "make")
- python specparser.py -i path_to_specfile (same as "make SPEC='path_to_specfile'")


Supported specfile fields:

    1 HEADER TAGS

    1.1 header tags in format "[TAG]:[VALUE]", where TAG is one of the 
    following:
        BUILDARCH, BUILDREQUIRES, BUILDROOT, CONFLICTS, EXCLUDEARCH, 
        EXCLUSIVEARCH, GROUP, LICENSE, NAME, PATCH, PRE, PREUN,
        POST, POSTUN, PROVIDES, RELEASE, REQUIRES, SOURCE, SUMMARY, URL,
        VERSION

    1.2 header tags in format "[TAG]([MODIFIER]):[VALUE]", where TAG is one of
    the following:
        BUILDREQUIRES, REQUIRES  

    1.3 header tags in format "[TAG][SEQUENCE_NUMBER]:[VALUE]", where TAG is 
    one of the following:
        SOURCE, PATCH

    2 SECTION TAGS

    2.1 sections in format "%[SECTION_HEADER] [NAME]? (-[PARAMETERS])? [SUBNAME]?\n[SECTION]",
    where SECTION_HEADER is one of the following: 
        BUILD, CHECK, CLEAN, DESCRIPTION, FILES, INSTALL, PRE, PREP, PREUN, POST, POSTUN

    2.2 sections in format "%PACKAGE (-[PARAMETERS])? [NAME]?\n[SECTION]"
        
    2.3 sections in format "%CHANGELOG\n[SECTION]"

    3 COMMENTS

    3.1 comments beginning with "#" as the first character on a line

    4 MACRO DEFINITIONS

    4.1 macro definitions in format: "%(global|define) [NAME] ([OPTIONS])? [BODY]"

    5 MACRO UNDEFINITIONS

    5.1 macro undefinitions in format: "%undefine [NAME]"

    6 CONDITIONAL MACROS
    
    6.1 macros used in a condition in format: "{!?[NAME]:[BODY]}" or
    "{?[NAME]:[BODY]}"

    7 CONDITIONS

    7.1 conditions in format: "%[KEYWORD] [CONDITION]\n[BODY] %endif" or 
    "%[KEYWORD] [CONDITION]\n[BODY] %else [ELSE_BODY]) %endif", where KEYWORD
    is one of the following:
        if, ifarch, ifnarch, ifos, ifnos

All keywords are not case sensitive.
