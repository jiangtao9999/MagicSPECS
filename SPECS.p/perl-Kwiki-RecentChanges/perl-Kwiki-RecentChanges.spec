Name:           perl-Kwiki-RecentChanges
Version:        0.14
Release:        29%{?dist}
Summary:        Kwiki Recent Changes Plugin
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Kwiki-RecentChanges/
Source0:        http://www.cpan.org/authors/id/G/GU/GUGOD/Kwiki-RecentChanges-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::All)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Kwiki) >= 0.37
Requires:       perl(Kwiki) >= 0.37
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# RPM 4.8 style
%{?filter_setup:
%filter_from_requires /^perl(mixin)/d
%{?perl_default_filter}
}
# RPM 4.9 style
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(mixin\\)$

%description
Kwiki Recent Changes plugin.

%prep
%setup -q -n Kwiki-RecentChanges-%{version}

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
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 0.14-29
- 为 Magic 3.0 重建

* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 0.14-28
- 为 Magic 3.0 重建

* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 0.14-27
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.14-26
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.14-25
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.14-24
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.14-23
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.14-22
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.14-21
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.14-20
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.14-19
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 26 2011 Petr Sabata <contyk@redhat.com> - 0.14-17
- Add RPM 4.9 style filters

* Fri Jul 22 2011 Petr Sabata <contyk@redhat.com> - 0.14-16
- BuildRequire IO::All

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.14-15
- Perl mass rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.14-14
- Perl mass rebuild

* Thu Feb 17 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.14-13
- Switch to using perl-filters/Abandon filter-requires.sh
  (Work around broken deps caused by rpm dep-tracker changes).

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.14-11
- 661697 rebuild for fixing problems with vendorach/lib

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.14-10
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.14-9
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.14-5
Rebuild for new perl

* Wed Jan 09 2008 Ralf Corsépius <rc040203@freenet.de> 0.14-4
- Update License-tag.
- BR: perl(Test::More) (BZ 419631).

* Wed Apr 18 2007 Steven Pritchard <steve@kspei.com> 0.14-3
- Use fixperms macro instead of our own chmod incantation.
- BR ExtUtils::MakeMaker.

* Wed Sep 13 2006 Steven Pritchard <steve@kspei.com> 0.14-2
- Fix find option order.

* Fri Apr 07 2006 Steven Pritchard <steve@kspei.com> 0.14-1
- Upgrade to 0.14.

* Fri Mar 10 2006 Steven Pritchard <steve@kspei.com> 0.13-3
- Cleanup.

* Mon Feb 27 2006 Steven Pritchard <steve@kspei.com> 0.13-2
- Drop explicit BR: perl.
- Filter perl(mixin) dependency.

* Thu Dec 29 2005 Steven Pritchard <steve@kspei.com> 0.13-1
- Specfile autogenerated.
