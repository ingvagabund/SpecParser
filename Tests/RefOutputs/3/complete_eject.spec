Summary:        A program that ejects removable media using software control
Name:           eject
Version:        2.1.5
Release:        21%{?dist}
License:        GPLv2+
Source:         %{name}-%{version}.tar.gz
Patch1:         eject-2.1.1-verbose.patch
Patch2:         eject-timeout.patch
Patch3:         eject-2.1.5-opendevice.patch
Patch4:         eject-2.1.5-spaces.patch
Patch5:         eject-2.1.5-lock.patch
Patch6:         eject-2.1.5-umount.patch
URL:            http://www.pobox.com/~tranter
ExcludeArch:    s390 s390x
BuildRequires:  gettext
BuildRequires:  libtool

%description
The eject program allows the user to eject removable media (typically
CD-ROMs, floppy disks or Iomega Jaz or Zip disks) using software
control. Eject can also control some multi-disk CD changers and even
some devices' auto-eject features.

Install eject if you'd like to eject removable media using software
control.

%prep
%autosetup -n %{name}

%build
%configure
%make_build

%install
%make_install

install -m 755 -d %{buildroot}/%{_sbindir}
ln -s ../bin/eject %{buildroot}/%{_sbindir}

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc README TODO ChangeLog
%{_bindir}/*
%{_sbindir}/*
%{_mandir}/man1/*

%changelog
* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 02 2010 Kamil Dudka <kdudka@redhat.com> 2.1.5-20
- handle multi-partition devices with spaces in mount points properly (#608502)

