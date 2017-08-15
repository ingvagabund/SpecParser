unit_list: []
metastring: "#00%0            %2\n#01%0               %2\n#02%0            %2\n#03%0\
    \            %2\n#04%0            %2\n#05%0             %2\n#06%0            \
    \ %2\n#07%0             %2\n#08%0             %2\n#09%0             %2\n#010%0\
    \             %2\n#011%0             %2\n#012%0                %2\n#013%0    \
    \    %2\n#10%0      %2\n#11%0      %2\n\n#12%0\n%4\n\n#13%0\n%4\n\n#14%0\n%4\n\
    \n#15%0\n%4\n\n#16%0 %2 %3\n%4\n\n#30%0\n%4\n\n%4\n"
main_unit:
  - content: gettext
    block_type: 0
    option:
    key: BuildRequires
  - content: libtool
    block_type: 0
    option:
    key: BuildRequires
  - content: "The eject program allows the user to eject removable media (typically\n\
        CD-ROMs, floppy disks or Iomega Jaz or Zip disks) using software\ncontrol.\
        \ Eject can also control some multi-disk CD changers and even\nsome devices'\
        \ auto-eject features.\n\nInstall eject if you'd like to eject removable media\
        \ using software\ncontrol."
    block_type: 1
    name:
    parameters:
    subname:
    keyword: description
  - content: '%autosetup -n %{name}'
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
  - content: "%make_install\n\ninstall -m 755 -d %{buildroot}/%{_sbindir}\nln -s ../bin/eject\
        \ %{buildroot}/%{_sbindir}\n\n%find_lang %{name}"
    block_type: 1
    name:
    parameters:
    subname:
    keyword: install
  - content: "%license COPYING\n%doc README TODO ChangeLog\n%{_bindir}/*\n%{_sbindir}/*\n\
        %{_mandir}/man1/*"
    block_type: 1
    name:
    parameters: f
    subname: '%{name}.lang'
    keyword: files
history:
    content:
      - "* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>\
        \ - 2.1.5-21\n- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild"
      - "* Fri Jul 02 2010 Kamil Dudka <kdudka@redhat.com> 2.1.5-20\n- handle multi-partition\
        \ devices with spaces in mount points properly (#608502)"
    block_type: 1
    keyword: changelog
comments: []
metadata:
  - content: A program that ejects removable media using software control
    block_type: 0
    option:
    key: Summary
  - content: eject
    block_type: 0
    option:
    key: Name
  - content: 2.1.5
    block_type: 0
    option:
    key: Version
  - content: 21%{?dist}
    block_type: 0
    option:
    key: Release
  - content: GPLv2+
    block_type: 0
    option:
    key: License
  - content: '%{name}-%{version}.tar.gz'
    block_type: 0
    option:
    key: Source
  - content: eject-2.1.1-verbose.patch
    block_type: 0
    option:
    key: Patch1
  - content: eject-timeout.patch
    block_type: 0
    option:
    key: Patch2
  - content: eject-2.1.5-opendevice.patch
    block_type: 0
    option:
    key: Patch3
  - content: eject-2.1.5-spaces.patch
    block_type: 0
    option:
    key: Patch4
  - content: eject-2.1.5-lock.patch
    block_type: 0
    option:
    key: Patch5
  - content: eject-2.1.5-umount.patch
    block_type: 0
    option:
    key: Patch6
  - content: http://www.pobox.com/~tranter
    block_type: 0
    option:
    key: URL
  - content: s390 s390x
    block_type: 0
    option:
    key: ExcludeArch

