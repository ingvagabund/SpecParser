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
          - '%doc %attr(0444,root,root) /usr/local/share/man/man1/wget.1'
metastring: "#40%0\n \n#08%0 %1     %3\n#09%0 %1            %3 \n#010%0 %1     %3\n\
    #011%0 %1     %3\n#012%0 %1 %3\n \n#00[0]%0  %2\n#01[1]%0        %2\n#02[2]%0\
    \        %2\n#03[3]%0           %2\n#04[4]%0        %2\n#05[5]%0        %2\n#06[6]%0\
    \         %2\n#07[7]%0          %2\n \n#10[0]%0\n%4\n \n#11[1]%0\n%4\n \n#12[2]%0\n\
    %4\n \n#13[3]%0\n%4\n \n#14[4]%0\n%40\n%41\n \n%42\n"
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

