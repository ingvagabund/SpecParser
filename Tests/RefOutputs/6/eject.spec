main_unit:
  - buildtime:
        dependencies:
          - name: requires description
  - runtime:
        dependencies:
          - name: reqs
  - description:
  - prep: '%autosetup'
  - build: "%configure\n%make_build"
  - check: make check
  - install: "rm -rf $RPM_BUILD_ROOT\n%make_install"
  - files: "%license add-license-file-here\n\n%doc README TODO"
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

