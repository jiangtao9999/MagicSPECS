Name:           perl-Devel-Size
Version:	0.80
Release:	3%{?dist}
Summary:        Perl extension for finding the memory usage of Perl variables
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Devel-Size/

Source0: http://www.cpan.org/modules/by-module/Devel/Devel-Size-%{version}.tar.gz

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# core
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
# cpan
# test
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
# Required by t/warnings.t, but not on CPAN
#BuildRequires:  perl(Test::PerlRun)

%?perl_default_filter

%description
This module figures out the real sizes of Perl variables in bytes. Call
functions with a reference to the variable you want the size of. If the
variable is a plain scalar it returns the size of the scalar. If the
variable is a hash or an array, use a reference when calling.

%prep
%setup -q -n Devel-Size-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc CHANGES t/
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Devel*
%{_mandir}/man3/*

%changelog
* Thu Nov 12 2015 Liu Di <liudidi@gmail.com> - 0.80-3
- 为 Magic 3.0 重建

* Mon Nov 02 2015 Liu Di <liudidi@gmail.com> - 0.80-2
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.80-1
- 更新到 0.80

* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 0.79-5
- 为 Magic 3.0 重建

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.79-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.79-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 20 2013 Petr Pisar <ppisar@redhat.com> - 0.79-2
- Perl 5.18 rebuild

* Tue May 28 2013 Robin Lee <cheeselee@fedoraproject.org> - 0.79-1
- Update to 0.79
- BR: perl(XSLoader)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.78-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Aug 22 2012 Robin Lee <cheeselee@fedoraproject.org> 0.78-1
- Update to 0.78

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.77-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 0.77-3
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.77-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Oct 08 2011 Iain Arnell <iarnell@gmail.com> 0.77-1
- update to latest upstream version
- clean up spec for modern rpmbuild
- use perl_default_filter

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.71-8
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.71-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.71-6
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.71-5
- Mass rebuild with perl-5.12.0

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.71-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.71-3
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.71-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Apr 02 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.71-1
- update to 0.71

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.69-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Mar  4 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.69-1
- update to 0.69

* Tue Mar  4 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.68-4
- rebuild for new perl

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.68-3
- Autorebuild for GCC 4.3

* Tue Aug 21 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.68-2
- bump

* Thu Aug 09 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.68-1
- update to 0.68
- refactor perl BR's

* Thu Mar 29 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.67-1
- update to 0.67

* Sat Mar 10 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.66-1
- update to 0.66 (0.65 update never pushed due to various issues)
- misc spec cleanups
- add br on perl(ExtUtils::MakeMaker) to satisfy any perl/perl-devel split

* Sun Feb 25 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.65-1
- update to 0.65

* Sun Sep 17 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.64-2
- bump

* Wed Aug 16 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.64-1
- Specfile autogenerated by cpanspec 1.68.
