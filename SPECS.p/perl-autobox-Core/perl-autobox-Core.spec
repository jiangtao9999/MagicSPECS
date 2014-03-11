Name:           perl-autobox-Core
Version:        1.2
Release:        7%{?dist}
Summary:        Core functions exposed as methods in primitive types
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/autobox-Core/
Source0:        http://www.cpan.org/modules/by-module/autobox/autobox-Core-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(autobox) >= 0.11
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
The autobox module lets you call methods on primitive datatypes such as
scalars and arrays.

%prep
%setup -q -n autobox-Core-%{version}

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
%doc README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 1.2-7
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 1.2-6
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 1.2-5
- 为 Magic 3.0 重建

* Sat Jan 28 2012 Liu Di <liudidi@gmail.com> - 1.2-4
- 为 Magic 3.0 重建

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Aug 14 2011 Iain Arnell <iarnell@gmail.com> 1.2-2
- remove explicit requires perl(autobox)

* Thu Aug 11 2011 Iain Arnell <iarnell@gmail.com> 1.2-1
- Specfile autogenerated by cpanspec 1.78.
