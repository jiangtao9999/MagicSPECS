Name:           perl-Git-PurePerl
Version:	0.51
Release:	1%{?dist}
Summary:        Pure Perl interface to Git repositories
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Git-PurePerl/
Source0:        http://search.cpan.org/CPAN/authors/id/B/BR/BROQ/Git-PurePerl-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Archive::Extract)
BuildRequires:  perl(Archive::Tar)
BuildRequires:  perl(Compress::Raw::Zlib)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(Config::GitLike)
BuildRequires:  perl(Data::Stream::Bulk)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(IO::Digest)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::StrictConstructor)
BuildRequires:  perl(MooseX::Types::Path::Class)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::utf8) >= 0.02
Requires:       perl(Config::GitLike)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
This module is a Pure Perl interface to Git repositories.

%prep
%setup -q -n Git-PurePerl-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
# live tests don't work in koji
%{?!_with_live_tests: rm t/protocol*.t}


%files
%doc CHANGES README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.51-1
- 更新到 0.51

* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 0.48-14
- 为 Magic 3.0 重建

* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 0.48-13
- 为 Magic 3.0 重建

* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 0.48-12
- 为 Magic 3.0 重建

* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 0.48-11
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.48-10
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.48-9
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.48-8
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.48-7
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.48-6
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.48-5
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.48-4
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.48-3
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.48-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 26 2011 Iain Arnell <iarnell@gmail.com> 0.48-1
- update to latest upstream
- remove test tarballs from documentation

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.47-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.47-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.47-2
- 661697 rebuild for fixing problems with vendorach/lib

* Mon Aug 30 2010 Iain Arnell <iarnell@gmail.com> 0.47-1
- update to latest upstream

* Mon Jul 19 2010 Iain Arnell <iarnell@gmail.com> 0.46-2
- update spec for modern rpmbuild

* Wed Jun 23 2010 Iain Arnell 0.46-1
- Specfile autogenerated by cpanspec 1.78.
