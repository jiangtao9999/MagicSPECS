Name:           perl-Package-Constants
# Epoch to compete with perl.spec
Epoch:          1
Version:        0.06
Release:        5%{?dist}
Summary:        List all constants declared in a package
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Package-Constants/
Source0:        http://www.cpan.org/authors/id/B/BI/BINGOS/Package-Constants-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(if)
%if 0%(perl -e 'print $] > 5.019006')
BuildRequires:  perl(deprecate)
%endif
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
%if 0%(perl -e 'print $] > 5.019006')
Requires:       perl(deprecate)
%endif

%description
Package::Constants lists all the constants defined in a certain package.
This can be useful for, among others, setting up an auto-generated
@EXPORT/@EXPORT_OK for a Constants.pm file.

%prep
%setup -q -n Package-Constants-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc CHANGES README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Nov 03 2015 Liu Di <liudidi@gmail.com> - 1:0.06-5
- 为 Magic 3.0 重建

* Thu Sep 17 2015 Liu Di <liudidi@gmail.com> - 1:0.06-4
- 为 Magic 3.0 重建

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.06-2
- Perl 5.22 rebuild

* Mon Jan 05 2015 Petr Pisar <ppisar@redhat.com> - 1:0.06-1
- 0.06 bump

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.04-310
- Increase release to favour standalone package

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.04-2
- Perl 5.20 rebuild

* Thu Jun 19 2014 Petr Pisar <ppisar@redhat.com> 1:0.04-1
- Specfile autogenerated by cpanspec 1.78.
