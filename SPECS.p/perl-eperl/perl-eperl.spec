Name:           perl-eperl
Version:        2.2.14
Release:        20%{?dist}
Summary:        Embedded Perl Language
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://www.ossp.org/pkg/tool/eperl/
Source0:        ftp://ftp.ossp.org/pkg/tool/eperl/eperl-%{version}.tar.gz
Patch0:         http://ftp.debian.org/pool/main/e/eperl/eperl_2.2.14-15.1.diff.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  gdbm-devel
BuildRequires:  db4-devel
BuildRequires:  perl(ExtUtils::Embed)
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
ePerl interprets an ASCII file bristled with Perl 5 program statements
by evaluating the Perl 5 code while passing through the plain ASCII
data. It can operate in various ways: As a stand-alone Unix filter or
integrated Perl 5 module for general file generation tasks and as a
powerful Webserver scripting language for dynamic HTML page
programming.

The documentation and latest release can be found on
http://www.ossp.org/pkg/tool/eperl/

Note that this package does not include the Apache::ePerl module,
which is designed for mod_perl 1.x.

%prep
%setup -q -n eperl-%{version}
%patch0 -p1
chmod u+x etc/shtool
find contrib/utils -perm +100 -type f -exec chmod 644 {} \;

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
#%{__perl} -pi -e 's/^\tLD_RUN_PATH=[^\s]+\s*/\t/' Makefile
make %{?_smp_mflags}
make -f Makefile.stand %{?_smp_mflags} eperl \
    prefix=%{_prefix} libdir=%{_datadir}/eperl

%install
rm -rf $RPM_BUILD_ROOT

# pure_install doesn't work.
make install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
make -f Makefile.stand install \
    prefix=$RPM_BUILD_ROOT%{_prefix} libdir=$RPM_BUILD_ROOT%{_datadir}/eperl

# Remove all of the Apache bits.
find $RPM_BUILD_ROOT -iname '*apache*' -exec rm -rf {} \; || :

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc ANNOUNCE ARTISTIC COPYING ChangeLog ChangeLog.1x ChangeLog.20 ChangeLog.21
%doc INSTALL.APACHE INSTALL.NSAPI KNOWN.BUGS NEWS README
%doc eperl_logo.gif eperl_powered.gif contrib/utils/
%{perl_vendorarch}/*
%{_bindir}/eperl
%{_datadir}/eperl
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 2.2.14-20
- 为 Magic 3.0 重建

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.14-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jun 16 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.2.14-18
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.14-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.2.14-16
- 661697 rebuild for fixing problems with vendorach/lib

* Sat May 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.2.14-15
- Mass rebuild with perl-5.12.0

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.2.14-14
- Mass rebuild with perl-5.12.0

* Fri Mar 12 2010 Marcela Mašláňová <mmaslano@redhat.com> - 2.2.14-13
- rebuild with new gdbm

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 2.2.14-12
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.14-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Aug 05 2008 Steven Pritchard <steve@kspei.com> 2.2.14-9
- Update to Debian's eperl_2.2.14-15.1.diff.gz.
- BR ExtUtils::Embed.
- Drop eperl-2.2.14-perl510-noDynaLoader.a.patch.

* Fri Mar 07 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.2.14-8
- actually commit patch to cvs

* Fri Mar 07 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.2.14-7
- perl 5.10 doesn't have DynaLoader.a

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.2.14-6
- Rebuild for new perl

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.2.14-5
- Autorebuild for GCC 4.3

* Tue Apr 17 2007 Steven Pritchard <steve@kspei.com> 2.2.14-4
- Fix find option order.
- Use fixperms macro instead of our own chmod incantation.
- BR ExtUtils::MakeMaker.

* Mon Aug 28 2006 Steven Pritchard <steve@kspei.com> 2.2.14-3
- Rebuild.

* Thu Jul 13 2006 Steven Pritchard <steve@kspei.com> 2.2.14-2
- Update to Debian's eperl_2.2.14-13.diff.gz.
- Spec cleanup.
- Drop docs that aren't relevant.

* Tue Jul 12 2005 Steven Pritchard <steve@kspei.com> 2.2.14-1
- Specfile autogenerated.
- Add eperl_2.2.14-12.diff.gz from Debian.
- Drop Apache::ePerl (requires mod_perl 1).
