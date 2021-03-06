Name:		perl-Test-Warnings
Version:	0.021
Release:	5%{?dist}
Summary:	Test for warnings and the lack of them
License:	GPL+ or Artistic
Group:		Development/Libraries
URL:		http://search.cpan.org/dist/Test-Warnings
Source0:	http://search.cpan.org/CPAN/authors/id/E/ET/ETHER/Test-Warnings-%{version}.tar.gz
BuildArch:	noarch
# Build
BuildRequires:	perl
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module
BuildRequires:	perl(Carp)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(Test::Builder)
BuildRequires:	perl(parent)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(CPAN::Meta) >= 2.120900
BuildRequires:	perl(CPAN::Meta::Check) >= 0.007
BuildRequires:	perl(CPAN::Meta::Prereqs)
BuildRequires:	perl(CPAN::Meta::Requirements)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(if)
BuildRequires:	perl(Test::More) >= 0.94
BuildRequires:	perl(Test::Tester) >= 0.108
# Runtime
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:	perl(Carp)

%description
If you've ever tried to use Test::NoWarnings to confirm there are no warnings
generated by your tests, combined with the convenience of done_testing to not
have to declare a test count, you'll have discovered that these two features do
not play well together, as the test count will be calculated before the
warnings test is run, resulting in a TAP error (see examples/test_nowarnings.pl
in this distribution for a demonstration).

This module is intended to be used as a drop-in replacement for
Test::NoWarnings: it also a%description -l zh_CN.UTF-8s an extra test, but runs this test before
done_testing calculates the test count, rather than after. It does this by
hooking into done_testing as well as via an END block. You can declare a plan,
or not, and things will still Just Work.

It is actually equivalent to:

    use Test::NoWarnings 1.04 ':early';

as warnings are still printed normally as they occur. You are safe, and
enthusiastically encouraged, to perform a global search-replace of the above
with use Test::Warnings; whether or not your tests have a plan.

%prep
%setup -q -n Test-Warnings-%{version}

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
%license LICENSE
%doc Changes CONTRIBUTING README examples/
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::Warnings.3*

%changelog
* Thu Nov 12 2015 Liu Di <liudidi@gmail.com> - 0.021-5
- 为 Magic 3.0 重建

* Tue Nov 03 2015 Liu Di <liudidi@gmail.com> - 0.021-4
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.021-1
- 更新到 0.021

* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 0.014-7
- 为 Magic 3.0 重建

* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 0.014-6
- 为 Magic 3.0 重建

* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 0.014-5
- 为 Magic 3.0 重建

* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 0.014-4
- 为 Magic 3.0 重建

* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 0.014-3
- 为 Magic 3.0 重建

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.014-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar  3 2014 Paul Howarth <paul@city-fan.org> - 0.014-1
- Update to 0.014
  - Fix test that fails when FOO or BAR environment variables are set
    (CPAN RT#93447)

* Mon Dec 16 2013 Paul Howarth <paul@city-fan.org> - 0.013-1
- Update to 0.013
  - Update configure_requires checking in Makefile.PL

* Mon Oct 14 2013 Paul Howarth <paul@city-fan.org> - 0.012-1
- Update to 0.012
  - Re-release to fix t/00-report-prereqs.t use of CPAN::Meta::Requirements

* Sun Oct 13 2013 Paul Howarth <paul@city-fan.org> - 0.011-1
- Update to 0.011
  - Unnecessary tests removed
  - CONTRIBUTING file added
- Drop buildreqs only needed for removed tests
- BR: optional test requirement perl(CPAN::Meta::Requirements)

* Wed Sep 25 2013 Paul Howarth <paul@city-fan.org> - 0.010-1
- Update to 0.010
  - Re-release with fixed compile test
- Update dependencies
- Package examples

* Wed Sep 11 2013 Paul Howarth <paul@city-fan.org> - 0.009-1
- Update to 0.009
  - Fixed error in synopsis (we do not export anything by default)
  - A caveat added to the documentation regarding embedding warning checks
    inside another sub
  - ':no_end_test' now also covers side effects of done_testing, as well as
    END blocks, making it possible to use the warning(s) subs without having an
    end warning test while using done_testing (necessary when combining with
    the 'if' pragma)
  - END tests will not be added by a subequent use of Test::Warnings if a
    previous one passed ':no_end_test'
- Update dependencies

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.008-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 0.008-2
- Perl 5.18 rebuild

* Mon Jul 15 2013 Paul Howarth <paul@city-fan.org> - 0.008-1
- Update to 0.008
  - Compile test updated, to hopefully fix mswin32 parsing issues

* Wed Jul 10 2013 Paul Howarth <paul@city-fan.org> - 0.007-1
- Update to 0.007
  - Fix subtest tests to work on Test::More before 0.95_01 (CPAN RT#86802)
- BR: perl(Capture::Tiny)
- Bump perl(Module::Build::Tiny) version requirement to 0.024
- Bump perl(Test::CheckDeps) version requirement to 0.006
- Drop perl(Test::More) version requirement to 0.94

* Tue Jul  9 2013 Paul Howarth <paul@city-fan.org> - 0.006-2
- Sanitize for Fedora submission

* Tue Jul  9 2013 Paul Howarth <paul@city-fan.org> - 0.006-1
- Initial RPM version
