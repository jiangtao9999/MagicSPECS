Name:           perl-Image-Math-Constrain
Version:        1.02
Release:        14%{?dist}
Summary:        Scaling math used in image size constraining (such as thumbnails)
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Image-Math-Constrain/
Source0:        http://www.cpan.org/authors/id/A/AD/ADAMK/Image-Math-Constrain-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Pod) >= 1.26
BuildRequires:  perl(Test::More) >= 0.47
BuildRequires:  perl(Test::CPAN::Meta) >= 0.12
BuildRequires:  perl(Test::MinimumVersion) >= 0.008
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
There are a number of different modules and systems that constrain image
sizes, such as thumbnailing. Every one of these independantly implement the
same logic. That is, given a width and/or height constraint, they check to
see if the image is bigger than the constraint, and if so scale the image
down proportionally so that it fits within the constraints.

%prep
%setup -q -n Image-Math-Constrain-%{version}

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
 AUTOMATED_TESTING=1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 1.02-14
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.02-13
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 1.02-12
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 1.02-11
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.02-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1.02-9
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.02-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 17 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.02-7
- 661697 rebuild for fixing problems with vendorach/lib

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.02-6
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.02-5
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.02-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.02-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Aug 05 2008 Steven Pritchard <steve@kspei.com> 1.02-1
- Update to 1.02.
- BR Test::More, Test::CPAN::Meta, and Test::MinimumVersion.
- Set AUTOMATED_TESTING so we run the pod and meta tests.

* Wed Mar 05 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.01-2
- rebuild for new perl

* Mon Apr 02 2007 Steven Pritchard <steve@kspei.com> 1.01-1
- Specfile autogenerated by cpanspec 1.70.
- Drop redundant explicit perl build dependency.
- Fix typo in description.
- BR Test::Pod for better test coverage.
