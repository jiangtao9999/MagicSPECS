Name:           perl-CGI-Application-Plugin-DBIx-Class
Version:        1.000100
Release:        18%{?dist}
Summary:        Access a DBIx::Class Schema from a CGI::Application
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/CGI-Application-Plugin-DBIx-Class/
Source0:        http://www.cpan.org/authors/id/F/FR/FREW/CGI-Application-Plugin-DBIx-Class-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(CGI::Application)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBIx::Class)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(parent)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(SQL::Translator)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
This module helps you to map various DBIx::Class features to CGI
parameters. For the most part that means it will help you search, sort, and
paginate with a minimum of effort and thought. Currently it uses the
connection from CGI::Application::Plugin::DBH.

%prep
%setup -q -n CGI-Application-Plugin-DBIx-Class-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check


%files
%doc Changes dist.ini LICENSE META.json README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 1.000100-18
- 为 Magic 3.0 重建

* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 1.000100-17
- 为 Magic 3.0 重建

* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 1.000100-16
- 为 Magic 3.0 重建

* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 1.000100-15
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 1.000100-14
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 1.000100-13
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.000100-12
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.000100-11
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.000100-10
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.000100-9
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 1.000100-8
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 1.000100-7
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 1.000100-6
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 1.000100-5
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.000100-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 1.000100-3
- Perl mass rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1.000100-2
- Perl mass rebuild

* Sun May 22 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 1.000100-1
- Update to 1.000100
- Spec clean-up
- Replace CGI::Application::Plugin::DBH with DBD::SQLite as a BR
- Enable tests

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.100210-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.100210-3
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.100210-2
- Mass rebuild with perl-5.12.0

* Mon Jan 25 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.100210-1
- Update to 0.100210

* Tue Jan 19 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.100180-1
- Update to 0.100180
- Remove end-of-line changes (change upstreamed)

* Sun Jan 17 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.100160-1
- update to 0.100160

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.093011-3
- rebuild against perl 5.10.1

* Thu Nov 05 2009 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 0.093011-2
- Fix rpmlint output

* Thu Oct 29 2009 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 0.093011-1
- Specfile autogenerated by cpanspec 1.78.
