Name:           perl-Math-Base36
Version:	0.14
Release:	1%{?dist}
Summary:        Encoding and decoding of base36 strings
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Math-Base36/
Source0:        http://www.cpan.org/authors/id/B/BR/BRICAS/Math-Base36-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
This module converts to and from Base36 numbers (0..9 - A..Z)

%prep
%setup -q -n Math-Base36-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check


%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.14-1
- 更新到 0.14

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.09-8
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.09-7
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.09-6
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.09-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.09-2
- 661697 rebuild for fixing problems with vendorach/lib

* Thu Dec 09 2010 Iain Arnell <iarnell@gmail.com> 0.09-1
- update to latest upstream version

* Mon Sep 06 2010 Iain Arnell <iarnell@gmail.com> 0.07-2
- don't BuildRequire perl itself

* Thu Sep 02 2010 Iain Arnell <iarnell@gmail.com> 0.07-1
- Specfile autogenerated by cpanspec 1.78.
