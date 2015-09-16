Name:           perl-MooseX-Types-LoadableClass
Version:	0.014
Release:	1%{?dist}
Summary:        ClassName type constraint with coercion to load the class
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/MooseX-Types-LoadableClass/
Source0:        http://www.cpan.org/authors/id/E/ET/ETHER/MooseX-Types-LoadableClass-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(Module::Build::Tiny) >= 0.030
# Run-time:
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Requirements)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
ClassName type constraint with coercion to load the class.

%prep
%setup -q -n MooseX-Types-LoadableClass-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
./Build

%install
./Build install '--destdir=%{buildroot}' --create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.014-1
- 更新到 0.014

* Thu Jun 19 2014 Liu Di <liudidi@gmail.com> - 0.012-3
- 为 Magic 3.0 重建

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.012-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 09 2014 Petr Pisar <ppisar@redhat.com> - 0.012-1
- 0.012 bump

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 0.008-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.008-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.008-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 0.008-2
- Perl 5.16 rebuild

* Wed Mar 14 2012 Iain Arnell <iarnell@gmail.com> 0.008-1
- update to latest upstream

* Tue Feb 21 2012 Iain Arnell <iarnell@gmail.com> 0.007-1
- update to latest upstream version

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.006-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 29 2011 Iain Arnell <iarnell@gmail.com> 0.006-1
- Specfile autogenerated by cpanspec 1.78.
