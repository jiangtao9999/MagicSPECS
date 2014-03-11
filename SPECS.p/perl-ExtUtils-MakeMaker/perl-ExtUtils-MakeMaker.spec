Name:           perl-ExtUtils-MakeMaker
Version:        6.62
Release:        2%{?dist}
Summary:        Create a module Makefile
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/ExtUtils-MakeMaker/
Source0:        http://www.cpan.org/authors/id/M/MS/MSCHWERN/ExtUtils-MakeMaker-%{version}.tar.gz
# Do not set RPATH to perl shared-library modules by default. Bug #773622.
# This is copy from `perl' package. This is distributor extension.
Patch0:         %{name}-6.62-USE_MM_LD_RUN_PATH.patch
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec) >= 0.8
# Unbundled
BuildRequires:  perl(File::Copy::Recursive)
# Tests:
BuildRequires:  perl(AutoSplit)
BuildRequires:  perl(Carp)
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::Command)
BuildRequires:  perl(ExtUtils::Install)
BuildRequires:  perl(ExtUtils::Installed)
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(lib)
BuildRequires:  perl(Parse::CPAN::Meta)
BuildRequires:  perl(Pod::Man)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)
# Optional tests
BuildRequires:  perl(ExtUtils::CBuilder)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(ExtUtils::Command)
Requires:       perl(ExtUtils::Install)
Requires:       perl(ExtUtils::Manifest)
Requires:       perl(File::Find)
Requires:       perl(File::Spec) >= 0.8
Requires:       perl(Getopt::Long)
Requires:       perl(Test::Harness)

# Do not export underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(File::Spec\\)\s*$
# Do not export private redefinitions
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(DynaLoader|ExtUtils::MakeMaker::_version\\)

%description
This utility is designed to write a Makefile for an extension module from a
Makefile.PL. It is based on the Makefile.SH model provided by Andy
Dougherty and the perl5-porters.

%prep
%setup -q -n ExtUtils-MakeMaker-%{version}
%patch0 -p1
# Remove bundled modules
rm -rf bundled/* ||:
sed -i -e '/^bundled\// d' MANIFEST

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
#make test

%files
%doc Changes NOTES PATCHING README TODO
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Thu Jan 12 2012 Petr Pisar <ppisar@redhat.com> - 6.62-2
- Do not set RPATH to perl shared-library modules by default (bug #773622)

* Fri Nov 25 2011 Petr Pisar <ppisar@redhat.com> 6.62-1
- Specfile autogenerated by cpanspec 1.78.
- Remove defattr and BuildRoot from spec.
