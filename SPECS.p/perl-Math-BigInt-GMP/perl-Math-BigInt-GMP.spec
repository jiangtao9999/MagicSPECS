Name:           perl-Math-BigInt-GMP
Version:        1.36
Release:        5%{?dist}.1
Summary:        Math::BigInt::GMP Perl module
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Math-BigInt-GMP/
Source0:        http://search.cpan.org/CPAN/authors/id/P/PJ/PJACKLAM/Math-BigInt-GMP-%{version}.tar.gz
BuildRequires:  gmp-devel
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Math::BigInt) >= 1.993
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
#BuildRequires:  perl(threads)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
This package contains a replacement (drop-in) module for Math::BigInt's
core, Math::BigInt::Calc.pm. It needs the new versions of Math::BigInt and
Math::BigFloat as they are from Perl 5.7.x onwards.

%prep
%setup -q -n Math-BigInt-GMP-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
# perl-Math-BigInt 1.87 (delivered with perl-5.10.x) is needed
%if 0%{?rhel} > 5 || 0%{?fedora} > 8

%endif

%files
%doc BUGS CHANGES CREDITS LICENSE README TODO
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Math*
%{_mandir}/man3/*

%changelog
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 1.36-5.1
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 1.36-4.1
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.36-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 12 2011 Peter Schiffer <pschiffe@redhat.com> - 1.36-2.1
- rebuild with new gmp

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.36-2
- Perl mass rebuild

* Sat Jun 18 2011 Iain Arnell <iarnell@gmail.com> 1.36-1
- update to latest upstream version to fix perl-5.14 FTBFS
- clean up spec for modern rpmbuild
- use perl_default_filter

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Steven Pritchard <steve@kspei.com> 1.32-1
- Update to 1.32.
- Update Source0 URL.
- BR threads.

* Mon Dec 20 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.24-7
- 661697 rebuild for fixing problems with vendorach/lib

* Mon May 03 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.24-6
- Mass rebuild with perl-5.12.0

* Tue Dec 15 2009 Stepan Kasal <skasal@redhat.com> - 1.24-5
- skip check in distributions with perl-5.8

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.24-4
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun May 18 2008 Steven Pritchard <steve@kspei.com> 1.24-1
- Specfile autogenerated by cpanspec 1.75.
- BR Test::More, Test::Pod, Test::Pod::Coverage, and gmp-devel.
