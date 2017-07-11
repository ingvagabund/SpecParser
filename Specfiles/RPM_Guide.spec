Summary: java source to bytecode compiler

%define version 1.17

License: IBM Public License, http://ibm.com/developerworks/oss/license10.html
Group: Development/Languages
Name: jikes
Provides: jikes
Release: 1
Source: jikes-%{version}.tar.gz
URL: http://ibm.com/developerworks/opensource/jikes
Version: %{version}
Buildroot: /tmp/jikesrpm

%description
The IBM Jikes compiler translates Java source files to bytecode. It
also supports incremental compilation and automatic makefile generation,
and is maintained by the Jikes Project:
http://ibm.com/developerworks/opensource/jikes

%clean
rm -rf $RPM_BUILD_ROOT

