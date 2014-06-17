Name:           perl-Hash-FieldHash
Version:        0.12
Release:        7%{?dist}
Summary:        Lightweight field hash implementation
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Hash-FieldHash/
Source0:        http://www.cpan.org/modules/by-module/Hash/Hash-FieldHash-%{version}.tar.gz
BuildRequires:  perl(Devel::PPPort) >= 3.19
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::ParseXS) >= 2.21
BuildRequires:  perl(parent) >= 0.221
BuildRequires:  perl(Test::LeakTrace)
BuildRequires:  perl(Test::More) >= 0.62
BuildRequires:  perl(XSLoader) >= 0.02
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
Hash::FieldHash provides the field hash mechanism which supports the inside-
out technique.

%prep
%setup -q -n Hash-FieldHash-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check


%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Hash*
%{_mandir}/man3/*

%changelog
* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.12-7
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.12-6
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.12-5
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.12-4
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.12-3
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct 23 2011 Iain Arnell <iarnell@gmail.com> 0.12-1
- update to latest upstream version

* Tue Aug 23 2011 Iain Arnell <iarnell@gmail.com> 0.10-2
- drop unnecessary explicit buildrequires

* Thu Aug 11 2011 Iain Arnell <iarnell@gmail.com> 0.10-1
- Specfile autogenerated by cpanspec 1.78.
