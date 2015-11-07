Name:           perl-DBIx-Class-EncodedColumn
Version:	0.00013
Release:	2%{?dist}
Summary:        Automatically encode columns
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/DBIx-Class-EncodedColumn/
Source0:        http://search.cpan.org/CPAN/authors/id/W/WR/WREIS/DBIx-Class-EncodedColumn-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Crypt::Eksblowfish::Bcrypt)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBIx::Class) >= 0.06002
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Dir::Self)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(SQL::Translator) >= 0.11002
BuildRequires:  perl(Sub::Name) >= 0.04
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
# undetected
Requires:       perl(DBIx::Class)

%{?perl_default_filter}

%description
This DBIx::Class component can be used to automatically encode a column's
contents whenever the value of that column is set.

%prep
%setup -q -n DBIx-Class-EncodedColumn-%{version}

sed -i -e '/auto_install/d' Makefile.PL

# no Crypt::OpenPGP in Fedora
rm lib/DBIx/Class/EncodedColumn/Crypt/OpenPGP.pm

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check


%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/DBIx/Class/*
%{_mandir}/man3/*

%changelog
* Mon Nov 02 2015 Liu Di <liudidi@gmail.com> - 0.00013-2
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.00013-1
- 更新到 0.00013

* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 0.00011-16
- 为 Magic 3.0 重建

* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 0.00011-15
- 为 Magic 3.0 重建

* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 0.00011-14
- 为 Magic 3.0 重建

* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 0.00011-13
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.00011-12
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.00011-11
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.00011-10
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.00011-9
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.00011-8
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.00011-7
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 0.00011-6
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.00011-5
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.00011-4
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.00011-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.00011-2
- Perl mass rebuild

* Wed Apr 20 2011 Iain Arnell <iarnell@gmail.com> 0.00011-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.00010-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.00010-3
- 661697 rebuild for fixing problems with vendorach/lib

* Sun Aug 29 2010 Iain Arnell <iarnell@gmail.com> 0.00010-2
- disable Module::AutoInstall

* Sun Aug 29 2010 Iain Arnell <iarnell@gmail.com> 0.00010-1
- update to latest upstream
- new BR perl(Crypt::Eksblowfish::Bcrypt)
- new BR perl(Test::Exception)

* Thu May 20 2010 Iain Arnell <iarnell@gmail.com> 0.00009-1
- update to latest upstream

* Sat May 01 2010 Iain Arnell <iarnell@gmail.com> 0.00008-1
- update to latest upstream
- use perl_default_filter and DESTDIR
- BR perl(Dir::Self)

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.00006-2
- Mass rebuild with perl-5.12.0

* Sun Jan 17 2010 Iain Arnell <iarnell@gmail.com> 0.00006-1
- update to latest upstream version

* Mon Jan 11 2010 Iain Arnell <iarnell@gmail.com> 0.00005-3
- fix source0 location (was BADURL)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.00005-2
- rebuild against perl 5.10.1

* Sun Oct 18 2009 Iain Arnell <iarnell@gmail.com> 0.00005-1
- update to latest upstream

* Sat Sep 05 2009 Iain Arnell <iarnell@gmail.com> 0.00004-1
- update to latest upstream (minor documentation fix)

* Wed Sep 02 2009 Iain Arnell <iarnell@gmail.com> 0.00003-1
- update to latest upstream (copyright notice added)
- remove temporary BRs due to BZ #499768

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.00002-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 26 2009 Tom "spot" Callaway <tcallawa@redhat.com> 0.00002-2
- fix duplicate directory ownership (perl-DBIx-Class owns %{perl_vendorlib}/DBIx/Class/)

* Mon May 04 2009 Iain Arnell <iarnell@gmail.com> 0.00002-1
- Specfile autogenerated by cpanspec 1.77.
- Disable support for OpenPGP since it's not available in Fedora
- Additional BRs due to BZ #499768
