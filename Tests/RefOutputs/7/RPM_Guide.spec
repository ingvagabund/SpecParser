unit_list: []
metastring: "#00%0 %2\n\n#010%0 %1 %3\n\n#01%0 %2\n#02%0 %2\n#03%0 %2\n#04%0 %2\n\
    #05%0 %2\n#06%0 %2\n#07%0 %2\n#08%0 %2\n#09%0 %2\n\n#10%0\n%4\n\n"
main_unit:
  - content: "The IBM Jikes compiler translates Java source files to bytecode. It\n\
        also supports incremental compilation and automatic makefile generation,\n\
        and is maintained by the Jikes Project:\nhttp://ibm.com/developerworks/opensource/jikes\n\
        \n%clean\nrm -rf $RPM_BUILD_ROOT"
    block_type: 1
    name:
    parameters:
    subname:
    keyword: description
history: {}
comments: []
metadata:
  - content: java source to bytecode compiler
    block_type: 0
    option:
    key: Summary
  - content: IBM Public License, http://ibm.com/developerworks/oss/license10.html
    block_type: 0
    option:
    key: License
  - content: Development/Languages
    block_type: 0
    option:
    key: Group
  - content: jikes
    block_type: 0
    option:
    key: Name
  - content: jikes
    block_type: 0
    option:
    key: Provides
  - content: '1'
    block_type: 0
    option:
    key: Release
  - content: jikes-%{version}.tar.gz
    block_type: 0
    option:
    key: Source
  - content: http://ibm.com/developerworks/opensource/jikes
    block_type: 0
    option:
    key: URL
  - content: '%{version}'
    block_type: 0
    option:
    key: Version
  - content: /tmp/jikesrpm
    block_type: 0
    option:
    key: Buildroot
  - body: '1.17'
    block_type: 2
    name: version
    keyword: define
    options:

