Name:           perl-HTML-FormHandler
Version:        0.36001
Release:        3%{?dist}
Summary:        HTML forms using Moose
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/HTML-FormHandler/
Source0:        http://www.cpan.org/authors/id/G/GS/GSHANK/HTML-FormHandler-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(aliased)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Load) >= 0.06
BuildRequires:  perl(Config::Any)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Format::Strptime)
BuildRequires:  perl(Email::Valid)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::ShareDir::Install)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(Locale::Maketext) >= 1.09
BuildRequires:  perl(Moose) >= 2.0007
BuildRequires:  perl(MooseX::Getopt) >= 0.16
BuildRequires:  perl(MooseX::Types) >= 0.20
BuildRequires:  perl(MooseX::Types::Common)
BuildRequires:  perl(MooseX::Types::LoadableClass) >= 0.006
BuildRequires:  perl(namespace::autoclean) >= 0.09
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Template)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Memory::Cycle) >= 1.04
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(Try::Tiny)
Requires:       perl(Class::Load) >= 0.06
Requires:       perl(Locale::Maketext) >= 1.09
Requires:       perl(Moose) >= 2.0007
Requires:       perl(MooseX::Getopt) >= 0.16
Requires:       perl(MooseX::Types) >= 0.20
Requires:       perl(MooseX::Types::Common)
Requires:       perl(MooseX::Types::LoadableClass) >= 0.006
Requires:       perl(namespace::autoclean) >= 0.09
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# hidden from Pause
Provides:       perl(HTML::FormHandler::Meta::Role)
Provides:       perl(HTML::FormHandler::Model::CDBI) = 0.02
Provides:       perl(HTML::FormHandler::Params)
Provides:       perl(HTML::FormHandler::Field::Repeatable::Instance)

%{?perl_default_filter}

%description
HTML::FormHandler is a form handling class that validates HTML form data and,
for database forms, saves it to the database on validation. It has field
classes that can be used for creating a set of widgets and highly automatic
templates. There are two simple rendering roles plus a set of widget roles for
individual form and field classes. FormHandler is designed to make it easy to
produce alternative rendering modules.

%prep
%setup -q -n HTML-FormHandler-%{version}

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
%doc Changes LICENSE README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.36001-3
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.36001-2
- 为 Magic 3.0 重建

* Wed Jan 25 2012 Iain Arnell <iarnell@gmail.com> 0.36001-1
- update to latest upstream version

* Mon Jan 23 2012 Iain Arnell <iarnell@gmail.com> 0.36000-1
- update to latest upstream version

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.35005-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Oct 22 2011 Iain Arnell <iarnell@gmail.com> 0.35005-1
- update to latest upstream version

* Sun Oct 02 2011 Iain Arnell <iarnell@gmail.com> 0.35003-2
- fix explicit provides - should be
  HTML::FormHandler::Field::Repeatable::Instance, not
  HTML::FormHandler::Field::Compound.

* Fri Sep 30 2011 Iain Arnell <iarnell@gmail.com> 0.35003-1
- Specfile autogenerated by cpanspec 1.78.
