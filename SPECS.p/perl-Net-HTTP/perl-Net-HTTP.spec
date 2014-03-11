Name:           perl-Net-HTTP
Version:        6.03
Release:        5%{?dist}
Summary:        Low-level HTTP connection (client)
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Net-HTTP/
Source0:        http://www.cpan.org/authors/id/G/GA/GAAS/Net-HTTP-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Getopt::Long)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Compress::Raw::Zlib)
BuildRequires:  perl(IO::Uncompress::Gunzip)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IO::Socket::SSL) >= 1.38
BuildRequires:  perl(Symbol)
# Tests only:
BuildRequires:  perl(Test)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(Compress::Raw::Zlib)
Requires:       perl(IO::Uncompress::Gunzip)
Requires:       perl(IO::Select)
Requires:       perl(IO::Socket::INET)
Requires:       perl(Symbol)
# Recommended
Requires:       perl(IO::Socket::SSL) >= 1.38
Conflicts:      perl-libwww-perl < 6

%description
The Net::HTTP class is a low-level HTTP client. An instance of the
Net::HTTP class represents a connection to an HTTP server. The HTTP
protocol is described in RFC 2616. The Net::HTTP class supports HTTP/1.0
and HTTP/1.1.

%prep
%setup -q -n Net-HTTP-%{version}

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
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 6.03-5
- 为 Magic 3.0 重建

* Mon Aug 13 2012 Petr Pisar <ppisar@redhat.com> - 6.03-4
- Specify all dependencies

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 14 2012 Petr Pisar <ppisar@redhat.com> - 6.03-2
- Perl 5.16 rebuild

* Mon Feb 20 2012 Petr Pisar <ppisar@redhat.com> - 6.03-1
- 6.03 bump: Restore blocking override for Net::SSL (RT #72790)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 22 2011 Petr Pisar <ppisar@redhat.com> - 6.02-1
- 6.02 bump
- Fixes HTTPS time-out in LWP::UserAgent/IO::Socket::SSL (bug #750793)

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 6.01-2
- Perl mass rebuild

* Mon Apr 18 2011 Petr Pisar <ppisar@redhat.com> - 6.01-1
- 6.01 bump

* Thu Mar 17 2011 Petr Pisar <ppisar@redhat.com> 6.00-1
- Specfile autogenerated by cpanspec 1.78.
- Remove BuildRoot stuff
- Conflicts with perl-libwww-perl-5* and older
