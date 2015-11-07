Name:           perl-Ace
Version:        1.92
Release:        23%{?dist}
Summary:        Perl module for interfacing with ACE bioinformatics databases
Summary(zh_CN.UTF-8): 提供 ACE 生物信息学数据库接口的 Perl 模块
License:        GPL+ or Artistic
Group:          Development/Libraries
Group(zh_CN.UTF-8): 开发/库
URL:            http://search.cpan.org/dist/AcePerl/
Source0:        http://www.cpan.org/modules/by-module/Ace/AcePerl-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Cache::Cache) >= 1.03
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
AcePerl is a Perl interface for the ACEDB object-oriented database.
Designed specifically for use in genome sequencing projects, ACEDB
provides powerful modeling and management services for biological and
laboratory data.

%description -l zh_CN.UTF-8
提供 ACE 生物信息学数据库接口的 Perl 模块。

%{?perl_default_filter}

%prep
%setup -q -n AcePerl-%{version}

# RPM 4.8 style
%{?filter_setup:
%filter_from_requires /perl(Ace::Browser::LocalSiteDefs)$/d
%filter_setup
}
# RPM 4.9 style
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}perl\\(Ace::Browser::LocalSiteDefs\\)$
# remove all execute bits from the doc stuff and fix interpreter
# so that dependency generator doesn't try to fulfill deps
find examples -type f -exec chmod -x {} 2>/dev/null ';'
find examples -type f -exec sed -i 's#/usr/local/bin/perl#/usr/bin/perl#' {} 2>/dev/null ';'

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" << EOF
1
n
EOF

make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*
magic_rpm_clean.sh

## disable tests because they require network access
%check
%{?_with_check: || :}

%files
%defattr(-,root,root,-)
%doc examples
%doc ChangeLog DISCLAIMER.txt README README.ACEBROWSER
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Mon Nov 02 2015 Liu Di <liudidi@gmail.com> - 1.92-23
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 1.92-22
- 为 Magic 3.0 重建

* Sun Apr 19 2015 Liu Di <liudidi@gmail.com> - 1.92-21
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 1.92-20
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 1.92-19
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.92-18
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.92-17
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.92-16
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 1.92-15
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 1.92-14
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 1.92-13
- 为 Magic 3.0 重建

* Fri Jan 27 2012 Liu Di <liudidi@gmail.com> - 1.92-12
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.92-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 22 2011 Petr Pisar <ppisar@redhat.com> - 1.92-10
- RPM 4.9 dependency filtering added

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.92-9
- Perl mass rebuild

* Tue Feb 15 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.92-8
- clean specfile, use filtering macro

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.92-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 14 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.92-6
- rebuild for fixing problems with vendorach/lib

* Thu Apr 29 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.92-5
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.92-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.92-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.92-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.92-1
- Update to latest upstream (1.92)

* Fri Feb 08 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.91-4
- rebuild for new perl

* Tue Sep 04 2007 Alex Lancaster <alexl@users.sourceforge.net> 1.91-3
- Clarified license terms: GPL+ or Artistic

* Mon Apr 02 2007 Alex Lancaster <alexl@users.sourceforge.net> 1.91-2
- Rename perl-AcePerl to perl-Ace
- Disable tests because they require network access
- Fix URL for source.
- Add examples doc directory

* Fri Mar 30 2007 Alex Lancaster <alexl@users.sourceforge.net> 1.91-1
- Make noarch (not building the C optimizations).
- Remove Requires on Ace::Browser::LocalSiteDefs , do not currently
  install the AceBrowser Apache module
- Specfile autogenerated by cpanspec 1.69.1.
