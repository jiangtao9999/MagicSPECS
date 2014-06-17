Name:           perl-CGI-Application-Plugin-AutoRunmode
Version:        0.18
Release:        13%{?dist}
Summary:        CGI::App plugin to automatically register runmodes
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/CGI-Application-Plugin-AutoRunmode/
Source0:        http://www.cpan.org/authors/id/T/TH/THILO/CGI-Application-Plugin-AutoRunmode-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(CGI)
BuildRequires:  perl(CGI::Application)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This plugin for CGI::Application provides easy ways to setup run modes. You
can just write the method that implement a run mode, you do not have to
explicitly register it with CGI::App anymore.

%prep
%setup -q -n CGI-Application-Plugin-AutoRunmode-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.18-13
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.18-12
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.18-11
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.18-10
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.18-9
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.18-8
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 0.18-7
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.18-6
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.18-5
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.18-4
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.18-2
- Perl mass rebuild

* Sat Feb 19 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.18-1
- Update to 0.18

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.17-3
- 661697 rebuild for fixing problems with vendorach/lib

* Sat Dec 11 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.17-2
- Add perl(CGI) to BuildRequires. (#660755)

* Fri May 21 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.17-1
- Update to 0.17.

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.16-5
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.16-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 19 2009 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 0.16-2
- Add Test::More to BuildRequires

* Tue May 05 2009 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 0.16-1
- Update to 0.16

* Mon Dec 22 2008 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 0.15-1
- Specfile autogenerated by cpanspec 1.77.
