Name:           perl-HTTP-Daemon
Version:        6.01
Release:        5%{?dist}
Summary:        Simple HTTP server class
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/HTTP-Daemon/
Source0:        http://www.cpan.org/authors/id/G/GA/GAAS/HTTP-Daemon-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Date) >= 6
BuildRequires:  perl(HTTP::Request) >= 6
BuildRequires:  perl(HTTP::Response) >= 6
BuildRequires:  perl(HTTP::Status) >= 6
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(LWP::MediaTypes) >= 6
BuildRequires:  perl(Sys::Hostname)
# Tests only:
BuildRequires:  perl(Config)
# Do not depend on perl(LWP::UserAgent), perl(LWP::RobotUA) to break
# circural dependency, then only t/chunked.t is executed.
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Socket)
BuildRequires:  perl(IO::Socket::INET)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(HTTP::Date) >= 6
Requires:       perl(HTTP::Request) >= 6
Requires:       perl(HTTP::Response) >= 6
Requires:       perl(HTTP::Status) >= 6
Requires:       perl(LWP::MediaTypes) >= 6
Requires:       perl(Sys::Hostname)
Conflicts:      perl-libwww-perl < 6

# Remove underspecified dependencies
%filter_from_requires /^perl(HTTP::Date)\s*$/d;
%filter_from_requires /^perl(HTTP::Request)\s*$/d;
%filter_from_requires /^perl(HTTP::Response)\s*$/d;
%filter_from_requires /^perl(HTTP::Status)\s*$/d;
%filter_from_requires /^perl(LWP::MediaTypes)\s*$/d;
%filter_setup

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(HTTP::(Date|Request|Response|Status)|LWP::MediaTypes\\)$

%description
Instances of the HTTP::Daemon class are HTTP/1.1 servers that listen on a
socket for incoming requests. The HTTP::Daemon is a subclass of
IO::Socket::INET, so you can perform socket operations directly on it too.

%prep
%setup -q -n HTTP-Daemon-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check


%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 6.01-5
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 6.01-4
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 6.01-2
- Perl 5.16 rebuild

* Mon Feb 20 2012 Petr Pisar <ppisar@redhat.com> - 6.01-1
- 6.01 bump

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.00-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 25 2011 Marcela Mašláňová <mmaslano@redhat.com> - 6.00-3
- add new filter

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 6.00-2
- Perl mass rebuild

* Thu Mar 17 2011 Petr Pisar <ppisar@redhat.com> 6.00-1
- Specfile autogenerated by cpanspec 1.78.
- Remove BuildRoot stuff
- Conflicts with perl-libwww-perl-5* and older
