%global cpan_version 5.1
Name:           perl-Module-Pluggable
# Epoch to compete with perl.spec
Epoch:          1
# Keep two digit decimal part
Version:        %{cpan_version}0
Release:        2%{?dist}
Summary:        Automatically give your module the ability to have plugins
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Module-Pluggable/
Source0:        http://www.cpan.org/authors/id/S/SI/SIMONW/Module-Pluggable-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
%if 0%(perl -e 'print $] > 5.017')
BuildRequires:  perl(deprecate)
%endif
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec::Functions) >= 3.00
BuildRequires:  perl(if)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 0.62
BuildRequires:  perl(warnings)
# Optional tests:
# App::FatPacker not yet packaged
#%%if !%%{defined perl_bootstrap}
#BuildRequires:  perl(App::FatPacker) >= 0.10.0
#BuildRequires:  perl(Cwd)
#BuildRequires:  perl(File::Copy)
#BuildRequires:  perl(File::Path)
#BuildRequires:  perl(File::Temp)
#%%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(File::Spec::Functions) >= 3.00
%if 0%(perl -e 'print $] > 5.017')
Requires:       perl(deprecate)
%endif

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(File::Spec::Functions\\)$

%description
This package provides a simple but, hopefully, extensible way of having
'plugins' for your module. Essentially all it does is export a method into
your name space that looks through a search path for .pm files and turn those
into class names. Optionally it instantiates those classes for you.

%prep
%setup -q -n Module-Pluggable-%{cpan_version}
find -type f -exec chmod -x {} +

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan 06 2014 Petr Pisar <ppisar@redhat.com> - 1:5.10-1
- 5.1 bump

* Mon Jan 06 2014 Petr Pisar <ppisar@redhat.com> - 1:5.00-1
- 5.0 bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.80-291
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 15 2013 Petr Pisar <ppisar@redhat.com> - 1:4.80-290
- Increase release to favour standalone package

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 1:4.8-2
- Perl 5.18 rebuild

* Tue May 28 2013 Petr Pisar <ppisar@redhat.com> - 1:4.8-1
- 4.8 bump

* Thu Feb 28 2013 Petr Pisar <ppisar@redhat.com> - 1:4.7-1
- 4.7 bump

* Thu Jan 24 2013 Petr Pisar <ppisar@redhat.com> 1:4.6-1
- Specfile autogenerated by cpanspec 1.78.
