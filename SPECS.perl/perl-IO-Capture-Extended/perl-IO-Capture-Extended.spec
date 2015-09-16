Name:           perl-IO-Capture-Extended
Version:	0.13
Release:	1%{?dist}
Summary:        Extend functionality of IO::Capture
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/IO-Capture-Extended/
Source0:        http://www.cpan.org/authors/id/J/JK/JKEENAN/IO-Capture-Extended-%{version}.tar.gz
BuildArch:      noarch
# Compile-time:
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(IO::Capture) >= 0.05
BuildRequires:  perl(IO::Capture::Stderr)
BuildRequires:  perl(IO::Capture::Stdout)
# Tests only:
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Simple) >= 0.44
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(IO::Capture) >= 0.05

%description
IO::Capture::Extended is a distribution consisting of two classes, each of
which is a collection of subroutines which are useful in extending the
functionality of CPAN modules IO::Capture::Stdout and IO::Capture::Stderr,
particularly when used in a testing context such as that provided by
Test::Simple, Test::More or other modules built on Test::Builder.

%prep
%setup -q -n IO-Capture-Extended-%{version}

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
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.13-1
- 更新到 0.13

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.11-6
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.11-5
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.11-3
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 12 2011 Petr Pisar <ppisar@redhat.com> 0.11-1
- Specfile autogenerated by cpanspec 1.78.
- BuildRoot and defattr removed from spec code.
