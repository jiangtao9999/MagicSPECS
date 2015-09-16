Name:           perl-Mail-MboxParser
Version:        0.55
Release:        12%{?dist}
Summary:        Read-only access to UNIX-mailboxes
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Mail-MboxParser/
Source0:        http://www.cpan.org/authors/id/V/VP/VPARSEVAL/Mail-MboxParser-%{version}.tar.gz
# Bug #715505, submitted to upstream
Patch0:         %{name}-0.55-Fix-garbled-attachment-name-RT-66576.patch
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(MIME::Tools) >= 5
# Tests:
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Seekable)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(MIME::QuotedPrint)
BuildRequires:  perl(Test)
# Optional test
BuildRequires:  perl(Encode)
BuildRequires:  perl(Mail::Mbox::MessageParser)
BuildRequires:  perl(MIME::Words)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(MIME::Tools) >= 5
Requires:       perl(Mail::Mbox::MessageParser)

%{?perl_default_filter}

%description
This module attempts to provide a simplified access to standard UNIX-
mailboxes. It offers only a subset of methods to get 'straight to the
point'. More sophisticated things can still be done by invoking any method
from MIME::Tools on the appropriate return values.

%prep
%setup -q -n Mail-MboxParser-%{version}
%patch0 -p1 -b .attachment_name

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
%doc Changelog README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.55-12
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.55-11
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.55-10
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.55-9
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.55-8
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.55-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.55-6
- Perl mass rebuild

* Thu Jun 23 2011 Petr Pisar <ppisar@redhat.com> - 0.55-5
- Add test-time buildrequires

* Thu Jun 23 2011 Petr Pisar <ppisar@redhat.com> - 0.55-4
- Remove obsolete code from spec file
- Fix failing test (bug #715505)
- Complete list of build-time dependencies

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.55-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 20 2011 Marcela Mašláňová <mmaslano@redhat.com> 0.55-2
- fix typo in requires

* Thu Jan 20 2011 Marcela Mašláňová <mmaslano@redhat.com> 0.55-1
- Specfile autogenerated by cpanspec 1.78.
