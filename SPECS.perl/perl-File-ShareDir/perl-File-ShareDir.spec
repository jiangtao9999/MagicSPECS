Name:           perl-File-ShareDir
Version:	1.102
Release:	3%{?dist}
Summary:        Locate per-dist and per-module shared files
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/File-ShareDir/
Source0:        http://search.cpan.org/CPAN/authors/id/R/RE/REHSACK/File-ShareDir-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(Class::Inspector) >= 1.12
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires:  perl(Test::More) >= 0.47
Requires:       perl(Class::Inspector) >= 1.12
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude}|perl\\(Class::Inspector\\)$

%description
The intent of File::ShareDir is to provide a companion to Class::Inspector
and File::HomeDir, modules that take a process that is well-known by
advanced Perl developers but gets a little tricky, and make it more
available to the larger Perl community.

%prep
%setup -q -n File-ShareDir-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*
chmod 644 share/sample.txt
chmod 644 share/subdir/sample.txt
rm -rf $RPM_BUILD_ROOT/blib/lib/auto/share/dist/File-ShareDir/
rm -rf $RPM_BUILD_ROOT/blib/lib/auto/share/module/File-ShareDir/test_file.txt

%check
 AUTOMATED_TESTING=1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Nov 02 2015 Liu Di <liudidi@gmail.com> - 1.102-3
- 为 Magic 3.0 重建

* Mon Sep 14 2015 Liu Di <liudidi@gmail.com> - 1.102-2
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 1.102-1
- 更新到 1.102

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.03-9
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 1.03-8
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 1.03-7
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 06 2012 Petr Pisar <ppisar@redhat.com> - 1.03-5
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 28 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.03-3
- Perl mass rebuild
- fix macros

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  2 2011 Petr Sabata <psabata@redhat.com> - 1.03-1
- 1.03 version bump

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.02-2
- 661697 rebuild for fixing problems with vendorach/lib

* Wed Sep 15 2010 Petr Pisar <ppisar@redhat.com> - 1.02-1
- 1.02 bump

* Sat May 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.00-6
- Mass rebuild with perl-5.12.0

* Thu Jan 14 2010 Marcela Mašláňová 1.00-5
- fix build

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.00-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Aug 11 2008 Marcela Mašláňová 1.00-1
- Specfile autogenerated by cpanspec 1.77.
