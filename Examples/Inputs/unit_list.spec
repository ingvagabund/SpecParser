%package cmd-dnfs-base
Summary: Set of basic commands definitions
BuildArch: noarch

%description cmd-dnfs-base
Basic gofed commands definition

%package cmd-dnfs-build
Summary: Set of build commands definitions
BuildArch: noarch

%description cmd-dnfs-build
Build gofed commands definition

%package cmd-dnfs-scan
Summary: Set of scan commands definitions
BuildArch: noarch

%description cmd-dnfs-scan
Scan gofed commands definition

%package base
Summary: Implementation of base commands for gofed
BuildArch: noarch

%description base
Basic commands

%files cmd-dnfs-base
/usr/share/%{name}/cmd/README.md
/usr/share/%{name}/cmd/repo2spec/*.yml
/usr/share/%{name}/cmd/fetch/*.yml

%files base
/usr/share/%{name}/cmd/version/version.py
/usr/share/%{name}/cmd/repo2spec/*.py
/usr/share/%{name}/cmd/repo2spec/bitbucket2gospec
/usr/share/%{name}/cmd/review-request/*.py
/usr/share/%{name}/cmd/clean-resources/*.py
#%{_sysconfdir}/bash_completion.d/gofed-base_bash_completion
/usr/share/man/man1/gofed.1.gz
