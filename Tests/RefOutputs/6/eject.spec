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
metastring: "#00[0]%0           %2\n#01[1]%0        %2\n#02[2]%0        %2\n#03[3]%0\
    \        %2\n\n#04[4]%0        %2\n#05[5]%0            %2\n#06[6]%0        %2\n\
    \n\n#12[0]%0%4\n\n\n#13[1]%0\n%4\n\n\n#14[2]%0\n%4\n\n#10[7]%0  %2\n#11[8]%0 \
    \      %2 \n\n\n#15[3]%0\n%4\n\n\n#16[4]%0\n%4\n\n\n#17[5]%0\n%40\n\n%41\n\n\n\
    \n#30%0\n%4 \n"
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

