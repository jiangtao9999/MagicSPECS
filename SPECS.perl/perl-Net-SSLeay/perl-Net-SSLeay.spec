Name:		perl-Net-SSLeay
Version:	1.72
Release:	2%{?dist}
Summary:	Perl extension for using OpenSSL
Group:		Development/Libraries
License:	OpenSSL
URL:		http://search.cpan.org/dist/Net-SSLeay/
Source0:	http://search.cpan.org/CPAN/authors/id/M/MI/MIKEM/Net-SSLeay-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(id -nu)
BuildRequires:	openssl, openssl-devel
# =========== Module Build ===========================
BuildRequires:	perl(Cwd)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(lib)
# =========== Module Runtime =========================
BuildRequires:	perl(AutoLoader)
BuildRequires:	perl(Carp)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(MIME::Base64)
BuildRequires:	perl(Socket)
BuildRequires:	perl(XSLoader)
# =========== Test Suite =============================
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(IO::Handle)
BuildRequires:	perl(Test::Exception)
# Test::Kwalitee => Module::CPANTS::Analyze => Net::HTTP => IO::Socket::SSL => Net::SSLeay
# Net::SSLeay in RHEL-7 cannot BR: Test::Kwalitee from EPEL-7
%if 0%{!?perl_bootstrap:1} && 0%{?rhel} < 7
BuildRequires:	perl(Test::Kwalitee)
%endif
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::NoWarnings)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)
BuildRequires:	perl(Test::Warn)
BuildRequires:	perl(threads)
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:	perl(MIME::Base64)
Requires:	perl(XSLoader)

# Don't "provide" private Perl libs or the redundant unversioned perl(Net::SSLeay) provide
%global __provides_exclude ^(perl\\(Net::SSLeay\\)$|SSLeay\\.so)

%description
This module offers some high level convenience functions for accessing
web pages on SSL servers (for symmetry, same API is offered for
accessing http servers, too), a sslcat() function for writing your own
clients, and finally access to the SSL API of SSLeay/OpenSSL package
so you can write servers or clients for more complicated applications.

%prep
%setup -q -n Net-SSLeay-%{version}

