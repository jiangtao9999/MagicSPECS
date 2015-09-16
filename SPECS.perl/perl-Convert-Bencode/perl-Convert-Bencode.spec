Name:           perl-Convert-Bencode
Version:        1.03
Release:        9%{?dist}
Summary:        Functions for converting to/from bencoded strings
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Convert-Bencode/
Source0:        http://www.cpan.org/authors/id/O/OR/ORCLEV/Convert-Bencode-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More) >= 0.45
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
This module provides two functions, bencode and bdecode, which encode and
decode bencoded strings respectively.

%prep
%setup -q -n Convert-Bencode-%{version}

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
%doc Changes LICENSE README Todo
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 1.03-9
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.03-8
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 1.03-7
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 1.03-6
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 1.03-5
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.03-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 15 2011 Iain Arnell <iarnell@gmail.com> 1.03-1
- Specfile autogenerated by cpanspec 1.78.
