Name:           perl-Class-Unload
Version:	0.09
Release:	1%{?dist}
Summary:        Unload given Class
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Class-Unload/
Source0:        http://www.cpan.org/authors/id/I/IL/ILMARI/Class-Unload-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl >= 0:5.005
BuildRequires:  perl(Class::Inspector)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.31
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Unloads the given class by clearing out its symbol table and removing it
from INC.

%prep
%setup -q -n Class-Unload-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=perl
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check


%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_privlib}/*
%{_mandir}/man3/*

%changelog
* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.09-1
- 更新到 0.09

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.07-8
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 0.07-7
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.07-6
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.07-5
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 28 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.07-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 27 2011 Petr Pisar <ppisar@redhat.com> - 0.07-1
- 0.07 bump
- Install into perl core directory
- Remove BuildRoot stuff

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.06-2
- 661697 rebuild for fixing problems with vendorach/lib

* Tue Jun  8 2010 Petr Pisar <ppisar@redhat.com> - 0.06-1
- 0.06 bump (bug #600628)

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.05-6
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.05-5
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 08 2008 Marcela Mašláňová <mmaslano@redhat.com> 0.05-2
- fix summary and description

* Fri Dec 05 2008 Marcela Mašláňová <mmaslano@redhat.com> 0.05-1
- Specfile autogenerated by cpanspec 1.77.
