Name:           perl-URI-ws
Version:        0.03
Release:        5%{?dist}
Summary:        WebSocket support for URI package
License:        GPL+ or Artistic

URL:            http://search.cpan.org/dist/URI-ws/
Source0:        http://search.cpan.org/CPAN/authors/id/P/PL/PLICEASE/URI-ws-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(base)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::_server)
BuildRequires:  perl(warnings)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
After this module is installed, the URI package provides the same set of
methods for WebSocket URIs as it does for HTTP ones. For secure WebSockets,
see URI::wss.

%prep
%setup -q -n URI-ws-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/URI*
%{_mandir}/man3/URI*

%changelog
* Tue Nov 03 2015 Liu Di <liudidi@gmail.com> - 0.03-5
- 为 Magic 3.0 重建

* Tue Sep 15 2015 Liu Di <liudidi@gmail.com> - 0.03-4
- 为 Magic 3.0 重建

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.03-2
- Perl 5.22 rebuild

* Sun Mar 29 2015 Emmanuel Seyman <emmanuel@seyman.fr> 0.03-1
- Specfile autogenerated by cpanspec 1.78.
