%define _root_libdir    %{_libdir}

Summary: NFSv4 User and Group ID Mapping Library
Name: libnfsidmap
Version: 0.25
Release: 2%{?dist}
Provides: nfs-utils-lib
Obsoletes: nfs-utils-lib
URL: http://www.citi.umich.edu/projects/nfsv4/linux/
License: BSD

%define _docdir %{_defaultdocdir}/%{name}-%{version}

Source0: http://www.citi.umich.edu/projects/nfsv4/linux/libnfsidmap/%{name}-%{version}.tar.gz

Group: System Environment/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: pkgconfig, openldap-devel
BuildRequires: automake, libtool
Requires(postun): /sbin/ldconfig
Requires(pre): /sbin/ldconfig
Requires: openldap

%description
Library that handles mapping between names and ids for NFSv4.

%package devel
Summary: Development files for the libnfsidmap library
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
This package includes header files and libraries necessary for
developing programs which use the libnfsidmap library.

%prep
%setup -q 

%build
./autogen.sh
%configure --disable-static  --with-pluginpath=%{_root_libdir}/%name
make %{?_smp_mflags} all

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} \
    libdir=%{_root_libdir} pkgconfigdir=%{_libdir}/pkgconfig

mkdir -p %{buildroot}/%{_docdir}
mkdir -p %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}%{_mandir}/man5

install -m 644 idmapd.conf %{buildroot}%{_sysconfdir}/idmapd.conf

# Delete unneeded libtool libs
rm -rf %{buildroot}%{_root_libdir}/*.{a,la}
rm -rf %{buildroot}%{_root_libdir}/%{name}/*.{a,la}

magic_rpm_clean.sh

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%dir  %{_docdir}

%config(noreplace) %{_sysconfdir}/idmapd.conf
%{_root_libdir}/*.so.*
%{_root_libdir}/%{name}/*.so
%{_mandir}/*/*
%doc AUTHORS ChangeLog NEWS README COPYING

%files devel
%defattr(0644,root,root,755)
%{_libdir}/pkgconfig/libnfsidmap.pc
%{_includedir}/nfsidmap.h
%{_root_libdir}/*.so

%changelog
* Fri Dec 07 2012 Liu Di <liudidi@gmail.com> - 0.25-2
- 为 Magic 3.0 重建

* Wed Apr 18 2012 Liu Di <liudidi@gmail.com> - 0.25-1
- 为 Magic 3.0 重建

* Tue Dec  6 2011 Steve Dickson <steved@redhat.com>  0.20-0
- Updated to latest release: libnfsidmap-0.25

* Mon Nov 14 2011 Steve Dickson <steved@redhat.com>  0.24-7
- Updated to latest rc release: libnfsidmap-0-25-rc3 (bz 753930)

* Mon Mar  7 2011 Steve Dickson <steved@redhat.com>  0.24-6
- Updated to latest rc release: libnfsidmap-0-25-rc2

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 14 2011 Steve Dickson <steved@redhat.com>  0.24-4
- Updated to latest rc release: libnfsidmap-0-25-rc1

* Wed Dec 22 2010 Steve Dickson <steved@redhat.com>  0.24-3
- Used the newly added --with-pluginpath config flag to 
  redefine where the plugins live (bz 664641).

* Fri Dec 10 2010 Steve Dickson <steved@redhat.com>  0.24-2
- Removed the versions from the Provides: and Obsoletes: lines

* Wed Dec  8 2010 Steve Dickson <steved@redhat.com>  0.24-1
- Updated to latest upstream release: 0.24
- Obsoleted nfs-utils-lib

* Mon Dec  6 2006 Steve Dickson <steved@redhat.com>  0.23-3
- Maded corrections in spec per review comments.

* Fri Dec  3 2006 Steve Dickson <steved@redhat.com>  0.23-2
- Initial commit
