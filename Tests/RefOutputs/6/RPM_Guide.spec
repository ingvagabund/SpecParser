main_unit:
  - description: "The IBM Jikes compiler translates Java source files to bytecode.\
        \ It\nalso supports incremental compilation and automatic makefile generation,\n\
        and is maintained by the Jikes Project:\nhttp://ibm.com/developerworks/opensource/jikes\n\
        \n%clean\nrm -rf $RPM_BUILD_ROOT"
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

