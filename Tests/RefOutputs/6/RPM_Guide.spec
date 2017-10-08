main_unit:
  - description: "The IBM Jikes compiler translates Java source files to bytecode.\
        \ It\nalso supports incremental compilation and automatic makefile generation,\n\
        and is maintained by the Jikes Project:\nhttp://ibm.com/developerworks/opensource/jikes\n\
        \n%clean\nrm -rf $RPM_BUILD_ROOT"
metastring: "#00[0]%0 %2\n\n#010%0 %1 %3\n\n#01[1]%0 %2\n#02[2]%0 %2\n#03[3]%0 %2\n\
    #04[4]%0 %2\n#05[5]%0 %2\n#06[6]%0 %2\n#07[7]%0 %2\n#08[8]%0 %2\n#09[9]%0 %2\n\
    \n#10[0]%0\n%4\n\n"
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

