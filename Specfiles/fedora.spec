%global _dwz_low_mem_die_limit 0
%global provider        github
%global provider_tld    com
%global project        	ingvagabund
%global repo            gofed
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}

%global cmdsignature_commit 33207573a1875bc828da3f863e1de439d7af8166
%global cmdsignature_shortcommit %(c=%{cmdsignature_commit}; echo ${c:0:7})

%global gofedlib_commit c2e5b00ebc01616820e571aa554429b1461dc2c4
%global gofedlib_shortcommit %(c=%{gofedlib_commit}; echo ${c:0:7})

%global gofedresources_commit 7e414c78930a81167dc2cd4d3e9adb79eeed38a6
%global gofedresources_shortcommit %(c=%{gofedresources_commit}; echo ${c:0:7})

%global gofedinfra_commit 6bff7ae54535689e2ade3d0bd3d33d903a2190b9
%global gofedinfra_shortcommit %(c=%{gofedinfra_commit}; echo ${c:0:7})

%global commit 48d80fe18e643be7bd3ebc6ece22a6a07bb188d1
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

%global cmdsignature_repo cmdsignature
%global gofedlib_repo gofedlib
%global gofedresources_repo resources
%global gofedinfra_repo infra

%if ! 0%{?gobuild:1}
%define gobuild(o:) go build -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n')" -a -v -x %{?**}; 
%endif

Name:		gofed
Version:	1.0.0
Release:	0.9.rc1%{?dist}
Summary:	Tool for development of golang devel packages
License:	GPLv2+
URL:		https://github.com/%{project}/%{repo}
Source0:	https://github.com/%{project}/%{repo}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz
Source1:	https://github.com/%{project}/%{cmdsignature_repo}/archive/%{cmdsignature_commit}/%{cmdsignature_repo}-%{cmdsignature_shortcommit}.tar.gz
Source2:	https://github.com/%{project}/%{gofedlib_repo}/archive/%{gofedlib_commit}/%{gofedlib_repo}-%{gofedlib_shortcommit}.tar.gz
Source3:	https://github.com/%{project}/%{gofedresources_repo}/archive/%{gofedresources_commit}/%{gofedresources_repo}-%{gofedresources_shortcommit}.tar.gz
Source4:	https://github.com/%{project}/%{gofedinfra_repo}/archive/%{gofedinfra_commit}/%{gofedinfra_repo}-%{gofedinfra_shortcommit}.tar.gz

Patch0:         set-correct-paths.patch

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}

BuildRequires:  python >= 2.7.5
BuildRequires:  python-devel
BuildRequires:  python-setuptools

Requires: python >= 2.7.5, bash, wget, rpmdevtools, rpmlint
Requires: coreutils, rpm-build, openssh-clients, tar

Requires: %{name}-cmd-dnfs-base = %{version}-%{release}
Requires: python-cmdsignature = %{version}-%{release}
Requires: %{name}-infra = %{version}-%{release}
Requires: %{name}-base = %{version}-%{release}
Requires: bash-completion

Conflicts: gofed < 1.0.0

%description
Tool to automize packaging of golang devel source codes.
The main goal is to automatize packaging, i.e. provide spec file generators,
discovery of tests, imported and provided packages,
check of up-to-date state of dependencies,
preparation of review and
check of spec file (gofed lint).

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

%package scan
Summary: Set of commands for scanning golang projects
Requires: %{name} = %{version}-%{release}
Requires: %{name}-cmd-dnfs-scan = %{version}-%{release}
Requires: python-cmdsignature = %{version}-%{release}
Requires: graphviz
BuildArch: noarch
Conflicts: gofed-scan < 1.0.0


%description scan
Subpackage providing commands for scanning of golang project, i.e.
comparison of APIs of two golang projects,
generator of xml files representing exported symbols and
scan of golang packages and generator of dependency graph.

%package build
Summary: Set of commands for building golang projects
Requires: %{name} = %{version}-%{release}
Requires: %{name}-cmd-dnfs-build = %{version}-%{release}
Requires: python-cmdsignature = %{version}-%{release}
BuildArch: noarch
Conflicts: gofed-build < 1.0.0

%description build
Subpackage providing commands for scratch builds, builds,
pulls, pushes, updates, overrides and other commands
that can be used for package maitainance.

The commands support running one command on multiple branches at once.

%package gofedlib
Summary: Gofedlib
BuildRequires: python-fedora python-jinja2 python-markupsafe
Requires: python-fedora python-jinja2 python-markupsafe python-PyGithub python2-hglib

