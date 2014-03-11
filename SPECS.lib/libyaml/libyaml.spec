%define tarballname yaml

#====================================================================#

Name:       libyaml
Version:    0.1.4
Release:    3%{?dist}
Summary:    YAML 1.1 parser and emitter written in C

Group:      System Environment/Libraries
License:    MIT
URL:        http://pyyaml.org/
Source0:    http://pyyaml.org/download/libyaml/%{tarballname}-%{version}.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


%description
YAML is a data serialization format designed for human readability and
interaction with scripting languages.  LibYAML is a YAML parser and
emitter written in C.


%package devel
Summary:   Development files for LibYAML applications
Group:     Development/Libraries
Requires:  libyaml = %{version}-%{release}, pkgconfig


%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use LibYAML.


%prep
%setup -q -n %{tarballname}-%{version}


%build
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} INSTALL="install -p" install
rm -f %{buildroot}%{_libdir}/*.{la,a}


%check
make check


%clean
rm -rf %{buildroot}


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc LICENSE README
%{_libdir}/%{name}*.so.*


%files devel
%defattr(-,root,root,-)
%doc doc/html
%{_libdir}/%{name}*.so
%{_libdir}/pkgconfig/yaml-0.1.pc
%{_includedir}/yaml.h


%changelog
* Fri Dec 07 2012 Liu Di <liudidi@gmail.com> - 0.1.4-3
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jun 23 2011 John Eckersberg <jeckersb@redhat.com> - 0.1.4-1
- New upstream release 0.1.4

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Oct 02 2009 John Eckersberg <jeckersb@redhat.com> - 0.1.3-1
- New upstream release 0.1.3

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 John Eckersberg <jeckersb@redhat.com> - 0.1.2-4
- Minor tweaks to spec file
- Enable %%check section
- Thanks Gareth Armstrong <gareth.armstrong@hp.com>

* Tue Mar 3 2009 John Eckersberg <jeckersb@redhat.com> - 0.1.2-3
- Remove static libraries

* Thu Feb 26 2009 John Eckersberg <jeckersb@redhat.com> - 0.1.2-2
- Remove README and LICENSE from docs on -devel package
- Remove -static package and merge contents into the -devel package

* Wed Feb 25 2009 John Eckersberg <jeckersb@redhat.com> - 0.1.2-1
- Initial packaging for Fedora
