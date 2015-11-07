Name:           perl-Module-Depends
Version:	0.15
Release:	2%{?dist}
Summary:        Identify the dependencies of a distribution
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Module-Depends/
Source0:        http://search.cpan.org/CPAN/authors/id/R/RC/RCLAMP/Module-Depends-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Class::Accessor::Chained)
BuildRequires:  perl(File::chdir)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(YAML)
Requires:       perl(Class::Accessor::Chained)
Requires:       perl(File::chdir)
Requires:       perl(YAML)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Module::Depends extracts module dependencies from an unpacked
distribution tree.

%prep
%setup -q -n Module-Depends-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Nov 02 2015 Liu Di <liudidi@gmail.com> - 0.15-2
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.15-1
- 更新到 0.15

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.14-17
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.14-16
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.14-15
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.14-14
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.14-13
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.14-12
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.14-11
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.14-10
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 29 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.14-8
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.14-6
- 661697 rebuild for fixing problems with vendorach/lib

* Mon May 03 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.14-5
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.14-4
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jun  6 2008 Ian Burrell <ianburrell@gmail.com> - 0.14-1
- Update to 0.14

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.13-2
Rebuild for new perl

* Thu Aug 16 2007 Ian M. Burrell <ianburrell@gmail.com> - 0.13-1
- Update to 0.13
- Fix BuildRequires

* Thu May 24 2007 Ian M. Burrell <ianburrell@gmail.com> - 0.12-1
- Update to 0.12

* Mon Jan 29 2007 Ian Burrell <ianburrell@gmail.com> 0.10-2
- Specfile autogenerated by cpanspec 1.69.1.

* Thu Mar 30 2006 Ian Burrell <ianburrell@gmail.com> 0.10-1
- Specfile autogenerated by cpanspec 1.64.
