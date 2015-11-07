Name:           perl-CatalystX-SimpleLogin
Version:	0.18
Release:	2%{?dist}
Summary:        Provide a simple Login controller which can be reused
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/CatalystX-SimpleLogin/
Source0:        http://www.cpan.org/authors/id/B/BO/BOBTFISH/CatalystX-SimpleLogin-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Catalyst::Action::RenderView)
BuildRequires:  perl(Catalyst::Action::REST) >= 0.74
BuildRequires:  perl(Catalyst::ActionRole::ACL)
# not available in fedora and upstream is currently broken
# see https://rt.cpan.org/Public/Bug/Display.html?id=70417
# BuildRequires:  perl(Catalyst::Authentication::Credential::OpenID)
BuildRequires:  perl(Catalyst::Authentication::Store::DBIx::Class)
BuildRequires:  perl(Catalyst::Controller::ActionRole) >= 0.12
BuildRequires:  perl(Catalyst::Model::DBIC::Schema)
BuildRequires:  perl(Catalyst::Plugin::Authentication)
BuildRequires:  perl(Catalyst::Plugin::Session) >= 0.27
BuildRequires:  perl(Catalyst::Plugin::Session::State::Cookie)
BuildRequires:  perl(Catalyst::Plugin::Session::Store::File)
BuildRequires:  perl(Catalyst::Runtime) >= 5.80013
BuildRequires:  perl(Catalyst::View::TT)
BuildRequires:  perl(CatalystX::Component::Traits) >= 0.13
BuildRequires:  perl(CatalystX::InjectComponent)
BuildRequires:  perl(Crypt::DH)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBIx::Class::Optional::Dependencies)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTML::FormHandler) >= 0.28001
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(JSON::Any) >= 1.22
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Autobox)
BuildRequires:  perl(MooseX::MethodAttributes) >= 0.18
BuildRequires:  perl(MooseX::RelatedClassRoles) >= 0.004
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::Common)
BuildRequires:  perl(MooseX::Types::JSON) >= 0.02
BuildRequires:  perl(MooseX::Types::Path::Class) >= 0.05
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(SQL::Translator)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More) >= 0.94
Requires:       perl(Catalyst::Action::REST) >= 0.74
Requires:       perl(Catalyst::Plugin::Authentication)
Requires:       perl(Catalyst::Plugin::Session) >= 0.27
Requires:       perl(Catalyst::Runtime) >= 5.80013
Requires:       perl(Catalyst::View::TT)
Requires:       perl(CatalystX::Component::Traits) >= 0.13
Requires:       perl(HTML::FormHandler) >= 0.28001
Requires:       perl(MooseX::MethodAttributes) >= 0.18
Requires:       perl(MooseX::RelatedClassRoles) >= 0.004
Requires:       perl(MooseX::Types)
Requires:       perl(MooseX::Types::Common)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
CatalystX::SimpleLogin is an application class which provides a simple login
and logout page with the addition of only one line of code and one template to
your application.

%prep
%setup -q -n CatalystX-SimpleLogin-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check


%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Nov 02 2015 Liu Di <liudidi@gmail.com> - 0.18-2
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.18-1
- 更新到 0.18

* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 0.15-17
- 为 Magic 3.0 重建

* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 0.15-16
- 为 Magic 3.0 重建

* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 0.15-15
- 为 Magic 3.0 重建

* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 0.15-14
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.15-13
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.15-12
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.15-11
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.15-10
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.15-9
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.15-8
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 0.15-7
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.15-6
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.15-5
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.15-4
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 12 2011 Iain Arnell <iarnell@gmail.com> 0.15-2
- fix spelling in description

* Fri Sep 30 2011 Iain Arnell <iarnell@gmail.com> 0.15-1
- Specfile autogenerated by cpanspec 1.78.
