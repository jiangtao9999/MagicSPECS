Name:           perl-String-Random
Version:        0.28
Release:        5%{?dist}
Summary:        Perl module to generate random strings based on a pattern
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/String-Random/
Source0:        http://search.cpan.org/CPAN/authors/id/S/SH/SHLOMIF/String-Random-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
This module makes it trivial to generate random strings.


%prep
%setup -q -n String-Random-%{version}


%build
%{__perl} Build.PL installdirs=vendor
./Build


%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*


%check
./Build test


%files
%doc Changes README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Tue Nov 03 2015 Liu Di <liudidi@gmail.com> - 0.28-5
- 为 Magic 3.0 重建

* Thu Sep 17 2015 Liu Di <liudidi@gmail.com> - 0.28-4
- 为 Magic 3.0 重建

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.28-2
- Perl 5.22 rebuild

* Sun Jan 25 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.28-1
- Update to 0.28

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.26-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Feb 02 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.26-1
- Update to 0.26

* Sun Dec 29 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.25-1
- Update to 0.25

* Sun Dec 08 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.24-1
- Update to 0.24

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.22-16
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Oct 28 2012 Emmanuel Seyman <emmanuel@seyman.fr> - 0.22-14
- Fix upstream URL
- Clean up spec file
- Add perl default filter

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 0.22-12
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.22-10
- Perl mass rebuild

* Thu Jun 09 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.22-9
- Perl 5.14 mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.22-7
- 661697 rebuild for fixing problems with vendorach/lib

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.22-6
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.22-5
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jun 23 2008 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> 0.22-2
- Add missing Test::More dependency, thanks to Parag AN

* Wed Jun 11 2008 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> 0.22-1
- Specfile autogenerated by cpanspec 1.75.
