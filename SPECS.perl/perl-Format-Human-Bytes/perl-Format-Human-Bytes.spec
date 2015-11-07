Name:           perl-Format-Human-Bytes
Version:        0.06
Release:        11%{?dist}
Summary:        Format a bytecount and make it human readable
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Format-Human-Bytes/
Source0:        http://www.cpan.org/authors/id/S/SE/SEWI/Format-Human-Bytes-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Patch0:         Format-Human-Bytes-no-autoinstall.patch
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Module::Install)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module returns you a printable string which is more readable by humans than 
a simple bytecount.

%prep
%setup -q -n Format-Human-Bytes-%{version}
%patch0 -p1 -b .noautoinstall

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
* Mon Nov 02 2015 Liu Di <liudidi@gmail.com> - 0.06-11
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.06-10
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.06-9
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 0.06-8
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.06-7
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.06-6
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.06-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.06-2
- 661697 rebuild for fixing problems with vendorach/lib

* Wed Sep 15 2010 Petr Sabata <psabata@redhat.com> - 0.06-1
- New release, v0.06
- License changed to Perl (GPL+ or Artistic)

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.04-2
- Mass rebuild with perl-5.12.0

* Wed Nov 18 2009 Marcela Mašláňová <mmaslano@redhat.com> 0.04-1
- Specfile autogenerated by cpanspec 1.78.