# Fix permissions in examples to avoid bogus doc-file dependencies
chmod -c 644 examples/*

# Remove redundant unversioned provide if we don't have rpm 4.9 or later
%global provfilt /bin/sh -c "%{__perl_provides} | grep -Fvx 'perl(Net::SSLeay)'"
%define __perl_provides %{provfilt}

%build
PERL_MM_USE_DEFAULT=1 perl Makefile.PL \
	INSTALLDIRS=vendor \
	OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}

# Remove script we don't want packaged
rm -f %{buildroot}%{perl_vendorarch}/Net/ptrtstrun.pl

%check


%clean
rm -rf %{buildroot}

%files
%doc Changes Credits QuickRef README examples/
%{perl_vendorarch}/auto/Net/
%dir %{perl_vendorarch}/Net/
%{perl_vendorarch}/Net/SSLeay/
%{perl_vendorarch}/Net/SSLeay.pm
%doc %{perl_vendorarch}/Net/SSLeay.pod
%{_mandir}/man3/Net::SSLeay.3pm*
%{_mandir}/man3/Net::SSLeay::Handle.3pm*

%changelog
* Tue Nov 03 2015 Liu Di <liudidi@gmail.com> - 1.72-2
- 更新到 1.72

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 1.70-1
- 更新到 1.70

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.49-3
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 1.49-2
- 为 Magic 3.0 重建

* Tue Sep 25 2012 Paul Howarth <paul@city-fan.org> - 1.49-1
- update to 1.49
  - fixed problem where on some platforms test t/local/07_tcpecho.t would bail
    out if it could not bind port 1212; it now tries a number of ports to bind
    to until successful
  - improvements to unsigned casting
  - improvements to Net::SSLeay::read to make it easier to use with
    non-blocking IO: it modifies Net::SSLeay::read() to return the result from
    SSL_read() as the second return value, if Net::SSLeay::read() is called in
    list context (its behavior should be unchanged if called in scalar or void
    context)
  - fixed a problem where t/local/kwalitee.t fails with
    Module::CPANTS::Analyse 0.86
  - fixed a number of typos
  - fixed a compiler warning from Compiling with gcc-4.4 and -Wall
  - Fixed problems with get_https4: documentation was wrong, $header_ref was
    not correctly set and $server_cert was not returned
  - fixed a problem that could cause a Perl exception about no blength method
    on undef (CPAN RT#79309)
  - added documentation about how to mitigate various SSL/TLS vulnerabilities
  - SSL_MODE_* are now available as constants
- drop upstreamed pod encoding patch

* Mon Aug 20 2012 Paul Howarth <paul@city-fan.org> - 1.48-6
- fix POD encoding (CPAN RT#78281)
- classify buildreqs by usage
- BR:/R: perl(XSLoader)

* Mon Aug 13 2012 Petr Pisar <ppisar@redhat.com> - 1.48-5
- specify all dependencies

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.48-4
- rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Petr Pisar <ppisar@redhat.com> - 1.48-3
- perl 5.16 re-rebuild of bootstrapped packages

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 1.48-2
- perl 5.16 rebuild

* Wed Apr 25 2012 Paul Howarth <paul@city-fan.org> - 1.48-1
- update to 1.48
  - removed unneeded Debian_CPANTS.txt from MANIFEST
  - fixed incorrect documentation about the best way to call CTX_set_options
  - fixed problem that caused "Undefined subroutine utf8::encode" in
    t/local/33_x509_create_cert.t (on perl 5.6.2)
  - in examples and pod documentation, changed #!/usr/local/bin/perl
    to #!/usr/bin/perl
  - t/local/06_tcpecho.t now tries a number of ports to bind to until
    successful
- no longer need to fix shellbangs in examples

* Thu Apr 19 2012 Paul Howarth <paul@city-fan.org> - 1.47-3
- simplify Test::Kwalitee conditional

* Thu Apr 19 2012 Marcela Mašláňová <mmaslano@redhat.com> - 1.47-2
- make module Kwalitee conditional

* Wed Apr  4 2012 Paul Howarth <paul@city-fan.org> - 1.47-1
- update to 1.47
  - fixed overlong lines and spelling errors in pod
  - fixed extra "garbage" files in 1.46 tarball
  - fixed incorrect fail reports on some 64 bit platforms
  - fix to avoid FAIL reports from cpantesters with missing openssl
  - use my_snprintf from ppport.h to prevent link failures with perl 5.8 and
    earlier when compiled with MSVC

* Tue Apr  3 2012 Paul Howarth <paul@city-fan.org> - 1.46-1
- update to 1.46 (see Changes file for details)
- BR: openssl as well as openssl-devel, needed for building
- no longer need help to find openssl
- upstream no longer shipping TODO
- drop %%defattr, redundant since rpm 4.4

* Sat Feb 25 2012 Paul Howarth <paul@city-fan.org> - 1.45-1
- update to 1.45 (see Changes file for full details)
  - added thread safety and dynamic locking, which should complete thread
    safety work, making Net::SSLeay completely thread-safe
  - lots of improved documentation
- BR: perl(Test::Pod::Coverage)
- install Net/SSLeay.pod as %%doc

* Thu Jan 12 2012 Paul Howarth <paul@city-fan.org> - 1.42-2
- use DESTDIR rather than PERL_INSTALL_ROOT
- use %%{_fixperms} macro rather than our own chmod incantation
- BR: perl(AutoLoader), perl(Exporter), perl(Socket)

* Mon Oct  3 2011 Paul Howarth <paul@city-fan.org> - 1.42-1
- update to 1.42
  - fixed incorrect documentation of how to enable CRL checking
  - fixed incorrect letter in Sebastien in Credits
  - changed order of the Changes file to be reverse chronological
  - fixed a compile error when building on Windows with MSVC6
- drop UTF8 patch, no longer needed

* Sun Sep 25 2011 Paul Howarth <paul@city-fan.org> - 1.41-1
- update to 1.41
  - fixed incorrect const signatures for 1.0 that were causing warnings; now
    have clean compile with 0.9.8a through 1.0.0
- BR: perl(Carp)

* Fri Sep 23 2011 Paul Howarth <paul@city-fan.org> - 1.40-1
- update to 1.40
  - fixed incorrect argument type in call to SSL_set1_param
  - fixed a number of issues with pointer sizes; removed redundant pointer cast
    tests from t/
  - added Perl version requirements to SSLeay.pm

* Wed Sep 21 2011 Paul Howarth <paul@city-fan.org> - 1.39-1
- update to 1.39
  - downgraded Module::Install to 0.93 since 1.01 was causing problems in the
    Makefile

* Fri Sep 16 2011 Paul Howarth <paul@city-fan.org> - 1.38-1
- update to 1.38
  - fixed a problem with various symbols that only became available in OpenSSL
    0.9.8 such as X509_VERIFY_PARAM and X509_POLICY_NODE, causing build
    failures with older versions of OpenSSL (CPAN RT#71013)

* Fri Sep 16 2011 Paul Howarth <paul@city-fan.org> - 1.37-1
- update to 1.37
  - added X509_get_fingerprint
  - added support for SSL_CTX_set1_param, SSL_set1_param and selected
    X509_VERIFY_PARAM_* OBJ_* functions
  - fixed the prototype for randomize()
  - fixed an uninitialized value warning in $Net::SSLeay::proxyauth
  - allow net-ssleay to compile if SSLV2 is not present
  - fixed a problem where sslcat (and possibly other functions) expect RSA
    keys and will not load DSA keys for client certificates
  - removed SSL_CTX_v2_new and SSLv2_method() for OpenSSL 1.0 and later
  - added CTX_use_PKCS12_file
- this release by MIKEM => update source URL

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1.36-7
- Perl mass rebuild

* Thu Jul 14 2011 Paul Howarth <paul@city-fan.org> - 1.36-6
- BR: perl(Test::Kwalitee) if we're not bootstrapping
- explicitly BR: pkgconfig
- use a patch rather than a scripted iconv to fix the character encoding
- modernize provides filter
- stop running the tests in verbose mode
- nobody else likes macros for commands

* Wed Jul 13 2011 Iain Arnell <iarnell@gmail.com> - 1.36-5
- drop obsolete BRs Array::Compare, Sub::Uplevel, Tree::DAG_Node

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.36-4
- rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.36-3
- rebuild to fix problems with vendorarch/lib (#661697)

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.36-2
- mass rebuild with perl-5.12.0

* Sun Jan 31 2010 Paul Howarth <paul@city-fan.org> - 1.36-1
- update to 1.36 (see Changes for details)
- drop svn patches

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.35-8
- rebuild against perl 5.10.1

* Sat Aug 22 2009 Paul Howarth <paul@city-fan.org> - 1.35-7
- update to svn trunk (rev 252), needed due to omission of MD2 functionality
  from OpenSSL 1.0.0 (CPAN RT#48916)

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1.35-6
- rebuilt with new openssl

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.35-5
- rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar  8 2009 Paul Howarth <paul@city-fan.org> - 1.35-4
- filter out unwanted provides for perl shared objects
- run tests in verbose mode

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.35-3
- rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> - 1.35-2
- rebuild with new openssl

* Mon Jul 28 2008 Paul Howarth <paul@city-fan.org> - 1.35-1
- update to 1.35
- drop flag and patch for enabling/disabling external tests - patch now upstream
- external hosts patch no longer needed as we don't do external tests
- filter out unversioned provide for perl(Net::SSLeay)
- use the distro openssl flags rather than guessing them

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.32-5
- rebuild for perl 5.10 (again)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.32-4
- autorebuild for GCC 4.3

* Thu Jan 31 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.32-3
- rebuild for new perl

* Wed Dec  5 2007 Paul Howarth <paul@city-fan.org> - 1.32-2
- rebuild with new openssl

* Wed Nov 28 2007 Paul Howarth <paul@city-fan.org> - 1.32-1
- update to 1.32, incorporate new upstream URLs
- cosmetic spec changes suiting new maintainer's preferences
- fix argument order for find with -depth
- remove patch for CVE-2005-0106, fixed upstream in 1.30 (#191351)
  (http://rt.cpan.org/Public/Bug/Display.html?id=19218)
- remove test patch, no longer needed
- re-encode Credits as UTF-8
- include TODO as %%doc
- add buildreqs perl(Array::Compare), perl(MIME::Base64), perl(Sub::Uplevel),
  perl(Test::Exception), perl(Test::NoWarnings), perl(Test::Pod),
  perl(Test::Warn), perl(Tree::DAG_Node)
- add patch needed to disable testsuite non-interactively
- run test suite but disable external tests by default; external tests can be
  enabled by using rpmbuild --with externaltests
- add patch to change hosts connected to in external tests

* Fri Nov 16 2007 Parag Nemade <panemade@gmail.com> - 1.30-7
- Merge Review (#226272) Spec cleanup

* Tue Nov  6 2007 Stepan Kasal <skasal@redhat.com> - 1.30-6
- fix a typo in description (#231756, #231757)

* Tue Oct 16 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1.30-5.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Tue Aug 21 2007 Warren Togami <wtogami@redhat.com> - 1.30-5
- rebuild

* Fri Jul 14 2006 Warren Togami <wtogami@redhat.com> - 1.30-4
- import into FC6

* Tue Feb 28 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.30-3
- Rebuild for FC5 (perl 5.8.8).

* Fri Jan 27 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.30-2
- CVE-2005-0106: patch from Mandriva
  http://wwwnew.mandriva.com/security/advisories?name=MDKSA-2006:023

* Sun Jan 15 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.30-1
- 1.30.
- Optionally run the test suite during build with "--with tests".

* Wed Nov  9 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.26-3
- Rebuild for new OpenSSL.
- Cosmetic cleanups.

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.26-2
- rebuilt

* Mon Dec 20 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.26-1
- Drop fedora.us release prefix and suffix.

* Mon Oct 25 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.26-0.fdr.2
- Convert manual page to UTF-8.

* Tue Oct 12 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.26-0.fdr.1
- Update to unofficial 1.26 from Peter Behroozi, adds get1_session(),
  enables session caching with IO::Socket::SSL (bug 1859, bug 1860).
- Bring outdated test14 up to date (bug 1859, test suite still not enabled).

* Sun Jul 11 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.25-0.fdr.4
- Rename to perl-Net-SSLeay, provide perl-Net_SSLeay for compatibility
  with the rest of the world.

* Wed Jul  7 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.25-0.fdr.3
- Bring up to date with current fedora.us Perl spec template.
- Include examples in docs.

* Sun Feb  8 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.25-0.fdr.2
- Reduce directory ownership bloat.

* Fri Oct 17 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.25-0.fdr.1
- First build.
