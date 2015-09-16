Name:           perl-Test-Most
Version:	0.34
Release:	1%{?dist}
Summary:        Perl module with test functions and features
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Test-Most/
Source0:        http://www.cpan.org/authors/id/O/OV/OVID/Test-Most-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::Dumper::Names) >= 0.03
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Exception::Class) >= 1.14
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(Test::Deep) >= 0.106
BuildRequires:  perl(Test::Differences) >= 0.61
BuildRequires:  perl(Test::Exception) >= 0.31
BuildRequires:  perl(Test::Harness) >= 3.21
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Warn) >= 0.23
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
# not automatically detected
Requires:       perl(Carp)
Requires:       perl(Test::Deep)
Requires:       perl(Test::Differences)
Requires:       perl(Test::Exception)
Requires:       perl(Test::Warn)


%description
Most commonly needed test functions and features. This module provides you with 
the most commonly used testing functions and gives you a bit more fine-grained 
control over your test suite.

%prep
%setup -q -n Test-Most-%{version}

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
* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.34-1
- 更新到 0.34

* Thu Jun 19 2014 Liu Di <liudidi@gmail.com> - 0.33-3
- 为 Magic 3.0 重建

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jan 15 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.33-1
- 0.33 bump

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.31-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Petr Pisar <ppisar@redhat.com> - 0.31-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Sep 13 2012 Jitka Plesnikova <jplesnik@redhat.com> - 0.31-1
- 0.31 bump
- Specify all dependencies.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 14 2012 Petr Pisar <ppisar@redhat.com> - 0.25-3
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Aug 18 2011 Petr Sabata <contyk@redhat.com> - 0.25-1
- 0.25 bump

* Tue Jul 26 2011 Petr Sabata <contyk@redhat.com> - 0.24-1
- 0.24 bump
- Removing now obsolete Buildroot and defattr

* Wed Jun 29 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.23-4
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 07 2010 Iain Arnell <iarnell@gmail.com> 0.23-2
- add explicit requires that are no longer automatically detected

* Tue Sep 14 2010 Petr Sabata <psabata@redhat.com> - 0.23-1
- New release, 0.23

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.21-6
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.21-5
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr  6 2009 Marcela Mašláňová <mmaslano@redhat.com> 0.21-3
- remove unnecesarry requirements

* Thu Apr 02 2009 Marcela Mašláňová <mmaslano@redhat.com> 0.21-1
- Specfile autogenerated by cpanspec 1.78.
