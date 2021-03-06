Name:           perl-Term-UI
Version:	0.46
Release:	3%{?dist}
Summary:        Term::ReadLine user interface made easy
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Term-UI/
Source0:        http://www.cpan.org/authors/id/B/BI/BINGOS/Term-UI-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
%if 0%(perl -e 'print $] > 5.017')
BuildRequires:  perl(deprecate)
%endif
BuildRequires:  perl(Exporter)
BuildRequires:  perl(if)
BuildRequires:  perl(Locale::Maketext::Simple)
BuildRequires:  perl(Log::Message)
BuildRequires:  perl(Log::Message::Simple)
BuildRequires:  perl(Params::Check)
BuildRequires:  perl(Term::ReadLine)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 0.31
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
%if 0%(perl -e 'print $] > 5.017')
Requires:       perl(deprecate)
%endif

%description
Term::UI is a transparent way of eliminating the overhead of having to
format a question and then validate the reply, informing the user if the
answer was not proper and re-issuing the question.

%prep
%setup -q -n Term-UI-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc CHANGES README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Nov 12 2015 Liu Di <liudidi@gmail.com> - 0.46-3
- 为 Magic 3.0 重建

* Tue Nov 03 2015 Liu Di <liudidi@gmail.com> - 0.46-2
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.46-1
- 更新到 0.46

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.42-3
- 为 Magic 3.0 重建

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 03 2014 Petr Pisar <ppisar@redhat.com> - 0.42-1
- 0.42 bump

* Tue Sep 24 2013 Petr Pisar <ppisar@redhat.com> - 0.38-1
- 0.38 bump

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.36-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 0.36-2
- Perl 5.18 rebuild

* Fri Jun 07 2013 Petr Pisar <ppisar@redhat.com> - 0.36-1
- 0.36 bump

* Tue May 28 2013 Petr Pisar <ppisar@redhat.com> - 0.34-2
- Correct typo in dependencies

* Fri Jan 25 2013 Petr Pisar <ppisar@redhat.com> 0.34-1
- Specfile autogenerated by cpanspec 1.78.
- Require deprecated module if needed
