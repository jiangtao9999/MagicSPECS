Name:           perl-Catalyst-Plugin-Session-Store-FastMmap
Version:	0.16
Release:	1%{?dist}
Summary:        FastMmap session storage backend
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Catalyst-Plugin-Session-Store-FastMmap/
Source0:        http://search.cpan.org/CPAN/authors/id/B/BO/BOBTFISH/Catalyst-Plugin-Session-Store-FastMmap-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Cache::FastMmap) >= 1.29
BuildRequires:  perl(Catalyst::Plugin::Session) >= 0.27
BuildRequires:  perl(Class::Data::Inheritable)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
Requires:       perl(Cache::FastMmap) >= 1.29
Requires:       perl(Catalyst::Plugin::Session) >= 0.27
Requires:       perl(Class::Accessor::Fast)
Requires:       perl(Class::Data::Inheritable)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Catalyst::Plugin::Session::Store::FastMmap is a fast session storage plugin
for Catalyst that uses an mmap'ed file to act as a shared memory
interprocess cache. It is based on Cache::FastMmap.

%prep
%setup -q -n Catalyst-Plugin-Session-Store-FastMmap-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
TEST_POD=1 

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.16-1
- 更新到 0.16

* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 0.14-18
- 为 Magic 3.0 重建

* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 0.14-17
- 为 Magic 3.0 重建

* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 0.14-16
- 为 Magic 3.0 重建

* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 0.14-15
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.14-14
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.14-13
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.14-12
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.14-11
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.14-10
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.14-9
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 0.14-8
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.14-7
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.14-6
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.14-5
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.14-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Nov 20 2010 Iain Arnell <iarnell@gmail.com> 0.14-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Sat May 08 2010 Iain Arnell <iarnell@gmail.com> 0.13-3
- BR perl(Class::Data::Inheritable)

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.13-2
- Mass rebuild with perl-5.12.0

* Mon Jan 04 2010 Iain Arnell <iarnell@gmail.com> 0.13-1
- update to latest upstream version

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.12-2
- rebuild against perl 5.10.1

* Sun Oct 18 2009 Iain Arnell <iarnell@gmail.com> 0.12-1
- update to latest upstream version

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jun 21 2009 Iain Arnell <iarnell@gmail.com> 0.11-1
- update to latest upstream version

* Thu May 14 2009 Iain Arnell <iarnell@gmail.com> 0.10-1
- update to latest upstream version
- R/BR Cache::FastMmap >= 1.29
- Fix missing requires (due to 'use base')


* Wed Apr 08 2009 Iain Arnell <iarnell@gmail.com> 0.07-1
- update to latest upstream
- BR MRO::Compat 

* Sat Apr 04 2009 Iain Arnell <iarnell@gmail.com> 0.07-1
- update to latest upstream

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 12 2009 Iain Arnell <iarnell@gmail.com> 0.06-1
- update to latest upstream release

* Thu Nov 13 2008 Iain Arnell <iarnell@gmail.com> 0.05-2
- Enabled optional tests

* Sun Sep 14 2008 Iain Arnell <iarnell@gmail.com> 0.05-1
- Specfile autogenerated by cpanspec 1.77.
