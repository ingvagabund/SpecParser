main_unit:
  - description:
  - prep: '%autosetup'
  - build: "%configure\n%make_build"
  - check: make check
  - install: "rm -rf $RPM_BUILD_ROOT\n%make_install"
  - files:
        list:
          - '%license add-license-file-here'
          - '%doc README TODO'
  - runtime:
        dependencies:
          - name: reqs
  - buildtime:
        dependencies:
          - name: requires description
metastring: "#00%0           %2\n#01%0        %2\n#02%0        %2\n#03%0        %2\n\
    \n#04%0        %2\n#05%0            %2\n#06%0        %2\n\n\n#12%0%4\n\n\n#13%0\n\
    %4\n\n\n#14%0\n%4\n\n#10%0  %2\n#11%0       %2 \n\n\n#15%0\n%4\n\n\n#16%0\n%4\n\
    \n\n#17%0\n%40\n\n%41\n\n\n\n#30%0\n%4 \n"
metadata:
  - Name: eject
  - Version: 1.2.5
  - Release: 1%{?dist}
  - Summary: Short sumary
  - License: GPLv2+
  - URL: http://www.pobox.com/~tranter
  - Source0: http://www.ibiblio.org/pub/Linux/utils/disk-management/%name}-%{version}%license}.tar.gz
history:
    '0':
        comment: '-'
        date: Wed Mar 22 2017
        mark:
        author: Nikola Valesova

