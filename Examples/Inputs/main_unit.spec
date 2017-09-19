BuildRequires:  python >= 2.7.5
BuildRequires:  python-devel
BuildRequires:  python-setuptools

Requires: python >= 2.7.5, bash, wget, rpmdevtools, rpmlint
Requires: coreutils, rpm-build, openssh-clients, tar

%description
The GNU wget program downloads files from the Internet using the command-line.
 
%prep
%setup -q
 
%build
./configure
make
 
%install
make install prefix=$RPM_BUILD_ROOT/usr
 
%files
%defattr(-,root,root)
/usr/local/bin/wget
 
%doc %attr(0444,root,root) /usr/local/share/man/man1/wget.1
