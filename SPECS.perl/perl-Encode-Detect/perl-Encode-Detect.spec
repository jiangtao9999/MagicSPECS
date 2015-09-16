Name: perl-Encode-Detect
Version: 1.01
Release: 19%{?dist}
Summary: Encode::Encoding subclass that detects the encoding of data

Group: Development/Libraries
License: MPLv1.1 or GPLv2+ or LGPLv2+
URL: http://search.cpan.org/dist/Encode-Detect/
Source0: http://www.cpan.org/authors/id/J/JG/JGMYERS/Encode-Detect-%{version}.tar.gz
Buildroot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: perl(ExtUtils::CBuilder)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Test::More)
Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires: perl(Encode::Encoding)

%description
This Perl module is an Encode::Encoding subclass that uses
Encode::Detect::Detector to determine the charset of the input data and then
decodes it using the encoder of the detected charset.

%prep
%setup -q -n Encode-Detect-%{version}
cat <<EOF >%{name}-req
#!/bin/sh
%{__perl_requires} $* |\
  sed -e '/perl(base)/d'
EOF
%define __perl_requires %{_builddir}/Encode-Detect-%{version}/%{name}-req
%{__chmod} +x %{__perl_requires}

%build
%{__perl} Build.PL installdirs=vendor optimize="${RPM_OPT_FLAGS}"
./Build

%check
./Build test

%install
%{__rm} -rf "${RPM_BUILD_ROOT}"
./Build install destdir="${RPM_BUILD_ROOT}" create_packlist=0
find "${RPM_BUILD_ROOT}" -type f -name "*.bs" -size 0 -exec %{__rm} -f {} \;
find "${RPM_BUILD_ROOT}" -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} "${RPM_BUILD_ROOT}"/*

%clean
%{__rm} -rf "${RPM_BUILD_ROOT}"

%files
%defattr(-,root,root,-)
%doc Changes LICENSE
%{perl_vendorarch}/auto/Encode
%{perl_vendorarch}/Encode
%{_mandir}/man3/Encode::Detect.3*
%{_mandir}/man3/Encode::Detect::Detector.3*

%changelog
* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 1.01-19
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 1.01-18
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 1.01-17
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.01-16
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.01-15
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.01-14
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.01-13
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 1.01-12
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 1.01-11
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 10 2012 Petr Pisar <ppisar@redhat.com> - 1.01-9
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.01-7
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.01-5
- 661697 rebuild for fixing problems with vendorach/lib

* Sat May 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.01-4
- Mass rebuild with perl-5.12.0

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.01-3
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.01-2
- rebuild against perl 5.10.1

* Thu Nov 12 2009 Warren Togami <wtogami@redhat.com> - 1.01-1
- 1.01 (no changes of consequence, only match latest upstream version)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 20 2008 James Ralston <ralston@pobox.com> - 1.00-4
- remove test before rm -rf $RPM_BUILD_ROOT; rpm will prevent badness

* Wed Dec 19 2007 James Ralston <ralston@pobox.com> - 1.00-3
- the "Build test" step requires perl(Test::More) and perl(Data::Dump)

* Thu Oct 11 2007 James Ralston <ralston@pobox.com> - 1.00-2
- adjust static Requires
- filter erroneous auto-generated Requires in %%prep

* Wed Oct 10 2007 James Ralston <ralston@pobox.com> - 1.00-1
- specfile autogenerated by cpanspec 1.73.
