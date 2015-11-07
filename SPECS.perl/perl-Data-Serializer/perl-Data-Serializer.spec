Name:           perl-Data-Serializer
Version:	0.60
Release:	2%{?dist}
Summary:        Modules that serialize data structures
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Data-Serializer/
Source0:        http://www.cpan.org/authors/id/N/NE/NEELY/Data-Serializer-%{version}.tar.gz
BuildArch:      noarch
# Compress::PPMd not available (broken on 64-bit)
#BuildRequires:  perl(Compress::PPMd)
BuildRequires:  perl(Bencode)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(Convert::Bencode)
BuildRequires:  perl(Convert::Bencode_XS)
BuildRequires:  perl(Config::General)
BuildRequires:  perl(Crypt::Blowfish)
BuildRequires:  perl(Crypt::CBC)
BuildRequires:  perl(Data::Denter)
BuildRequires:  perl(Data::Taxi)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Digest::SHA1)
BuildRequires:  perl(FreezeThaw)
BuildRequires:  perl(JSON)
BuildRequires:  perl(JSON::Syck)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(PHP::Serialization)
BuildRequires:  perl(Test::Kwalitee)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(XML::Dumper)
BuildRequires:  perl(XML::Simple)
BuildRequires:  perl(YAML)
BuildRequires:  perl(YAML::Syck)
# Compress::PPMd not available (broken on 64-bit)
#Requires:       perl(Compress::PPMd)
Requires:       perl(Compress::Zlib)
Requires:       perl(Crypt::Blowfish)
Requires:       perl(Crypt::CBC)
Requires:       perl(Digest::SHA)
Requires:       perl(JSON::XS)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
Provides a unified interface to the various serializing modules currently
available. Adds the functionality of both compression and encryption.

%prep
%setup -q -n Data-Serializer-%{version}

#fix permissions
find lib -name \*.pm -print0 | xargs -0 chmod 0644

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Nov 02 2015 Liu Di <liudidi@gmail.com> - 0.60-2
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.60-1
- 更新到 0.60

* Thu Jun 19 2014 Liu Di <liudidi@gmail.com> - 0.59-9
- 为 Magic 3.0 重建

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.59-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.59-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Pisar <ppisar@redhat.com> - 0.59-6
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.59-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.59-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 23 2012 Petr Pisar <ppisar@redhat.com> - 0.59-3
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.59-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 26 2011 Iain Arnell <iarnell@gmail.com> 0.59-1
- update to latest upstream

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.57-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.57-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 20 2011 Iain Arnell <iarnell@gmail.com> 0.57-1
- update to latest upstream version
- BR perl(Bencode), perl(Convert::Bencode), and perl(Convert::Bencode_XS)

* Fri Jan 14 2011 Iain Arnell <iarnell@gmail.com> 0.54-1
- update to latest upstream version

* Fri Jan 07 2011 Iain Arnell <iarnell@gmail.com> 0.52-1
- update to latest upstream version

* Sun Jan 02 2011 Iain Arnell <iarnell@gmail.com> 0.51-1
- update to latest upstream
- clean up spec for modern rpmbuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.49-3
- 661697 rebuild for fixing problems with vendorach/lib

* Tue Jul 13 2010 Iain Arnell <iarnell@gmail.com> 0.49-2
- fix modules' permissions

* Sun Jun 27 2010 Iain Arnell <iarnell@gmail.com> 0.49-1
- Specfile autogenerated by cpanspec 1.78.
- Tweak requires
