Name:           perl-Log-Report-Optional
Version:        1.01
Release:        7%{?dist}
Summary:        Base class for large Log::Report and simple Log::Report::Minimal
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Log-Report-Optional/
Source0:        http://www.cpan.org/authors/id/M/MA/MARKOV/Log-Report-Optional-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(String::Print) >= 0.13
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test::More) >= 0.86
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(String::Print) >= 0.13
# This package is a sprout of perl-Log-Report. It replaces part of
# perl-Log-Report-0.998 and it's required by perl-Log-Report >= 1.01.
Conflicts:      perl-Log-Report < 0.999

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(String::Print\\)$

%description
This module will allow libraries (helper modules) to have a dependency to a
small module instead of the full Log-Report distribution. The full power of
Log::Report is only released when the main program uses that module. In
that case, the module using the 'Optional' will also use the full
Log::Report, otherwise the dressed-down Log::Report::Minimal version.

%prep
%setup -q -n Log-Report-Optional-%{version}

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
%doc ChangeLog README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Nov 02 2015 Liu Di <liudidi@gmail.com> - 1.01-7
- 为 Magic 3.0 重建

* Thu Sep 17 2015 Liu Di <liudidi@gmail.com> - 1.01-6
- 为 Magic 3.0 重建

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.01-4
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.01-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 11 2014 Petr Pisar <ppisar@redhat.com> - 1.01-1
- 1.01 bump

* Fri Jan 31 2014 Petr Pisar <ppisar@redhat.com> 1.00-1
- Specfile autogenerated by cpanspec 1.78.
