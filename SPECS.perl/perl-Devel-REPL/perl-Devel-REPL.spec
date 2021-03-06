Name:           perl-Devel-REPL
Version:	1.003027
Release:	2%{?dist}
Summary:        Modern perl interactive shell
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Devel-REPL/
Source0:        http://search.cpan.org/CPAN/authors/id/E/ET/ETHER/Devel-REPL-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(App::Nopaste)
BuildRequires:  perl(B::Keywords)
BuildRequires:  perl(CPAN)
BuildRequires:  perl(Data::Dumper::Concise)
BuildRequires:  perl(Data::Dump::Streamer)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(File::Next)
BuildRequires:  perl(Lexical::Persistence)
BuildRequires:  perl(Module::Refresh)
BuildRequires:  perl(Moose) >= 0.93
BuildRequires:  perl(MooseX::Getopt) >= 0.18
BuildRequires:  perl(MooseX::Object::Pluggable) >= 0.0009
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(PPI)
BuildRequires:  perl(Sys::SigAction)
BuildRequires:  perl(Task::Weaken)
BuildRequires:  perl(Test::More)
# undetected requires
Requires:       perl(App::Nopaste)
Requires:       perl(MooseX::Getopt) >= 0.18
Requires:       perl(MooseX::Object::Pluggable) >= 0.0009
Requires:       perl(Task::Weaken)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
This is an interactive shell for Perl, commonly known as a REPL - Read,
Evaluate, Print, Loop. The shell provides for rapid development or testing
of code without the need to create a temporary source code file.

%prep
%setup -q -n Devel-REPL-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README examples
%{perl_vendorlib}/*
%{_bindir}/*
%{_mandir}/man3/*

%changelog
* Mon Nov 02 2015 Liu Di <liudidi@gmail.com> - 1.003027-2
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 1.003027-1
- 更新到 1.003027

* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 1.003015-5
- 为 Magic 3.0 重建

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.003015-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 05 2013 Petr Pisar <ppisar@redhat.com> - 1.003015-3
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.003015-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 08 2013 Iain Arnell <iarnell@gmail.com> 1.003015-1
- update to latest upstream version

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.003014-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 04 2013 Iain Arnell <iarnell@gmail.com> 1.003014-1
- update to latest upstream version

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.003013-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 23 2012 Petr Pisar <ppisar@redhat.com> - 1.003013-2
- Perl 5.16 rebuild

* Sun May 20 2012 Iain Arnell <iarnell@gmail.com> 1.003013-1
- update to latest upstream version

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.003012-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1.003012-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.003012-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Oct 03 2010 Iain Arnell <iarnell@gmail.com> 1.003012-1
- update to latest upstream
- clean up spec for modern rpmbuild

* Wed Jun 16 2010 Iain Arnell <iarnell@gmail.com> 1.003011-1
- update to latest upstream

* Fri May 28 2010 Iain Arnell <iarnell@gmail.com> 1.003010-1
- update to latest upstream version
- use perl_default_filter and DESTDIR

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.003009-3
- Mass rebuild with perl-5.12.0

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.003009-2
- Mass rebuild with perl-5.12.0

* Tue Mar 09 2010 Iain Arnell <iarnell@gmail.com> 1.003009-1
- update to latest upstream version
- br perl(Data::Dumper::Concise)
- br perl(Sys::SigAction)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.003007-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.003007-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 07 2009 Iain Arnell <iarnell@gmail.com> 1.003007-2
- BR perl(CPAN)

* Tue Jul 07 2009 Iain Arnell <iarnell@gmail.com> 1.003007-1
- update to latest version (fixes rt#44919)

* Sat May 02 2009 Iain Arnell <iarnell@gmail.com> 1.003006-2
- remove BR perl

* Sun Apr 19 2009 Iain Arnell <iarnell@gmail.com> 1.003006-1
- Specfile autogenerated by cpanspec 1.77.
- add requires for optional modules
