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

