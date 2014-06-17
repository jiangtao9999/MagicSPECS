Name:           perl-LWP-MediaTypes
Version:        6.01
Release:        8%{?dist}
Summary:        Guess media type for a file or a URL
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/LWP-MediaTypes/
Source0:        http://www.cpan.org/authors/id/G/GA/GAAS/LWP-MediaTypes-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
# Tests only:
BuildRequires:  perl(Test)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(File::Basename)
Requires:       mailcap
Conflicts:      perl-libwww-perl < 6

%description
This module provides functions for handling media (also known as MIME)
types and encodings. The mapping from file extensions to media types is
defined by the media.types file. If the ~/.media.types file exists it is
used instead. For backwards compatibility we will also look for
~/.mime.types.

%prep
%setup -q -n LWP-MediaTypes-%{version}
# Use system-wide mailcap database
sed -i -e '/my @priv_files = ();/ s|()|("%{_sysconfdir}/mime.types")|' \
    lib/LWP/MediaTypes.pm

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
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 6.01-8
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 6.01-7
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.01-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 6.01-5
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.01-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 6.01-3
- Perl mass rebuild

* Thu Mar 17 2011 Petr Pisar <ppisar@redhat.com> - 6.01-2
- Use MIME type database from mailcap

* Thu Mar 17 2011 Petr Pisar <ppisar@redhat.com> 6.01-1
- Specfile autogenerated by cpanspec 1.78.
- Remove BuildRoot stuff
- Conflicts with perl-libwww-perl 5* and older
