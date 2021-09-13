################################################################################

%global crc_check pushd ../SOURCES ; sha512sum -c %{SOURCE100} ; popd

################################################################################

%define _posixroot        /
%define _root             /root
%define _bin              /bin
%define _sbin             /sbin
%define _srv              /srv
%define _home             /home
%define _lib32            %{_posixroot}lib
%define _lib64            %{_posixroot}lib64
%define _libdir32         %{_prefix}%{_lib32}
%define _libdir64         %{_prefix}%{_lib64}
%define _logdir           %{_localstatedir}/log
%define _rundir           %{_localstatedir}/run
%define _lockdir          %{_localstatedir}/lock/subsys
%define _cachedir         %{_localstatedir}/cache
%define _spooldir         %{_localstatedir}/spool
%define _crondir          %{_sysconfdir}/cron.d
%define _loc_prefix       %{_prefix}/local
%define _loc_exec_prefix  %{_loc_prefix}
%define _loc_bindir       %{_loc_exec_prefix}/bin
%define _loc_libdir       %{_loc_exec_prefix}/%{_lib}
%define _loc_libdir32     %{_loc_exec_prefix}/%{_lib32}
%define _loc_libdir64     %{_loc_exec_prefix}/%{_lib64}
%define _loc_libexecdir   %{_loc_exec_prefix}/libexec
%define _loc_sbindir      %{_loc_exec_prefix}/sbin
%define _loc_bindir       %{_loc_exec_prefix}/bin
%define _loc_datarootdir  %{_loc_prefix}/share
%define _loc_includedir   %{_loc_prefix}/include
%define _loc_mandir       %{_loc_datarootdir}/man
%define _rpmstatedir      %{_sharedstatedir}/rpm-state
%define _pkgconfigdir     %{_libdir}/pkgconfig

################################################################################

Summary:           Yum plugin to simplify working with only one repository
Name:              yum-plugin-fromrepo
Version:           0.0.2
Release:           1%{?dist}
License:           Apache License, Version 2.0
Group:             System Environment/Base
URL:               https://kaos.sh/yum-plugin-fromrepo

Source0:           https://source.kaos.st/%{name}/%{name}-%{version}.tar.bz2
Source100:         checksum.sha512

BuildRoot:         %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:         noarch

Requires:          yum

################################################################################

%description
Plugin add option '--repo' which allows to specify one repository for action.

################################################################################

%prep
%{crc_check}

%setup -qn %{name}-%{version}

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_sysconfdir}/yum/pluginconf.d/ \
         %{buildroot}%{_libdir32}/yum-plugins/

install -pm 0644 fromrepo.conf \
    %{buildroot}%{_sysconfdir}/yum/pluginconf.d/

install -pm 0644 fromrepo.py \
    %{buildroot}%{_libdir32}/yum-plugins/

%clean
rm -rf %{buildroot}

################################################################################

%files
%defattr(-,root,root,-)
%doc LICENSE SECURITY.md
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/fromrepo.conf
%{_libdir32}/yum-plugins/fromrepo.py*

################################################################################

%changelog
* Mon Sep 13 2021 Anton Novojilov <andy@essentialkaos.com> - 0.0.2-1
- Spec improved
- License changed to Apache v2

* Sun Nov 05 2017 Anton Novojilov <andy@essentialkaos.com> - 0.0.2-0
- Fixed using '--repo' option with clean command
- Checking existence of given repository

* Sun Oct 22 2017 Anton Novojilov <andy@essentialkaos.com> - 0.0.1-0
- Initial release
