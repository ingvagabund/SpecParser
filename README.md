# SpecParser


Runnable with commands:
    - make (runs specfile parsing, the path to specfile is prompted in the command line)
    - make SPEC="path_to_specfile" (runs specfile parsing on the file 'path_to_specfile')
    - make test (runs available tests on the implementation of the specfile parser)
    - python specparser.py (same as "make")
    - python specparser.py -i path_to_specfile (same as "make SPEC='path_to_specfile'")


Supported specfile fields:

    1 HEADER TAGS

    1.1 header tags in format "[KEY]:[VALUE]", where KEY is one of the 
    following:
        NAME, VERSION, RELEASE, SUMMARY, LICENSE, URL, PREFIX, GROUP, 
        BUILDROOT, EXCLUDEARCH, EXCLUSIVEARCH, CONFLICTS, BUILDARCH, PROVIDES,
        PREP, PRE, PREUN, POST, POSTUN, BUILDREQUIRES, REQUIRES, SOURCE, PATCH

    1.2 header tags in format "[KEY]([MODIFIER]):[VALUE]", where KEY is one of
    the following:
        BUILDREQUIRES, REQUIRES  

    1.3 header tags in format "[KEY][SEQUENCE_NUMBER]:[VALUE]", where KEY is 
    one of the following:
        SOURCE, PATCH

    2 SECTION TAGS

    2.1 sections in format "%[KEY] [NAME]? (-[PARAMETERS])? [SUBNAME]?\n[VALUE]",
    where KEY is one of the following: 
        DESCRIPTION, PREP, BUILD, CHECK, INSTALL, PREUN, PRE, POSTUN, POST,
        FILES

    2.2 sections in format "%PACKAGE (-[PARAMETERS])? [NAME]?\n[VALUE]"
        
    2.3 sections in format "%CHANGELOG\n[VALUE]"

    3 COMMENTS

    3.1 comments beginning with "#" as the first character on a line

    4 MACRO DEFINITIONS

    4.1 macro definitions in format: "%(global|define) [NAME] ([OPTIONS])? [BODY]"

    5 MACRO UNDEFINITIONS

    5.1 macro undefinitions in format: "%undefine [NAME]"

    6 MACRO CONDITIONS
    
    6.1 macros used in a condition in format: "{!?[NAME]:[BODY]}" or
    "{?[NAME]:[BODY]}"

    7 CONDITIONS

    7.1 conditions in format: "%[KEYWORD] [CONDITION]\n[BODY] %endif" or 
    "%[KEYWORD] [CONDITION]\n[BODY] %else [ELSE_BODY]) %endif", where KEYWORD
    is one of the following:
        if, ifarch, ifos, ifnarch, ifnos

All keywords are not case sensitive.
