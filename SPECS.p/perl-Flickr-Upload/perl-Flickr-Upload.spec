Name:           perl-Flickr-Upload
Version:        1.32
Release:        21%{?dist}
Summary:        Flickr.com upload module and script
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Flickr-Upload/
Source0:        http://www.cpan.org/authors/id/C/CP/CPB/Flickr-Upload-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Flickr::API) >= 0.07
BuildRequires:  perl(HTTP::Request::Common) >= 1
BuildRequires:  perl(LWP::UserAgent) >= 1
BuildRequires:  perl(XML::Parser::Lite::Tree) >= 0.03
Requires:       perl(Flickr::API) >= 0.07
Requires:       perl(HTTP::Request::Common) >= 1
Requires:       perl(LWP::UserAgent) >= 1
Requires:       perl(XML::Parser::Lite::Tree) >= 0.03
Requires:       perl(Term::ProgressBar) >= 2.09
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Patch0: 	perl-Flickr-Upload-remotetests.patch

%description
Module and script for uploading images to flickr.com web gallery.

%prep
%setup -q -n Flickr-Upload-%{version}
%patch0 -p0 -b .remotetests

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
%doc ChangeLog README
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_bindir}/flickr_upload
%{_mandir}/man1/flickr_upload.1.gz


%changelog
* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 1.32-21
- 为 Magic 3.0 重建

* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 1.32-20
- 为 Magic 3.0 重建

* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 1.32-19
- 为 Magic 3.0 重建

* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 1.32-18
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 1.32-17
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 1.32-16
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.32-15
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.32-14
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.32-13
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.32-12
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 1.32-11
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 1.32-10
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 1.32-9
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.32-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1.32-7
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.32-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.32-5
- 661697 rebuild for fixing problems with vendorach/lib

* Sat May 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.32-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.32-3
- rebuild against perl 5.10.1

* Wed Aug 12 2009 Michal Ingeli <mi@v3.sk> 1.32-2
- Added missing buildrequire for Test::Simple
- Removed test that interact with api.flickr.com

* Sun Jun 21 2009 Michal Ingeli <mi@v3.sk> 1.32-1
- Specfile autogenerated by cpanspec 1.77.
