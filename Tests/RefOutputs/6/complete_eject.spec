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
metastring: "#00%0            %2\n#01%0               %2\n#02%0            %2\n#03%0\
    \            %2\n#04%0            %2\n#05%0             %2\n#06%0            \
    \ %2\n#07%0             %2\n#08%0             %2\n#09%0             %2\n#010%0\
    \             %2\n#011%0             %2\n#012%0                %2\n#013%0    \
    \    %2\n#10%0      %2\n#11%0      %2\n\n#12%0\n%4\n\n#13%0\n%4\n\n#14%0\n%4\n\
    \n#15%0\n%4\n\n#16%0 %2 %3\n%4\n\n#30%0\n%4\n\n%4\n"
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

