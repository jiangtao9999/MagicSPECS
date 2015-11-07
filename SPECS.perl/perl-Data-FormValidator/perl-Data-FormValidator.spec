Name:           perl-Data-FormValidator
Version:	4.81
Release:	2%{?dist}
Summary:        Validates user input (usually from an HTML form) based on input profile
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Data-FormValidator/
Source0:        http://www.cpan.org/authors/id/M/MA/MARKSTOS/Data-FormValidator-%{version}.tar.gz
# see https://bugzilla.redhat.com/show_bug.cgi?id=712694
# and https://rt.cpan.org/Public/Bug/Display.html?id=61792
Patch0:         cve-2011-2201.patch
BuildArch:      noarch
BuildRequires:  perl(CGI) >= 3.48
BuildRequires:  perl(Date::Calc) >= 5
BuildRequires:  perl(Email::Valid)
BuildRequires:  perl(File::MMagic) >= 1.17
BuildRequires:  perl(Image::Size)
BuildRequires:  perl(MIME::Types) >= 1.005
BuildRequires:  perl(Module::Build) >= 0.38
BuildRequires:  perl(Perl6::Junction) >= 1.1
BuildRequires:  perl(Regexp::Common)
BuildRequires:  perl(Template)
BuildRequires:  perl(Template::Stash)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
# not detected by rpm
Requires:       perl(Date::Calc) >= 5
Requires:       perl(Email::Valid)
Requires:       perl(File::MMagic) >= 1.17
Requires:       perl(Image::Size)
Requires:       perl(Regexp::Common)

%{?perl_default_filter}

%description
Data::FormValidator's main aim is to make input validation expressible in a
simple format.

%prep
%setup -q -n Data-FormValidator-%{version}
%patch0 -p1

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes RELEASE_NOTES
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Nov 02 2015 Liu Di <liudidi@gmail.com> - 4.81-2
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 4.81-1
- 更新到 4.81

* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 4.80-12
- 为 Magic 3.0 重建

* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 4.80-11
- 为 Magic 3.0 重建

* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 4.80-10
- 为 Magic 3.0 重建

* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 4.80-9
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 4.80-8
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 4.80-7
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 4.80-6
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 4.80-5
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 4.80-4
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 4.80-3
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 4.80-2
- 为 Magic 3.0 重建

* Fri Nov 02 2012 Iain Arnell <iarnell@gmail.com> 4.80-1
- update to latest upstream version

* Sun Oct 21 2012 Iain Arnell <iarnell@gmail.com> 4.71-1
- update to latest upstream version

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.70-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 21 2012 Petr Pisar <ppisar@redhat.com> - 4.70-4
- Perl 5.16 rebuild

* Thu May 31 2012 Petr Pisar <ppisar@redhat.com> - 4.70-3
- Round Module::Build version to 2 digits

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.70-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 20 2011 Iain Arnell <iarnell@gmail.com> 4.70-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Sun Aug 28 2011 Iain Arnell <iarnell@gmail.com> 4.66-6
- add patch to resolve CVE-2011-2201

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 4.66-5
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.66-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 4.66-3
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 4.66-2
- Mass rebuild with perl-5.12.0

* Thu Feb 25 2010 Iain Arnell <iarnell@gmail.com> 4.66-1
- update to latest upstream version

* Mon Jan 04 2010 Iain Arnell <iarnell@gmail.com> 4.65-1
- update to latest upstream version
- BR perl(Template), perl(Template::Stash), perl(Test::Pod) for tests

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 4.63-3
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.63-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Feb 28 2009 Iain Arnell <iarnell@gmail.com> 4.63-1
- Specfile autogenerated by cpanspec 1.77.
- remove unnecessary requires
