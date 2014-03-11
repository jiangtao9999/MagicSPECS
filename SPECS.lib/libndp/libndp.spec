Name: libndp
Version: 1.2
Release: 1%{?dist}
Summary: Library for Neighbor Discovery Protocol
Group: System Environment/Libraries
License: LGPLv2+
URL: http://www.libndp.org/
Source: http://www.libndp.org/files/libndp-%{version}.tar.gz

%description
This package contains a library which provides a wrapper
for IPv6 Neighbor Discovery Protocol.  It also provides a tool
named ndptool for sending and receiving NDP messages.

%package devel
Group: Development/Libraries
Summary: Libraries and header files for libndp development
Requires: libndp = %{version}-%{release}

%description devel
The libndp-devel package contains the header files and libraries
necessary for developing programs using libndp.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name \*.la -delete

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc COPYING
%{_libdir}/*so.*
%{_bindir}/ndptool
%{_mandir}/man8/ndptool.8*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Tue Oct 15 2013 Jiri Pirko <jpirko@redhat.com> - 1.2-1
- Update to 1.2
- libndp: silently ignore packets with optlen 0
- libndp: fix processing for larger options
- libndp: do not fail on receiving non-ndp packets

* Fri Oct 04 2013 Jiri Pirko <jpirko@redhat.com> - 1.1-1
- Update to 1.1

* Fri Sep 13 2013 Dan Williams <dcbw@redhat.com> - 1.0-2
- Fix .pc file includes path
- Fix ndptool -v argument

* Thu Aug 08 2013 Jiri Pirko <jpirko@redhat.com> - 1.0-1
- Update to 1.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-4.20130723git873037a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Dan Williams <dcbw@redhat.com> - 0.1-3.20130723git873037a
- Update to git 873037a

* Fri Jun 07 2013 Jiri Pirko <jpirko@redhat.com> - 0.1-2.20130607git39e1f53
- Update to git 39e1f53

* Sat May 04 2013 Jiri Pirko <jpirko@redhat.com> - 0.1-1.20130504gitca3c399
- Initial build.
