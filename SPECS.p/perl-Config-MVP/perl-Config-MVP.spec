Name:           perl-Config-MVP
Version:        2.200001
Release:        7%{?dist}
Summary:        Multivalue-property package-oriented configuration
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Config-MVP/
Source0:        http://www.cpan.org/authors/id/R/RJ/RJBS/Config-MVP-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Class::Load) >= 0.06
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Pluggable::Object)
BuildRequires:  perl(Moose) >= 0.91
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::OneArgNew)
BuildRequires:  perl(overload)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(Role::HasMessage)
BuildRequires:  perl(Role::Identifiable::HasIdent)
BuildRequires:  perl(StackTrace::Auto)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Throwable)
BuildRequires:  perl(Tie::IxHash)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
# not automatically detected
Requires:       perl(Throwable)
Requires:       perl(Role::Identifiable::HasIdent)
Requires:       perl(Role::HasMessage)
Requires:       perl(StackTrace::Auto)
Requires:       perl(MooseX::OneArgNew)

%{?perl_default_filter}

%description
MVP is a mechanism for loading configuration (or other information) for
libraries. It doesn't read a file or a database. It's a helper for
things that do.

%prep
%setup -q -n Config-MVP-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check


%files
%defattr(-,root,root,-)
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 2.200001-7
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 2.200001-6
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 2.200001-5
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.200001-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 2.200001-3
- Perl mass rebuild

* Fri Apr 08 2011 Iain Arnell <iarnell@gmail.com> 2.200001-2
- explicitly declare undetected requires

* Thu Mar 31 2011 Iain Arnell <iarnell@gmail.com> 2.200001-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.101650-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.101650-2
- 661697 rebuild for fixing problems with vendorach/lib

* Wed Jun 16 2010 Iain Arnell <iarnell@gmail.com> 2.101650-1
- update to latest upstream

* Mon Jun 07 2010 Iain Arnell <iarnell@gmail.com> 2.101540-1
- update to latest upstream version
- BR perl(Try::Tiny)

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.100780-2
- Mass rebuild with perl-5.12.0

* Sat Mar 20 2010 Iain Arnell <iarnell@gmail.com> 0.100780-1
- update to latest upstream version

* Thu Feb 18 2010 Iain Arnell <iarnell@gmail.com> 0.093350-1
- Specfile autogenerated by cpanspec 1.78.
- Tweak for tests
- perl_default_filter
