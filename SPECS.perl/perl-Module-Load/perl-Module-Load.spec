Name:           perl-Module-Load
# Epoch to compete with perl.spec
Epoch:          1
Version:        0.32
Release:        5%{?dist}
Summary:        Run-time require of both modules and files
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Module-Load/
Source0:        http://www.cpan.org/authors/id/B/BI/BINGOS/Module-Load-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(vars)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
If you consult "perldoc -f require" you will see that "require" will behave
differently when given a bare-word or a string. In the case of a string,
"require" assumes you are wanting to load a file. But in the case of
a bare-word, it assumes you mean a module.

This gives nasty overhead when you are trying to dynamically require modules
at run-time, since you will need to change the module notation to a file
notation fitting the particular platform you are on.

"load" eliminates the need for this overhead and will just DWYM.

%prep
%setup -q -n Module-Load-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR='%{buildroot}'
find '%{buildroot}' -type f -name .packlist -exec rm -f {} +
%{_fixperms} '%{buildroot}'/*

%check
make test

%files
%doc CHANGES README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Nov 02 2015 Liu Di <liudidi@gmail.com> - 1:0.32-5
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 1:0.32-4
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 1:0.32-3
- 为 Magic 3.0 重建

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 21 2014 Petr Pisar <ppisar@redhat.com> - 1:0.32-1
- 0.32 bump

* Mon Jan 27 2014 Petr Pisar <ppisar@redhat.com> - 1:0.30-1
- 0.30 bump

* Tue Jan 07 2014 Petr Pisar <ppisar@redhat.com> - 1:0.28-1
- 0.28 bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.24-291
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 15 2013 Petr Pisar <ppisar@redhat.com> - 1:0.24-290
- Increase release to favour standalone package

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 1:0.24-3
- Perl 5.18 rebuild

* Fri Apr 05 2013 Petr Pisar <ppisar@redhat.com> - 1:0.24-2
- Set epoch to compete with perl.spec

* Mon Mar 18 2013 Petr Pisar <ppisar@redhat.com> 0.24-1
- Specfile autogenerated by cpanspec 1.78.
