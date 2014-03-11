Name:           perl-Test-Trap
Version:        0.2.2
Release:        4%{?dist}
Summary:        Trap exit codes, exceptions, output, etc
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Test-Trap/
Source0:        http://www.cpan.org/authors/id/E/EB/EBHANSSEN/Test-Trap-v%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl >= 1:v5.6.2
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Tester) >= 0.107
BuildRequires:  perl(version)
Requires:       perl(Test::More)
Requires:       perl(Test::Tester) >= 0.107
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Primarily (but not exclusively) for use in test scripts: A block eval on
steroids, configurable and extensible, but by default trapping (Perl)
STDOUT, STDERR, warnings, exceptions, would-be exit codes, and return
values from boxed blocks of test code.

%prep
%setup -q -n Test-Trap-v%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%defattr(-,root,root,-)
%doc Changes README xt
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jan 15 2013 Liu Di <liudidi@gmail.com> - 0.2.2-4
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.2.2-2
- Perl 5.16 rebuild

* Thu May 31 2012 Petr Pisar <ppisar@redhat.com> - 0.2.2-1
- 0.2.2 bump (fixes temporary file handling and internal tests)

* Thu May 31 2012 Petr Pisar <ppisar@redhat.com> - 0.2.1-4
- Round Module::Build version to 2 digits

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.2.1-2
- Perl mass rebuild

* Mon May 02 2011 Petr Sabata <psabata@redhat.com> - 0.2.1-1
- Specfile autogenerated by cpanspec 1.78.
- Buildroot stuff removed
