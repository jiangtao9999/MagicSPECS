Name:           perl-DBD-Mock
Version:        1.45
Release:        1%{?dist}
Summary:        Mock database driver for testing
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/DBD-Mock/
Source0:        http://www.cpan.org/modules/by-module/DBD/DBD-Mock-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Module::Build)
# Run-time
BuildRequires:  perl(constant)
BuildRequires:  perl(DBI) >= 1.3
# Tests
BuildRequires:  perl(Test::More) >= 0.47
BuildRequires:  perl(Test::Exception) >= 0.31
# Optional tests
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(DBI) >= 1.3

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude|%__requires_exclude|}^perl\\(DBI\\)$

%description
Testing with databases can be tricky. If you are developing a system
married to a single database then you can make some assumptions about your
environment and ask the user to provide relevant connection information.
But if you need to test a framework that uses DBI, particularly a framework
that uses different types of persistence schemes, then it may be more
useful to simply verify what the framework is trying to do -- ensure the
right SQL is generated and that the correct parameters are bound. DBD::Mock
makes it easy to just modify your configuration (presumably held outside
your code) and just use it instead of DBD::Foo (like DBD::Pg or DBD::mysql)
in your framework.

%prep
%setup -q -n DBD-Mock-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Oct 22 2012 Petr Pisar <ppisar@redhat.com> - 1.45-1
- 1.45 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.43-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 16 2012 Petr Pisar <ppisar@redhat.com> - 1.43-2
- Perl 5.16 rebuild

* Wed Jan 25 2012 Petr Pisar <ppisar@redhat.com> - 1.43-1
- 1.43 bump

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.39-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.39-8
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.39-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.39-6
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.39-5
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.39-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.39-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.39-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 11 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.39-1
- update to 1.39

* Sat Oct 25 2008 Chris Weyl <cweyl@alumni.drew.edu> 1.37-1
- update to 1.37

* Thu Mar  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.36-2
- rebuild for new perl

* Tue Oct 23 2007 Chris Weyl <cweyl@alumni.drew.edu> 1.36-1
- update to 1.36
- license tag: GPL -> GPL+

* Thu Aug 09 2007 Chris Weyl <cweyl@alumni.drew.edu> 1.35-1
- update to 1.35
- add t/ to doc
- refactor perl br's
- update source url to pull by module, rather than by author

* Mon Mar 19 2007 Chris Weyl <cweyl@alumni.drew.edu> 1.34-2
- bump

* Sat Mar 10 2007 Chris Weyl <cweyl@alumni.drew.edu> 1.34-1
- Specfile autogenerated by cpanspec 1.70.
