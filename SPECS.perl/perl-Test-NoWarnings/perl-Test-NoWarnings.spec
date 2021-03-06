Name:           perl-Test-NoWarnings
Version:        1.04
Release:        9%{?dist}
Summary:        Make sure you didn't emit any warnings while testing
License:        LGPLv2+
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Test-NoWarnings/
Source0:        http://www.cpan.org/authors/id/A/AD/ADAMK/Test-NoWarnings-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Carp)
BuildRequires:  perl(Devel::StackTrace)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Builder) >= 0.86
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Tester) >= 0.107
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
In general, your tests shouldn't produce warnings. This module causes any
warnings to be captured and stored. It automatically adds an extra test
that will run when your script ends to check that there were no warnings.
If there were any warnings, the test will give a "not ok" and diagnostics of
where, when and what the warning was, including a stack trace of what was
going on when the it occurred.

%prep
%setup -q -n Test-NoWarnings-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Nov 12 2015 Liu Di <liudidi@gmail.com> - 1.04-9
- 为 Magic 3.0 重建

* Tue Nov 03 2015 Liu Di <liudidi@gmail.com> - 1.04-8
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 1.04-7
- 为 Magic 3.0 重建

* Thu Jun 19 2014 Liu Di <liudidi@gmail.com> - 1.04-6
- 为 Magic 3.0 重建

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 1.04-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jan 05 2013 Iain Arnell <iarnell@gmail.com> 1.04-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Thu Nov 08 2012 Jitka Plesnikova <jplesnik@redhat.com> - 1.02-7
- Update dependencies

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.02-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1.02-5
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.02-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jun 19 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.02-3
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 08 2010 Steven Pritchard <steve@kspei.com> 1.02-1
- Update to 1.02.
- Update Source0 URL.
- BR Test::Builder and Test::More, plus update versioned Test::Tester BR.
- CHANGES renamed to Changes, and LGPL renamed to LICENSE.

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.084-7
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.084-6
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.084-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.084-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.084-3
- Rebuild for perl 5.10 (again)

* Mon Jan 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.084-2
- rebuild for new perl

* Sat Jan 12 2008 Steven Pritchard <steve@kspei.com> 0.084-1
- Update to 0.084.
- Update License.
- BR Devel::StackTrace.

* Wed Apr 18 2007 Steven Pritchard <steve@kspei.com> 0.083-2
- BR ExtUtils::MakeMaker.

* Tue Dec 26 2006 Steven Pritchard <steve@kspei.com> 0.083-1
- Update to 0.083.
- Use fixperms macro instead of our own chmod incantation.

* Sat Sep 16 2006 Steven Pritchard <steve@kspei.com> 0.082-2
- Fix find option order.

* Sat Apr 08 2006 Steven Pritchard <steve@kspei.com> 0.082-1
- Specfile autogenerated by cpanspec 1.64.
- Fix License.
- Drop explicit dependency on perl(Test::Tester).  (Seems to be bogus.)
