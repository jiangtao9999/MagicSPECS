Name:           perl-Perl-Critic-Dynamic
Version:	0.04
Release:	1%{?dist}
Summary:        Non-static policies for Perl::Critic
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Perl-Critic-Dynamic/
Source0:        http://search.cpan.org/CPAN/authors/id/T/TH/THALJEF/dynamic/Perl-Critic-Dynamic-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Module::Build) >= 0.36
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Devel::Symdump) >= 2.07
BuildRequires:  perl(English)
BuildRequires:  perl(Perl::Critic::Policy) >= 1.108
BuildRequires:  perl(Perl::Critic::Utils) >= 1.108
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Storable) >= 2.16
# Tests only:
BuildRequires:  perl(CGI)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Perl::Critic::Policy)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(Devel::Symdump) >= 2.07
Requires:       perl(Perl::Critic::Policy) >= 1.108
Requires:       perl(Perl::Critic::Utils) >= 1.108
Requires:       perl(Storable) >= 2.16

# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Devel::Symdump\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Perl::Critic::(Policy|Utils)\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Storable\\)$

%description
Perl::Critic is primarily used as a static source code analyzer, which means
that it never compiles or executes any of the code that it examines. But
since Perl is a dynamic language, there are certain types of problems that
cannot be discovered until the code is actually compiled.

This distribution includes Perl::Critic::DynamicPolicy, which can be used as
a base class for Policies that wish to compile the code they analyze. 

%prep
%setup -q -n Perl-Critic-Dynamic-%{version}

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
* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.04-1
- 更新到 0.04

* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 0.05-10
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.05-9
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.05-8
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.05-7
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.05-6
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.05-5
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.05-4
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 20 2012 Petr Pisar <ppisar@redhat.com> - 0.05-2
- Perl 5.16 rebuild

* Thu Jan 19 2012 Petr Pisar <ppisar@redhat.com> 0.05-1
- Specfile autogenerated by cpanspec 1.78.
