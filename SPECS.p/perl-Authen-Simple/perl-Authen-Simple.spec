Name:           perl-Authen-Simple
Version:        0.5
Release:        5%{?dist}
Summary:        Simple Authentication
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Authen-Simple/
Source0:        http://www.cpan.org/authors/id/C/CH/CHANSEN/Authen-Simple-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(Class::Data::Inheritable)
BuildRequires:  perl(Crypt::PasswdMD5)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Params::Validate)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# Required by Authen::Simple::Adapter
Requires:       perl(Class::Accessor::Fast)
Requires:       perl(Class::Data::Inheritable)

%{?perl_default_filter}

%description
Simple and consistent framework for authentication.

%prep
%setup -q -n Authen-Simple-%{version}

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
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.5-5
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 0.5-4
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 0.5-2
- Perl 5.16 rebuild

* Fri Apr 20 2012 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 0.5-1
- Update to 0.5
- Move to the Makefile.PL build system

* Thu Mar 29 2012 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.4-8
- Add Class::Accessor::Fast and Class::Data::Inheritable to Requires

* Wed Jan 11 2012 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 0.4-7
- Clean up spec file

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.4-6
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.4-4
- 661697 rebuild for fixing problems with vendorach/lib

* Thu Apr 29 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.4-3
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.4-2
- rebuild against perl 5.10.1

* Wed Oct 07 2009 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 0.4-1
- Specfile autogenerated by cpanspec 1.78.
