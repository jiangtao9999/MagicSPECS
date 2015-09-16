Name:           perl-Version-Requirements
Version:	0.101023
Release:	1%{?dist}
Summary:        Set of version requirements for a CPAN dist (DEPRECATED)
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Version-Requirements/
Source0:        http://www.cpan.org/authors/id/R/RJ/RJBS/Version-Requirements-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.30
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Scalar::Util)
# tests
BuildRequires:  perl(Test::More) >= 0.88
%if !%{defined perl_bootstrap}
BuildRequires:  perl(Test::Pod) >= 1.41
%endif
BuildRequires:  perl(version) >= 0.77
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
Version:	0.101023

Use CPAN::Meta::Requirements, which is a drop-in replacement.

A Version:	0.101023
those specified in the META.yml or META.json files in CPAN distributions.
It can be built up by adding more and more constraints, and it will reduce
them to the simplest representation.

%prep
%setup -q -n Version-Requirements-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
RELEASE_TESTING=1 make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.101023-1
- 更新到 0.101023

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.101022-248
- 为 Magic 3.0 重建

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.101022-247
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 14 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.101022-246
- Perl 5.18 re-rebuild of bootstrapped packages

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.101022-245
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.101022-244
- Perl 5.18 rebuild

* Tue Apr 30 2013 Petr Pisar <ppisar@redhat.com> - 0.101022-243
- Increase release number to supersede perl sub-package (bug #957931)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.101022-242
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 23 2012 Jitka Plesnikova <jplesnik@redhat.com> - 0.101022-241
- Update description
- Clean up %%doc

* Fri Aug 17 2012 Petr Pisar <ppisar@redhat.com> - 0.101022-240
- Increase release to replace perl sub-package (bug #848961)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.101022-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Petr Pisar <ppisar@redhat.com> - 0.101022-4
- Perl 5.16 re-rebuild of bootstrapped packages

* Wed Jun 06 2012 Petr Pisar <ppisar@redhat.com> - 0.101022-3
- Perl 5.16 rebuild

* Fri Jun 01 2012 Petr Pisar <ppisar@redhat.com> - 0.101022-2
- Update dependencies

* Sat Feb 04 2012 Iain Arnell <iarnell@gmail.com> 0.101022-1
- update to latest upstream version (still DEPRECATED)

* Fri Feb 03 2012 Iain Arnell <iarnell@gmail.com> 0.101021-1
- update to latest upstream
- Version:	0.101023
  use CPAN::Meta::Requirements, which is a drop-in replacement

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.101020-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.101020-5
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.101020-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 23 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.101020-3
- 661697 rebuild for fixing problems with vendorach/lib

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.101020-2
- Mass rebuild with perl-5.12.0

* Wed Apr 14 2010 Iain Arnell <iarnell@gmail.com> 0.101020-1
- update to latest upstream version

* Fri Apr 02 2010 Iain Arnell <iarnell@gmail.com> 0.100660-1
- Specfile autogenerated by cpanspec 1.78.
- use perl_default_filter and DESTDIR
