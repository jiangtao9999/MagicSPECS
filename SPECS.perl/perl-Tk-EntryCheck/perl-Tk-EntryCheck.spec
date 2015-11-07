Name:           perl-Tk-EntryCheck
Version:        0.04
Release:        7%{?dist}
Summary:        Interface to Tk::Entry for controlling its length and content
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Tk-EntryCheck/
Source0:        http://www.cpan.org/authors/id/S/ST/STRAT/Tk-EntryCheck-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Tk::Derived)
BuildRequires:  perl(Tk::Entry)
# Tests
BuildRequires:  font(:lang=en)
BuildRequires:  perl(Test)
BuildRequires:  perl(Tk)
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  xorg-x11-xinit
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module acts as a little wrapper around Tk::Entry and adds an easy to
use interface to -validate and -validatecommand for controlling length and
content of an entry widget.

%prep
%setup -q -n Tk-EntryCheck-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
xinit /bin/sh -c 'rm -f ok;  && touch ok' -- /usr/bin/Xvfb :666
test -e ok

%files
%doc example CHANGES README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Nov 03 2015 Liu Di <liudidi@gmail.com> - 0.04-7
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.04-6
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.04-5
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.04-4
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.04-2
- Perl 5.16 rebuild

* Wed Feb 22 2012 Petr Pisar <ppisar@redhat.com> 0.04-1
- Specfile autogenerated by cpanspec 1.78.
