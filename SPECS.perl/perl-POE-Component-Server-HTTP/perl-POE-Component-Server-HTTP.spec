Name:           perl-POE-Component-Server-HTTP
Version:        0.09
Release:        19%{?dist}
Summary:        Foundation of a POE HTTP Daemon
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/POE-Component-Server-HTTP/
Source0:        http://www.cpan.org/authors/id/R/RC/RCLAMP/POE-Component-Server-HTTP-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

BuildRequires:  perl(LWP)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Status)
# >= 0.3007     vvvvvvvv
BuildRequires:  perl(POE) 
BuildRequires:  perl(YAML)
BuildRequires:  perl(Test::More)

# Note that this _is_ listed as a BR in Makefile.PL, but 1) is only used in
# t/30_error.t and 2) depends on Devel::Size, which is broken on x86_64 (see
# cpan bug at, e.g., http://rt.cpan.org/Public/Bug/Display.html?id=21037)
# When this is addressed, I'll gladly package those two as well, for proper
# build-time testing.
#BuildRequires:  perl(POE::API::Peek)


%description
POE::Component::Server::HTTP (PoCo::HTTPD) is a framework for building
custom HTTP servers based on POE. It is loosely modeled on the ideas of
apache and the mod_perl/Apache module.


%prep
%setup -q -n POE-Component-Server-HTTP-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf %{buildroot}

make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*


%check
# see rant in BR's, above
rm t/30_error.t

# I'm unsure as to wrapping this with _with_network_tests logic.  Should be
# kosher, it's only doing tests on localhost.



%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc Changes README test.perl
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Nov 03 2015 Liu Di <liudidi@gmail.com> - 0.09-19
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.09-18
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.09-17
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.09-16
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Petr Pisar <ppisar@redhat.com> - 0.09-14
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.09-12
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.09-10
- 661697 rebuild for fixing problems with vendorach/lib

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.09-9
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.09-8
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.09-5
- rebuild for new perl

* Thu Jan 10 2008 Ralf Corsépius <rc040203@freenet.de> 0.09-4
- Update License-tag.
- BR: perl(Test::More) (BZ 419631).

* Thu Aug 31 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.09-3
- bump for mass rebuild

* Thu Aug 17 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.09-2
- bump

* Wed Aug 16 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.09-1
- Specfile autogenerated by cpanspec 1.68.
- Initial spec file for F-E
