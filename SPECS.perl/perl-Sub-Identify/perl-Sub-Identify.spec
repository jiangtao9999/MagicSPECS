Name:		perl-Sub-Identify
Version:	0.12
Release:	1%{?dist}
Summary:	Retrieve names of code references
License:	GPL+ or Artistic
Group:		Development/Libraries
URL:		http://search.cpan.org/dist/Sub-Identify/
Source0:	http://search.cpan.org/CPAN/authors/id/R/RG/RGARCIA/Sub-Identify-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(id -nu)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Pod)
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

# Don't provide private perl libs
%{?perl_default_filter}

%description
Sub::Identify allows you to retrieve the real name of code references. For
this, it uses Perl's introspection mechanism, provided by the B module.

%prep
%setup -q -n Sub-Identify-%{version}

# Fix script interpreters
perl -pi -e 's|^#!perl|#!/usr/bin/perl|' t/*

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
%{_fixperms} %{buildroot}

%check


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc Changes t/
%{perl_vendorarch}/auto/Sub/
%{perl_vendorarch}/Sub/
%{_mandir}/man3/Sub::Identify.3pm*

%changelog
* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.12-1
- 更新到 0.12

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.04-17
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.04-16
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.04-14
- Perl 5.16 rebuild

* Mon Mar  5 2012 Paul Howarth <paul@city-fan.org> - 0.04-13
- Use %%{optflags}
- BR: perl(Exporter) and perl(Test::Pod)
- Make %%files list more explicit
- Use DESTDIR rather than PERL_INSTALL_ROOT
- No need to remove empty directories from buildroot
- Don't use macros for commands
- Use tabs

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.04-11
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.04-9
- Rebuild to fix problems with vendorarch/lib (#661697)

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.04-8
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.04-7
- Rebuild against perl 5.10.1

* Fri Aug 28 2009 Chris Weyl <cweyl@alumni.drew.edu> - 0.04-6
- Bump

* Thu Aug 27 2009 Chris Weyl <cweyl@alumni.drew.edu> - 0.04-5
- Filtering errant private provides

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 11 2009 Chris Weyl <cweyl@alumni.drew.edu> - 0.04-2
- Aaaand change files to look in the the arch-dependent dirs

* Wed Feb 11 2009 Chris Weyl <cweyl@alumni.drew.edu> - 0.04-1
- Update to 0.04
- Drop buildarch noarch, as we have some XS bits now

* Wed May 28 2008 Chris Weyl <cweyl@alumni.drew.edu> - 0.03-1
- Update to 0.03

* Tue Mar 04 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.02-3
- Rebuild for new perl

* Tue Oct 16 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 0.02-2.2
- Add BR: perl(Test::More)

* Tue Oct 16 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 0.02-2.1
- Correct license tag
- Add BR: perl(ExtUtils::MakeMaker)

* Wed Sep 06 2006 Chris Weyl <cweyl@alumni.drew.edu> - 0.02-2
- Bump

* Tue Sep 05 2006 Chris Weyl <cweyl@alumni.drew.edu> - 0.02-1
- Specfile autogenerated by cpanspec 1.69.1
