Name:           perl-Daemon-Generic
Version:        0.81
Release:        7%{?dist}
Summary:        Framework to provide start/stop/reload for a daemon
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Daemon-Generic/
Source0:        http://www.cpan.org/authors/id/M/MU/MUIR/modules/Daemon-Generic-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(Eval::LineNumbers)
BuildRequires:  perl(Event)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Flock)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
Daemon::Generic provides a framework for starting, stopping, reconfiguring
daemon-like programs. The framework provides for standard commands that
work for as init.d files and as apachectl-like commands.

%prep
%setup -q -n Daemon-Generic-%{version}

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
%doc CHANGELOG README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.81-7
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.81-6
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 0.81-5
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.81-4
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.81-3
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.81-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Aug 03 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.81-1
- Update to 0.81

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.72-2
- Perl mass rebuild

* Sun May 22 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.72-1
- Update to 0.71
- Spec clean-up

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.71-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.71-2
- 661697 rebuild for fixing problems with vendorach/lib

* Sat Jul 17 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.71-1
- Update to 0.71

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.61-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.61-3
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.61-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May 05 2009 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 0.61-1
- Update to 0.61

* Mon Dec 29 2008 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 0.51-1
- Specfile autogenerated by cpanspec 1.77.
- Minor fixes
