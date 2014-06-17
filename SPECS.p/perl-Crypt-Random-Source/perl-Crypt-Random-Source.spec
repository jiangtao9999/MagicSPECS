Name:           perl-Crypt-Random-Source
Version:        0.07
Release:        8%{?dist}
Summary:        Get weak or strong random data from pluggable sources
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Crypt-Random-Source/
Source0:        http://www.cpan.org/authors/id/N/NU/NUFFIN/Crypt-Random-Source-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(Any::Moose)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Module::Find)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(ok)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
This module provides implementations for a number of byte oriented sources
of random data.

%prep
%setup -q -n Crypt-Random-Source-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check


%files
%defattr(-,root,root,-)
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.07-8
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 0.07-7
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.07-6
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.07-5
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.07-3
- Perl mass rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.07-2
- Perl mass rebuild

* Mon Feb 14 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 0.07-1
- Specfile autogenerated by cpanspec 1.78.
