Name:           perl-Data-Taxi
Version:        0.96
Release:        8%{?dist}
Summary:        Taint-aware, XML-ish data serialization
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Data-Taxi/
Source0:        http://www.cpan.org/authors/id/M/MI/MIKO/Data-Taxi-%{version}.tar.gz
Patch0:         no-debug-showstuff.patch
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
Taxi (Taint-Aware XML-Ish) is a data serializer with several handy
features.

%prep
%setup -q -n Data-Taxi-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check


%files
%defattr(-,root,root,-)
%doc README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.96-8
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.96-7
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 0.96-6
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.96-5
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.96-4
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 16 2011 Iain Arnell <iarnell@gmail.com> 0.96-1
- update to latest upstream version
- clean up spec for modern rpmbuild
- remove the need for Debug::ShowStuff

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.95-2
- 661697 rebuild for fixing problems with vendorach/lib

* Wed Jun 23 2010 Iain Arnell <iarnell@gmail.com> 0.95-1
- Specfile autogenerated by cpanspec 1.78.
