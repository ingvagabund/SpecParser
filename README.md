# SpecParser


Runnable with commands:
    - make (runs specfile parsing, the path to specfile is prompted in the command line)
    - make SPEC="path_to_specfile" (runs specfile parsing on the file 'path_to_specfile')
    - make test (runs available tests on the implementation of the specfile parser)
    - python specparser.py (same as "make")
    - python specparser.py -i path_to_specfile (same as "make SPEC='path_to_specfile'")


Supported specfile fields:

    - header tags in format "KEY:VALUE", where KEY is one of the following:
    NAME, VERSION, RELEASE, SUMMARY, LICENSE, URL, BUILDREQUIRES, REQUIRES, PREFIX,
    GROUP, BUILDROOT, EXCLUDEARCH, EXCLUSIVEARCH, CONFLICTS, BUILDARCH

    - sections in format "%KEY (-[PARAMETER])? [NAME]? \n [VALUE]", where KEY is
    one of the following: DESCRIPTION, PREP, BUILD, CHECK, INSTALL, PRE, FILES, 
    PACKAGE, CHANGELOG

    - commentaries beginning with "#" as the first character on a line

    - macro definitions in format: "%(global|define) [NAME] (OPTIONS)? BODY"

    - macro undefinitions in format: "%undefine [NAME]"
    
    - macro used in a condition in format: "{!?[NAME]:[BODY]}" or "{?[NAME]:[BODY]}"

    - conditions in format: "%(if|ifarch|ifos|ifnarch|ifnos) [CONDITION] \n [BODY]
    (%else [BODY])? %endif"
    