Name:           perl-Getopt-Long
Version:        2.47
Release:        3%{?dist}
Summary:        Extended processing of command line options
License:        GPLv2+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Getopt-Long/
Source0:        http://www.cpan.org/authors/id/J/JV/JV/Getopt-Long-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 5.0
BuildRequires:  perl(lib)
# Run-time:
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(vars)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(overload)
Requires:       perl(Text::ParseWords)
# Recommended:
Requires:       perl(Pod::Usage) >= 1.14
# Dependencies on these Perl 4 files are generated as perl(foo.pl):
Provides:       perl(newgetopt.pl) = %{version}

%description
The Getopt::Long module implements an extended getopt function called
GetOptions(). It parses the command line from @ARGV, recognizing and removing
specified options and their possible values.  It adheres to the POSIX syntax
for command line options, with GNU extensions. In general, this means that
options have long names instead of single letters, and are introduced with
a double dash "--". Support for bundling of command line options, as was the
case with the more traditional single-letter approach, is provided but not
enabled by default.

%prep
%setup -q -n Getopt-Long-%{version}

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
%doc CHANGES examples README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Nov 02 2015 Liu Di <liudidi@gmail.com> - 2.47-3
- 为 Magic 3.0 重建

* Wed Sep 16 2015 Liu Di <liudidi@gmail.com> - 2.47-2
- 为 Magic 3.0 重建

* Wed Jun 17 2015 Petr Pisar <ppisar@redhat.com> - 2.47-1
- 2.47 bump

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.46-2
- Perl 5.22 rebuild

* Tue Jun 02 2015 Petr Pisar <ppisar@redhat.com> - 2.46-1
- 2.46 bump

* Tue Feb 24 2015 Petr Pisar <ppisar@redhat.com> - 2.45-1
- 2.45 bump

* Thu Feb 19 2015 Petr Pisar <ppisar@redhat.com> - 2.44-1
- 2.44 bump

* Fri Jan 30 2015 Petr Pisar <ppisar@redhat.com> - 2.43-1
- 2.43 bump

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.42-310
- Increase release to favour standalone package

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.42-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Oct 02 2013 Petr Pisar <ppisar@redhat.com> - 2.42-1
- 2.42 bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.41-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 2.41-2
- Link minimal build-root packages against libperl.so explicitly

* Wed Jul 10 2013 Petr Pisar <ppisar@redhat.com> - 2.41-1
- 2.41 bump

* Thu Jun 20 2013 Petr Pisar <ppisar@redhat.com> - 2.40-1
- 2.40 bump

* Fri Apr 05 2013 Petr Pisar <ppisar@redhat.com> 2.39-1
- Specfile autogenerated by cpanspec 1.78.
