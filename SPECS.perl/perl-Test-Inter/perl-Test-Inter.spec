Name:           perl-Test-Inter
Version:	1.06
Release:	1%{?dist}
Summary:        Framework for more readable interactive test scripts
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Test-Inter/
Source0:        http://www.cpan.org/authors/id/S/SB/SBECK/Test-Inter-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Module::Build)
# Tests only:
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This is another framework for writing test scripts. It is loosely inspired
by Test::More, and has most of it's functionality, but it is not a drop-in
replacement.

%prep
%setup -q -n Test-Inter-%{version}
chmod -x examples/*

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 1.06-1
- 更新到 1.06

* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 1.03-12
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 1.03-11
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 1.03-10
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.03-9
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.03-8
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.03-7
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 1.03-6
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 1.03-4
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 18 2011 Petr Sabata <contyk@redhat.com> - 1.03-2
- Perl mass rebuild

* Thu Jul 07 2011 Petr Pisar <ppisar@redhat.com> - 1.03-1
- 1.03 bump

* Fri Jun 24 2011 Petr Pisar <ppisar@redhat.com> - 1.02-1
- 1.02 bump
- Move to vendor path
- Remove BuildRoot and defattr

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.01-4
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.01-2
- 661697 rebuild for fixing problems with vendorach/lib

* Tue Sep 14 2010 Petr Pisar <ppisar@redhat.com> 1.01-1
- Specfile autogenerated by cpanspec 1.78.
- Add BuildRequires covered by perl package
- Distribute examples
- Install into perl core (i.e. do not use vendor paths)
