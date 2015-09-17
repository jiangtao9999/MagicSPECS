Name:           perl-ExtUtils-Install
Version:        2.04
Release:        347%{?dist}
Summary:        Install Perl files from here to there
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/ExtUtils-Install/
Source0:        http://www.cpan.org/authors/id/B/BI/BINGOS/ExtUtils-Install-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(AutoSplit)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
# Data::Dumper not used at tests
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(vars)
# Win32API::File not used
# Tests:
BuildRequires:  perl(diagnostics)
# ExtUtils::CBuilder not used
BuildRequires:  perl(ExtUtils::MM)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More)
# VMS::DCLsymnot used
# Unbundled tests:
# Test::Builder not used
# Optional testes:
%if !%{defined perl_bootstrap}
BuildRequires:  perl(Test::Pod) >= 1.14
# Test::Pod::Coverage 1.08 not used
# Pod::Coverage 0.17 not used
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Data::Dumper)

%{?perl_default_filter}

%description
Handles the installing and uninstalling of Perl modules, scripts, man
pages, etc.

%prep
%setup -q -n ExtUtils-Install-%{version}
# Remove bundled modules
rm -rf t/lib/Test
sed -i -e '/^t\/lib\/Test\//d' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
%{_fixperms} %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.04-347
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.04-346
- Perl 5.22 re-rebuild of bootstrapped packages

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.04-345
- Increase release to favour standalone package

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.04-2
- Perl 5.22 rebuild

* Thu Sep 18 2014 Petr Pisar <ppisar@redhat.com> 2.04-1
- Specfile autogenerated by cpanspec 1.78.
