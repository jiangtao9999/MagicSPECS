Name:           perl-Test-Mock-LWP
Version:	0.08
Release:	1%{?dist}
Summary:        Easy mocking of LWP packages
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Test-Mock-LWP/
Source0:        http://search.cpan.org/CPAN/authors/id/L/LU/LUKEC/Test-Mock-LWP-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::MockObject) >= 1.08
BuildRequires:  perl(Test::More) >= 0.42
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%define bogusprovs 'perl(HTTP::Request)\
perl(HTTP::Response)\
perl(LWP::UserAgent)'
%global provfilt sh -c "%{__perl_provides} | %{__grep} -Fv %{bogusprovs}"
%define __perl_provides %{provfilt}

# Equivalent filter for rpm 4.9 onwards
%global __provides_exclude ^perl\\((HTTP::(Request|Response)|LWP::UserAgent)\\)


%description
This package arises from duplicating the same code to mock LWP et al in
several different modules I've written. This version is very minimalist,
but works for my needs so far. I'm very open to new suggestions and
improvements.


%prep
%setup -q -n Test-Mock-LWP-%{version}


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
* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.08-1
- 更新到 0.08

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.06-6
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.06-5
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 14 2012 Petr Pisar <ppisar@redhat.com> - 0.06-3
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct  2 2011 Tom Callaway <spot@fedoraproject.org> - 0.06-1
- update to 0.06

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.05-10
- Perl mass rebuild

* Mon Feb 14 2011 Paul Howarth <paul@city-fan.org> - 0.05-9
- Add rpm 4.9 compatible provides filter

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.05-7
- 661697 rebuild for fixing problems with vendorach/lib

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.05-6
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.05-5
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 22 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 0.05-3
- Filter out perl(..) Provides for HTTP::Request, HTTP::Response and
  LWP::UserAgent, which come from files not stored in Perl's search
  path for modules (#472354).

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jun 16 2008 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> 0.05-1
- Specfile autogenerated by cpanspec 1.75.
- Fixed dependencies
- Fixed strings
