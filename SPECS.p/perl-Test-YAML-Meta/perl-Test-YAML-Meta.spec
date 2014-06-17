Name:           perl-Test-YAML-Meta
Version:        0.19
Release:        6%{?dist}
Summary:        Validation of the META.yml file in a distribution
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Test-YAML-Meta/
Source0:        http://www.cpan.org/modules/by-module/Test/Test-YAML-Meta-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 0.08
BuildRequires:  perl(Test::YAML::Valid) >= 0.03
BuildRequires:  perl(Test::CPAN::Meta::YAML)
BuildRequires:  perl(YAML)
BuildRequires:  perl(YAML::Syck)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module was written to ensure that a META.yml file, provided with a
standard distribution uploaded to CPAN, meets the specifications that
slowly being introduced to module uploads, via the use of
ExtUtils::MakeMaker, Module::Build and Module::Install.

%prep
%setup -q -n Test-YAML-Meta-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
mv LICENSE LICENSE.in
iconv -fiso88591 -tutf8 -oLICENSE LICENSE.in
rm LICENSE.in

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
%doc Changes LICENSE README examples
%dir %{perl_vendorlib}/Test/
%dir %{perl_vendorlib}/Test/YAML/
%{perl_vendorlib}/Test/YAML/Meta.pm
%{_mandir}/man3/*.3pm*

%changelog
* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.19-6
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.19-5
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 21 2012 Petr Pisar <ppisar@redhat.com> - 0.19-3
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 11 2011 Daniel P. Berrange <berrange@redhat.com> - 0.19-1
- Update to 0.19 release

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.16-4
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.16-2
- 661697 rebuild for fixing problems with vendorach/lib

* Wed Jun 30 2010 Mark Chappell <tremble@fedoraproject.org> - 0.16-1
- Update for new upstream version

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.15-2
- Mass rebuild with perl-5.12.0

* Thu Jan  7 2010 Daniel P. Berrange <berrange@redhat.com> - 0.15-1
- Update to 0.15 release

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.12-3
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Daniel P. Berrange <berrange@redhat.com> - 0.12-1
- Update to 0.12 release

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Sep  5 2008 Daniel Berrange <berrange@redhat.com> - 0.11-1
- Update to 0.11 release

* Fri Feb  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.06-4
- rebuild for new perl

* Mon Dec 24 2007 Daniel P. Berrange <berrange@redhat.com> - 0.06-3.fc9
- Convert LICENSE from iso8859-1 to utf-8
- Add examples to doc

* Sun Dec 23 2007 Daniel P. Berrange <berrange@redhat.com> 0.06-2.fc9
- Added YAML and YAML::Syck as build requirements

* Fri Dec 21 2007 Daniel P. Berrange <berrange@redhat.com> 0.06-1.fc9
- Specfile autogenerated by cpanspec 1.73.
