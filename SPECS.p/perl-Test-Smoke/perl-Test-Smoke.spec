Name:           perl-Test-Smoke
Version:        1.53
Release:        4%{?dist}
Summary:        Perl core test smoke suite
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Test-Smoke/
Source0:        http://www.cpan.org/authors/id/A/AB/ABELTJE/Test-Smoke-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec::Functions)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec) >= 0.82
BuildRequires:  perl(JSON)
BuildRequires:  perl(LWP::UserAgent)
# Net::FTP is not needed for tests
BuildRequires:  perl(Text::ParseWords)
# Time::Local is not needed for tests
# Tests:
BuildRequires:  perl(Archive::Tar)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(lib)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Mail::Sendmail)
Requires:       perl(File::Spec) >= 0.82

%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}perl\\(Mail::Sendmail\\)

%description
The perl core test smoke suite is a set of scripts and modules that try to run
the perl core tests on as many configurations as possible and combine the
results into an easy to read report.

%prep
%setup -q -n Test-Smoke-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} %{buildroot}/*
rm -rf %{buildroot}/%{_bindir}/W32Configure.pl
rm -rf %{buildroot}/%{_mandir}/man1/W32Configure*
rm -rf %{buildroot}/%{perl_vendorlib}/inc/Mail/Sendmail.pm

%check


%files
%doc Changes README ReleaseNotes
%{_bindir}/archiverpt.pl
%{_bindir}/chkbcfg.pl
%{_bindir}/configsmoke.pl
%{_bindir}/mailrpt.pl
%{_bindir}/patchtree.pl
%{_bindir}/runsmoke.pl
%{_bindir}/sendrpt.pl
%{_bindir}/smokeperl.pl
%{_bindir}/smokestatus.pl
%{_bindir}/synctree.pl
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 1.53-4
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.53-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 28 2012 Petr Pisar <ppisar@redhat.com> - 1.53-2
- Perl 5.16 rebuild

* Tue Jun 19 2012 Petr Šabata <contyk@redhat.com> - 1.53-1
- 1.53 bump
- Drop command macros

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1.50-1
- 1.50 bump

* Sun Jun 10 2012 Petr Pisar <ppisar@redhat.com> - 1.47-2
- Perl 5.16 rebuild

* Mon Mar 19 2012 Petr Pisar <ppisar@redhat.com> - 1.47-1
- 1.47 bump

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.44-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 25 2011 Iain Arnell <iarnell@gmail.com> 1.44-4
- update filtering for rpm 4.9

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.44-3
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.44-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov  8 2010 Petr Sabata <psabata@redhat.com> 1.44-1
- New upstream release, v1.44

* Tue Sep  7 2010 Marcela Mašláňová <mmaslano@redhat.com> 1.43-2
- 630802 filter Mail::Sendmail from provides, require it from RPM

* Fri Mar 26 2010 Marcela Mašláňová <mmaslano@redhat.com> 1.43-1
- Specfile autogenerated by cpanspec 1.78.
