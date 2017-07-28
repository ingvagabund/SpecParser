{"HeaderTags": [{"block_type": 0, "content": "java source to bytecode compiler", "key": "Summary", "option": null}, {"block_type": 0, "content": "IBM Public License, http://ibm.com/developerworks/oss/license10.html", "key": "License", "option": null}, {"block_type": 0, "content": "Development/Languages", "key": "Group", "option": null}, {"block_type": 0, "content": "jikes", "key": "Name", "option": null}, {"block_type": 0, "content": "jikes", "key": "Provides", "option": null}, {"block_type": 0, "content": "1", "key": "Release", "option": null}, {"block_type": 0, "content": "jikes-%{version}.tar.gz", "key": "Source", "option": null}, {"block_type": 0, "content": "http://ibm.com/developerworks/opensource/jikes", "key": "URL", "option": null}, {"block_type": 0, "content": "%{version}", "key": "Version", "option": null}, {"block_type": 0, "content": "/tmp/jikesrpm", "key": "Buildroot", "option": null}], "MacroDefinitions": [{"block_type": 2, "body": "1.17", "keyword": "define", "name": "version", "options": null}], "SectionTags": [{"block_type": 1, "content": "The IBM Jikes compiler translates Java source files to bytecode. It\nalso supports incremental compilation and automatic makefile generation,\nand is maintained by the Jikes Project:\nhttp://ibm.com/developerworks/opensource/jikes\n\n%clean\nrm -rf $RPM_BUILD_ROOT", "keyword": "description", "name": null, "parameters": null, "subname": null}], "metastring": "#00%0 %2\n\n#20%0 %1 %3\n\n#01%0 %2\n#02%0 %2\n#03%0 %2\n#04%0 %2\n#05%0 %2\n#06%0 %2\n#07%0 %2\n#08%0 %2\n#09%0 %2\n\n#10%0\n%4\n\n"}