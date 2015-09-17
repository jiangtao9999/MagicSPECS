Name:           perl-Struct-Dumb
Version:        0.03
Release:        4%{?dist}
Summary:        Make simple lightweight record-like structures
License:        GPL+ or Artistic

URL:            http://search.cpan.org/dist/Struct-Dumb/
Source0:        http://www.cpan.org/authors/id/P/PE/PEVANS/Struct-Dumb-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(Carp)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
Struct::Dumb creates record-like structure types, similar to the struct
keyword in C, C++ or C#, or Record in Pascal. An invocation of this module
will create a construction function which returns new object references
with the given field values. These references all respond to lvalue methods
that access or modify the values stored.

%prep
%setup -q -n Struct-Dumb-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/Struct
%{_mandir}/man3/Struct*


%changelog
* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.03-3
- Perl 5.22 rebuild

* Mon Oct 20 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.03-2
- Take into account review feedback (#1154405)

* Sun Oct 19 2014 Emmanuel Seyman <emmanuel@seyman.fr> 0.03-1
- Specfile autogenerated by cpanspec 1.78.
