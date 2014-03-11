Name:           perl-Test-UseAllModules
Version:        0.14
Release:        2%{?dist}
Summary:        Do use_ok() for all the MANIFESTed modules
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Test-UseAllModules/
Source0:        http://www.cpan.org/authors/id/I/IS/ISHIGAKI/Test-UseAllModules-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::Manifest)
# perl(Test::Builder) needed for lib/Test/UseAllModules.pm:55:
# Test::More->builder->{Have_Plan};
BuildRequires:  perl(Test::Builder) >= 0.30
BuildRequires:  perl(Test::More) >= 0.60
# Tests only:
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
Requires:       perl(Test::Builder) >= 0.30
Requires:       perl(Test::More) >= 0.60
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# Remove underspecifies dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(Test::More\\)

%description
I'm sick of writing 00_load.t (or something like that) that will do use_ok()
for every module I write. I'm sicker of updating 00_load.t when I add
another file to the distribution. This module reads MANIFEST to find modules
to be tested and does use_ok() for each of them. Now all you have to do is
update MANIFEST. You don't have to modify the test any more (hopefully).

%prep
%setup -q -n Test-UseAllModules-%{version}
for F in Changes README; do
    tr -d '\r' <"$F" >"$F.unix"
    touch -r "$F"{,.unix}
    mv "${F}"{.unix,}
done

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
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.14-2
- 为 Magic 3.0 重建

* Fri Aug 03 2012 Petr Pisar <ppisar@redhat.com> - 0.14-1
- 0.14 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 0.13-3
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 20 2011 Petr Pisar <ppisar@redhat.com> 0.13-1
- Specfile autogenerated by cpanspec 1.78.
- Remove BuildRoot and defattr code
- Recode documentation to UNIX end-of-lines
