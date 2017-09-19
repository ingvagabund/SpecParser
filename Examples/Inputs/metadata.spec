%define _topdir     /home/strike/mywget
%define name        wget 
%define release     1
%define version     1.12
%define buildroot   %{_topdir}/%{name}-%{version}-root

BuildRoot:      %{buildroot}
Summary:        GNU wget
License:        GPL
Name:           %{name}
Version:        %{version}
Release:        %{release}
Source:         %{name}-%{version}.tar.gz
Group:          Development/Tools
