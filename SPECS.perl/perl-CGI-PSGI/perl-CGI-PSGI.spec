Name:           perl-CGI-PSGI
Version:        0.15
Release:        9%{?dist}
Summary:        Enable your CGI.pm aware applications to adapt PSGI protocol
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/CGI-PSGI/
Source0:        http://www.cpan.org/authors/id/M/MI/MIYAGAWA/CGI-PSGI-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(CGI)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
This module is for web application framework developers who currently uses
CGI to handle query parameters. You can switch to use CGI::PSGI instead of
CGI, to make your framework compatible to PSGI with a slight modification
of your framework adapter. The framework should already be collecting the
body content to print at one place, and not printing any content directly
to STDOUT.

%prep
%setup -q -n CGI-PSGI-%{version}

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
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Nov 02 2015 Liu Di <liudidi@gmail.com> - 0.15-9
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.15-8
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.15-7
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 0.15-6
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.15-5
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.15-4
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.15-2
- Perl mass rebuild

* Wed May 18 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.15-1
- Update to 0.15
- Spec clean-up

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 27 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.14-1
- Update to 0.14

* Sun Oct 31 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.13-1
- Update to 0.13

* Tue Oct 26 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.12-1
- Update to 0.12.

* Sun May 02 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.11-1
- Update to 0.11.

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.10-2
- Mass rebuild with perl-5.12.0

* Thu Apr 01 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.10-1
- Update to 0.10

* Sun Mar 14 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 0.09-1
- Specfile autogenerated by cpanspec 1.78.
