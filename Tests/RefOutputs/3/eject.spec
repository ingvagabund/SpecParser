Name:           eject
Version:        1.2.5
Release:        1%{?dist}
Summary:        Short sumary
License:        GPLv2+
URL:            http://www.pobox.com/~tranter
Source0:        http://www.ibiblio.org/pub/Linux/utils/disk-management/%name}-%{version}%license}.tar.gz
BuildRequires:  requires description
Requires:       reqs

%description


%prep
%autosetup

%build
%configure
%make_build

%check
make check

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
%license add-license-file-here

%doc README TODO

%changelog
* Wed Mar 22 2017 Nikola Valesova
-

