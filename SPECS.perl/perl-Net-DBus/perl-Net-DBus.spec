Name:           perl-Net-DBus
Version:	1.1.0
Release:	1%{?dist}
Summary:        Use and provide DBus services
License:        GPLv2+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Net-DBus/
Source0:        http://search.cpan.org/CPAN/authors/id/D/DA/DANBERR/Net-DBus-%{version}.tar.gz
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildRequires:  dbus-devel  >= 1.00, pkgconfig
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(XML::Grove)
BuildRequires:  perl(XML::Parser)
BuildRequires:  perl(XML::Twig)
BuildRequires:  perl(XSLoader)
# test
BuildRequires:  perl(Carp)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
Requires:       perl(XSLoader)

%{?perl_default_filter}

%description
Net::DBus provides a Perl API for the DBus message system. The DBus Perl
interface is currently operating against the 0.33 development version of
DBus, but should work with later versions too, providing the API changes
have not been too drastic.

%prep
%setup -q -n Net-DBus-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} +
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} +
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} %{buildroot}/*

%check
make test

%files
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Net*
%{_mandir}/man3/*

%changelog
* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 1.1.0-1
- 更新到 1.1.0

* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 1.0.0-11
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 1.0.0-10
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 1.0.0-9
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.0.0-8
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.0.0-7
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.0.0-6
- 为 Magic 3.0 重建

* Tue Jan 15 2013 Liu Di <liudidi@gmail.com> - 1.0.0-5
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 18 2012 Petr Pisar <ppisar@redhat.com> - 1.0.0-3
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 11 2011 Petr Šabata <contyk@redhat.com> - 1.0.0-1
- 1.0.0 bump
- Removing now obsolete Buildroot and defattr
- License updated to GPLv2+ or Artistic

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.33.6-10
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.33.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.33.6-8
- 661697 rebuild for fixing problems with vendorach/lib

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.33.6-7
- Mass rebuild with perl-5.12.0

* Wed Jan 20 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.33.6-6
- add default filtering
- auto-update to 0.33.6 (by cpan-spec-update 0.01)
- added a new req on perl(Time::HiRes) (version 0)
- added a new req on perl(XML::Twig) (version 0)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.33.6-5
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.33.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.33.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.33.6-2
Rebuild for new perl

* Thu Feb 21 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.33.6-1
- update to 0.33.6
- update license tag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.33.5-3
- Autorebuild for GCC 4.3

* Tue Aug 21 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.33.5-2
- bump

* Thu Aug 09 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.33.5-1
- update to 0.33.5
- fixup perl BR's
- add t/ to doc

* Tue Nov 21 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.33.4-3
- nix t/30-server.t until the test is fixed

* Sat Nov 11 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.33.4-2
- add additional BR's
- update summary

* Tue Nov 07 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.33.4-1
- update to 0.33.4
- nix now-unneeded source regexp/tweak

* Sat Nov 04 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.33.3-1
- Specfile autogenerated by cpanspec 1.69.1.
