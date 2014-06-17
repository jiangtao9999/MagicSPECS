Name:           perl-Test-YAML-Valid
Version:        0.04
Release:        22%{?dist}
Summary:        Lets you test the validity of YAML files in unit tests
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Test-YAML-Valid/
Source0:        http://www.cpan.org/authors/id/J/JR/JROCKWAY/Test-YAML-Valid-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(YAML) >= 0.60
BuildRequires:  perl(YAML::XS)
BuildRequires:  perl(YAML::Tiny)
BuildRequires:  perl(YAML::Syck)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(CPAN)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Builder::Tester)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(YAML)
Requires:       perl(YAML::Syck)

%description
Lets you test the validity of YAML files inside your
(Test::Builder-based) unit tests.

%prep
%setup -q -n Test-YAML-Valid-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
%dir %{perl_vendorlib}/Test/
%dir %{perl_vendorlib}/Test/YAML/
%{perl_vendorlib}/Test/YAML/Valid.pm
%{_mandir}/man3/*3pm*

%changelog
* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 0.04-22
- 为 Magic 3.0 重建

* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 0.04-21
- 为 Magic 3.0 重建

* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 0.04-20
- 为 Magic 3.0 重建

* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 0.04-19
- 为 Magic 3.0 重建

* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 0.04-18
- 为 Magic 3.0 重建

* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 0.04-17
- 为 Magic 3.0 重建

* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 0.04-16
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.04-15
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.04-14
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.04-13
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.04-12
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.04-11
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.04-10
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 20 2012 Petr Pisar <ppisar@redhat.com> - 0.04-8
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.04-6
- Perl mass rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.04-5
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.04-3
- 661697 rebuild for fixing problems with vendorach/lib

* Thu Jul 01 2010 Mark Chappell <tremble@fedoraproject.org> - 0.04-2
- Add in missing BR for extra tests

* Wed Jun 30 2010 Mark Chappell <tremble@fedoraproject.org> - 0.04-1
- New upstream version

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.03-8
- Mass rebuild with perl-5.12.0

* Tue Jan 12 2010 Daniel P. Berrange <berrange@redhat.com> - 0.03-7
- Fix source URL

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.03-6
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 14 2009 Daniel P. Berrange <berrange@redhat.com> - 0.03-4.fc11
- Add perl(YAML) and perl(YAML::Syck) requirements (rhbz #495401)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.03-2
- rebuild for new perl

* Fri Dec 21 2007 Daniel P. Berrange <berrange@redhat.com> 0.03-1.fc9
- Specfile autogenerated by cpanspec 1.73.
