# MRO is part of the Perl core since 5.9.5
%global mro_in_core %(perl -e 'print $] > 5.009005 ? 1 : 0;')

Name:		perl-MRO-Compat
Version:	0.12
Release:	2%{?dist}
Summary:	Mro::* interface compatibility for Perls < 5.9.5
License:	GPL+ or Artistic
Group:		Development/Libraries
URL:		http://search.cpan.org/dist/MRO-Compat/
Source0:        http://search.cpan.org/CPAN/authors/id/B/BO/BOBTFISH/MRO-Compat-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(id -nu)
BuildArch:	noarch
# Build
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.42
# Module
%if ! %{mro_in_core}
BuildRequires:	perl(Class::C3) >= 0.20
BuildRequires:	perl(Class::C3::XS) >= 0.08
%endif
# Test
BuildRequires:	perl(Test::More) >= 0.47
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)
# Runtime
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
%if ! %{mro_in_core}
Requires:	perl(Class::C3) >= 0.20
Requires:	perl(Class::C3::XS) >= 0.08
%endif

%description
The "mro" namespace provides several utilities for dealing with method
resolution order and method caching in general in Perl 5.9.5 and higher.
This module provides those interfaces for earlier versions of Perl (back
to 5.6.0 anyways).

It is a harmless no-op to use this module on 5.9.5+. That is to say,
code which properly uses MRO::Compat will work unmodified on both older
Perls and 5.9.5+.

If you're writing a piece of software that would like to use the parts
of 5.9.5+'s mro:: interfaces that are supported here, and you want
compatibility with older Perls, this is the module for you.

%prep
%setup -q -n MRO-Compat-%{version}

# Fix script interpreter
perl -pi -e 's|^#!./perl|#!/usr/bin/perl|' t/15pkg_gen.t

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} \; 2>/dev/null
%{_fixperms} %{buildroot}

%check


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc ChangeLog README t/
%{perl_vendorlib}/MRO/
%{_mandir}/man3/MRO::Compat.3pm*

%changelog
* Tue Nov 03 2015 Liu Di <liudidi@gmail.com> - 0.12-2
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.12-1
- 更新到 0.12

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.11-13
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.11-12
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 0.11-10
- Perl 5.16 rebuild

* Thu Jan 26 2012 Paul Howarth <paul@city-fan.org> - 0.11-9
- Spec clean-up:
  - Only require Class::C3 with perl < 5.9.5
  - Require Class::C3::XS for performance and consistency, but only with
    perl < 5.9.5
  - Use DESTDIR rather than PERL_INSTALL_ROOT
  - Make %%files list more explicit
  - Classify buildreqs by build/module/test
  - Don't use macros for commands
  - Use tabs

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.11-7
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.11-5
- Rebuild to fix problems with vendorarch/lib (#661697)

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.11-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.11-3
- Rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 02 2009 Chris Weyl <cweyl@alumni.drew.edu> - 0.11-1
- Auto-update to 0.11 (by cpan-spec-update 0.01)
- Altered br on perl(ExtUtils::MakeMaker) (0 => 6.42)
- Altered br on perl(Class::C3) (0.19 => 0.20)

* Thu Apr 02 2009 Chris Weyl <cweyl@alumni.drew.edu> - 0.10-1
- Update to 0.10

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jun 28 2008 Chris Weyl <cweyl@alumni.drew.edu> - 0.09
- Update to 0.09

* Wed May 28 2008 Chris Weyl <cweyl@alumni.drew.edu> - 0.07-1
- Update to 0.07

* Wed Mar 05 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.05-6
- Rebuild for new perl

* Thu Dec 06 2007 Chris Weyl <cweyl@alumni.drew.edu> - 0.05-5
- Bump

* Wed Dec 05 2007 Chris Weyl <cweyl@alumni.drew.edu> - 0.05-4
- Update INstall -> install

* Wed Dec 05 2007 Chris Weyl <cweyl@alumni.drew.edu> - 0.05-3
- Add Test::Pod deps

* Tue Dec 04 2007 Chris Weyl <cweyl@alumni.drew.edu> - 0.05-2
- Make Class::C3 dep explicit

* Tue Sep 18 2007 Chris Weyl <cweyl@alumni.drew.edu> - 0.05-1
- Specfile autogenerated by cpanspec 1.71
