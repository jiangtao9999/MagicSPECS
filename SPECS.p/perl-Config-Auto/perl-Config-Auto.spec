Name:           perl-Config-Auto
Version:        0.38
Release:        13%{?dist}
Summary:        Magical config file parser
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Config-Auto/
Source0:        http://www.cpan.org/authors/id/B/BI/BINGOS/Config-Auto-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Config::IniFiles)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(YAML)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
This module was written after having to write Yet Another Config File
Parser for some variety of colon-separated config. It searches the filesystem
for the program's configuration file, basing itself on the program's name
and returns a data structure based on the file's contents.

%prep
%setup -q -n Config-Auto-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check


%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 0.38-13
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.38-12
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.38-11
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.38-10
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.38-9
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.38-8
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.38-7
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 0.38-6
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.38-5
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.38-4
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.38-3
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 09 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.38-1
- Update to 0.38
- Add Test::Pod to the BR to enable optionnal tests

* Mon Jul 18 2011 Petr Sabata <contyk@redhat.com> - 0.36-2
- Perl mass rebuild

* Fri Jul 08 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.36-1
- Update to 0.36
- Clean up spec file

* Wed Jun 29 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.34-2
- Perl mass rebuild

* Wed Mar 09 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.34-1
- Update to 0.34

* Thu Feb 24 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.32-1
- Update to 0.32

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 24 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.30-1
- Update to 0.30

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.20-5
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.20-4
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.20-3
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Dec 22 2008 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 0.20-1
- Specfile autogenerated by cpanspec 1.77.
