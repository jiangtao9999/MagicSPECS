Name:           perl-URI-Find-Simple
Version:        1.03
Release:        13%{?dist}
Summary:        Simple interface to URI::Find
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/URI-Find-Simple/
Source0:        http://www.cpan.org/authors/id/T/TO/TOMI/URI-Find-Simple-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(lib)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI::Find)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
URI::Find is all very well, but sometimes you just want a list of the links
in a given piece of text, or you want to change all the URLs in some text
somehow, and don't want to mess with callback interfaces.

This module uses URI::Find, but hides the callback interface, providing two
functions - one to list all the uris, and one to change all the uris.

%prep
%setup -q -n URI-Find-Simple-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} %{buildroot}/*

%check


%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 1.03-13
- 为 Magic 3.0 重建

* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 1.03-12
- 为 Magic 3.0 重建

* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 1.03-11
- 为 Magic 3.0 重建

* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 1.03-10
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 1.03-9
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 1.03-8
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.03-7
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.03-6
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.03-5
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 1.03-4
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 1.03-2
- Perl 5.16 rebuild

* Fri Jan 20 2012 Petr Šabata <contyk@redhat.com> 1.03-1
- Specfile autogenerated by cpanspec 1.78.
