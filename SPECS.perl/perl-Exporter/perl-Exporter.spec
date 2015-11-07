Name:           perl-Exporter
Version:	5.72
Release:	2%{?dist}
Summary:        Implements default import method for modules
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Exporter/
Source0:        http://www.cpan.org/authors/id/T/TO/TODDR/Exporter-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(Carp) >= 1.05
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)
%if !%{defined perl_bootstrap}
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.18
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Carp) >= 1.05
Requires:       perl(warnings)

%description
The Exporter module implements an import method which allows a module to
export functions and variables to its users' name spaces. Many modules use
Exporter rather than implementing their own import method because Exporter
provides a highly flexible interface, with an implementation optimized for
the common case.

%prep
%setup -q -n Exporter-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Nov 02 2015 Liu Di <liudidi@gmail.com> - 5.72-2
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 5.72-1
- 更新到 5.72

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 5.70-4
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 5.70-3
- 为 Magic 3.0 重建

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.70-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 14 2014 Petr Pisar <ppisar@redhat.com> - 5.70-1
- 5.70 bump

* Wed Aug 14 2013 Jitka Plesnikova <jplesnik@redhat.com> - 5.68-293
- Perl 5.18 re-rebuild of bootstrapped packages

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.68-292
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 26 2013 Petr Pisar <ppisar@redhat.com> - 5.68-291
- Specify all dependencies

* Mon Jul 15 2013 Petr Pisar <ppisar@redhat.com> - 5.68-290
- Increase release to favour standalone package

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 5.68-2
- Link minimal build-root packages against libperl.so explicitly

* Thu Mar 28 2013 Petr Pisar <ppisar@redhat.com> - 5.68-1
- 5.68 bump

* Fri Mar 22 2013 Petr Pisar <ppisar@redhat.com> 5.67-1
- Specfile autogenerated by cpanspec 1.78.
