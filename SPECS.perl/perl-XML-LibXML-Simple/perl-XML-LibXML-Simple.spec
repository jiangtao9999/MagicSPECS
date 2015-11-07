Name:           perl-XML-LibXML-Simple
Version:        0.95
Release:        5%{?dist}
Summary:        Read XML strings or files
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/XML-LibXML-Simple/
Source0:        http://www.cpan.org/authors/id/M/MA/MARKOV/XML-LibXML-Simple-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(File::Slurp::Tiny)
BuildRequires:  perl(Test::More) >= 0.54
BuildRequires:  perl(XML::LibXML) >= 1.64
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(XML::LibXML) >= 1.64

# drop unversioned Requires on XML::LibXML
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude|%__requires_exclude|}^perl\\(XML::LibXML\\)$

%description
This Perl module reads XML from strings or files.  It is a blunt rewrite
of XML::Simple (by Grant McLean) to use the XML::LibXML parser for XML
structures, where the original uses plain Perl or SAX parsers.

%prep
%setup -q -n XML-LibXML-Simple-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc ChangeLog README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Nov 03 2015 Liu Di <liudidi@gmail.com> - 0.95-5
- 为 Magic 3.0 重建

* Mon Sep 14 2015 Liu Di <liudidi@gmail.com> - 0.95-4
- 为 Magic 3.0 重建

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.95-2
- Perl 5.22 rebuild

* Wed Jun 10 2015 Colin B. Macdonald <cbm@m.fsf.org> 0.95-1
- Version bump

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.94-4
- Perl 5.22 rebuild

* Wed Nov 19 2014 Colin B. Macdonald <cbm@m.fsf.org> 0.94-3
- clean-up following further review.

* Wed Nov 19 2014 Colin B. Macdonald <cbm@m.fsf.org> 0.94-2
- clean-up following review, better summary/description.

* Thu Jun 26 2014 Colin B. Macdonald <cbm@m.fsf.org> 0.94-1
- Specfile autogenerated by cpanspec 1.78.

* Wed Aug 22 2012 Mary Ellen Foster <mefoster@gmail.com> 0.91-1
- Specfile autogenerated by cpanspec 1.78.
