Name:           perl-Module-Install-ReadmeFromPod
Version:        0.18
Release:        8%{?dist}
Summary:        Module::Install extension to automatically convert POD to a README
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Module-Install-ReadmeFromPod/
Source0:        http://www.cpan.org/authors/id/B/BI/BINGOS/Module-Install-ReadmeFromPod-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl >= 1:5.6.0
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(base)
BuildRequires:  perl(Capture::Tiny) >= 0.05
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Install) >= 1
BuildRequires:  perl(Module::Install::AutoLicense)
BuildRequires:  perl(Module::Install::Base)
BuildRequires:  perl(Module::Install::GithubMeta)
BuildRequires:  perl(Pod::Html)
BuildRequires:  perl(Pod::Man)
BuildRequires:  perl(Pod::Text) >= 3.13
BuildRequires:  perl(Test::More) >= 0.47
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
Requires:       perl(Module::Install) >= 1
Requires:       perl(Pod::Html)
Requires:       perl(Pod::Man)
Requires:       perl(Pod::Text) >= 3.13
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Module::Install::ReadmeFromPod is a Module::Install extension that
generates a README file automatically from an indicated file containing
POD, whenever the author runs Makefile.PL. Several output formats are
supported: plain-text, HTML, PDF or manual page.

%prep
%setup -q -n Module-Install-ReadmeFromPod-%{version}
rm -r inc
sed -i -e '/^inc\// d' MANIFEST
find -type f -exec chmod -x {} +

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check


%files
%doc Changes LICENSE tools
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.18-8
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.18-7
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.18-6
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.18-5
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.18-4
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.18-3
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.18-2
- 为 Magic 3.0 重建

* Fri Jun 22 2012 Jitka Plesnikova <jplesnik@redhat.com> 0.18-1
- Specfile autogenerated by cpanspec 1.78.
