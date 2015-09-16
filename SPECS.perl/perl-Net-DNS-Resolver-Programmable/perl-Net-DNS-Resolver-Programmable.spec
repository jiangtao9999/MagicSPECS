Name:           perl-Net-DNS-Resolver-Programmable
Version:	0.003
Release:	23%{?dist}
Summary:        Programmable DNS resolver class for offline emulation of DNS
License:        GPLv2+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Net-DNS-Resolver-Programmable/
Source0:        http://search.cpan.org/CPAN/authors/id/J/JM/JMEHNLE/net-dns-resolver-programmable/Net-DNS-Resolver-Programmable-v%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Module::Build)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Net::DNS::Resolver::Programmable is a Net::DNS::Resolver descendant class
that allows a virtual DNS to be emulated instead of querying the real DNS.
A set of static DNS records may be supplied, or arbitrary code may be
specified as a means for retrieving DNS records, or even generating them
on the fly.

%prep
%setup -q -n Net-DNS-Resolver-Programmable-v%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc CHANGES LICENSE README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 0.003-21
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.003-20
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.003-19
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.003-18
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.003-17
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.003-16
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.003-15
- 为 Magic 3.0 重建

* Tue Oct 23 2012 Petr Pisar <ppisar@redhat.com> - 0.003-14
- Change license to "GPLv2+ or Artistic" and remove unneeded dependencies

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.003-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 0.003-12
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.003-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.003-10
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.003-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.003-8
- 661697 rebuild for fixing problems with vendorach/lib

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.003-7
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.003-6
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.003-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.003-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Mar  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.003-3
- rebuild for new perl

* Wed Jul 11 2007 Steven Pritchard <steve@kspei.com> 0.003-2
- Rebuild.

* Tue Jul 10 2007 Steven Pritchard <steve@kspei.com> 0.003-1
- Specfile autogenerated by cpanspec 1.72.
- Add "v" to files and path names.
- Drop explicit redundant dependencies.
