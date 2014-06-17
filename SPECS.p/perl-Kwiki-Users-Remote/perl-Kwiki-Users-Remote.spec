Name:           perl-Kwiki-Users-Remote
Version:        0.04
Release:        27%{?dist}
Summary:        Automatically set Kwiki user name from HTTP authentication
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Kwiki-Users-Remote/
Source0:        http://www.cpan.org/authors/id/I/IA/IAN/Kwiki-Users-Remote-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Kwiki) >= 0.32
BuildRequires:  perl(Kwiki::UserName) >= 0.14
BuildRequires:  perl(Kwiki::Users)
# For improved tests
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
BuildRequires:  perl(Test::Pod) >= 1.14

Requires:       perl(Kwiki) >= 0.32
Requires:       perl(Kwiki::UserName) >= 0.14
Requires:       perl(Kwiki::Users)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# RPM 4.8 style
%{?filter_setup:
%filter_from_requires /^perl(mixin)/d
%{?perl_default_filter}
}
# RPM 4.9 style
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(mixin\\)$

%description
When using HTTP authentication for your Kwiki, use this module to
automatically set the user's name from the username they logged in with.
This name will appear in any Recent Changes listing.

%prep
%setup -q -n Kwiki-Users-Remote-%{version}

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
rm -f debug*.list


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 0.04-27
- 为 Magic 3.0 重建

* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 0.04-26
- 为 Magic 3.0 重建

* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 0.04-25
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.04-24
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.04-23
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.04-22
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.04-21
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.04-20
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.04-19
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.04-18
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.04-17
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 26 2011 Petr Sabata <contyk@redhat.com> - 0.04-15
- Add RPM 4.9 style filters

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.04-14
- Perl mass rebuild

* Thu Feb 17 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.04-13
- Switch to using perl-filters/Abandon filter-requires.sh
  (Work around broken deps caused by rpm dep-tracker changes).

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.04-11
- 661697 rebuild for fixing problems with vendorach/lib

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.04-10
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.04-9
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.04-6
Rebuild for new perl

* Wed Jan 09 2008 Ralf Corsépius <rc040203@freenet.de> 0.04-5
- Update License tag.
- BR: perl(Test::More) (BZ 419631).
- BR: perl(Test::Pod), perl(Test::Pod::Coverage).

* Wed Apr 18 2007 Steven Pritchard <steve@kspei.com> 0.04-4
- Use fixperms macro instead of our own chmod incantation.
- BR ExtUtils::MakeMaker.

* Tue Sep 05 2006 Steven Pritchard <steve@kspei.com> 0.04-3
- Fix find option order.
- Improve description and Summary slightly.

* Fri Mar 10 2006 Steven Pritchard <steve@kspei.com> 0.04-2
- Cleanup.

* Mon Feb 27 2006 Steven Pritchard <steve@kspei.com> 0.04-1
- Specfile autogenerated.
- Drop auto-detected explicit BR: perl.
- Improve description.
- Remove debug*.list so "" works.
- Filter out perl(mixin) dependency.
