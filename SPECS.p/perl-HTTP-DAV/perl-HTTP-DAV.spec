Name:           perl-HTTP-DAV
Version:        0.42
Release:        8%{?dist}
Summary:        WebDAV client library for Perl5
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/HTTP-DAV/
Source0:        http://www.cpan.org/authors/id/O/OP/OPERA/HTTP-DAV-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(LWP) >= 5.48
BuildRequires:  perl(XML::DOM)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
HTTP::DAV is a Perl API for interacting with and modifying content on
web servers using the WebDAV protocol. Now you can LOCK, DELETE and PUT
files and much more on a DAV-enabled web server.

%prep
%setup -q -n HTTP-DAV-%{version}

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
%doc Changes README TODO
%{_bindir}/dave
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_mandir}/man1/*

%changelog
* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.42-8
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.42-7
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.42-6
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.42-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.42-4
- Perl mass rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.42-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 28 2010 Steven Pritchard <steve@kspei.com> 0.42-1
- Update to 0.42.

* Fri Dec 17 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.40-3
- 661697 rebuild for fixing problems with vendorach/lib

* Tue Aug 24 2010 Adam Tkac <atkac redhat com> - 0.40-2
- rebuild

* Fri Jun 18 2010 Petr Sabata <psabata@redhat.com> - 0.40-1
- Update to the latest release
- Description updated
- BuildRequires updated
- rhbz#605662

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.35-6
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.35-5
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.35-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.35-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec 12 2008 Steven Pritchard <steve@kspei.com> 0.35-1
- Update to 0.35.
- Update Source0 URL.

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.31-2
- Rebuild for new perl

* Mon Jul 16 2007 Steven Pritchard <steve@kspei.com> 0.31-1
- Specfile autogenerated by cpanspec 1.73.
- Fix License.
- Include dave script.
