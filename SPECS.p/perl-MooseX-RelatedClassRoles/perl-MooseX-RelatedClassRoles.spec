Name:           perl-MooseX-RelatedClassRoles
Version:        0.004
Release:        8%{?dist}
Summary:        Apply roles to a class related to yours
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/MooseX-RelatedClassRoles/
Source0:        http://www.cpan.org/authors/id/H/HD/HDP/MooseX-RelatedClassRoles-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Class::MOP) >= 0.80
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Moose) >= 0.73
BuildRequires:  perl(MooseX::Role::Parameterized) >= 0.04
BuildRequires:  perl(Test::More)
Requires:       perl(Class::MOP) >= 0.80
Requires:       perl(Moose) >= 0.73
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
Frequently, you have to use a class that provides some foo_class accessor
or attribute as a method of dependency injection. Use this role when you'd
rather apply roles to make your custom foo_class instead of manually
setting up a subclass.

%prep
%setup -q -n MooseX-RelatedClassRoles-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.004-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 0.004-7
- Perl 5.18 rebuild

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 0.004-6
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.004-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.004-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 0.004-3
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.004-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 30 2011 Iain Arnell <iarnell@gmail.com> 0.004-1
- Specfile autogenerated by cpanspec 1.78.
