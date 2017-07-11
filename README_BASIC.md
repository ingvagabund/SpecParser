List of supported specfile fields:

    1 Header Tags
        Header tag and its value are separated by ':'. The ':' character
        can be surrounded by whitespace characters.

        Header tags may contain the following keywords:
        BUILDARCH, BUILDREQUIRES, BUILDROOT, CONFLICTS, EXCLUDEARCH, 
        EXCLUSIVEARCH, GROUP, LICENSE, NAME, PATCH, PRE, PREFIX, PREP, PREUN,
        POST, POSTUN, PROVIDES, RELEASE, REQUIRES, SOURCE, SUMMARY, URL,
        VERSION

        Syntax of header tags can be found here:    
        http://wiki.rosalab.ru/en/index.php/RPM_spec_file_syntax#Spec_Header

    2 Section Tags
        Starting with section header tag, ending with the start of a new field
        (except for comments).

        Section header tags may contain the following header tags:
        BUILD, CHANGELOG, CHECK, CLEAN, DESCRIPTION, FILES, INSTALL, PACKAGE, 
        PRE, PREP, PREUN, POST, POSTUN

        Detailed syntax of section tags and sections can be found here:
        https://fedoraproject.org/wiki/How_to_create_an_RPM_package#SPEC_file_sections_explained

    3 Comments
        Comments start with '#' at the beginning of a line and end with 
        a newline. A '#' anywhere else will not be identified as a comment.
        
        Comments have the same syntax as described here:
        https://docs.fedoraproject.org/ro/Fedora_Draft_Documentation/0.1/html/RPM_Guide/ch-specfile-syntax.html#id722547

    4 Macro Definitions
        Macros can be defined by using one of the following keywords:
        define, global.

        The keyword, name and body of a macro are separated by at least one
        whitespace character.

        Syntax of macro definitions and some examples can be found here:        
        https://docs.fedoraproject.org/ro/Fedora_Draft_Documentation/0.1/html/RPM_Guide/ch22s02.html

    5 Macro Undefinitions
        Macro undefinitions can be done by using the keyword undefine. The name
        of a macro is separated by at least one whitespace character.

        Syntax of a macro undefinition can be found here:
        https://docs.fedoraproject.org/ro/Fedora_Draft_Documentation/0.1/html/RPM_Guide/ch22s02.html

    6 Conditional Macros
        Syntax of conditional macros can be found here:
        https://docs.fedoraproject.org/ro/Fedora_Draft_Documentation/0.1/html/RPM_Guide/ch22s02s02.html
        
        The macro name and expression are separated by ':'. No whitespace 
        characters allowed between '%', '{', '!' and '?' characters.

    7 Conditionals
        Conditionals may contain one of the following keywords:
        if, ifarch, ifnarch, ifos, ifnos, else, endif.

        When 'ifXXX' keyword is used, the rest of the line is considered
        as a conditional expression that shall be evaluated. The keyword
        and the conditional expression are separated by at least one
        whitespace character.

        Conditionals nested within other conditionals are supported. 

        Syntax of conditionals can be found here:        
        http://ftp.rpm.org/max-rpm/s1-rpm-specref-conditionals.html
