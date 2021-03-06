Name:           perl-Digest-SHA
Epoch:          1
Version:	5.95
Release:	3%{?dist}
Summary:        Perl extension for SHA-1/224/256/384/512
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Digest-SHA/
Source0:        http://www.cpan.org/authors/id/M/MS/MSHELOR/Digest-SHA-%{version}.tar.gz
# Since 5.80, upstream overrides CFLAGS because they think it improves
# performance. Revert it.
Patch0:         Digest-SHA-5.91-Reset-CFLAGS.patch
BuildRequires:  perl
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Getopt::Std)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
# Getopt::Long not used at tests
BuildRequires:  perl(integer)
BuildRequires:  perl(warnings)
# Optional run-time
BuildRequires:  perl(Digest::base)
# Tests
BuildRequires:  perl(FileHandle)
# Optional tests
%if !%{defined perl_bootstrap}
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 0.08
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Carp)
# Optional but recommended
Requires:       perl(Digest::base)

%{?perl_default_filter}

%description
Digest::SHA is a complete implementation of the NIST Secure Hash Standard. It
gives Perl programmers a convenient way to calculate SHA-1, SHA-224, SHA-256,
SHA-384, SHA-512, SHA-512/224, and SHA-512/256 message digests. The module can
handle all types of input, including partial-byte data.

%prep
%setup -q -n Digest-SHA-%{version}
%patch0 -p1
chmod -x examples/*
perl -MExtUtils::MakeMaker -e 'ExtUtils::MM_Unix->fixin(q{examples/dups})'

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE='%{optflags}'
make %{?_smp_mflags}

%install
make pure_install DESTDIR='%{buildroot}'
find '%{buildroot}' -type f -name .packlist -exec rm -f {} +
find '%{buildroot}' -type f -name '*.bs' -size 0 -exec rm -f {} +
%{_fixperms} '%{buildroot}'/*

%check
make test

%files
%doc Changes examples README
%{_bindir}/*
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Digest*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Thu Nov 12 2015 Liu Di <liudidi@gmail.com> - 1:5.95-3
- 为 Magic 3.0 重建

* Mon Nov 02 2015 Liu Di <liudidi@gmail.com> - 1:5.95-2
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 1:5.95-1
- 更新到 5.95

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 1:5.92-3
- 为 Magic 3.0 重建

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.92-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jun 02 2014 Petr Pisar <ppisar@redhat.com> - 1:5.92-1
- 5.92 bump

* Mon May 26 2014 Petr Pisar <ppisar@redhat.com> - 1:5.91-1
- 5.91 bump

* Fri May 09 2014 Petr Pisar <ppisar@redhat.com> - 1:5.90-1
- 5.90 bump

* Fri Apr 25 2014 Petr Pisar <ppisar@redhat.com> - 1:5.89-1
- 5.89 bump

* Tue Mar 18 2014 Petr Pisar <ppisar@redhat.com> - 1:5.88-1
- 5.88 bump

* Wed Feb 19 2014 Petr Pisar <ppisar@redhat.com> - 1:5.87-1
- 5.87 bump

* Mon Feb 03 2014 Petr Pisar <ppisar@redhat.com> - 1:5.86-1
- 5.86 bump

* Wed Aug 14 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.85-4
- Perl 5.18 re-rebuild of bootstrapped packages

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.85-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 1:5.85-2
- Perl 5.18 rebuild

* Fri Jun 28 2013 Petr Pisar <ppisar@redhat.com> - 1:5.85-1
- 5.85 bump

* Mon Mar 11 2013 Petr Pisar <ppisar@redhat.com> - 1:5.84-1
- 5.84 bump

* Tue Mar 05 2013 Petr Pisar <ppisar@redhat.com> - 1:5.83-1
- 5.83 bump

* Mon Jan 28 2013 Petr Pisar <ppisar@redhat.com> - 1:5.82-1
- 5.82 bump

* Tue Jan 15 2013 Petr Pisar <ppisar@redhat.com> - 1:5.81-1
- 5.81 bump

* Tue Dec 11 2012 Petr Pisar <ppisar@redhat.com> - 1:5.80-1
- 5.80 bump

* Fri Nov 30 2012 Petr Pisar <ppisar@redhat.com> - 1:5.74-2
- Restore epoch value broken in 5.73 bump

* Mon Nov 26 2012 Petr Pisar <ppisar@redhat.com> - 0:5.74-1
- 5.74 bump

* Thu Nov 01 2012 Petr Pisar <ppisar@redhat.com> - 0:5.73-2
- 5.73 bump

* Wed Sep 26 2012 Petr Pisar <ppisar@redhat.com> - 1:5.72-1
- 5.72 bump

* Mon Aug 13 2012 Marcela Mašláňová <mmaslano@redhat.com> - 1:5.71-240
- bump release to override sub-package from perl.spec 

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.71-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Petr Pisar <ppisar@redhat.com> - 1:5.71-4
- Perl 5.16 re-rebuild of bootstrapped packages

* Wed Jun 06 2012 Petr Pisar <ppisar@redhat.com> - 1:5.71-3
- Perl 5.16 rebuild

* Fri Jun 01 2012 Petr Pisar <ppisar@redhat.com> - 1:5.71-2
- Omit optional POD tests on bootstrap

* Wed Mar 14 2012 Petr Pisar <ppisar@redhat.com> - 1:5.71-1
- 5.71 bump

* Tue Feb 14 2012 Petr Pisar <ppisar@redhat.com> 1:5.70-1
- Specfile autogenerated by cpanspec 1.78.
