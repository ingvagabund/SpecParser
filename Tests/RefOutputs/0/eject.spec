{"beginning": "", "block_list": [{"block_type": 0, "content": "eject", "key": "Name"}, {"block_type": 0, "content": "1.2.5", "key": "Version"}, {"block_type": 0, "content": "1%{?dist}", "key": "Release"}, {"block_type": 0, "content": "Short sumary", "key": "Summary"}, {"block_type": 0, "content": "GPLv2+", "key": "License"}, {"block_type": 0, "content": "http://www.pobox.com/~tranter", "key": "URL"}, {"block_type": 0, "content": "http://www.ibiblio.org/pub/Linux/utils/disk-management/%name}-%{version}%license}.tar.gz", "key": "Source0"}, {"block_type": 1, "content": "", "keyword": "description"}, {"block_type": 1, "content": "%autosetup", "keyword": "prep"}, {"block_type": 1, "content": "%configure\n%make_build", "keyword": "build"}, {"block_type": 0, "content": "requires description", "key": "BuildRequires"}, {"block_type": 0, "content": "reqs", "key": "Requires"}, {"block_type": 1, "content": "make check", "keyword": "check"}, {"block_type": 1, "content": "rm -rf $RPM_BUILD_ROOT\n%make_install", "keyword": "install"}, {"block_type": 1, "content": "%license add-license-file-here\n\n%doc README TODO", "keyword": "files"}, {"block_type": 1, "content": ["* Wed Mar 22 2017 Nikola Valesova\n-"], "keyword": "changelog"}], "end": "\n", "metastring": "#%0           %2\n#%0        %2\n#%0        %2\n#%0        %2\n\n#%0        %2\n#%0            %2\n#%0        %2\n\n\n#%0%4\n\n\n#%0\n%4\n\n\n#%0\n%4\n\n#%0  %2\n#%0       %2 \n\n\n#%0\n%4\n\n\n#%0\n%4\n\n\n#%0\n%4\n\n\n\n#%0\n%4 "}
