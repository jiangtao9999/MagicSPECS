Name:           perl-Catalyst-View-Component-SubInclude
Version:        0.10
Release:        19%{?dist}
Summary:        Use subincludes in your Catalyst views
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Catalyst-View-Component-SubInclude/
Source0:        http://www.cpan.org/authors/id/B/BO/BOBTFISH/Catalyst-View-Component-SubInclude-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Catalyst::Action::RenderView)
BuildRequires:  perl(Catalyst::Plugin::SubRequest)
# perl-Catalyst-Runtime provides unversioned perl(Catalyst::Runtime)
# Ensure that we really have a good version
BuildRequires:  perl(Catalyst) >= 5.80014
BuildRequires:  perl(Catalyst::Runtime) >= 5.80014
BuildRequires:  perl(Catalyst::View::TT)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Copy::Recursive)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(URI)
Requires:       perl(Catalyst::Plugin::SubRequest)
# perl-Catalyst-Runtime provides unversioned perl(Catalyst::Runtime)
# Ensure that we really have a good version
Requires:       perl(Catalyst) >= 5.80014
Requires:       perl(Catalyst::Runtime) >= 5.80014
Requires:       perl(Catalyst::View::TT)
Requires:       perl(MooseX::Types)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
Catalyst::View::Component::SubInclude allows you to include content in your
templates (or, more generally, somewhere in your view's render processing)
which comes from another action in your application. It's implemented as a
Moose::Role, so using Moose in your view is required.

%prep
%setup -q -n Catalyst-View-Component-SubInclude-%{version}

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
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.10-19
- 为 Magic 3.0 重建

* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 0.10-18
- 为 Magic 3.0 重建

* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 0.10-17
- 为 Magic 3.0 重建

* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 0.10-16
- 为 Magic 3.0 重建

* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 0.10-15
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.10-14
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.10-13
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.10-12
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.10-11
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.10-10
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.10-9
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 0.10-8
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.10-7
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.10-6
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.10-5
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.10-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Iain Arnell <iarnell@gmail.com> 0.10-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.09-4
- 661697 rebuild for fixing problems with vendorach/lib

* Thu Jul 01 2010 Iain Arnell <iarnell@gmail.com> 0.09-3
- Require perl(Catalyst) >= 5.80014

* Thu Jul 01 2010 Iain Arnell <iarnell@gmail.com> 0.09-2
- remove automatically detected explicit requires

* Wed Jun 30 2010 Iain Arnell <iarnell@gmail.com> 0.09-1
- Specfile autogenerated by cpanspec 1.78.
