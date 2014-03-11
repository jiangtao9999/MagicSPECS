Name:           perl-Mozilla-CA
# You do not need to back-port new version for list of certificates solely.
# They are taken from ca-certificates package instead per bug #738383.
Version:        20130114
Release:        2%{?dist}
Summary:        Mozilla's CA cert bundle in PEM format
License:        MPLv1.1 or LGPLv2+ or GPLv2+
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Mozilla-CA/
Source0:        http://www.cpan.org/authors/id/A/AB/ABH/Mozilla-CA-%{version}.tar.gz
# Bug #738383
Patch0:         Mozilla-CA-20130114-Redirect-to-ca-certificates-bundle.patch
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
# Tests:
BuildRequires:  ca-certificates
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       ca-certificates

%description
Mozilla::CA provides a path to ca-certificates copy of Mozilla's bundle of
certificate authority certificates in a form that can be consumed by modules
and libraries based on OpenSSL.

%prep
%setup -q -n Mozilla-CA-%{version}
%patch0 -p1
# Do not distribute Mozilla downloader, we take certificates from
# ca-certificates package
rm mk-ca-bundle.pl
sed -i '/^mk-ca-bundle.pl$/d' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130114-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 15 2013 Petr Pisar <ppisar@redhat.com> - 20130114-1
- 20130114 bump

* Thu Aug 23 2012 Petr Pisar <ppisar@redhat.com> - 20120823-1
- 20120823 bump

* Wed Aug 22 2012 Petr Pisar <ppisar@redhat.com> - 20120822-1
- 20120822 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120309-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 20120309-2
- Perl 5.16 rebuild

* Wed Mar 14 2012 Petr Pisar <ppisar@redhat.com> - 20120309-1
- 20120309 bump

* Wed Jan 18 2012 Petr Pisar <ppisar@redhat.com> - 20120118-1
- 20120118 bump

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20111025-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 25 2011 Petr Pisar <ppisar@redhat.com> - 20111025-1
- 20111025 bump
- Remove defattr from spec code

* Fri Sep 16 2011 Petr Pisar <ppisar@redhat.com> - 20110914-2
- Redirect to ca-certificates bundle (bug #738383)

* Thu Sep 15 2011 Petr Pisar <ppisar@redhat.com> - 20110914-1
- 20110914 bump

* Mon Sep 05 2011 Petr Pisar <ppisar@redhat.com> - 20110904-1
- 20110904 bump

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 20110409-2
- Perl mass rebuild

* Mon Apr 11 2011 Petr Pisar <ppisar@redhat.com> - 20110409-1
- 20110409 bump

* Mon Mar 28 2011 Petr Pisar <ppisar@redhat.com> 20110301-1
- Specfile autogenerated by cpanspec 1.78.
- Correct License tag
- Remove BuildRoot stuff
