Name:           perl-CPAN-Inject
Version:	1.14
Release:	2%{?dist}
Summary:        Base class for injecting distributions into CPAN sources
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/CPAN-Inject/
Source0:        http://search.cpan.org/CPAN/authors/id/P/PS/PSHANGOV/CPAN-Inject-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(CPAN) >= 1.36
BuildRequires:  perl(CPAN::Checksums) >= 1.05
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::chmod) >= 0.30
BuildRequires:  perl(File::Remove) >= 0.34
BuildRequires:  perl(Params::Util) >= 0.21
BuildRequires:  perl(Test::More) >= 0.42
BuildRequires:  perl(Test::Script) >= 1.02
BuildRequires:  perl(Test::Harness)
Requires:       perl(CPAN) >= 1.36
Requires:       perl(CPAN::Checksums) >= 1.05
Requires:       perl(File::chmod) >= 0.30
Requires:       perl(Params::Util) >= 0.21
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Following the release of CPAN::Mini, the CPAN::Mini::Inject module was
created to add additional distributions into a minicpan mirror.

%prep
%setup -q -n CPAN-Inject-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{perl_vendorlib}/*
%{_bindir}/cpaninject
%{_mandir}/man1/cpaninject.1.gz
%{_mandir}/man3/*

%changelog
* Mon Sep 14 2015 Liu Di <liudidi@gmail.com> - 1.14-2
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 1.14-1
- 更新到 1.14

* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 1.13-15
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 1.13-14
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 1.13-13
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.13-12
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.13-11
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.13-10
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.13-9
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 1.13-8
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 1.13-7
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 1.13-6
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 1.13-5
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1.13-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan  5 2011 Petr Sabata <psabata@redhat.com> - 1.13-1
- 1.13 version bump

* Mon Jan  3 2011 Petr Sabata <psabata@redhat.com> - 1.12-1
- 1.12 version bump

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.11-4
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.11-3
- Mass rebuild with perl-5.12.0

* Tue Dec 22 2009 Marcela Mašláňová <mmaslano@redhat.com> 0.11-2
- switch off test which had problems with cpan in mock

* Wed Nov 18 2009 Marcela Mašláňová <mmaslano@redhat.com> 0.11-1
- Specfile autogenerated by cpanspec 1.78.
