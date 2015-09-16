Name:           perl-Authen-OATH
Version:	1.0.0
Release:	15%{?dist}
Summary:        OATH One Time Passwords
Summary(zh_CN.UTF-8): OATH 一次性密码
License:        GPL+ or Artistic
Group:          Development/Libraries
Group(zh_CN.UTF-8): 开发/库
URL:            http://search.cpan.org/dist/Authen-OATH/
Source0:        http://www.cpan.org/authors/id/S/SI/SIFUKURT/Authen-OATH-v%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Module::Build)
# Tests only:
BuildRequires:  perl(Digest::HMAC)
BuildRequires:  perl(Digest::SHA1)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Simple)
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.22
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
# SHA1 is needed by HOTP specification.
Requires:       perl(Digest::SHA1)

%description
Implementation of the HOTP and TOTP One Time Password algorithms as defined by
OATH (http://www.openauthentication.org).

%description -l zh_CN.UTF-8
OATH 一次性密码。

%prep
%setup -q -n Authen-OATH-v%{version}
for F in README Changes; do
    sed -e 's/\r//' <"$F" >"${F}.unix"
    touch -r "$F" "${F}.unix"
    mv "${F}.unix" "$F"
done

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*
magic_rpm_clean.sh

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 1.0.0-15
- 为 Magic 3.0 重建

* Fri Apr 24 2015 Liu Di <liudidi@gmail.com> - 1.0.0-14
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 1.0.0-13
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 1.0.0-12
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.0.0-11
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.0.0-10
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.0.0-9
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.0.0-8
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 1.0.0-7
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 1.0.0-6
- 为 Magic 3.0 重建

* Sat Jan 28 2012 Liu Di <liudidi@gmail.com> - 1.0.0-5
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 1.0.0-3
- Perl mass rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 1.0.0-2
- Perl mass rebuild

* Mon Jun 27 2011 Petr Pisar <ppisar@redhat.com> 1.0.0-1
- Specfile autogenerated by cpanspec 1.78.
- Remove BuildRoot and defattr
- Recode documentation to have UNIX end of lines
- Require at run-time Digest::SHA1 to fulfill RFC 4226 (HOTP)
