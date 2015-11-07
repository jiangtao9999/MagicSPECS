Name:           perl-Convert-Binary-C
Version:	0.77
Release:	2%{?dist}
Summary:        Binary data conversion using C types
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Convert-Binary-C/
Source0:        http://www.cpan.org/modules/by-module/Convert/Convert-Binary-C-%{version}.tar.gz
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Convert::Binary::C is a preprocessor and parser for C type definitions. It
is highly configurable and supports arbitrarily complex data structures.
Its object-oriented interface has pack and unpack methods that act as
replacements for Perl's pack and unpack and allow to use C types instead of
a string representation of the data structure for conversion of binary data
from and to Perl's complex data structures.

%prep
%setup -q -n Convert-Binary-C-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check


%files
%doc Changes README TODO
%{_bindir}/*
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Convert*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Mon Nov 02 2015 Liu Di <liudidi@gmail.com> - 0.77-2
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.77-1
- 更新到 0.77

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.76-6
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 0.76-5
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.76-4
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.76-3
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.76-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Iain Arnell <iarnell@gmail.com> 0.76-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.74-7
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.74-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.74-5
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.74-4
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.74-3
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.74-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May  5 2009 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.74-1
- Update to latest upstream (0.74)
- Drop GCC 4.4 patch (fixed upstream)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.71-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb  8 2009 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.71-2
- Add patch to fix #elif directives for new GCC 4.4

* Wed Jun  4 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.71-1
- Update to latest upstream (0.71)

* Mon Mar  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.70-5
- rebuild for new perl (again)

* Sat Feb 23 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.70-4
- Bump release to fix koji problem that prevented tagging the previous
  (correct) build.

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.70-3
- Autorebuild for GCC 4.3

* Fri Feb  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.70-2
- rebuild for new perl

* Sun Jan  6 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.70-1
- Update to latest upstream (0.70)

* Thu Aug 23 2007 Alex Lancaster <alexlan[AT]fedoraproject org> 0.68-2
- License tag to GPL+ or Artistic as per new guidelines.

* Sat Aug 18 2007 Alex Lancaster <alexlan[AT]fedoraproject org> 0.68-1
- Update to latest upstream

* Mon Apr 02 2007 Alex Lancaster <alexlan[AT]fedoraproject org> 0.67-4
- Remove '%{?_smp_mflags}', package does not support parallel make.

* Thu Mar 29 2007 Alex Lancaster <alexlan[AT]fedoraproject org> 0.67-3
- Add BuildRequires:  perl(Test::Pod), perl(Test::Pod::Coverage)

* Tue Mar 27 2007 Alex Lancaster <alexlan[AT]fedoraproject org> 0.67-2
- Add perl(ExtUtils::MakeMaker) BR.

* Fri Mar 23 2007 Alex Lancaster <alexlan[AT]fedoraproject org> 0.67-1
- Specfile autogenerated by cpanspec 1.69.1.
