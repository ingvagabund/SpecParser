%pre
getent group gofed >/dev/null || groupadd -r gofed
getent passwd gofed >/dev/null || useradd -r -g gofed -d / -s /sbin/nologin \
        -c "Gofed user" gofed

%if ! 0%{?gobuild:1}
%define gobuild(o:) go build -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n')" -a -v -x %{?**}; 
%endif

