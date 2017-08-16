main_unit:
  - description: "The IBM Jikes compiler translates Java source files to bytecode.\
        \ It\nalso supports incremental compilation and automatic makefile generation,\n\
        and is maintained by the Jikes Project:\nhttp://ibm.com/developerworks/opensource/jikes\n\
        \n%clean\nrm -rf $RPM_BUILD_ROOT"
metastring: "#00%0 %2\n\n#010%0 %1 %3\n\n#01%0 %2\n#02%0 %2\n#03%0 %2\n#04%0 %2\n\
    #05%0 %2\n#06%0 %2\n#07%0 %2\n#08%0 %2\n#09%0 %2\n\n#10%0\n%4\n\n"
metadata:
  - Summary: java source to bytecode compiler
  - License: IBM Public License, http://ibm.com/developerworks/oss/license10.html
  - Group: Development/Languages
  - Name: jikes
  - Provides: jikes
  - Release: '1'
  - Source: jikes-%{version}.tar.gz
  - URL: http://ibm.com/developerworks/opensource/jikes
  - Version: '%{version}'
  - Buildroot: /tmp/jikesrpm
  - '%version': '1.17'

