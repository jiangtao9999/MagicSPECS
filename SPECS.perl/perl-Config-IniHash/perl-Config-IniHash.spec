Name:           perl-Config-IniHash
Version:        3.01.01
Release:        8%{?dist}
Summary:        Perl extension for reading and writing INI files
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Config-IniHash/
Source0:        http://www.cpan.org/authors/id/J/JE/JENDA/Config-IniHash-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# core
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
# cpan
BuildRequires:  perl(Hash::Case)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(Hash::WithDefaults) >= 0.04

# not automagically picked up
Requires:       perl(Hash::Case)
Requires:       perl(Hash::WithDefaults) >= 0.04

%{?perl_default_filter}

%description
This module reads and writes INI files.

%prep
%setup -q -n Config-IniHash-%{version}

sed -i 's/\r//' README Changes

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check


%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 3.01.01-8
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 3.01.01-7
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 3.01.01-6
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 3.01.01-5
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 3.01.01-4
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 3.01.01-3
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 3.01.01-2
- 为 Magic 3.0 重建

* Sun Jan 15 2012 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 3.01.01-1
- Update to 3.01.01
- Clean up spec file
- Add perl default filter

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.00.00-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 3.00.00-9
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.00.00-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 3.00.00-7
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 3.00.00-6
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 3.00.00-5
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.00.00-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.00.00-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Oct 01 2008 Chris Weyl <cweyl@alumni.drew.edu> 3.00.00-2
- add requires on Hash::Case, Hash::WithDefaults (rhbz#465164)

* Mon Sep 08 2008 Chris Weyl <cweyl@alumni.drew.edu> 3.00.00-1
- update to 3.00.00

* Wed Mar  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.9.0-3
- rebuild for new perl

* Fri Apr 27 2007 Chris Weyl <cweyl@alumni.drew.edu> 2.9.0-2
- bump

* Thu Apr 26 2007 Chris Weyl <cweyl@alumni.drew.edu> 2.9.0-1
- update to 2.9.0 (?!)

* Thu Apr 26 2007 Chris Weyl <cweyl@alumni.drew.edu> 2.8-2
- add missing BR on perl(IO::Scalar)

* Wed Apr 18 2007 Chris Weyl <cweyl@alumni.drew.edu> 2.8-1
- Specfile autogenerated by cpanspec 1.69.1.
