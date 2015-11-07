Name:           perl-Unicode-Normalize
Version:        1.19
Release:        3%{?dist}
Summary:        Unicode Normalization Forms
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Unicode-Normalize/
Source0:        http://www.cpan.org/authors/id/S/SA/SADAHIRO/Unicode-Normalize-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# unicore/CombiningClass.pl and unicore/Decomposition.pl from perl
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
# unicore/CombiningClass.pl and unicore/Decomposition.pl from perl, perl is
# auto-detected.
Conflicts:      perl < 4:5.22.0-347

%description
This package provides Perl functions that can convert strings into various
Unicode normalization forms as defined in Unicode Standard Annex #15.

%prep
%setup -q -n Unicode-Normalize-%{version}

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
* Tue Nov 03 2015 Liu Di <liudidi@gmail.com> - 1.19-3
- 为 Magic 3.0 重建

* Thu Sep 17 2015 Liu Di <liudidi@gmail.com> - 1.19-2
- 为 Magic 3.0 重建

* Mon Jul 13 2015 Petr Pisar <ppisar@redhat.com> - 1.19-1
- 1.19 bump

* Thu Jul 02 2015 Petr Pisar <ppisar@redhat.com> 1.18-348
- Specfile autogenerated by cpanspec 1.78.
