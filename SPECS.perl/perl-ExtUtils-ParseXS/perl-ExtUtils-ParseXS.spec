Name:           perl-ExtUtils-ParseXS
# Epoch to compete with perl.spec
Epoch:          1
Version:	3.30
Release:	1%{?dist}
Summary:        Module and a script for converting Perl XS code into C code
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/ExtUtils-ParseXS/
Source0:        http://www.cpan.org/authors/id/S/SM/SMUELLER/ExtUtils-ParseXS-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.46
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter) >= 5.57
# ExtUtils::XSSymSet not needed
BuildRequires:  perl(File::Basename)
# Getopt::Long not tested
BuildRequires:  perl(lib)
BuildRequires:  perl(re)
BuildRequires:  perl(Symbol)
# Tests:
BuildRequires:  perl-devel
BuildRequires:  perl(attributes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(overload)
BuildRequires:  perl(Test::More) >= 0.47
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl-devel
Requires:       perl(Exporter) >= 5.57
# perl-ExtUtils-Typemaps has been merged into perl-ExtUtils-ParseXS, bug #891952
Obsoletes:      perl-ExtUtils-Typemaps

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Exporter\\)$

%description
ExtUtils::ParseXS will compile XS code into C code by embedding the
constructs necessary to let C functions manipulate Perl values and creates
the glue necessary to let Perl access those functions.

%prep
%setup -q -n ExtUtils-ParseXS-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*
# Do not install xsubpp twice, RT#117289
rm $RPM_BUILD_ROOT%{perl_vendorlib}/ExtUtils/xsubpp
ln -s ../../../../bin/xsubpp $RPM_BUILD_ROOT%{perl_vendorlib}/ExtUtils/

%check
make test

%files
%doc Changes README
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 1:3.30-1
- 更新到 3.30

* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 1:3.24-4
- 为 Magic 3.0 重建

* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 1:3.24-3
- 为 Magic 3.0 重建

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 10 2014 Petr Pisar <ppisar@redhat.com> - 1:3.24-1
- 3.24 bump

* Mon Sep 02 2013 Petr Pisar <ppisar@redhat.com> - 1:3.22-1
- 3.22 bump

* Mon Aug 26 2013 Petr Pisar <ppisar@redhat.com> - 1:3.21-1
- 3.21 bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.18-291
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 15 2013 Petr Pisar <ppisar@redhat.com> - 1:3.18-290
- Increase release to favour standalone package

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 1:3.18-2
- Perl 5.18 rebuild

* Fri Mar 22 2013 Petr Pisar <ppisar@redhat.com> 1:3.18-1
- Specfile autogenerated by cpanspec 1.78.
