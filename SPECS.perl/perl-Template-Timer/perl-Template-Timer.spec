Name:           perl-Template-Timer
Version:	1.01_02
Release:	1%{?dist}
Summary:        Template::Timer Perl module
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Template-Timer/
Source0:        http://www.cpan.org/authors/id/P/PE/PETDANCE/Template-Timer-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Template)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)

# not automagically picked up: use base
Requires:       perl(Template::Context)

%description
Template::Timer provides inline timings of the template processing
througout your code.  It's an overridden version of Template::Context that
wraps the process() and include() methods.

%prep
%setup -q -n Template-Timer-%{version}

perl -pi -e 's|^#!perl|#!/usr/bin/perl|' t/*.t

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} +
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
make test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 1.01_02-1
- 更新到 1.01_02

* Thu Jun 19 2014 Liu Di <liudidi@gmail.com> - 1.00-14
- 为 Magic 3.0 重建

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 29 2013 Petr Pisar <ppisar@redhat.com> - 1.00-11
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 21 2012 Petr Pisar <ppisar@redhat.com> - 1.00-8
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 1.00-6
- Perl mass rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.00-5
- 661697 rebuild for fixing problems with vendorach/lib

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.00-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.00-3
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Apr 10 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.00-1
- update to 1.00

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Mar 18 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.04-2
- bump

* Mon Mar 17 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.04-1
- Specfile autogenerated by cpanspec 1.74.
