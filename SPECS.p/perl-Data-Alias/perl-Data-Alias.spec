Name:           perl-Data-Alias
Version:        1.15
Release:        8%{?dist}
Summary:        Comprehensive set of aliasing operations
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Data-Alias/
Source0:        http://www.cpan.org/authors/id/Z/ZE/ZEFRAM/Data-Alias-%{version}.tar.gz

BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Filter::Util::Call)
BuildRequires:  perl(lib)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
Aliasing is the phenomenon where two different expressions actually refer
to the same thing. Modifying one will modify the other, and if you take a
reference to both, the two values are the same.

%prep
%setup -q -n Data-Alias-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check


%files
%doc README Changes
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Data*
%{_mandir}/man3/*

%changelog
* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.15-8
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 1.15-7
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 1.15-6
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 1.15-5
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 24 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.15-3
- Perl mass rebuild

* Fri Jun 24 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.15-2
- Perl mass rebuild

* Fri Jun 24 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.15-1
- update to 1.15, which fixes issues with systemtap

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.12-2
- Perl mass rebuild

* Thu Apr 14 2011 Marcela Mašláňová <mmaslano@redhat.com> 1.12-1
- Specfile autogenerated by cpanspec 1.79 for new release. This package
  was resurected for 5.12.x

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.07-6
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.07-3
Rebuild for new perl

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.07-2
- Autorebuild for GCC 4.3

* Mon Nov 05 2007 Chris Weyl <cweyl@alumni.drew.edu> 1.07-1
- update to 1.07

* Tue Aug 21 2007 Chris Weyl <cweyl@alumni.drew.edu> 1.06-2
- bump

* Fri Aug 10 2007 Chris Weyl <cweyl@alumni.drew.edu> 1.06-1
- update to 1.06
- license tag: GPL -> GPL+

* Fri Jun 01 2007 Chris Weyl <cweyl@alumni.drew.edu> 1.05-1
- update to 1.05

* Fri May 04 2007 Chris Weyl <cweyl@alumni.drew.edu> 1.04-1
- update to 1.04
- add t/ to %%doc
- perl splittage BR's added

* Mon Mar 19 2007 Chris Weyl <cweyl@alumni.drew.edu> 1.03-1
- update to 1.03

* Mon Feb 19 2007 Chris Weyl <cweyl@alumni.drew.edu> 1.02-1
- update to 1.02

* Tue Oct 03 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.01-1
- update to 1.01

* Thu Aug 31 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.0-3
- bump for mass rebuild

* Thu Aug 17 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.0-2
- bump for build & release

* Wed Aug 16 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.0-1
- Specfile autogenerated by cpanspec 1.68.
- Initial spec file for F-E
