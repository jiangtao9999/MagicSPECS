Name:           perl-Catalyst-Plugin-Session-Store-File
Version:        0.18
Release:        11%{?dist}
Summary:        File storage backend for session data
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Catalyst-Plugin-Session-Store-File/
Source0:        http://search.cpan.org/CPAN/authors/id/F/FL/FLORA/Catalyst-Plugin-Session-Store-File-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 1:5.8.0
BuildRequires:  perl(Cache::Cache) >= 1.02
BuildRequires:  perl(Catalyst::Plugin::Session) >= 0.27
BuildRequires:  perl(Catalyst::Runtime) >= 5.7000
BuildRequires:  perl(Class::Data::Inheritable) >= 0.04
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(MRO::Compat) >= 0.10
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
Requires:       perl(Cache::Cache) >= 1.02
Requires:       perl(Catalyst::Plugin::Session)
Requires:       perl(Catalyst::Runtime) >= 5.7000
Requires:       perl(Class::Data::Inheritable) >= 0.04
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Catalyst::Plugin::Session::Store::File is an easy to use storage plugin for
Catalyst that uses an simple file to act as a shared memory interprocess
cache. It is based on Cache::FileCache.

%prep
%setup -q -n Catalyst-Plugin-Session-Store-File-%{version}

%build
PERL5_CPANPLUS_IS_RUNNING=1 %{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
TEST_POD=1 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.18-11
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.18-10
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.18-9
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.18-7
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.18-5
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.18-4
- Mass rebuild with perl-5.12.0

* Mon Jan 11 2010 Iain Arnell <iarnell@gmail.com> 0.18-3
- fix source0 location (was BADURL)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.18-2
- rebuild against perl 5.10.1

* Sat Oct 10 2009 Iain Arnell <iarnell@gmail.com> 0.18-1
- update to latest upstream version

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jun 21 2009 Iain Arnell <iarnell@gmail.com> 0.17-1
- update to latest upstream version
- pretend that CPANPLUS is running

* Sun May 10 2009 Iain Arnell <iarnell@gmail.com> 0.16-1
- update to 0.16 (upstream 0.14 was mistakenly released as 0.15)

* Wed Apr 22 2009 Iain Arnell <iarnell@gmail.com> 0.15-1
- update to 0.15
- BR perl(MRO::Compat)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Nov 27 2008 Iain Arnell <iarnell@gmail.com> 0.13-1
- Specfile autogenerated by cpanspec 1.77.
