Name:           perl-Hardware-Vhdl-Parser
Version:        0.12
Release:        15%{?dist}
Summary:        Complete grammar for parsing VHDL code using perl

License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Hardware-Vhdl-Parser/
Source0:        http://www.cpan.org/authors/id/G/GS/GSLONDON/Hardware-Vhdl-Parser-%{version}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Parse::RecDescent)

Requires:       perl(Parse::RecDescent)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))


%description
This module defines the complete grammar needed to parse any VHDL code. By
overloading this grammar, it is possible to easily create perl scripts
which run through VHDL code and perform specific functions.

%prep
%setup -q -n Hardware-Vhdl-Parser-%{version}

find . -type f | xargs %{__perl} -pi -e 's|#! /bin/perl|#! /usr/bin/perl|'

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{__rm} -f $RPM_BUILD_ROOT%{perl_vendorlib}//Hardware/Vhdl/*.pl

%{_fixperms} $RPM_BUILD_ROOT/*


%check


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes readme.txt test1.vhd
%doc parser.pl hierarchy.pl
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Nov 02 2015 Liu Di <liudidi@gmail.com> - 0.12-15
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.12-14
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.12-13
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.12-12
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.12-11
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.12-9
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 17 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.12-7
- 661697 rebuild for fixing problems with vendorach/lib

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.12-6
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.12-5
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Dec 14 2008 Chitlesh GOORAH <chitlesh [AT] fedoraproject DOT org> 0.12-2
- Fixed %%bindir

* Sun Dec 14 2008 Chitlesh GOORAH <chitlesh [AT] fedoraproject DOT org> 0.12-1
- Specfile autogenerated by cpanspec 1.77.
