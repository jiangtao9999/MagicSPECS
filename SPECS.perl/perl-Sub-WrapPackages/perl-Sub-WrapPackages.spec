Name:           perl-Sub-WrapPackages
Version:        2.0
Release:        12%{?dist}
Summary:        Add wrappers around all the subroutines in packages
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Sub-WrapPackages/
Source0:        http://www.cpan.org/authors/id/D/DC/DCANTRELL/Sub-WrapPackages-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(base)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::Caller::IgnoreNamespaces)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Hook::LexWrap)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Sub::Prototype)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}
%global __provides_exclude %{?__provides_exclude}|perl\\(lib\\)

%description
This is mostly a wrapper around Damian Conway's Hook::LexWrap module. This
module allows you to wrap function calls and exits with functions of your
choice.

%prep
%setup -q -n Sub-WrapPackages-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 2.0-12
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 2.0-11
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 2.0-9
- Perl 5.16 rebuild
- Specify all dependencies

* Sun Jan 29 2012 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 2.0-8
- Correctly filter perl(lib)
- Clean up spec file

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 29 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.0-6
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov 26 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 2.0-4
- Reverse the Provides filters so they actually work

* Wed Nov 24 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 2.0-3
- Remove perl(lib) from the Provides set. (#657015)

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.0-2
- Mass rebuild with perl-5.12.0

* Sat Mar 13 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 2.0-1
- Update to 2.0.

* Wed Feb 10 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 1.31-1
- Update to 1.31

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.3-2
- rebuild against perl 5.10.1

* Thu Aug 20 2009 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 1.3-1
- Update to 1.3

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Dec 22 2008 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 1.2-1
- Specfile autogenerated by cpanspec 1.77.
