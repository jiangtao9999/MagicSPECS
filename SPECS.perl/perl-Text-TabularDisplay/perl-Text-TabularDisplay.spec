Name:           perl-Text-TabularDisplay
Version:	1.38
Release:	2%{?dist}
Summary:        Display text in formatted table output
# see TabularDisplay.pm's header
License:        GPLv2
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Text-TabularDisplay/
Source0:        http://www.cpan.org/authors/id/D/DA/DARREN/Text-TabularDisplay-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker) 
BuildRequires:  perl(Test)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
Text::TabularDisplay simplifies displaying textual data in a table. The
output is identical to the columnar display of query results in the mysql
text monitor. For example, this data:

%prep
%setup -q -n Text-TabularDisplay-%{version}
chmod -c -x t/* examples/*

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} %{buildroot}/*

%check
make test

%files
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Nov 03 2015 Liu Di <liudidi@gmail.com> - 1.38-2
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 1.38-1
- 更新到 1.38

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.33-4
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.33-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 09 2012 Petr Pisar <ppisar@redhat.com> - 1.33-2
- Perl 5.16 rebuild

* Mon Jul 09 2012 Petr Šabata <contyk@redhat.com> - 1.33-1
- 1.33 bump

* Thu Jun 28 2012 Petr Pisar <ppisar@redhat.com> - 1.31-2
- Perl 5.16 rebuild

* Fri Jun 22 2012 Petr Šabata <contyk@redhat.com> - 1.31-1
- 1.31 bump

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 1.30-2
- Perl 5.16 rebuild

* Mon Apr 02 2012 Petr Šabata <contyk@redhat.com> - 1.30-1
- 1.30 bump
- Drop command macros

* Mon Jan 16 2012 Petr Šabata <contyk@redhat.com> - 1.28-1
- 1.28 bump
- Spec cleanup

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.22-11
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 23 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.22-9
- 661697 rebuild for fixing problems with vendorach/lib

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.22-8
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 1.22-7
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.22-4
- rebuild for new perl

* Wed May 16 2007 Chris Weyl <cweyl@alumni.drew.edu> 1.22-3
- bump

* Wed May 16 2007 Chris Weyl <cweyl@alumni.drew.edu> 1.22-2
- BR perl(Test), not perl(Test::More)

* Tue May 15 2007 Chris Weyl <cweyl@alumni.drew.edu> 1.22-1
- Specfile autogenerated by cpanspec 1.71.
