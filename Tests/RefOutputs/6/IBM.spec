main_unit:
  - description: The GNU wget program downloads files from the Internet using the
        command-line.
  - prep: '%setup -q'
  - build: "./configure\nmake"
  - install: make install prefix=$RPM_BUILD_ROOT/usr
  - files:
        list:
          - '%defattr(-,root,root)'
          - /usr/local/bin/wget
          - ' '
          - '%doc %attr(0444,root,root) /usr/local/share/man/man1/wget.1'
metastring: "#40%0\n \n#08%0 %1     %3\n#09%0 %1            %3 \n#010%0 %1     %3\n\
    #011%0 %1     %3\n#012%0 %1 %3\n \n#00%0  %2\n#01%0        %2\n#02%0        %2\n\
    #03%0           %2\n#04%0        %2\n#05%0        %2\n#06%0         %2\n#07%0\
    \          %2\n \n#10%0\n%4\n \n#11%0\n%4\n \n#12%0\n%4\n \n#13%0\n%4\n \n#14%0\n\
    %4\n"
comments:
  - '# This is a sample spec file for wget'
metadata:
  - BuildRoot: '%{buildroot}'
  - Summary: GNU wget
  - License: GPL
  - Name: '%{name}'
  - Version: '%{version}'
  - Release: '%{release}'
  - Source: '%{name}-%{version}.tar.gz'
  - Group: Development/Tools
  - '%_topdir': /home/strike/mywget
  - '%name': wget
  - '%release': '1'
  - '%version': '1.12'
  - '%buildroot': '%{_topdir}/%{name}-%{version}-root'

