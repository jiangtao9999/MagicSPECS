Name:           perl-DateTime-Format-Epoch
Version:	0.16
Release:	2%{?dist}
Summary:        Convert DateTimes to/from epoch seconds
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/DateTime-Format-Epoch/
Source0:        http://www.cpan.org/modules/by-module/DateTime/DateTime-Format-Epoch-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl >= 0:5.00503
BuildRequires:  perl(DateTime) >= 0.31
BuildRequires:  perl(Math::BigInt) >= 1.66
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Params::Validate)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
Requires:       perl(DateTime) >= 0.31
Requires:       perl(Math::BigInt) >= 1.66
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
This module can convert a DateTime object (or any object that can be
converted to a DateTime object) to the number of seconds since a given
epoch. It can also do the reverse.

%prep
%setup -q -n DateTime-Format-Epoch-%{version}

# replace CRLF
find -type f -print0 | xargs -0 sed -i 's/\r$//'

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes LICENSE README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Nov 02 2015 Liu Di <liudidi@gmail.com> - 0.16-2
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.16-1
- 更新到 0.16

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.13-11
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.13-10
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.13-9
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.13-8
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.13-7
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.13-6
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 0.13-5
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.13-4
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.13-3
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Aug 11 2011 Iain Arnell <iarnell@gmail.com> 0.13-1
- Specfile autogenerated by cpanspec 1.78.
