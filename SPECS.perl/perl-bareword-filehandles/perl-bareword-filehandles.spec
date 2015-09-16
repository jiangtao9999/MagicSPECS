Name:           perl-bareword-filehandles
Version:        0.003
Release:        13%{?dist}
Summary:        Disables bareword filehandles
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/bareword-filehandles/
Source0:        http://www.cpan.org/authors/id/I/IL/ILMARI/bareword-filehandles-%{version}.tar.gz
# Lexical::SealRequireHints is only necessary on perl < 5.12
Patch0:         no-Lexical-SealRequireHints.patch
BuildRequires:  perl(B::Hooks::OP::Check)
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Pod::Coverage::TrustPod)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(XSLoader)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
This module lexically disables the use of bareword filehandles with built-in
functions, except for the special built-in filehandles STDIN, STDOUT,
STDERR, ARGV, ARGVOUT and DATA.

%prep
%setup -q -n bareword-filehandles-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;

%{_fixperms} %{buildroot}/*

%check
RELEASE_TESTING=1 make test

%files
%doc Changes LICENSE README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/bareword*
%{_mandir}/man3/*

%changelog
* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.003-13
- 为 Magic 3.0 重建

* Fri Apr 17 2015 Liu Di <liudidi@gmail.com> - 0.003-12
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.003-11
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.003-10
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.003-9
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.003-8
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.003-7
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.003-6
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 0.003-5
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.003-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 14 2012 Petr Pisar <ppisar@redhat.com> - 0.003-3
- Perl 5.16 rebuild

* Thu May 10 2012 Iain Arnell <iarnell@gmail.com> 0.003-2
- drop unnecessary perl BR

* Mon Apr 09 2012 Iain Arnell <iarnell@gmail.com> 0.003-1
- Specfile autogenerated by cpanspec 1.79.
- remove Lexical::SealRequireHints dependency
