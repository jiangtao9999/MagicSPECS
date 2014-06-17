Name:           perl-HTML-StripScripts-Parser
Version:        1.03
Release:        8%{?dist}
Summary:        XSS filter using HTML::Parser
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/HTML-StripScripts-Parser/
Source0:        http://search.cpan.org/CPAN/authors/id/D/DR/DRTECH/HTML-StripScripts-Parser-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTML::Parser) >= 3.56
BuildRequires:  perl(HTML::StripScripts) >= 1.04
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
Requires:       perl(HTML::Parser) >= 3.56
Requires:       perl(HTML::StripScripts) >= 1.04
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This class provides an easy interface to HTML::StripScripts, using
HTML::Parser to parse the HTML.

%prep
%setup -q -n HTML-StripScripts-Parser-%{version}

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
* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.03-8
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 1.03-7
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 1.03-6
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.03-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 17 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.03-2
- 661697 rebuild for fixing problems with vendorach/lib

* Tue Dec 14 2010 Xavier Bachelot <xavier@bachelot.org> 1.03-1
- Update to 1.03.
- Update Source0 URL.
- BuildRequires perl(Test::Pod) and perl(Test::Pod::Coverage).

* Sun Dec 12 2010 Iain Arnell <iarnell@gmail.com> 1.02-5
- doesn't require perl(Test::More)

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.02-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.02-3
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Apr 24 2009 Xavier Bachelot <xavier@bachelot.org> 1.02-1
- Specfile autogenerated by cpanspec 1.77.
