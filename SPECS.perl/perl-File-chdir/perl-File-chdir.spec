Name:           perl-File-chdir
Version:	0.1010
Release:	2%{?dist}
Summary:        A more sensible way to change directories
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/File-chdir/
Source0:        http://www.cpan.org/modules/by-module/File/File-chdir-%{version}.tar.gz
BuildRequires:  perl(Cwd) >= 3.16
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec) >= 3.27
BuildRequires:  perl(File::Spec::Functions) >= 3.27
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More)
BuildArch:      noarch
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Perl's chdir() has the unfortunate problem of being very, very, very
global. If any part of your program calls chdir() or if any library you
use calls chdir(), it changes the current working directory for the
whole program.

%prep
%setup -q -n File-chdir-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type d -depth -exec rmdir {} 2>/dev/null \;
chmod -R u+rwX,go+rX,go-w %{buildroot}/*

%check


%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Nov 02 2015 Liu Di <liudidi@gmail.com> - 0.1010-2
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.1010-1
- 更新到 0.1010

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.1007-4
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 0.1007-3
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.1007-2
- 为 Magic 3.0 重建

* Wed Sep 19 2012 Petr Pisar <ppisar@redhat.com> - 0.1007-1
- 0.1007 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1006-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.1006-2
- Perl 5.16 rebuild

* Wed Jan 11 2012 Petr Šabata <contyk@redhat.com> - 0.1006-1
- 0.1006 bump

* Sat Jun 18 2011 Iain Arnell <iarnell@gmail.com> 0.1003-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.09-10
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.09-8
- 661697 rebuild for fixing problems with vendorach/lib

* Sat May 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.09-7
- Mass rebuild with perl-5.12.0

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.09-6
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.09-5
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Mar  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.09-2
- rebuild for new perl

* Thu Jan 17 2008 Ian Burrell <ianburrell@gmail.com> - 0.09-1
- Update to 0.09

* Thu Aug 16 2007 Ian M. Burrell <ianburrell@gmail.com> - 0.06-3
- Fix BuildRequires

* Tue Jun 27 2006 Ian M. Burrell <ianburrell@gmail.com> - 0.06-2
- Fix rpmlint warnings

* Thu Mar 30 2006 Ian Burrell <ianburrell@gmail.com> 0.06-1
- Specfile autogenerated by cpanspec 1.64.
