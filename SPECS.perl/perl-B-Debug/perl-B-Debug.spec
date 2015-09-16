Name:           perl-B-Debug
Version:        1.23
Release:        348%{?dist}
Summary:        Walk Perl syntax tree, print debug information about op-codes
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/B-Debug/
Source0:        http://www.cpan.org/authors/id/R/RU/RURBAN/B-Debug-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(B)
# B::Asmdata not used
BuildRequires:  perl(Config)
BuildRequires:  perl(strict)
# Optional run-time:
# B::Flags 0.04 not packaged
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
# Optional test:
%if !%{defined perl_bootstrap}
BuildRequires:  perl(Test::Pod) >= 1.00
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
Walk Perl syntax tree and print debug information about op-codes. See
B::Concise and B::Terse for other details.

%prep
%setup -q -n B-Debug-%{version}

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
%license Artistic Copying
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Sep 14 2015 Liu Di <liudidi@gmail.com> - 1.23-348
- 为 Magic 3.0 重建

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-347
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.23-346
- Perl 5.22 re-rebuild of bootstrapped packages

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.23-345
- Increase release to favour standalone package

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.23-2
- Perl 5.22 rebuild

* Mon Feb 02 2015 Petr Pisar <ppisar@redhat.com> - 1.23-1
- 1.23 bump

* Wed Oct 29 2014 Petr Pisar <ppisar@redhat.com> - 1.22-2
- Do not build-require version module

* Mon Oct 27 2014 Petr Pisar <ppisar@redhat.com> - 1.22-1
- 1.22 bump

* Wed Sep 17 2014 Petr Pisar <ppisar@redhat.com> 1.21-1
- Specfile autogenerated by cpanspec 1.78.