%description gofedlib
Gofedlib

%package resources
Summary: Gofed resources
BuildRequires: python2-hglib
Requires: python2-hglib
Requires: %{name}-gofedlib = %{version}-%{release}
BuildArch: noarch

%description resources
Gofed resources

%package infra
Summary: Gofed infra
BuildRequires: python-jsonschema koji GitPython python-pycurl python2-hglib python-gitdb
Requires: python-jsonschema koji GitPython python-pycurl python2-hglib python-gitdb
Requires: %{name}-gofedlib = %{version}-%{release}
Requires: %{name}-resources = %{version}-%{release}
BuildArch: noarch

%description infra
Gofed infra

%package docker
Summary: Run gofed commands as a container
Requires: %{name}-cmd-dnfs-base = %{version}-%{release}
Requires: python-cmdsignature = %{version}-%{release}
Requires: docker
BuildArch: noarch
ExclusiveArch: %{ix86} x86_64 %{arm} aarch64 ppc64le s390x %{mips}

%description docker
Run gofed commands as a container

%package -n python-cmdsignature
Summary: Command signature python module
BuildArch: noarch
BuildRequires: PyYAML
Requires: python >= 2.7.5
Requires: PyYAML

%description -n python-cmdsignature
Command signature python module

%prep
%setup -q -n %{cmdsignature_repo}-%{cmdsignature_commit} -T -b 1
%setup -q -n %{gofedlib_repo}-%{gofedlib_commit} -T -b 2
%setup -q -n %{gofedresources_repo}-%{gofedresources_commit} -T -b 3
%setup -q -n %{gofedinfra_repo}-%{gofedinfra_commit} -T -b 4
%setup -q -n %{repo}-%{commit}
%patch0 -p1

%build
pushd ../%{cmdsignature_repo}-%{cmdsignature_commit}
%{__python2} setup.py build
popd

pushd ../%{gofedlib_repo}-%{gofedlib_commit}
pushd gofedlib/go/symbolsextractor
%gobuild -o parseGo parseGo.go
popd
%{__python2} setup.py build
popd

pushd ../%{gofedresources_repo}-%{gofedresources_commit}
%{__python2} setup.py build
popd

pushd ../%{gofedinfra_repo}-%{gofedinfra_commit}
%{__python2} setup.py build
popd

%install
# install cmdsignature as standard python module
pushd ../%{cmdsignature_repo}-%{cmdsignature_commit}
%{__python2} setup.py install --skip-build --root %{buildroot}
popd

pushd ../%{gofedlib_repo}-%{gofedlib_commit}
%{__python2} setup.py install --skip-build --root %{buildroot}
popd

pushd ../%{gofedresources_repo}-%{gofedresources_commit}
%{__python2} setup.py install --skip-build --root %{buildroot}
popd

pushd ../%{gofedinfra_repo}-%{gofedinfra_commit}
%{__python2} setup.py install --skip-build --root %{buildroot}
popd

# copy command definitions under gofed-cmd-dnf-[base|build|scan]
mkdir -p %{buildroot}/usr/share/%{name}/
cp -rpav cmd %{buildroot}/usr/share/%{name}/.
cp -pav *.py %{buildroot}/usr/share/%{name}/.

# install binaries
install -m 755 -d %{buildroot}/%{_bindir}
cp -pav gofed %{buildroot}/usr/bin/gofed
cp -pav gofed-docker %{buildroot}/usr/bin/gofed-docker

# TODO: generate bash completion via cmdsignature
# TODO: generate man pages via cmdsignature

cp -r modules %{buildroot}/usr/share/%{name}/.
# copy config
mkdir -p %{buildroot}%{_sysconfdir}
cp config/gofed.conf %{buildroot}%{_sysconfdir}/.
mkdir -p %{buildroot}/usr/share/%{name}/config
cp config/gofed.conf %{buildroot}/usr/share/%{name}/config/.
# directory for local database
install -m 755 -d %{buildroot}/%{_sharedstatedir}/%{name}
# copy golang list and native imports
cp -r data %{buildroot}%{_sharedstatedir}/%{name}/.
# working directory under /var/lib/gofed
install -m 775 -d %{buildroot}/%{_sharedstatedir}/%{name}/resource_provider
install -m 775 -d %{buildroot}/%{_sharedstatedir}/%{name}/resource_client
install -m 775 -d %{buildroot}/%{_sharedstatedir}/%{name}/storage
install -m 775 -d %{buildroot}/%{_sharedstatedir}/%{name}/simplefilestorage
# man pages
mkdir -p %{buildroot}/usr/share/man/man1
cp docs/gofed.1 %{buildroot}/usr/share/man/man1/gofed.1

