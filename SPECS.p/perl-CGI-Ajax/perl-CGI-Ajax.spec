Name:           perl-CGI-Ajax
Version:        0.707
Release:        11%{?dist}
Summary:        Perl-specific system for writing Asynchronous web applications
License:        GPL+ or Artistic 
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/CGI-Ajax/
Source0:        http://search.cpan.org/CPAN/authors/id/B/BP/BPEDERSE/CGI-Ajax-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(CGI), perl(Class::Accessor)
BuildRequires:  perl(Test::More)

# neither are picked up automagically.
Requires:       perl(CGI), perl(Class::Accessor)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
CGI::Ajax is an object-oriented module that provides a unique mechanism for
using perl code asynchronously from javascript- enhanced HTML pages.
CGI::Ajax unburdens the user from having to write extensive javascript,
except for associating an exported method with a document-defined event
(such as onClick, onKeyUp, etc). CGI::Ajax also mixes well with HTML
containing more complex javascript.

%prep
%setup -q -n CGI-Ajax-%{version}

find scripts/ -type f -exec chmod -c -x {} + 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} +
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc Changes LICENSE README Todo scripts/
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.707-11
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.707-10
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.707-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.707-8
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.707-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.707-6
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.707-5
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.707-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.707-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.707-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Oct 23 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.707-1
- update to 0.707-1

* Mon Sep 08 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.706-1
- update to 0.706

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.701-4
- Rebuild for new perl

* Tue Jan 08 2008 Ralf Corsépius <rc040203@freenet.de> 0.701-3
- Update License-tag.
- BR: perl(Test::More) (BZ 419631).

* Mon Apr 16 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.701-2
- bump

* Mon Apr 09 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.701-1
- Specfile autogenerated by cpanspec 1.70.
