Name:           perl-podlinkcheck
Version:        12
Release:        8%{?dist}
Summary:        Check Perl POD L<> link references
License:        GPLv3+
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/podlinkcheck/
Source0:        http://www.cpan.org/authors/id/K/KR/KRYDE/podlinkcheck-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
# The inc/my_pod2html is not executed
BuildRequires:  perl(lib)
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant::defer)
BuildRequires:  perl(File::Find::Iterator)
BuildRequires:  perl(File::Spec) >= 0.8
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IPC::Run)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Locale::TextDomain)
BuildRequires:  perl(Pod::Find)
BuildRequires:  perl(Pod::Simple)
BuildRequires:  perl(Text::Tabs)
# Recommended run-time:
BuildRequires:  perl(Sort::Key::Natural)
# Tests:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::FindRef)
BuildRequires:  perl(Devel::StackTrace)
BuildRequires:  perl(File::HomeDir)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(File::Find::Iterator)
Requires:       perl(File::Spec) >= 0.8
Requires:       perl(File::Temp)
Requires:       perl(Getopt::Long)
Requires:       perl(IPC::Run)
Requires:       perl(Pod::Find)
# Recommended:
Requires:       perl(Sort::Key::Natural)
# We do not (build-)require CPAN on purpose

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(File::Spec\\)$

%description
PodLinkCheck parses Perl POD from a script, module or documentation
and checks that L<> links within it refer to a known program, module,
or man page.

%prep
%setup -q -n podlinkcheck-%{version}

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
%doc Changes COPYING
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 12-8
- 为 Magic 3.0 重建

* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 12-7
- 为 Magic 3.0 重建

* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 12-6
- 为 Magic 3.0 重建

* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 12-5
- 为 Magic 3.0 重建

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Petr Pisar <ppisar@redhat.com> - 12-2
- Perl 5.18 rebuild

* Mon Feb 18 2013 Petr Pisar <ppisar@redhat.com> - 12-1
- 12 bump

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 03 2012 Petr Pisar <ppisar@redhat.com> - 11-1
- 11 bump

* Mon Nov 26 2012 Petr Pisar <ppisar@redhat.com> - 10-1
- 10 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 28 2012 Petr Pisar <ppisar@redhat.com> - 9-2
- Perl 5.16 rebuild

* Tue Jun 19 2012 Petr Pisar <ppisar@redhat.com> - 9-1
- 9 bump

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 8-2
- Perl 5.16 rebuild

* Wed Apr 25 2012 Petr Pisar <ppisar@redhat.com> 8-1
- Specfile autogenerated by cpanspec 1.78.
