Name:           perl-CPAN-Checksums
Version:	2.10
Release:	1%{?dist}
Summary:        Write a CHECKSUMS file for a directory as on CPAN
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/CPAN-Checksums/
Source0:        http://www.cpan.org/authors/id/A/AN/ANDK/CPAN-Checksums-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Compress::Bzip2)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(Data::Compare)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::MD5) >= 2.36
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(DirHandle)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::File) >= 1.14
BuildRequires:  perl(Module::Signature)
BuildRequires:  perl(Safe)
BuildRequires:  perl(Test::More)
# Optional tests
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 0.18
Requires:       perl(Safe)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Write a CHECKSUMS file for a directory as on CPAN.

%prep
%setup -q -n CPAN-Checksums-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} %{buildroot}/*

%check
# test checks MANIFEST -  would fail because of debug files
rm -rf ./debugfiles.list ./debuglinks.list ./debugsources.list


%files
%doc README Todo
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 2.10-1
- 更新到 2.10

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 2.08-7
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 2.08-6
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 2.08-5
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 2.08-4
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 2.08-3
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 30 2011 Petr Sabata <contyk@redhat.com> - 2.08-1
- 2.08 bump
- Drop now obsolete BuildRoot and defattr

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 2.07-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 23 2010 Petr Sabata <psabata@redhat.com> - 2.07-1
- New upstream release, v2.07

* Wed Oct 27 2010 Petr Pisar <ppisar@redhat.com> - 2.06-3
- 2.06 bump

* Tue Sep 14 2010 Petr Pisar <ppisar@redhat.com> - 2.05-2
- Do POD tests

* Tue Sep 14 2010 Petr Pisar <ppisar@redhat.com> - 2.05-1
- 2.05 bump
- Add missing BuildRequires that overlay perl package Provides

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.04-3
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 2.04-2
- rebuild against perl 5.10.1

* Wed Nov 18 2009 Marcela Mašláňová <mmaslano@redhat.com> 2.04-1
- Specfile autogenerated by cpanspec 1.78.
