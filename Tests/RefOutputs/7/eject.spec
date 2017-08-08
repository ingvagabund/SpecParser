unit_list: []
metastring: "#00%0           %2\n#01%0        %2\n#02%0        %2\n#03%0        %2\n\
    \n#04%0        %2\n#05%0            %2\n#06%0        %2\n\n\n#12%0%4\n\n\n#13%0\n\
    %4\n\n\n#14%0\n%4\n\n#10%0  %2\n#11%0       %2 \n\n\n#15%0\n%4\n\n\n#16%0\n%4\n\
    \n\n#17%0\n%4\n\n\n\n#30%0\n%4 \n"
main_unit:
  - buildtime:
        dependencies:
          - name: requires description
  - runtime:
        dependencies:
            name: reqs
  - content: ''
    block_type: 1
    name:
    parameters:
    subname:
    keyword: description
  - content: '%autosetup'
    block_type: 1
    name:
    parameters:
    subname:
    keyword: prep
  - content: "%configure\n%make_build"
    block_type: 1
    name:
    parameters:
    subname:
    keyword: build
  - content: make check
    block_type: 1
    name:
    parameters:
    subname:
    keyword: check
  - content: "rm -rf $RPM_BUILD_ROOT\n%make_install"
    block_type: 1
    name:
    parameters:
    subname:
    keyword: install
  - content: "%license add-license-file-here\n\n%doc README TODO"
    block_type: 1
    name:
    parameters:
    subname:
    keyword: files
history:
    content:
      - "* Wed Mar 22 2017 Nikola Valesova\n-"
    block_type: 1
    keyword: changelog
comments: []
metadata:
  - content: eject
    block_type: 0
    option:
    key: Name
  - content: 1.2.5
    block_type: 0
    option:
    key: Version
  - content: 1%{?dist}
    block_type: 0
    option:
    key: Release
  - content: Short sumary
    block_type: 0
    option:
    key: Summary
  - content: GPLv2+
    block_type: 0
    option:
    key: License
  - content: http://www.pobox.com/~tranter
    block_type: 0
    option:
    key: URL
  - content: http://www.ibiblio.org/pub/Linux/utils/disk-management/%name}-%{version}%license}.tar.gz
    block_type: 0
    option:
    key: Source0

