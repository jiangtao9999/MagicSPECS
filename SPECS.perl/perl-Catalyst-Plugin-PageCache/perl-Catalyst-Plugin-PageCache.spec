Name:           perl-Catalyst-Plugin-PageCache
Version:        0.31
Release:        20%{?dist}
Summary:        Cache the output of entire pages
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Catalyst-Plugin-PageCache/
Source0:        http://search.cpan.org/CPAN/authors/id/T/TI/TIMB/Catalyst-Plugin-PageCache-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Cache::Cache) >= 1.04
BuildRequires:  perl(Cache::FileCache)
BuildRequires:  perl(Catalyst::Plugin::Cache) >= 0.10
BuildRequires:  perl(Catalyst::Plugin::I18N)
BuildRequires:  perl(Catalyst::Runtime)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(Digest::SHA1)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(MRO::Compat) >= 0.10
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)

Requires:       perl(Catalyst::Runtime)
Requires:       perl(Class::Accessor::Fast)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Many dynamic websites perform heavy processing on most pages, yet this
information may rarely change from request to request. Using the PageCache
plugin, you can cache the full output of different pages so they are served
to your visitors as fast as possible. This method of caching is very useful
for withstanding a Slashdotting, for example.

%prep
%setup -q -n Catalyst-Plugin-PageCache-%{version}
iconv -f iso-8859-1 -t utf-8 README >README.conv && mv README.conv README

%build
PERL5_CPANPLUS_IS_RUNNING=1 %{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
TEST_POD=yep 

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Nov 02 2015 Liu Di <liudidi@gmail.com> - 0.31-20
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.31-19
- 为 Magic 3.0 重建

* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 0.31-18
- 为 Magic 3.0 重建

* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 0.31-17
- 为 Magic 3.0 重建

* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 0.31-16
- 为 Magic 3.0 重建

* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 0.31-15
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.31-14
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.31-13
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.31-12
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.31-11
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.31-10
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.31-9
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 0.31-8
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.31-7
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.31-6
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.31-5
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.31-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.31-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Nov 20 2010 Iain Arnell <iarnell@gmail.com> 0.31-1
- update to latest upstream
- no longer needs private copy of FileCache for testing
- clean up spec for modern rpmbuild

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.22-3
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.22-2
- rebuild against perl 5.10.1

* Sun Jul 19 2009 Iain Arnell 0.22-1
- Specfile autogenerated by cpanspec 1.78.
