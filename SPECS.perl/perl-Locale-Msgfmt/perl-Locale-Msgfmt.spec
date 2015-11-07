Name:           perl-Locale-Msgfmt
Version:        0.15
Release:        9%{?dist}
Summary:        Compile .po files to .mo files
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Locale-Msgfmt/
Source0:        http://search.cpan.org/CPAN/authors/id/A/AZ/AZAWAWI/Locale-Msgfmt-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module does the same thing as msgfmt from GNU gettext-tools, 
except this is pure Perl. The interface is best explained through
examples on home page.

%prep
%setup -q -n Locale-Msgfmt-%{version}

%build
%{__perl} Makefile.PL installdirs=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT%{_bindir}
cp -v script/msgfmt.pl $RPM_BUILD_ROOT%{_bindir}
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
%{_bindir}/msgfmt.pl
%{_mandir}/man3/*

%changelog
* Mon Nov 02 2015 Liu Di <liudidi@gmail.com> - 0.15-9
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.15-8
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.15-7
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.15-6
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.15-5
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.15-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov 19 2010 Petr Sabata <psabata@redhat.com> - 0.15-1
- New upstream version, v0.15
- Now uses ExtUtils::MakeMaker

* Mon May 03 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.14-3
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.14-2
- rebuild against perl 5.10.1

* Fri Aug 14 2009 Marcela Mašláňová <mmaslano@redhat.com> 0.14-1
- Specfile autogenerated by cpanspec 1.78.
