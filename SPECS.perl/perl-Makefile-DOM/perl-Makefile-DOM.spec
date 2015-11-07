Name:           perl-Makefile-DOM
Version:	0.008
Release:	2%{?dist}
Summary:        Simple DOM parser for Makefiles
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Makefile-DOM/
Source0:        http://www.cpan.org/authors/id/A/AG/AGENT/Makefile-DOM-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl >= 1:5.6.1
BuildRequires:  perl(Clone) >= 0.18
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(List::MoreUtils) >= 0.21
BuildRequires:  perl(Params::Util) >= 0.22
BuildRequires:  perl(CPAN)
BuildRequires:  perl(ExtUtils::Embed)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Simple)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This libary can serve as an advanced lexer for (GNU) makefiles. It parses
makefiles as "documents" and the parsing is lossless. The results are data
structures similar to DOM trees. The DOM trees hold every single bit of the
information in the original input files, including white spaces, blank
lines and makefile comments. That means it's possible to reproduce the
original makefiles from the DOM trees. In addition, each node of the DOM
trees is modifiable and so is the whole tree, just like the PPI module used
for Perl source parsing and the HTML::TreeBuilder module used for parsing
HTML source.

%prep
%setup -q -n Makefile-DOM-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} %{buildroot}/*

%check


%files
%doc Changes README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Nov 02 2015 Liu Di <liudidi@gmail.com> - 0.008-2
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.008-1
- 更新到 0.008

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.006-10
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.006-9
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.006-8
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.006-7
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.006-6
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.006-5
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.006-4
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.006-3
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.006-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 29 2011 Petr Sabata <contyk@redhat.com> - 0.006-1
- 0.006 bump

* Thu Aug 18 2011 Petr Sabata <contyk@redhat.com> - 0.005-1
- 0.005 bump
- Removing now obsolete Buildroot and defattr
- Useless Requires and Provides removed
- Changelog corrected (whitespace)

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.004-7
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.004-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.004-5
- 661697 rebuild for fixing problems with vendorach/lib

* Mon May 03 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.004-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.004-3
- rebuild against perl 5.10.1

* Tue Sep 08 2009 Ryan Lerch <rlerch@redhat.com> 0.004-2
- Added BuildRequires and Provides lines to the specfile, as per the Fedora Perl Packaging Guidelines. 

* Mon Sep 07 2009 Ryan Lerch <rlerch@redhat.com> 0.004-1
- Specfile autogenerated by cpanspec 1.78.
