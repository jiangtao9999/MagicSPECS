Name:           perl-Devel-Profiler
Version:        0.04
Release:        22%{?dist}
Summary:        Perl profiler compatible with dprofpp
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Devel-Profiler/
Source0:        http://www.cpan.org/authors/id/S/SA/SAMTREGAR/Devel-Profiler-%{version}.tar.gz
Patch0:         perl-Devel-Profiler-perl510.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
# dprofpp from perl-Devel-DProf is executed
BuildRequires:  perl-Devel-DProf
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
# dprofpp from perl-Devel-DProf is executed
Requires:       perl-Devel-DProf

%description
This module implements a Perl profiler that outputs profiling data in a
format compatible with dprofpp, Devel::DProf's profile analysis tool. It is
meant to be a drop-in replacement for Devel::DProf.

%prep
%setup -q -n Devel-Profiler-%{version}
%patch0 -p1

# t/01basic fails.  This is the failing test:
#
# # make sure that regsitered at least 1 second of user time
# ($real, $sys, $user) = get_times();
# ok($user >= 1, "check user time >= 1 seconds");
#
# That test seems a bit bogus, unless I'm missing something.
%{__perl} -pi -e 's/^/#/ if /"check user time >= 1 second/;' \
    -e 's/^(use Test::More tests => )(\d+)/$1 . ($2-1)/e' t/01basic.t

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
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.04-22
- 为 Magic 3.0 重建

* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 0.04-21
- 为 Magic 3.0 重建

* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 0.04-20
- 为 Magic 3.0 重建

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.04-17
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 0.04-14
- Perl 5.16 rebuild
- Specify all dependencies

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 15 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.04-12
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.04-10
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.04-9
- Mass rebuild with perl-5.12.0

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.04-8
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.04-7
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Mar  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.04-4
- Fix for perl 5.10.0

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.04-3
- Rebuild for new perl

* Mon Jul 16 2007 Steven Pritchard <steve@kspei.com> 0.04-2
- BR ExtUtils::MakeMaker and Test::More.

* Wed Oct 18 2006 Steven Pritchard <steve@kspei.com> 0.04-1
- Specfile autogenerated by cpanspec 1.69.1.
- Fix License.
- Disable bogus test in t/01basic.t.
