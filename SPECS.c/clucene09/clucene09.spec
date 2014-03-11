Summary:	A C++ port of Lucene
Name:		clucene09
Version:	0.9.21b
Release:	5%{?dist}
License:	LGPLv2+ or ASL 2.0
Group:		System Environment/Libraries
URL:		http://www.sourceforge.net/projects/clucene/
Source0:	http://downloads.sourceforge.net/clucene/clucene-core-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
CLucene is a C++ port of Lucene. It is a high-performance, full-
featured text search engine written in C++. CLucene is faster than
lucene as it is written in C++.

This package contains an old and deprecated version of clucene. You
need it only if the software you are using has not been updated to
work with the newer version and the newer API.

%package core
Summary:	Core clucene module
Group:		System Environment/Libraries
Provides:	%{name} = %{version}-%{release}
Provides:	%{name}%{?_isa} = %{version}-%{release}

%description core
The core clucene module.

This package contains an old and deprecated version of clucene-core.
You need it only if the software you are using has not been updated
to work with the newer version and the newer API.

%package core-devel
Summary:	Development files for clucene-core
Group:		Development/Libraries
Requires:	%{name}-core%{?_isa} = %{version}-%{release}

%description core-devel
The clucene-core-devel package includes header files and libraries
necessary for developing programs which use clucene-core library. 

This package contains an old and deprecated version of clucene-core.
You need it only if the software you are using has not been updated
to work with the newer version and the newer API.

%prep
%setup -q -n clucene-core-%{version}

%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p' install

# Perform the necessary renaming according to package renaming
mkdir -p $RPM_BUILD_ROOT{%{_includedir},%{_libdir}}/%{name}/
mv -f $RPM_BUILD_ROOT%{_includedir}/{CLucene,CLucene.h,%{name}}
mv -f $RPM_BUILD_ROOT%{_libdir}/{CLucene,%{name}}
rm -f $RPM_BUILD_ROOT%{_libdir}/libclucene.so
ln -sf ../libclucene.so.0.0.0 $RPM_BUILD_ROOT%{_libdir}/%{name}/libclucene.so

# Don't install any libtool .la files
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.la

# Fix incorrect end-of-line encoding
sed -e 's/\r//' LGPL.license > LGPL.license.eol
touch -c -r LGPL.license LGPL.license.eol
mv -f LGPL.license.eol LGPL.license

# Convert everything to UTF-8
iconv -f iso-8859-1 -t utf-8 -o README.utf8 README
touch -c -r README README.utf8
mv -f README.utf8 README

%ifnarch ppc64 s390x sparc64
%check
make check
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post core -p /sbin/ldconfig

%postun core -p /sbin/ldconfig

%files core
%defattr(-,root,root,-)
%doc AUTHORS COPYING HACKING README REQUESTS APACHE.license LGPL.license
%doc doc/*.htm doc/*.jpg
%{_libdir}/libclucene.so.*

%files core-devel
%defattr(-,root,root,-)
# clucene-config.h is arch/platform specific, see RHBZ #381481
%{_libdir}/%{name}/
%{_includedir}/%{name}/

%changelog
* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.21b-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.21b-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.21b-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 05 2011 Robert Scheck <robert@fedoraproject.org> 0.9.21b-2
- Corrected line endings and charset in %%doc files (#750013 #c5)
- Clarified need of clucene-config.h in %%{_libdir} (#750013 #c5)

* Sun Oct 30 2011 Robert Scheck <robert@fedoraproject.org> 0.9.21b-1
- Renamed clucene-0.9.21b-3 into clucene09-0.9.21b-1 (#750013)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.21b-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 08 2010 Deji Akingunola <dakingun@gmail.com> 0.9.21b-2
- Include the license text in the -core subpackage.

* Sun Jun 06 2010 Robert Scheck <robert@fedoraproject.org> 0.9.21b-1
- Update to 0.9.21b

* Wed Nov 04 2009 Dennis Gilmore <dennis@ausil.us> - 0.9.21-5
- disable 'make check on sparc64 along with ppc64 and s390x

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 14 2009 Karsten Hopp <karsten@redhat.com> 0.9.21-3
- bypass 'make check' on s390x, similar to ppc64

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Aug 27 2008 Deji Akingunola <dakingun@gmail.com> - 0.9.21-1
- Update to version 0.9.21

* Sun Feb 10 2008 Deji Akingunola <dakingun@gmail.com> - 0.9.20-4
- Rebuild for gcc43

* Wed Oct 25 2007 Deji Akingunola <dakingun@gmail.com> - 0.9.20-3
- Fix a typo in the License field

* Wed Oct 25 2007 Deji Akingunola <dakingun@gmail.com> - 0.9.20-2
- Fix multiarch conflicts (BZ #340891)
- Bypass 'make check' for ppc64, its failing two tests there

* Tue Aug 21 2007 Deji Akingunola <dakingun@gmail.com> - 0.9.20-1
- Update to version 0.9.20

* Sat Aug 11 2007 Deji Akingunola <dakingun@gmail.com> - 0.9.19-1
- Latest release update

* Fri Aug 03 2007 Deji Akingunola <dakingun@gmail.com> - 0.9.16a-2
- License tag update

* Thu Feb 22 2007 Deji Akingunola <dakingun@gmail.com> - 0.9.16a-2
- Add -contrib subpackage 

* Thu Dec 07 2006 Deji Akingunola <dakingun@gmail.com> - 0.9.16a-1
- Update to latest stable release 
- Run make check during build

* Mon Nov 20 2006 Deji Akingunola <dakingun@gmail.com> - 0.9.15-3
- Don't package APACHE.license since we've LGPL instead 
- Package documentation in devel subpackage

* Mon Nov 13 2006 Deji Akingunola <dakingun@gmail.com> - 0.9.15-2
- Fix a bunch of issues with the spec (#215258)
- Moved the header file away from lib dir

* Sat Nov 04 2006 Deji Akingunola <dakingun@gmail.com> - 0.9.15-1
- Initial packaging for Fedora Extras
