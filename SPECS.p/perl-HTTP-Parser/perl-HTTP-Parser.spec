Name:           perl-HTTP-Parser
Version:        0.06
Release:        5%{?dist}
Summary:        Parse HTTP/1.1 request into HTTP::Request/Response object
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/HTTP-Parser/
Source0:        http://www.cpan.org/authors/id/E/ED/EDECA/HTTP-Parser-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This is an HTTP request parser. It takes chunks of text as received and
returns a 'hint' as to what is required, or returns the HTTP::Request when
a complete request has been read. HTTP/1.1 chunking is supported. It dies
if it finds an error.

%prep
%setup -q -n HTTP-Parser-%{version}

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
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.06-5
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.06-4
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.06-2
- Perl mass rebuild

* Tue Mar 08 2011 Petr Pisar <ppisar@redhat.com> - 0.06-1
- 1.06 bump
- Remove BuildRoot stuff

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 17 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.05-2
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Jun 18 2010 Petr Pisar <ppisar@redhat.com> 0.05-1
- Specfile autogenerated by cpanspec 1.78.
- License verified from README.
- Test::More required by tests.
