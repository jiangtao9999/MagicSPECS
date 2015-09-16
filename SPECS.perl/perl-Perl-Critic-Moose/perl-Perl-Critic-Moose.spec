%global cpan_version 0.999_002
Name:           perl-Perl-Critic-Moose
Version:	1.03
Release:	1%{?dist}
Summary:        Policies for Perl::Critic concerned with using Moose
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Perl-Critic-Moose/
Source0:        http://search.cpan.org/CPAN/authors/id/E/EL/ELLIOTJS/Perl-Critic-Moose-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Module::Build)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Perl::Critic::Policy) >= 1.098
BuildRequires:  perl(Perl::Critic::Utils) >= 1.098
BuildRequires:  perl(Perl::Critic::Utils::PPI) >= 1.098
BuildRequires:  perl(Readonly)
# Tests only
BuildRequires:  perl(Carp)
BuildRequires:  perl(Perl::Critic::TestUtils) >= 1.098
BuildRequires:  perl(Perl::Critic::Violation) >= 1.098
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(Perl::Critic::Policy) >= 1.098
Requires:       perl(Perl::Critic::Utils) >= 1.098
Requires:       perl(Perl::Critic::Utils::PPI) >= 1.098

# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Perl::Critic::(Policy|Utils(|::PPI))\\)$

# Augment provide versions with development digits
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Perl::Critic::(Policy::)?Moose(::.*)?\\)\\s*=
Provides:       perl(Perl::Critic::Moose) = %{version}
Provides:       perl(Perl::Critic::Policy::Moose::ProhibitMultipleWiths) = %{version}
Provides:       perl(Perl::Critic::Policy::Moose::ProhibitNewMethod) = %{version}
Provides:       perl(Perl::Critic::Policy::Moose::RequireCleanNamespace) = %{version}
Provides:       perl(Perl::Critic::Policy::Moose::RequireMakeImmutable) = %{version}

%description
Some Perl::Critic policies that will help you keep your code in good shape
with regards to Moose.

%prep
%setup -q -n Perl-Critic-Moose-%{cpan_version}

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
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 1.03-1
- 更新到 1.03

* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 0.999.002-10
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.999.002-9
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.999.002-8
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.999.002-7
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.999.002-6
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.999.002-5
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.999.002-4
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.999.002-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 20 2012 Petr Pisar <ppisar@redhat.com> - 0.999.002-2
- Perl 5.16 rebuild

* Thu Jan 19 2012 Petr Pisar <ppisar@redhat.com> 0.999.002-1
- Specfile autogenerated by cpanspec 1.78.
