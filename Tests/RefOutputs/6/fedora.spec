metadata:
  - Name: gofed
  - Version: 1.0.0
  - Release: 0.9.rc1%{?dist}
  - Summary: Tool for development of golang devel packages
  - License: GPLv2+
  - URL: https://github.com/%{project}/%{repo}
  - Source0: https://github.com/%{project}/%{repo}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz
  - Source1: https://github.com/%{project}/%{cmdsignature_repo}/archive/%{cmdsignature_commit}/%{cmdsignature_repo}-%{cmdsignature_shortcommit}.tar.gz
  - Source2: https://github.com/%{project}/%{gofedlib_repo}/archive/%{gofedlib_commit}/%{gofedlib_repo}-%{gofedlib_shortcommit}.tar.gz
  - Source3: https://github.com/%{project}/%{gofedresources_repo}/archive/%{gofedresources_commit}/%{gofedresources_repo}-%{gofedresources_shortcommit}.tar.gz
  - Source4: https://github.com/%{project}/%{gofedinfra_repo}/archive/%{gofedinfra_commit}/%{gofedinfra_repo}-%{gofedinfra_shortcommit}.tar.gz
  - Patch0: set-correct-paths.patch
  - ExclusiveArch: '%{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 %{arm}}'
  - Conflicts: gofed < 1.0.0
  - '%_dwz_low_mem_die_limit': '0'
  - '%provider': github
  - '%provider_tld': com
  - '%project': ingvagabund
  - '%repo': gofed
  - '%provider_prefix': '%{provider}.%{provider_tld}/%{project}/%{repo}'
  - '%cmdsignature_commit': 33207573a1875bc828da3f863e1de439d7af8166
  - '%cmdsignature_shortcommit': '%(c=%{cmdsignature_commit}; echo ${c:0:7})'
  - '%gofedlib_commit': c2e5b00ebc01616820e571aa554429b1461dc2c4
  - '%gofedlib_shortcommit': '%(c=%{gofedlib_commit}; echo ${c:0:7})'
  - '%gofedresources_commit': 7e414c78930a81167dc2cd4d3e9adb79eeed38a6
  - '%gofedresources_shortcommit': '%(c=%{gofedresources_commit}; echo ${c:0:7})'
  - '%gofedinfra_commit': 6bff7ae54535689e2ade3d0bd3d33d903a2190b9
  - '%gofedinfra_shortcommit': '%(c=%{gofedinfra_commit}; echo ${c:0:7})'
  - '%commit': 48d80fe18e643be7bd3ebc6ece22a6a07bb188d1
  - '%shortcommit': '%(c=%{commit}; echo ${c:0:7})'
  - '%cmdsignature_repo': cmdsignature
  - '%gofedlib_repo': gofedlib
  - '%gofedresources_repo': resources
  - '%gofedinfra_repo': infra
  - '%gobuild': go build -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An
        -tx1|tr -d ' \\n')" -a -v -x %{?**};
    condition:
      - '! 0%{?gobuild:1}'
comments:
  - '# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required'
  - '# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.'
  - '#define license tag if not already defined'
