Name:           perl-BZ-Client
Version:	2.0_1
Release:	2%{?dist}
Summary:        A client for the Bugzilla web services API
Summary(zh_CN.UTF-8): Bugzilla 网页服务 API 的客户端
License:        GPL+ or Artistic
Group:          Development/Libraries
Group(zh_CN.UTF-8): 开发/库
URL:            http://search.cpan.org/dist/BZ-Client/
Source0:        http://www.cpan.org/authors/id/D/DJ/DJZORT/BZ-Client-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Format::ISO8601)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(LWP)
BuildRequires:  perl(XML::Parser)
BuildRequires:  perl(XML::Writer)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
This module provides an interface to the Bugzilla web services API.

%description -l zh_CN.UTF-8
Bugzilla 网页服务 API 的客户端。

%prep
%setup -q -n BZ-Client-%{version}
chmod 644 Changes README LICENSE

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
find $RPM_BUILD_ROOT -type f -name '*.pm' -exec chmod -x {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*
magic_rpm_clean.sh

%check


%files
%doc Changes README LICENSE
%{perl_vendorlib}/BZ
%{_mandir}/man3/*

%changelog
* Mon Nov 02 2015 Liu Di <liudidi@gmail.com> - 2.0_1-2
- 更新到 2.0_1

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 1.072-1
- 更新到 1.072

* Thu Apr 30 2015 Liu Di <liudidi@gmail.com> - 1.061-1
- 更新到 1.061

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 1.04-13
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 1.04-12
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.04-11
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.04-10
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.04-9
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.04-8
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 1.04-7
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 1.04-6
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 1.04-5
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 1.04-4
- 为 Magic 3.0 重建

* Sat Jan 28 2012 Liu Di <liudidi@gmail.com> - 1.04-3
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Sep 24 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 1.04-1
- Update to 1.04
- Clean up spec file
- Add perl default filter
- Add perl(DateTime) to the BuildRequires
- Add perl(DateTime::Format::ISO8601) to the BuildRequires

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 1.03-6
- Perl mass rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 1.03-5
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.03-3
- 661697 rebuild for fixing problems with vendorach/lib

* Thu Apr 29 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.03-2
- Mass rebuild with perl-5.12.0

* Fri Feb 05 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 1.03-1
- Update to 1.03
- Fix file permissons

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.02-2
- rebuild against perl 5.10.1

* Tue Aug 11 2009 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 1.02-1
- Specfile autogenerated by cpanspec 1.78.
