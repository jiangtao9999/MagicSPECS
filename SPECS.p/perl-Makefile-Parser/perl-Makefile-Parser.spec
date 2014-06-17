Name:           perl-Makefile-Parser
Version:        0.211
Release:        15%{?dist}
Summary:        Simple parser for Makefiles
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Makefile-Parser/
Source0:        http://www.cpan.org/authors/id/A/AG/AGENT/Makefile-Parser-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 1:5.6.1
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(Class::Trigger) >= 0.13
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(IPC::Run3) >= 0.036
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Makefile::DOM) >= 0.003
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Balanced)
Requires:       perl(Class::Accessor::Fast)
Requires:       perl(Class::Trigger) >= 0.13
Requires:       perl(File::Slurp)
Requires:       perl(List::MoreUtils)
Requires:       perl(Makefile::DOM) >= 0.003
Requires:       perl(Text::Balanced)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This is a simple parser for Makefiles. At this very early stage, the parser
only supports a limited set of features, so it may not recognize most of
the advanced features provided by certain make tools like GNU make. Its
initial purpose is to provide basic support for another module named
Makefile::GraphViz, which is aimed to render the building process specified
by a Makefile using the amazing GraphViz library. The Make module is not
satisfactory for this purpose, so I decided to build one of my own.

%prep
%setup -q -n Makefile-Parser-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

#%check
#

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_mandir}/man1/*
%{_bindir}/makesimple
%{_bindir}/pgmake-db
%{_bindir}/plmake

%changelog
* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.211-15
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.211-14
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.211-13
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.211-12
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.211-11
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.211-10
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.211-9
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.211-8
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.211-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.211-6
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.211-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.211-4
- 661697 rebuild for fixing problems with vendorach/lib

* Mon May 03 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.211-3
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.211-2
- rebuild against perl 5.10.1

* Mon Sep 07 2009 Scott Radvan <sradvan@redhat.com> 0.211-1
- Specfile autogenerated by cpanspec 1.78.
