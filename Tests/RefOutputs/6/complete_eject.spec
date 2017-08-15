main_unit:
  - description: "The eject program allows the user to eject removable media (typically\n\
        CD-ROMs, floppy disks or Iomega Jaz or Zip disks) using software\ncontrol.\
        \ Eject can also control some multi-disk CD changers and even\nsome devices'\
        \ auto-eject features.\n\nInstall eject if you'd like to eject removable media\
        \ using software\ncontrol."
  - prep: '%autosetup -n %{name}'
  - build: "%configure\n%make_build"
  - install: "%make_install\n\ninstall -m 755 -d %{buildroot}/%{_sbindir}\nln -s ../bin/eject\
        \ %{buildroot}/%{_sbindir}\n\n%find_lang %{name}"
  - files:
        meta:
            file: '%{name}.lang'
        list:
          - '%license COPYING'
          - '%doc README TODO ChangeLog'
          - '%{_bindir}/*'
          - '%{_sbindir}/*'
          - '%{_mandir}/man1/*'
  - buildtime:
        dependencies:
          - name: libtool
          - name: gettext
metadata:
  - Summary: A program that ejects removable media using software control
  - Name: eject
  - Version: 2.1.5
  - Release: 21%{?dist}
  - License: GPLv2+
  - Source: '%{name}-%{version}.tar.gz'
  - Patch1: eject-2.1.1-verbose.patch
  - Patch2: eject-timeout.patch
  - Patch3: eject-2.1.5-opendevice.patch
  - Patch4: eject-2.1.5-spaces.patch
  - Patch5: eject-2.1.5-lock.patch
  - Patch6: eject-2.1.5-umount.patch
  - URL: http://www.pobox.com/~tranter
  - ExcludeArch: s390 s390x
history:
    '1':
        comment: '- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild'
        date: Tue Feb 08 2011
        mark: '- 2.1.5-21'
        author: Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
    '0':
        comment: '- handle multi-partition devices with spaces in mount points properly
            (#608502)'
        date: Fri Jul 02 2010
        mark: 2.1.5-20
        author: Kamil Dudka <kdudka@redhat.com>

