Name:           perl-IO-Socket-IP
Version:	0.37
Release:	2%{?dist}
Summary:        Drop-in replacement for IO::Socket::INET supporting both IPv4 and IPv6
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/IO-Socket-IP/
Source0:        http://www.cpan.org/authors/id/P/PE/PEVANS/IO-Socket-IP-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(Carp)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Socket) >= 1.97
BuildRequires:  perl(Socket6)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%{?perl_default_filter}

%description
This module provides a protocol-independent way to use IPv4 and IPv6
sockets, as a drop-in replacement for IO::Socket::INET. Most constructor
arguments and methods are provided in a backward-compatible way.

%prep
%setup -q -n IO-Socket-IP-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} %{buildroot}/*

%check
# Don'd do the live test
rm -f t/21nonblocking-connect-internet.t
./Build test

%files
%doc Changes examples LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Nov 02 2015 Liu Di <liudidi@gmail.com> - 0.37-2
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.37-1
- 更新到 0.37

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.17-8
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.17-7
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.17-6
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.17-5
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.17-4
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.17-3
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.17-2
- 为 Magic 3.0 重建

* Wed Aug 22 2012 Petr Šabata <contyk@redhat.com> - 0.17-1
- 0.17 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 28 2012 Petr Pisar <ppisar@redhat.com> - 0.16-2
- Perl 5.16 rebuild

* Mon Jun 25 2012 Petr Šabata <contyk@redhat.com> - 0.16-1
- 0.16 (IO::Socket::INET compatibility enhancement)

* Thu Jun 21 2012 Petr Šabata <contyk@redhat.com> - 0.15-1
- 0.15 bump

* Tue Jun 19 2012 Petr Šabata <contyk@redhat.com> - 0.14-1
- 0.14 bump

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.11-2
- Perl 5.16 rebuild

* Wed Jun 06 2012 Petr Šabata <contyk@redhat.com> - 0.11-1
- 0.11 bump

* Fri May 11 2012 Petr Šabata <contyk@redhat.com> - 0.10-1
- 0.10 bump

* Wed Mar 14 2012 Petr Šabata <contyk@redhat.com> - 0.09-1
- 0.09 bump

* Fri Jan 27 2012 Petr Šabata <contyk@redhat.com> 0.08-1
- Specfile autogenerated by cpanspec 1.78.
