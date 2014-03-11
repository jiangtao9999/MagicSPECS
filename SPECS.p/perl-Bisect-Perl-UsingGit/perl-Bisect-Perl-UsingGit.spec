Name:           perl-Bisect-Perl-UsingGit
Version:        0.33
Release:        4%{?dist}
Summary:        Help you to bisect Perl
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Bisect-Perl-UsingGit/
Source0:        http://www.cpan.org/authors/id/L/LB/LBROCARD/Bisect-Perl-UsingGit-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::Getopt)
BuildRequires:  perl(MooseX::Types::Path::Class)
# Tests only:
BuildRequires:  perl(Test::More) >= 0.01
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.14
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       git
Requires:       perl(MooseX::Getopt)

%description
Bisect::Perl::UsingGit is a module which holds the code which helps you to
bisect Perl. See bisect_perl_using_git for practical examples.

%prep
%setup -q -n Bisect-Perl-UsingGit-%{version}

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
%doc CHANGES
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.33-4
- 为 Magic 3.0 重建

* Sat Jan 28 2012 Liu Di <liudidi@gmail.com> - 0.33-3
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 30 2011 Petr Pisar <ppisar@redhat.com> 0.33-1
- Specfile autogenerated by cpanspec 1.78.
- Remove BuildRoot and defattr spec code
