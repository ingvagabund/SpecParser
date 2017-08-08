unit_list: []
metastring: "#40%0\n \n#08%0 %1     %3\n#09%0 %1            %3 \n#010%0 %1     %3\n\
    #011%0 %1     %3\n#012%0 %1 %3\n \n#00%0  %2\n#01%0        %2\n#02%0        %2\n\
    #03%0           %2\n#04%0        %2\n#05%0        %2\n#06%0         %2\n#07%0\
    \          %2\n \n#10%0\n%4\n \n#11%0\n%4\n \n#12%0\n%4\n \n#13%0\n%4\n \n#14%0\n\
    %4\n"
main_unit:
  - content: The GNU wget program downloads files from the Internet using the command-line.
    block_type: 1
    name:
    parameters:
    subname:
    keyword: description
  - content: '%setup -q'
    block_type: 1
    name:
    parameters:
    subname:
    keyword: prep
  - content: "./configure\nmake"
    block_type: 1
    name:
    parameters:
    subname:
    keyword: build
  - content: make install prefix=$RPM_BUILD_ROOT/usr
    block_type: 1
    name:
    parameters:
    subname:
    keyword: install
  - content: "%defattr(-,root,root)\n/usr/local/bin/wget\n \n%doc %attr(0444,root,root)\
        \ /usr/local/share/man/man1/wget.1"
    block_type: 1
    name:
    parameters:
    subname:
    keyword: files
history: {}
comments:
  - content: '# This is a sample spec file for wget'
    block_type: 5
metadata:
  - content: '%{buildroot}'
    block_type: 0
    option:
    key: BuildRoot
  - content: GNU wget
    block_type: 0
    option:
    key: Summary
  - content: GPL
    block_type: 0
    option:
    key: License
  - content: '%{name}'
    block_type: 0
    option:
    key: Name
  - content: '%{version}'
    block_type: 0
    option:
    key: Version
  - content: '%{release}'
    block_type: 0
    option:
    key: Release
  - content: '%{name}-%{version}.tar.gz'
    block_type: 0
    option:
    key: Source
  - content: Development/Tools
    block_type: 0
    option:
    key: Group
  - body: /home/strike/mywget
    block_type: 2
    name: _topdir
    keyword: define
    options:
  - body: wget
    block_type: 2
    name: name
    keyword: define
    options:
  - body: '1'
    block_type: 2
    name: release
    keyword: define
    options:
  - body: '1.12'
    block_type: 2
    name: version
    keyword: define
    options:
  - body: '%{_topdir}/%{name}-%{version}-root'
    block_type: 2
    name: buildroot
    keyword: define
    options:

