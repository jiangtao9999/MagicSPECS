Name:           perl-Module-Install-Repository
Version:        0.06
Release:        6%{?dist}
Summary:        Automatically sets repository URL from Svn/Svk/Git checkout
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Module-Install-Repository/
Source0:        http://www.cpan.org/authors/id/M/MI/MIYAGAWA/Module-Install-Repository-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl >= 0:5.005
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(base)
BuildRequires:  perl(Module::Install::AuthorTests)
BuildRequires:  perl(Module::Install::Base)
BuildRequires:  perl(Module::Install::TestBase)
# Tests
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Module::Install::Repository is a Module::Install plugin to automatically
figure out repository URL and set it via repository() which then will be
added to resources under META.yml.

%prep
%setup -q -n Module-Install-Repository-%{version}
rm -r inc
sed -i -e '/^inc\// d' MANIFEST
sed -i -e '/^auto_set_repository/ d' Makefile.PL
find -type f -exec chmod -x {} +

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
rm -r inc/.author
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
* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.06-6
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.06-5
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.06-4
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 0.06-2
- Perl 5.16 rebuild

* Wed May 16 2012 Jitka Plesnikova <jplesnik@redhat.com> 0.06-1
- Specfile autogenerated by cpanspec 1.78.
