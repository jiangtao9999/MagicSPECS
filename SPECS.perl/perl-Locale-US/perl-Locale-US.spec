Name:           perl-Locale-US
Version:	3.04
Release:	1%{?dist}
Summary:        Two letter codes for state identification in the United States and vice versa
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Locale-US/
Source0:        http://search.cpan.org/CPAN/authors/id/A/AC/ACCARDO/Locale-US-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.30
# Run-time
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::Section::Simple)
# Tests
BuildRequires:  perl(Test)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
Map from US two-letter codes to states and vice versa.

%prep
%setup -q -n Locale-US-%{version}

# doesn't actually use Data::Dumper
sed -i -e '/use Data::Dumper/d' lib/Locale/US.pm

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name kruft2codes.pl -exec rm -f {} \;
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check


%files
%doc Changes README kruft2codes.pl
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 3.04-1
- 更新到 3.04

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 2.112150-6
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 2.112150-5
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.112150-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 2.112150-3
- Perl 5.16 rebuild
- Specify all dependencies

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.112150-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Aug 28 2011 Iain Arnell <iarnell@gmail.com> 2.112150-1
- update to latest upstream
- drop unnecessary patches

* Wed Jun 15 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.2-3
- Perl mass rebuild

* Tue Mar 22 2011 Iain Arnell <iarnell@gmail.com> 1.2-2
- fix spelling in pod (rt#62218)
- install kruft2codes.pl as doc

* Thu Jan 27 2011 Iain Arnell <iarnell@gmail.com> 1.2-1
- Specfile autogenerated by cpanspec 1.78.