main_unit:
  - description: "Tool to automize packaging of golang devel source codes.\nThe main\
        \ goal is to automatize packaging, i.e. provide spec file generators,\ndiscovery\
        \ of tests, imported and provided packages,\ncheck of up-to-date state of\
        \ dependencies,\npreparation of review and\ncheck of spec file (gofed lint)."
  - runtime:
        dependencies:
          - name: bash-completion
          - name: '%{name}-base = %{version}-%{release}'
          - name: '%{name}-infra = %{version}-%{release}'
          - name: python-cmdsignature = %{version}-%{release}
          - name: '%{name}-cmd-dnfs-base = %{version}-%{release}'
          - name: coreutils, rpm-build, openssh-clients, tar
          - name: python >= 2.7.5, bash, wget, rpmdevtools, rpmlint
  - buildtime:
        dependencies:
          - name: python-setuptools
          - name: python-devel
          - name: python >= 2.7.5
          - name: '%{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}'
  - prep: "%setup -q -n %{cmdsignature_repo}-%{cmdsignature_commit} -T -b 1\n%setup\
        \ -q -n %{gofedlib_repo}-%{gofedlib_commit} -T -b 2\n%setup -q -n %{gofedresources_repo}-%{gofedresources_commit}\
        \ -T -b 3\n%setup -q -n %{gofedinfra_repo}-%{gofedinfra_commit} -T -b 4\n\
        %setup -q -n %{repo}-%{commit}\n%patch0 -p1"
  - build: "pushd ../%{cmdsignature_repo}-%{cmdsignature_commit}\n%{__python2} setup.py\
        \ build\npopd\n\npushd ../%{gofedlib_repo}-%{gofedlib_commit}\npushd gofedlib/go/symbolsextractor\n\
        %gobuild -o parseGo parseGo.go\npopd\n%{__python2} setup.py build\npopd\n\n\
        pushd ../%{gofedresources_repo}-%{gofedresources_commit}\n%{__python2} setup.py\
        \ build\npopd\n\npushd ../%{gofedinfra_repo}-%{gofedinfra_commit}\n%{__python2}\
        \ setup.py build\npopd"
  - install: "# install cmdsignature as standard python module\npushd ../%{cmdsignature_repo}-%{cmdsignature_commit}\n\
        %{__python2} setup.py install --skip-build --root %{buildroot}\npopd\n\npushd\
        \ ../%{gofedlib_repo}-%{gofedlib_commit}\n%{__python2} setup.py install --skip-build\
        \ --root %{buildroot}\npopd\n\npushd ../%{gofedresources_repo}-%{gofedresources_commit}\n\
        %{__python2} setup.py install --skip-build --root %{buildroot}\npopd\n\npushd\
        \ ../%{gofedinfra_repo}-%{gofedinfra_commit}\n%{__python2} setup.py install\
        \ --skip-build --root %{buildroot}\npopd\n\n# copy command definitions under\
        \ gofed-cmd-dnf-[base|build|scan]\nmkdir -p %{buildroot}/usr/share/%{name}/\n\
        cp -rpav cmd %{buildroot}/usr/share/%{name}/.\ncp -pav *.py %{buildroot}/usr/share/%{name}/.\n\
        \n# install binaries\ninstall -m 755 -d %{buildroot}/%{_bindir}\ncp -pav gofed\
        \ %{buildroot}/usr/bin/gofed\ncp -pav gofed-docker %{buildroot}/usr/bin/gofed-docker\n\
        \n# TODO: generate bash completion via cmdsignature\n# TODO: generate man\
        \ pages via cmdsignature\n\ncp -r modules %{buildroot}/usr/share/%{name}/.\n\
        # copy config\nmkdir -p %{buildroot}%{_sysconfdir}\ncp config/gofed.conf %{buildroot}%{_sysconfdir}/.\n\
        mkdir -p %{buildroot}/usr/share/%{name}/config\ncp config/gofed.conf %{buildroot}/usr/share/%{name}/config/.\n\
        # directory for local database\ninstall -m 755 -d %{buildroot}/%{_sharedstatedir}/%{name}\n\
        # copy golang list and native imports\ncp -r data %{buildroot}%{_sharedstatedir}/%{name}/.\n\
        # working directory under /var/lib/gofed\ninstall -m 775 -d %{buildroot}/%{_sharedstatedir}/%{name}/resource_provider\n\
        install -m 775 -d %{buildroot}/%{_sharedstatedir}/%{name}/resource_client\n\
        install -m 775 -d %{buildroot}/%{_sharedstatedir}/%{name}/storage\ninstall\
        \ -m 775 -d %{buildroot}/%{_sharedstatedir}/%{name}/simplefilestorage\n# man\
        \ pages\nmkdir -p %{buildroot}/usr/share/man/man1\ncp docs/gofed.1 %{buildroot}/usr/share/man/man1/gofed.1"
  - check: "export PYTHONPATH=%{buildroot}/%{python2_sitelib}:%{buildroot}/usr/share/gofed:%{buildroot}/usr/share\n\
        ./hack/test-cmd.sh\nrm $(find %{buildroot}/usr/share/%{name} -iname \"*.py[c|o]\"\
        )\nrm -r %{buildroot}/usr/share/%{name}/config"
  - pre: "getent group gofed >/dev/null || groupadd -r gofed\ngetent passwd gofed\
        \ >/dev/null || useradd -r -g gofed -d / -s /sbin/nologin \\\n        -c \"\
        Gofed user\" gofed"
  - files:
        list:
          - '%license LICENSE'
          - '%doc *.md'
          - '%config(noreplace) /etc/gofed.conf'
          - /usr/share/%{name}/modules
          - '#%{_mandir}/man1/gofed.1.gz'
          - '%attr(-, gofed, gofed) %{_sharedstatedir}/%{name}'
          - /usr/bin/%{name}
          - /usr/share/%{name}/*.py
history:
    '24':
        comment: '- Compile the docker one only for supported arches'
        date: Tue Dec 27 2016
        mark: '- 1.0.0-0.6.rc1'
        author: Fabio Alessandro Locati <fale@fedoraproject.org>
    '25':
        comment: "- Bump to a7766e5587800fc3b49c46149605cd95a98eb31b\n  resolves:\
            \ #1416407"
        date: Wed Jan 25 2017
        mark: '- 1.0.0-0.7.rc1'
        author: Jan Chaloupka <jchaloup@redhat.com>
    '22':
        comment: '- extend the list of known deps directories with vendor (upstream
            #117)'
        date: Fri Sep 23 2016
        mark: '- 1.0.0-0.4.rc1'
        author: jchaloup <jchaloup@redhat.com>
    '26':
        comment: '- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild'
        date: Fri Feb 10 2017
        mark: '- 1.0.0-0.8.rc1'
        author: Fedora Release Engineering <releng@fedoraproject.org>
    '27':
        comment: "- Provide a simple man page\n  resolves: #1426854"
        date: Wed Mar 01 2017
        mark: '- 1.0.0-0.9.rc1'
        author: Jan Chaloupka <jchaloup@redhat.com>
    '20':
        comment: '- Bump deps, conflict with older gofed'
        date: Wed Sep 21 2016
        mark: '- 1.0.0-0.2.rc1'
        author: jchaloup <jchaloup@redhat.com>
    '21':
        comment: '- Add missing deps, minor fixes'
        date: Thu Sep 22 2016
        mark: '- 1.0.0-0.3.rc1'
        author: jchaloup <jchaloup@redhat.com>
    '11':
        comment: '- Updated to version 0.0.9'
        date: Thu Sep 10 2015
        mark: '- 0.0.9-1'
        author: jchaloup <jchaloup@redhat.com>
    '10':
        comment: '- Add -d option when copying symlinks. Otherwise symlinks are followed.'
        date: Mon Aug 31 2015
        mark: '- 0.0.8-3'
        author: jchaloup <jchaloup@redhat.com>
    '13':
        comment: '- Bump to upstream 04cd8f0c083e3e80bbe17fc4acd2192a1628a5be'
        date: Thu Sep 17 2015
        mark: '- 0.0.9-3'
        author: jchaloup <jchaloup@redhat.com>
    '12':
        comment: '- Define license macro if not defined'
        date: Thu Sep 10 2015
        mark: '- 0.0.9-2'
        author: jchaloup <jchaloup@redhat.com>
    '15':
        comment: '- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild'
        date: Wed Feb 03 2016
        mark: '- 0.0.10-2'
        author: Fedora Release Engineering <releng@fedoraproject.org>
    '14':
        comment: '- Update to 0.0.10'
        date: Wed Nov 18 2015
        mark: '- 0.0.10-1'
        author: jchaloup <jchaloup@redhat.com>
    '17':
        comment: '- Define gobuild macro if not defined (for other distros without
            go-srpm-macros)'
        date: Wed Apr 06 2016
        mark: '- 0.0.10-4'
        author: jchaloup <jchaloup@redhat.com>
    '23':
        comment: '- create missing directories under /var/lib/gofed'
        date: Tue Oct 04 2016
        mark: '- 1.0.0-0.5.rc1'
        author: jchaloup <jchaloup@redhat.com>
    '19':
        comment: '- Update to gofed infrastructure'
        date: Sun Sep 18 2016
        mark: '- 1.0.0-0.rc1.1'
        author: jchaloup <jchaloup@redhat.com>
    '18':
        comment: '- https://fedoraproject.org/wiki/Changes/golang1.7'
        date: Thu Jul 21 2016
        mark: '- 0.0.10-5'
        author: Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
    '16':
        comment: '- https://fedoraproject.org/wiki/Changes/golang1.6'
        date: Mon Feb 22 2016
        mark: '- 0.0.10-3'
        author: Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
    '1':
        comment: "- Update to version 0.0.1\n  related: #1204614"
        date: Thu Apr 02 2015
        mark: '- 0.0.1-0.1.git62b0051'
        author: jchaloup <jchaloup@redhat.com>
    '0':
        comment: "- Initial commit for Fedora\n  resolves: #1204614"
        date: Mon Mar 23 2015
        mark: '- 0-0.1.gitcab0f0b'
        author: jchaloup <jchaloup@redhat.com>
    '3':
        comment: "- Update to version 0.0.4\n  related: #1204614"
        date: Tue Jun 09 2015
        mark: '- 0.0.4-1'
        author: jchaloup <jchaloup@redhat.com>
    '2':
        comment: "- Update to version 0.0.3\n  related: #1204614"
        date: Sat May 09 2015
        mark: '- 0.0.3-1'
        author: jchaloup <jchaloup@redhat.com>
    '5':
        comment: '- Updated to version 0.0.5'
        date: Tue Jun 23 2015
        mark: '- 0.0.5-1'
        author: jchaloup <jchaloup@redhat.com>
    '4':
        comment: '- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild'
        date: Wed Jun 17 2015
        mark: '- 0.0.4-2'
        author: Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
    '7':
        comment: '- Updated to version 0.0.7'
        date: Sat Aug 01 2015
        mark: '- 0.0.7-1'
        author: jchaloup <jchaloup@redhat.com>
    '6':
        comment: '- Updated to version 0.0.6'
        date: Sat Jul 11 2015
        mark: '- 0.0.6-1'
        author: jchaloup <jchaloup@redhat.com>
    '9':
        comment: '- Add missing symlinks'
        date: Sat Aug 29 2015
        mark: '- 0.0.8-2'
        author: jchaloup <jchaloup@redhat.com>
    '8':
        comment: '- Updated to version 0.0.8'
        date: Fri Aug 21 2015
        mark: '- 0.0.8-1'
        author: jchaloup <jchaloup@redhat.com>
unit_list:
  -   - Summary: Set of basic commands definitions
      - BuildArch: noarch
      - name: cmd-dnfs-base
      - description: Basic gofed commands definition
      - files:
            list:
              - /usr/share/%{name}/cmd/README.md
              - /usr/share/%{name}/cmd/repo2spec/*.yml
              - /usr/share/%{name}/cmd/fetch/*.yml
              - /usr/share/%{name}/cmd/create-tracker/*.yml
              - /usr/share/%{name}/cmd/ggi/*.yml
              - /usr/share/%{name}/cmd/inspect/*.yml
              - /usr/share/%{name}/cmd/check-deps/*.yml
              - /usr/share/%{name}/cmd/lint/*.yml
              - /usr/share/%{name}/cmd/review-request/*.yml
              - /usr/share/%{name}/cmd/clean-resources/*.yml
              - /usr/share/%{name}/cmd/base.yml
  -   - Summary: Set of build commands definitions
      - BuildArch: noarch
      - name: cmd-dnfs-build
      - description: Build gofed commands definition
      - files:
            list:
              - /usr/share/%{name}/cmd/tools/*.yml
              - /usr/share/%{name}/cmd/bump-spec/*.yml
              - /usr/share/%{name}/cmd/wizard/*.yml
              - /usr/share/%{name}/cmd/build.yml
  -   - Summary: Set of scan commands definitions
      - BuildArch: noarch
      - name: cmd-dnfs-scan
      - description: Scan gofed commands definition
      - files:
            list:
              - /usr/share/%{name}/cmd/goapidiff/*.yml
              - /usr/share/%{name}/cmd/approx-deps/*.yml
              - /usr/share/%{name}/cmd/scan-deps/*.yml
              - /usr/share/%{name}/cmd/scan-distro/*.yml
              - /usr/share/%{name}/cmd/scan-packages/*.yml
              - /usr/share/%{name}/cmd/unit-test/*.yml
              - /usr/share/%{name}/cmd/scan.yml
  -   - Summary: Implementation of base commands for gofed
      - BuildArch: noarch
      - name: base
      - description: Basic commands
      - files:
            list:
              - /usr/share/%{name}/cmd/version/version.py
              - /usr/share/%{name}/cmd/repo2spec/*.py
              - /usr/share/%{name}/cmd/repo2spec/bitbucket2gospec
              - /usr/share/%{name}/cmd/repo2spec/github2gospec
              - /usr/share/%{name}/cmd/repo2spec/googlecode2gospec
              - /usr/share/%{name}/cmd/fetch/*.py
              - /usr/share/%{name}/cmd/create-tracker/*.py
              - /usr/share/%{name}/cmd/ggi/*.py
              - /usr/share/%{name}/cmd/inspect/*.py
              - /usr/share/%{name}/cmd/check-deps/*.py
              - /usr/share/%{name}/cmd/lint/*.py
              - /usr/share/%{name}/cmd/review-request/*.py
              - /usr/share/%{name}/cmd/clean-resources/*.py
              - '#%{_sysconfdir}/bash_completion.d/gofed-base_bash_completion'
              - /usr/share/man/man1/gofed.1.gz
  -   - Summary: Set of commands for scanning golang projects
      - BuildArch: noarch
      - Conflicts: gofed-scan < 1.0.0
      - name: scan
      - description: "Subpackage providing commands for scanning of golang project,\
            \ i.e.\ncomparison of APIs of two golang projects,\ngenerator of xml files\
            \ representing exported symbols and\nscan of golang packages and generator\
            \ of dependency graph."
      - runtime:
            dependencies:
              - name: '%{name} = %{version}-%{release}'
              - name: '%{name}-cmd-dnfs-scan = %{version}-%{release}'
              - name: python-cmdsignature = %{version}-%{release}
              - name: graphviz
      - files:
            list:
              - /usr/share/%{name}/cmd/tools/*.py
              - /usr/share/%{name}/cmd/tools/bbobranches
              - /usr/share/%{name}/cmd/tools/build
              - /usr/share/%{name}/cmd/tools/gcp
              - /usr/share/%{name}/cmd/tools/pull
              - /usr/share/%{name}/cmd/tools/push
              - /usr/share/%{name}/cmd/tools/scratch-build
              - /usr/share/%{name}/cmd/tools/update
              - /usr/share/%{name}/cmd/bump-spec/*.py
              - /usr/share/%{name}/cmd/wizard/*.py
              - '#%{_sysconfdir}/bash_completion.d/gofed-build_bash_completion'
  -   - Summary: Set of commands for building golang projects
      - BuildArch: noarch
      - Conflicts: gofed-build < 1.0.0
      - name: build
      - description: "Subpackage providing commands for scratch builds, builds,\n\
            pulls, pushes, updates, overrides and other commands\nthat can be used\
            \ for package maitainance.\n\nThe commands support running one command\
            \ on multiple branches at once."
      - runtime:
            dependencies:
              - name: '%{name} = %{version}-%{release}'
              - name: '%{name}-cmd-dnfs-build = %{version}-%{release}'
              - name: python-cmdsignature = %{version}-%{release}
      - files:
            list:
              - /usr/share/%{name}/cmd/goapidiff/*.py
              - /usr/share/%{name}/cmd/approx-deps/*.py
              - /usr/share/%{name}/cmd/scan-deps/*.py
              - /usr/share/%{name}/cmd/scan-distro/*.py
              - /usr/share/%{name}/cmd/scan-packages/*.py
              - /usr/share/%{name}/cmd/unit-test/*.py
              - '#%{_sysconfdir}/bash_completion.d/gofed-scan_bash_completion'
  -   - Summary: Gofedlib
      - name: gofedlib
      - description: Gofedlib
      - buildtime:
            dependencies:
              - name: python-fedora python-jinja2 python-markupsafe
      - runtime:
            dependencies:
              - name: python-fedora python-jinja2 python-markupsafe python-PyGithub
                    python2-hglib
      - files:
            list:
              - '%license LICENSE '
              - '%{python2_sitelib}/gofedlib'
              - '%{python2_sitelib}/gofedlib-?.?.???-py2.7.egg-info'
              - '%{_bindir}/gofedlib-cli'
  -   - Summary: Gofed resources
      - BuildArch: noarch
      - name: resources
      - description: Gofed resources
      - buildtime:
            dependencies:
              - name: python2-hglib
      - runtime:
            dependencies:
              - name: python2-hglib
              - name: '%{name}-gofedlib = %{version}-%{release}'
      - files:
            list:
              - '%license LICENSE '
              - '%{python2_sitelib}/gofedresources'
              - '%{python2_sitelib}/gofedresources-?.?.?-py2.7.egg-info'
  -   - Summary: Gofed infra
      - BuildArch: noarch
      - name: infra
      - description: Gofed infra
      - buildtime:
            dependencies:
              - name: python-jsonschema koji GitPython python-pycurl python2-hglib
                    python-gitdb
      - runtime:
            dependencies:
              - name: python-jsonschema koji GitPython python-pycurl python2-hglib
                    python-gitdb
              - name: '%{name}-gofedlib = %{version}-%{release}'
              - name: '%{name}-resources = %{version}-%{release}'
      - files:
            list:
              - '%license LICENSE '
              - '%{python2_sitelib}/gofedinfra'
              - '%{python2_sitelib}/gofedinfra-?.?.?-py2.7.egg-info'
  -   - Summary: Run gofed commands as a container
      - BuildArch: noarch
      - ExclusiveArch: '%{ix86} x86_64 %{arm} aarch64 ppc64le s390x %{mips}'
      - name: docker
      - description: Run gofed commands as a container
      - runtime:
            dependencies:
              - name: '%{name}-cmd-dnfs-base = %{version}-%{release}'
              - name: python-cmdsignature = %{version}-%{release}
              - name: docker
      - files:
            meta:
                file: python-cmdsignature
            list:
              - '%license LICENSE '
              - '%{python2_sitelib}/cmdsignature'
              - '%{python2_sitelib}/cmdsignature-?.?.?-py2.7.egg-info'
  -   - Summary: Command signature python module
      - BuildArch: noarch
      - name: python-cmdsignature
      - description: Command signature python module
      - buildtime:
            dependencies:
              - name: PyYAML
      - runtime:
            dependencies:
              - name: python >= 2.7.5
              - name: PyYAML
      - files:
            list:
              - '%{_bindir}/gofed-docker'

