Name:           perl-autobox-dump
Version:        20090426.1746
Release:        13%{?dist}
Summary:        Human/perl readable strings from the results of an EXPR
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/autobox-dump/
Source0:        http://www.cpan.org/modules/by-module/autobox/autobox-dump-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(autobox)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
The autobox::dump pragma adds, via the autobox pragma, a method to normal
expression (such as scalars, arrays, hashes, math, literals, etc.) that
produces a human/perl readable representation of the value of that expression.

%prep
%setup -q -n autobox-dump-%{version}

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
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 20090426.1746-13
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 20090426.1746-12
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 20090426.1746-11
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 20090426.1746-10
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 20090426.1746-9
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 20090426.1746-8
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 20090426.1746-7
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 20090426.1746-6
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 20090426.1746-5
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 20090426.1746-4
- 为 Magic 3.0 重建

* Sat Jan 28 2012 Liu Di <liudidi@gmail.com> - 20090426.1746-3
- 为 Magic 3.0 重建

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090426.1746-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Aug 11 2011 Iain Arnell <iarnell@gmail.com> 20090426.1746-1
- Specfile autogenerated by cpanspec 1.78.
