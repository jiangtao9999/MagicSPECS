Name:           perl-Perl-Critic-PetPeeves-JTRAMMELL
Version:	0.04
Release:	1%{?dist}
Summary:        Policies to prohibit/require my pet peeves
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Perl-Critic-PetPeeves-JTRAMMELL/
Source0:        http://www.cpan.org/authors/id/J/JT/JTRAMMELL/Perl-Critic-PetPeeves-JTRAMMELL-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Module::Build)
# Tests only:
BuildRequires:  perl(Perl::Critic::Config)
BuildRequires:  perl(Perl::Critic::Policy)
BuildRequires:  perl(Perl::Critic::Utils)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(Perl::Critic::Policy)

%description
Module Perl::Critic::PetPeeves::JTRAMMELL provides policies that I want
that haven't already been implemented elsewhere.

%prep
%setup -q -n Perl-Critic-PetPeeves-JTRAMMELL-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.04-1
- 更新到 0.04

* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 0.02-12
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.02-11
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.02-10
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.02-9
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.02-8
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.02-7
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.02-6
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.02-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 20 2012 Petr Pisar <ppisar@redhat.com> - 0.02-4
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.02-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.02-2
- Perl mass rebuild

* Wed Apr 06 2011 Petr Pisar <ppisar@redhat.com> - 0.02-1
- 0.02 bump

* Wed Jan 26 2011 Petr Pisar <ppisar@redhat.com> 0.01-1
- Specfile autogenerated by cpanspec 1.78.
- Remove BuildRoot stuff