%check
export PYTHONPATH=%{buildroot}/%{python2_sitelib}:%{buildroot}/usr/share/gofed:%{buildroot}/usr/share
./hack/test-cmd.sh
rm $(find %{buildroot}/usr/share/%{name} -iname "*.py[c|o]")
rm -r %{buildroot}/usr/share/%{name}/config

%pre
getent group gofed >/dev/null || groupadd -r gofed
getent passwd gofed >/dev/null || useradd -r -g gofed -d / -s /sbin/nologin \
        -c "Gofed user" gofed

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files cmd-dnfs-base
/usr/share/%{name}/cmd/README.md
/usr/share/%{name}/cmd/repo2spec/*.yml
/usr/share/%{name}/cmd/fetch/*.yml
/usr/share/%{name}/cmd/create-tracker/*.yml
/usr/share/%{name}/cmd/ggi/*.yml
/usr/share/%{name}/cmd/inspect/*.yml
/usr/share/%{name}/cmd/check-deps/*.yml
/usr/share/%{name}/cmd/lint/*.yml
/usr/share/%{name}/cmd/review-request/*.yml
/usr/share/%{name}/cmd/clean-resources/*.yml
/usr/share/%{name}/cmd/base.yml

%files cmd-dnfs-build
/usr/share/%{name}/cmd/tools/*.yml
/usr/share/%{name}/cmd/bump-spec/*.yml
/usr/share/%{name}/cmd/wizard/*.yml
/usr/share/%{name}/cmd/build.yml

%files cmd-dnfs-scan
/usr/share/%{name}/cmd/goapidiff/*.yml
/usr/share/%{name}/cmd/approx-deps/*.yml
/usr/share/%{name}/cmd/scan-deps/*.yml
/usr/share/%{name}/cmd/scan-distro/*.yml
/usr/share/%{name}/cmd/scan-packages/*.yml
/usr/share/%{name}/cmd/unit-test/*.yml
/usr/share/%{name}/cmd/scan.yml

%files base
/usr/share/%{name}/cmd/version/version.py
/usr/share/%{name}/cmd/repo2spec/*.py
/usr/share/%{name}/cmd/repo2spec/bitbucket2gospec
/usr/share/%{name}/cmd/repo2spec/github2gospec
/usr/share/%{name}/cmd/repo2spec/googlecode2gospec
/usr/share/%{name}/cmd/fetch/*.py
/usr/share/%{name}/cmd/create-tracker/*.py
/usr/share/%{name}/cmd/ggi/*.py
/usr/share/%{name}/cmd/inspect/*.py
/usr/share/%{name}/cmd/check-deps/*.py
/usr/share/%{name}/cmd/lint/*.py
/usr/share/%{name}/cmd/review-request/*.py
/usr/share/%{name}/cmd/clean-resources/*.py
#%{_sysconfdir}/bash_completion.d/gofed-base_bash_completion
/usr/share/man/man1/gofed.1.gz

%files build
/usr/share/%{name}/cmd/tools/*.py
/usr/share/%{name}/cmd/tools/bbobranches
/usr/share/%{name}/cmd/tools/build
/usr/share/%{name}/cmd/tools/gcp
/usr/share/%{name}/cmd/tools/pull
/usr/share/%{name}/cmd/tools/push
/usr/share/%{name}/cmd/tools/scratch-build
/usr/share/%{name}/cmd/tools/update
/usr/share/%{name}/cmd/bump-spec/*.py
/usr/share/%{name}/cmd/wizard/*.py
#%{_sysconfdir}/bash_completion.d/gofed-build_bash_completion

%files scan
/usr/share/%{name}/cmd/goapidiff/*.py
/usr/share/%{name}/cmd/approx-deps/*.py
/usr/share/%{name}/cmd/scan-deps/*.py
/usr/share/%{name}/cmd/scan-distro/*.py
/usr/share/%{name}/cmd/scan-packages/*.py
/usr/share/%{name}/cmd/unit-test/*.py
#%{_sysconfdir}/bash_completion.d/gofed-scan_bash_completion

%files gofedlib
%license LICENSE 
%{python2_sitelib}/gofedlib
%{python2_sitelib}/gofedlib-?.?.???-py2.7.egg-info
%{_bindir}/gofedlib-cli

%files resources
%license LICENSE 
%{python2_sitelib}/gofedresources
%{python2_sitelib}/gofedresources-?.?.?-py2.7.egg-info

%files infra
%license LICENSE 
%{python2_sitelib}/gofedinfra
%{python2_sitelib}/gofedinfra-?.?.?-py2.7.egg-info

%files -n python-cmdsignature
%license LICENSE 
%{python2_sitelib}/cmdsignature
%{python2_sitelib}/cmdsignature-?.?.?-py2.7.egg-info

%files docker
%{_bindir}/gofed-docker

%files
%license LICENSE
%doc *.md
%config(noreplace) /etc/gofed.conf
/usr/share/%{name}/modules
#%{_mandir}/man1/gofed.1.gz
%attr(-, gofed, gofed) %{_sharedstatedir}/%{name}
/usr/bin/%{name}
/usr/share/%{name}/*.py

%changelog
* Wed Mar 01 2017 Jan Chaloupka <jchaloup@redhat.com> - 1.0.0-0.9.rc1
- Provide a simple man page
  resolves: #1426854

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.8.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 25 2017 Jan Chaloupka <jchaloup@redhat.com> - 1.0.0-0.7.rc1
- Bump to a7766e5587800fc3b49c46149605cd95a98eb31b
  resolves: #1416407

* Tue Dec 27 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.0.0-0.6.rc1
- Compile the docker one only for supported arches

* Tue Oct 04 2016 jchaloup <jchaloup@redhat.com> - 1.0.0-0.5.rc1
- create missing directories under /var/lib/gofed

* Fri Sep 23 2016 jchaloup <jchaloup@redhat.com> - 1.0.0-0.4.rc1
- extend the list of known deps directories with vendor (upstream #117)

* Thu Sep 22 2016 jchaloup <jchaloup@redhat.com> - 1.0.0-0.3.rc1
- Add missing deps, minor fixes

* Wed Sep 21 2016 jchaloup <jchaloup@redhat.com> - 1.0.0-0.2.rc1
- Bump deps, conflict with older gofed

* Sun Sep 18 2016 jchaloup <jchaloup@redhat.com> - 1.0.0-0.rc1.1
- Update to gofed infrastructure

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.10-5
- https://fedoraproject.org/wiki/Changes/golang1.7

* Wed Apr 06 2016 jchaloup <jchaloup@redhat.com> - 0.0.10-4
- Define gobuild macro if not defined (for other distros without go-srpm-macros)

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.10-3
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 18 2015 jchaloup <jchaloup@redhat.com> - 0.0.10-1
- Update to 0.0.10

* Thu Sep 17 2015 jchaloup <jchaloup@redhat.com> - 0.0.9-3
- Bump to upstream 04cd8f0c083e3e80bbe17fc4acd2192a1628a5be

* Thu Sep 10 2015 jchaloup <jchaloup@redhat.com> - 0.0.9-2
- Define license macro if not defined

* Thu Sep 10 2015 jchaloup <jchaloup@redhat.com> - 0.0.9-1
- Updated to version 0.0.9

* Mon Aug 31 2015 jchaloup <jchaloup@redhat.com> - 0.0.8-3
- Add -d option when copying symlinks. Otherwise symlinks are followed.

* Sat Aug 29 2015 jchaloup <jchaloup@redhat.com> - 0.0.8-2
- Add missing symlinks

* Fri Aug 21 2015 jchaloup <jchaloup@redhat.com> - 0.0.8-1
- Updated to version 0.0.8

* Sat Aug 01 2015 jchaloup <jchaloup@redhat.com> - 0.0.7-1
- Updated to version 0.0.7

* Sat Jul 11 2015 jchaloup <jchaloup@redhat.com> - 0.0.6-1
- Updated to version 0.0.6

* Tue Jun 23 2015 jchaloup <jchaloup@redhat.com> - 0.0.5-1
- Updated to version 0.0.5

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 09 2015 jchaloup <jchaloup@redhat.com> - 0.0.4-1
- Update to version 0.0.4
  related: #1204614

* Sat May 09 2015 jchaloup <jchaloup@redhat.com> - 0.0.3-1
- Update to version 0.0.3
  related: #1204614

* Thu Apr 02 2015 jchaloup <jchaloup@redhat.com> - 0.0.1-0.1.git62b0051
- Update to version 0.0.1
  related: #1204614

* Mon Mar 23 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.gitcab0f0b
- Initial commit for Fedora
  resolves: #1204614
