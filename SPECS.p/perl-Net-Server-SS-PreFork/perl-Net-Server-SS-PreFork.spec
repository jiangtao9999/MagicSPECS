Name:           perl-Net-Server-SS-PreFork
Version:        0.05
Release:        11%{?dist}
Summary:        Hot-deployable variant of Net::Server::PreFork
License:        GPL+ or Artistic

URL:            http://search.cpan.org/dist/Net-Server-SS-PreFork/
Source0:        http://www.cpan.org/authors/id/K/KA/KAZUHO/Net-Server-SS-PreFork-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl(CPAN)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Server::Simple::CGI)
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(Net::Server)
BuildRequires:  perl(Server::Starter)
BuildRequires:  perl(Test::TCP)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
Net::Server::SS::PreFork is a Net::Server personality, extending
Net::Server::PreFork. It can be run by the start_server script of
Server::Starter.

%prep
%setup -q -n Net-Server-SS-PreFork-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Net
%{_mandir}/man3/Net*

%changelog
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Aug 01 2013 Petr Pisar <ppisar@redhat.com> - 0.05-9
- Perl 5.18 rebuild

* Sun Feb 17 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.05-8
- Add perl(CPAN) to BuildRequires
- Remove perl(CGI) from the BuildRequires (no longer needed)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Petr Pisar <ppisar@redhat.com> - 0.05-5
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.05-3
- Perl mass rebuild

* Tue Jul 05 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 0.05-2
- Add perl(CGI) as a BuildRequires until brc #719048 is fixed.
- Use more explicit entries in the files stanza

* Fri Jun 17 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 0.05-1
- Specfile autogenerated by cpanspec 1.78.
