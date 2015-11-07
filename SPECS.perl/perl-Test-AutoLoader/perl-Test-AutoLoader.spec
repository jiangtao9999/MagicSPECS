Name:           perl-Test-AutoLoader
Version:        0.03
Release:        8%{?dist}
Summary:        Testing utility for autosplit/autoloaded modules
License:        GPL+
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Test-AutoLoader/
Source0:        http://www.cpan.org/authors/id/B/BW/BWARFIELD/NRGN/Test-AutoLoader-%{version}.tar.gz
# Fix test plan number (RT#66399)
Patch0:         Test-AutoLoader-0.03-Fix-test-plan-number.patch
# Perl 5.16 does not autosplit POSIX module (RT#77942)
Patch1:         Test-AutoLoader-0.03-Skip-POSIX-tests-with-perl-5.16.patch
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::Builder)
# Tests:
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 0.95
BuildRequires:  perl(Test::Tester) >= 0.08
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This single-purpose module attempts to eliminate uncaught syntax errors or
other obvious goofs in subroutines that are autosplit, and hence not looked
at by perl -c Module.pm. Ideally, this module will become unnecessary as
you reach full coverage of those subroutines in your unit tests. Until that
happy day, however, this should provide a quick and dirty backstop for
embarrassing typos.

%prep
%setup -q -n Test-AutoLoader-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
# Tests expect non-localized messages (RT#62839)
LC_ALL=C 

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Nov 03 2015 Liu Di <liudidi@gmail.com> - 0.03-8
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.03-7
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.03-6
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.03-5
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.03-4
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 0.03-2
- Perl 5.16 rebuild
- Make tests compatible with perl 5.16 (RT#77942)

* Thu Apr 26 2012 Petr Pisar <ppisar@redhat.com> 0.03-1
- Specfile autogenerated by cpanspec 1.78.
