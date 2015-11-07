Name:           perl-Module-CPANfile
Version:        1.1001
Release:        3%{?dist}
Summary:        Parse cpanfile
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Module-CPANfile/
Source0:        http://www.cpan.org/authors/id/M/MI/MIYAGAWA/Module-CPANfile-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(CPAN::Meta) >= 2.12091
BuildRequires:  perl(CPAN::Meta::Feature) >= 2.12091
BuildRequires:  perl(CPAN::Meta::Prereqs) >= 2.12091
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# tests
BuildRequires:  perl(Exporter)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More) >= 0.88

Requires:       perl(CPAN::Meta) >= 2.12091
Requires:       perl(CPAN::Meta::Prereqs) >= 2.12091
Requires:       perl(CPAN::Meta::Feature) >= 2.12091
Requires:       perl(Data::Dumper)
Requires:       perl(Pod::Usage)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%?perl_default_filter
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(CPAN::Meta\\)$

%description
Module::CPANfile is a tool to handle cpanfile format to load application
specific dependencies, not just for CPAN distributions.

%prep
%setup -q -n Module-CPANfile-%{version}

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
%license LICENSE
%doc Changes README
%{_bindir}/mymeta-cpanfile
%{_bindir}/cpanfile-dump
%{perl_vendorlib}/*
%{_mandir}/man1/mymeta-cpanfile*
%{_mandir}/man1/cpanfile-dump*
%{_mandir}/man3/*

%changelog
* Mon Nov 02 2015 Liu Di <liudidi@gmail.com> - 1.1001-3
- 为 Magic 3.0 重建

* Tue Sep 15 2015 Liu Di <liudidi@gmail.com> - 1.1001-2
- 为 Magic 3.0 重建

* Mon Sep 07 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.1001-1
- 1.1001 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1000-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.1000-2
- Perl 5.22 rebuild

* Fri Sep 19 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.1000-1
- 1.1000 bump

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.0001-5
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0001-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 30 2013 Marcela Mašláňová <mmaslano@redhat.com> 1.0001-3
- fix all problems found in review rhbz#929254

* Tue Aug 27 2013 Marcela Mašláňová <mmaslano@redhat.com> 1.0001-2
- fix all problems found in review rhbz#929254

* Tue Aug 27 2013 Marcela Mašláňová <mmaslano@redhat.com> 1.0001-1
- Specfile autogenerated by cpanspec 1.78.
