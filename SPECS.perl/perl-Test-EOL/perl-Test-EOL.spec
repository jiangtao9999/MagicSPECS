Name:		perl-Test-EOL
Version:	1.6
Release:	2%{?dist}
Summary:	Check the correct line endings in your project
Group:		Development/Libraries
License:	GPL+ or Artistic
URL:		http://search.cpan.org/dist/Test-EOL/
Source0:        http://search.cpan.org/CPAN/authors/id/F/FR/FREW/Test-EOL-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(id -nu)
BuildArch:	noarch
BuildRequires:	perl(Cwd)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Pod::Coverage::TrustPod)
BuildRequires:	perl(Test::Builder)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::NoTabs) >= 1.2
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage) >= 1.08
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
This module scans your project/distribution for any perl files (scripts,
modules, etc.) with Windows line endings. It can also check for trailing
whitespace.

%prep
%setup -q -n Test-EOL-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
%{_fixperms} %{buildroot}

%check
 RELEASE_TESTING=1

%clean
rm -rf %{buildroot}

%files
%doc Changes LICENSE README
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::EOL.3pm*

%changelog
* Tue Nov 03 2015 Liu Di <liudidi@gmail.com> - 1.6-2
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 1.6-1
- 更新到 1.6

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.5-3
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 1.5-2
- 为 Magic 3.0 重建

* Sun Sep  9 2012 Paul Howarth <paul@city-fan.org> - 1.5-1
- Update to 1.5
  - Properly fix Win32 (CPAN RT#76037)
  - Change default to searching for trailing whitespace from the current
    directory downwards (as tests are run from the top of a dist normally),
    rather than one directory above the test file, as then we don't work as
    expected if tests are in t/author or similar
- BR: perl(Pod::Coverage::TrustPod) even when bootstrapping

* Tue Aug  7 2012 Paul Howarth <paul@city-fan.org> - 1.3-6
- Reinstate EPEL-5 compatibility
- Drop redundant patch for building with ExtUtils::MakeMaker < 6.30

* Tue Aug  7 2012 Jitka Plesnikova <jplesnik@redhat.com>
- Update BR and clean up spec for modern rpmbuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Petr Pisar <ppisar@redhat.com> - 1.3-3
- Perl 5.16 re-rebuild of bootstrapped packages

* Thu Jun 28 2012 Petr Pisar <ppisar@redhat.com> - 1.3-2
- Perl 5.16 rebuild

* Sun Jun 17 2012 Paul Howarth <paul@city-fan.org> - 1.3-1
- Update to 1.3
  - Fix to ignore inc/ directory used by Module::Install
- Drop hack to remove tabs from bundled Module::Install
- Bump version requirement for perl(Test::NoTabs) to 1.2 to avoid failing
  release tests due to tabs in bundled Module::Install

* Fri Jun 15 2012 Paul Howarth <paul@city-fan.org> - 1.2-1
- Update to 1.2
  - Fix bad regex matching directories containing 'svn', not just '.svn'
    directories (CPAN RT#75968)
- BR: perl(Cwd)
- Drop non-dual-lived buildreqs perl(File::Find) and perl(FindBin)
- This release by BOBTFISH -> update source URL
- Remove tabs from bundled Module::Install that break release tests
- Don't need to remove empty directories from the buildroot
- Drop %%defattr, redundant since rpm 4.4

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 1.1-2
- Perl 5.16 rebuild

* Mon Jan 16 2012 Paul Howarth <paul@city-fan.org> - 1.1-1
- Update to 1.1
  - Fix test fails on < 5.8 perls
  - Fix t/13-latin1.t failures on Win32 and under TB1.5
- Add buildreqs for required core modules, which might be dual-lived

* Thu Jan  5 2012 Paul Howarth <paul@city-fan.org> - 1.0-1
- Update to 1.0
  - Fix misleading test failure diagnostics when only issue is trailing
    whitespace
  - No longer blindly assume utf8 on input files (CPAN RT#59877)
  - Properly document testing options
- This release by RIBASUSHI -> update source URL
- Drop upstreamed patch for CPAN RT#59877
- Update patch for building with old ExtUtils::MakeMaker versions

* Thu Jun 30 2011 Paul Howarth <paul@city-fan.org> - 0.9-5
- Restore EPEL-4 compatibility
- perl(Pod::Coverage::TrustPod) is available everywhere now
- %%{?perl_default_filter} isn't needed for this tiny package
- Nobody else likes macros for commands

* Tue Jun 28 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.9-4
- Perl mass rebuild
- Add macro perl_bootstrap

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Oct 18 2010 Paul Howarth <paul@city-fan.org> - 0.9-2
- Don't assume tested files are UTF-8 encoded (CPAN RT#59877)

* Wed Jun 16 2010 Paul Howarth <paul@city-fan.org> - 0.9-1
- Update to 0.9 (fix warnings on very old perls - CPAN RT#58442)
- Use DESTDIR instead of PERL_INSTALL_ROOT
- Add %%{?perl_default_filter}

* Wed Jun 16 2010 Paul Howarth <paul@city-fan.org> - 0.8-1
- Initial RPM version
