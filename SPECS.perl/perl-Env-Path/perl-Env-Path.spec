Name:           perl-Env-Path
Version:	0.19
Release:	1%{?dist}
Summary:        Advanced operations on path variables
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Env-Path/
Source0:        http://www.cpan.org/authors/id/D/DS/DSB/Env-Path-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
Env::Path presents an object-oriented interface to path variables, defined
as that subclass of environment variables which name an ordered list of
filesystem elements separated by a platform-standard separator.

%prep
%setup -q -n Env-Path-%{version}

chmod 0644 examples/Whence
sed -i '1s,#!.*,#!%{__perl},' examples/Whence

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
%doc Changes README examples/Whence
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_mandir}/man1/*
%{_bindir}/*

%changelog
* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.19-1
- 更新到 0.19

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.18-6
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 0.18-5
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.18-4
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.18-3
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 05 2011 Iain Arnell <iarnell@gmail.com> 0.18-1
- Specfile autogenerated by cpanspec 1.79.
