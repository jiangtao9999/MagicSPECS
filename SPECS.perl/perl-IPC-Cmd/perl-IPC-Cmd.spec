Name:           perl-IPC-Cmd
# Epoch to compete with perl.spec
Epoch:          1
Version:        0.92
Release:        4%{?dist}
Summary:        Finding and running system commands made easy
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/IPC-Cmd/
Source0:        http://www.cpan.org/authors/id/B/BI/BINGOS/IPC-Cmd-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Locale::Maketext::Simple)
BuildRequires:  perl(Module::Load::Conditional)
BuildRequires:  perl(Params::Check) >= 0.20
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(vars)
# Tests:
# output.pl/IO::Handle not used
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(ExtUtils::MakeMaker)
Requires:       perl(FileHandle)
Requires:       perl(IO::Handle)
Requires:       perl(IO::Select)
Requires:       perl(IPC::Open3)
Requires:       perl(Params::Check) >= 0.20
Requires:       perl(POSIX)

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Params::Check\\)$

%description
IPC::Cmd allows you to run commands platform independently, interactively
if desired, but have them still work.

%prep
%setup -q -n IPC-Cmd-%{version}

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
%doc CHANGES README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 1:0.92-4
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 1:0.92-3
- 为 Magic 3.0 重建

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.92-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 23 2014 Petr Pisar <ppisar@redhat.com> - 1:0.92-1
- 0.92 bump

* Tue Nov 19 2013 Petr Pisar <ppisar@redhat.com> - 1:0.90-1
- 0.90 bump

* Tue Nov 05 2013 Petr Pisar <ppisar@redhat.com> - 1:0.86-1
- 0.86 bump

* Thu Aug 08 2013 Petr Pisar <ppisar@redhat.com> - 1:0.84-1
- 0.84 bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.82-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 1:0.82-2
- Perl 5.18 rebuild

* Mon Jul 08 2013 Petr Pisar <ppisar@redhat.com> - 1:0.82-1
- 0.82 bump

* Mon May 20 2013 Petr Pisar <ppisar@redhat.com> - 1:0.80-3
- Remove unneeded dependency on Config

* Thu Mar 14 2013 Petr Pisar <ppisar@redhat.com> - 1:0.80-2
- Set epoch to compete with core module from perl.spec

* Mon Mar 04 2013 Petr Pisar <ppisar@redhat.com> - 0.80-1
- 0.80 bump

* Fri Feb 08 2013 Petr Pisar <ppisar@redhat.com> 0.78-1
- Specfile autogenerated by cpanspec 1.78.
