Name:           perl-DBIx-Class-TimeStamp
Version:        0.14
Release:        18%{?dist}
Summary:        DBIx::Class extension to update and create date and time based fields
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/DBIx-Class-TimeStamp/
Source0:        http://search.cpan.org/CPAN/authors/id/R/RI/RIBASUSHI/DBIx-Class-TimeStamp-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Class::Accessor::Grouped)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Format::MySQL)
BuildRequires:  perl(DateTime::Format::SQLite)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBIx::Class)
BuildRequires:  perl(DBIx::Class::DynamicDefault)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Time::Warp)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
# not picked up automatically
Requires:       perl(DBIx::Class) >= 0.08009
Requires:       perl(DBIx::Class::DynamicDefault) >= 0.03
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
Works in conjunction with InflateColumn::DateTime to automatically set
update and create date and time based fields in a table.

%prep
%setup -q -n DBIx-Class-TimeStamp-%{version}

%build
PERL5_CPANPLUS_IS_RUNNING=1 %{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
TEST_POD=1 

%files
%defattr(-,root,root,-)
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 0.14-18
- 为 Magic 3.0 重建

* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 0.14-17
- 为 Magic 3.0 重建

* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 0.14-16
- 为 Magic 3.0 重建

* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 0.14-15
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.14-14
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.14-13
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.14-12
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.14-11
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.14-10
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.14-9
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 0.14-8
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.14-7
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.14-6
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.14-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.14-2
- 661697 rebuild for fixing problems with vendorach/lib

* Sat Sep 25 2010 Iain Arnell <iarnell@gmail.com> 0.14-1
- update to latest upstream version

* Fri May 28 2010 Iain Arnell <iarnell@gmail.com> 0.13-1
- update to latest upstream
- BR perl(Time::HiRes)
- use perl_default_filter and DESTDIR

* Sat May 08 2010 Iain Arnell <iarnell@gmail.com> 0.12-4
- BR perl(DBD::SQLite)

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.12-3
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.12-2
- rebuild against perl 5.10.1

* Sun Aug 02 2009 Iain Arnell 0.12-1
- Specfile autogenerated by cpanspec 1.78.
