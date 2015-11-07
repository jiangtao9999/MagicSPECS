Name:           perl-File-ShareDir-PAR
Version:        0.06
Release:        22%{?dist}
Summary:        File::ShareDir with PAR support
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/File-ShareDir-PAR/
Source0:        http://www.cpan.org/authors/id/S/SM/SMUELLER/File-ShareDir-PAR-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(Class::Inspector) >= 1.12
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::ShareDir) >= 1.02
BuildRequires:  perl(PAR) >= 0.989
BuildRequires:  perl(Test::More) >= 0.47
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(File::ShareDir) >= 1.02
Requires:       perl(PAR) >= 0.989

# RPM 4.8 style:
%filter_from_requires /perl(File::ShareDir)$/d
%filter_setup
# RPM 4.9 style
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}perl\\(File::ShareDir\\)$

%description
File::ShareDir::PAR provides the same functionality as File::ShareDir but
tries hard to be compatible with PAR packaged applications.

%prep
%setup -q -n File-ShareDir-PAR-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
rm -rf $RPM_BUILD_ROOT/blib/lib/auto/share/dist/File-ShareDir-PAR/
rm -rf $RPM_BUILD_ROOT/blib/lib/auto/share/module/File-ShareDir-PAR/test_file.txt
%{_fixperms} $RPM_BUILD_ROOT/*

%check


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes LICENSE
%{perl_vendorlib}/File/ShareDir
%{perl_vendorlib}/auto/share/*/File-ShareDir-PAR
%{_mandir}/man3/*

%changelog
* Mon Nov 02 2015 Liu Di <liudidi@gmail.com> - 0.06-22
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.06-21
- 为 Magic 3.0 重建

* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 0.06-20
- 为 Magic 3.0 重建

* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 0.06-19
- 为 Magic 3.0 重建

* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 0.06-18
- 为 Magic 3.0 重建

* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 0.06-17
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.06-16
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.06-15
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.06-14
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.06-13
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.06-12
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.06-11
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 0.06-10
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.06-9
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.06-8
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 25 2011 Petr Pisar <ppisar@redhat.com> - 0.06-6
- RPM 4.9 dependency filtering added

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.06-5
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.06-3
- 661697 rebuild for fixing problems with vendorach/lib

* Wed Sep 15 2010 Petr Pisar <ppisar@redhat.com> - 0.06-2
- Add not autodetected perl(PAR) >= 0.989 (Build)Requires

* Wed Sep 15 2010 Petr Pisar <ppisar@redhat.com> - 0.06-1
- 0.06 bump
- Add versioned perl(File::ShareDir) (Build)Requires as stated by META.yml

* Sat May 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.05-5
- Mass rebuild with perl-5.12.0

* Thu Jan 14 2010 Marcela Mašláňová <mmaslano@redhat.com> - 0.05-4
- fix build problems

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.05-3
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun  3 2009 Marcela Mašláňová <mmaslano@redhat.com> - 0.05-1
- update to the latest upstream

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec 05 2008 Marcela Mašláňová <mmaslano@redhat.com> 0.03-1
- update to 0.03

* Tue Nov 18 2008 Marcela Mašláňová <mmaslano@redhat.com> 0.02-2
- owns correct directories and check provides

* Mon Nov 03 2008 Marcela Mašláňová <mmaslano@redhat.com> 0.02-1
- Specfile autogenerated by cpanspec 1.77.
