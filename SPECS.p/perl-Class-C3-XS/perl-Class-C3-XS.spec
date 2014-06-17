Name:		perl-Class-C3-XS
Version:	0.13
Release:	12%{?dist}
Summary:	XS speedups for Class::C3
License:	GPL+ or Artistic
Group:		Development/Libraries
URL:		http://search.cpan.org/dist/Class-C3-XS/
Source0:	http://search.cpan.org/CPAN/authors/id/F/FL/FLORA/Class-C3-XS-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(id -nu)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Sub::Name)
BuildRequires:	perl(Test::More) >= 0.47
BuildRequires:	perl(Test::Pod)
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

# Filter bogus requires/provides
%{?filter_from_requires: %filter_from_requires /^perl(base)$/d}
%{?filter_from_provides: %filter_from_provides /^perl(t::.*)$/d}
%{?perl_default_filter}

%description
This contains XS performance enhancers for Class::C3 version 0.16 and
higher. The main Class::C3 package will use this package automatically if
it can find it. Do not use this package directly, use Class::C3 instead.

%prep
%setup -q -n Class-C3-XS-%{version}

# Filter bogus provides and requires if we don't have %%{perl_default_filter}
%global provfilt /bin/sh -c "%{__perl_provides} | grep -v '^perl(t::'"
%define __perl_provides %{provfilt}
%global reqfilt /bin/sh -c "%{__perl_requires} | grep -Fvx 'perl(base)'"
%define __perl_requires %{reqfilt}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -a -size 0 -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} \; 2>/dev/null
%{_fixperms} %{buildroot}

%check


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc ChangeLog README t/
%{perl_vendorarch}/auto/Class/
%{perl_vendorarch}/Class/
%{_mandir}/man3/Class::C3::XS.3pm*

%changelog
* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.13-12
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 0.13-11
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.13-10
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.13-9
- 为 Magic 3.0 重建

* Wed Jan 18 2012 Paul Howarth <paul@city-fan.org> - 0.13-8
- BR: perl(Sub::Name) for testing
- Make %%files list more explicit
- Filter unwanted requires and provides
- Use DESTDIR rather than PERL_INSTALL_ROOT
- Use tabs

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.13-6
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.13-4
- Rebuild to fix problems with vendorarch/lib (#661697)

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.13-3
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.13-2
- Rebuild against perl 5.10.1

* Sat Sep 26 2009 Chris Weyl <cweyl@alumni.drew.edu> - 0.13-1
- Update filtering
- Auto-update to 0.13 (by cpan-spec-update 0.01)
- Altered br on perl(ExtUtils::MakeMaker) (0 => 6.42)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Apr 02 2009 Chris Weyl <cweyl@alumni.drew.edu> - 0.11-1
- Update to 0.11

* Sat Feb 28 2009 Chris Weyl <cweyl@alumni.drew.edu> - 0.08-6
- Stripping bad provides of private Perl extension libs

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Mar  4 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.08-4
- Rebuild for new perl

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.08-3
- Autorebuild for GCC 4.3

* Tue Aug 21 2007 Chris Weyl <cweyl@alumni.drew.edu> - 0.08-2
- Bump

* Thu Aug 09 2007 Chris Weyl <cweyl@alumni.drew.edu> - 0.08-1
- Update to 0.08

* Thu May 31 2007 Chris Weyl <cweyl@alumni.drew.edu> - 0.06-1
- Update to 0.06

* Sun May 13 2007 Chris Weyl <cweyl@alumni.drew.edu> - 0.04-1
- Update to 0.04

* Wed May 09 2007 Chris Weyl <cweyl@alumni.drew.edu> - 0.03-2
- Bump

* Wed May 09 2007 Chris Weyl <cweyl@alumni.drew.edu> - 0.03-1
- Update to 0.03

* Fri May 04 2007 Chris Weyl <cweyl@alumni.drew.edu> - 0.02-1
- Specfile autogenerated by cpanspec 1.71
