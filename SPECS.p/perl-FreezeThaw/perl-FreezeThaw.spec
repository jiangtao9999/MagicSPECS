Name:           perl-FreezeThaw
Version:        0.5001
Release:        9%{?dist}
Summary:        Convert Perl structures to strings and back

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/FreezeThaw/
Source0:        http://www.cpan.org/authors/id/I/IL/ILYAZ/modules/FreezeThaw-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Converts data to/from stringified form, appropriate for
saving-to/reading-from permanent storage.


%prep
%setup -q -n FreezeThaw-%{version}
# Fix permissions
find -type d -exec chmod 0755 {} \;
find -type f -exec chmod 0644 {} \;

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check



%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3pm*


%changelog
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.5001-9
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5001-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 0.5001-7
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5001-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 15 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.5001-5
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5001-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.5001-3
- 661697 rebuild for fixing problems with vendorach/lib

* Fri May 14 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.5001-2
- Bump version for perl-5.12.0.

* Sat May 08 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.5001-1
- Upstream update (Fix perl-5.12.0 build breakdown).

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.45-5
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.45-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.45-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.45-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 12 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.45-1
- Upstream update.
- Fix source permissions.

* Sat Feb  2 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.43-6
- rebuild for new perl

* Mon Oct 15 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 0.43-5.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Thu Sep  7 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.43-5
- Rebuild for FC6.

* Thu Feb 16 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.43-4
- Rebuild for FC5 (perl 5.8.8).

* Thu Dec 29 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.43-3
- Dist tag.

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.43-2
- rebuilt

* Sun Oct 31 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:0.43-0.fdr.1
- Bring up to date with current fedora.us perl spec template.

* Tue Mar 9 2004 Steven Pritchard <steve@kspei.com> - 0.43-0.fdr.0
- Specfile autogenerated.
