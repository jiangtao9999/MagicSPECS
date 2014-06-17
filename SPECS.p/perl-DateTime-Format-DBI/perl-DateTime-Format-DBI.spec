Name:           perl-DateTime-Format-DBI
Version:        0.040
Release:        16%{?dist}
Summary:        Find a parser class for a database connection
License:        GPL+ or Artistic 
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/DateTime-Format-DBI/
Source0:        http://www.cpan.org/authors/id/C/CF/CFAERBER/DateTime-Format-DBI-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

BuildRequires:  perl(DateTime)            >= 0.1
BuildRequires:  perl(DBI)                 >= 1.21
BuildRequires:  perl(ExtUtils::MakeMaker)
# test
BuildRequires:  perl(DateTime::Format::SQLite)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)

# require the dbd-specific datetime formats, so this "just works" the way we
# expect it to.
Requires:       perl(DateTime::Format::MySQL)
Requires:       perl(DateTime::Format::Pg)
Requires:       perl(DateTime::Format::DB2)

%description
This module finds a DateTime::Format::* class that is suitable for the use
with a given DBI connection (and DBD::* driver).

Note that this is most useful if you actually have the DateTime::Format::*
class for your particular database(s) installed!  See, e.g.,
perl-DateTime-MySQL, perl-DateTime-Oracle, perl-DateTime-DB2, etc.

%prep
%setup -q -n DateTime-Format-DBI-%{version}

for i in LICENSE README lib/DateTime/Format/DBI.pm ; do
    
    # correct UTF-8 wonkiness
    cat $i | iconv -f ISO-8859-1 -t UTF-8 > foo
    mv foo $i
done

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
%defattr(-,root,root,-)
%doc Changes LICENSE README t/
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 0.040-16
- 为 Magic 3.0 重建

* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 0.040-15
- 为 Magic 3.0 重建

* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 0.040-14
- 为 Magic 3.0 重建

* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 0.040-13
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.040-12
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.040-11
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.040-10
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.040-9
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.040-8
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.040-7
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 0.040-6
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.040-5
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.040-4
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.040-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.040-2
- Perl mass rebuild

* Mon Mar 14 2011 Iain Arnell <iarnell@gmail.com> 0.040-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.032-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.032-6
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.032-5
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.032-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.032-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.032-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Oct 25 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.032-1
- update to 0.032
- drop more_dbds.patch -- incorperated upstream

* Wed Sep 03 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.031-4
- add the dbd-specific DateTime::Format's as requires.  Makes sense that
  installing this package should have stuff "just work".
- patch for additional DBD support (just DB2 at this point)

* Thu Jul 24 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.031-3
- bump

* Tue Jul 22 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.031-2
- override perl's auto-prov.  see RH BZ#456357

* Wed Jul 16 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.031-1
- Specfile autogenerated by cpanspec 1.74.
