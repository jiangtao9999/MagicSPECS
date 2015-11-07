Name:           perl-App-Daemon
Version:	0.22
Release:	4%{?dist}
Summary:        Start an Application as a Daemon
Summary(zh_CN.UTF-8): 以守护程序的方式启动应用程序
License:        GPL+ or Artistic
Group:          Development/Libraries
Group(zh_CN.UTF-8): 开发/库
URL:            http://search.cpan.org/dist/App-Daemon/
Source0:        http://www.cpan.org/authors/id/M/MS/MSCHILLI/App-Daemon-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Pid)
BuildRequires:  perl(Log::Log4perl) >= 1.0
BuildRequires:  perl(Proc::ProcessTable)
BuildRequires:  perl(Sysadm::Install)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
App::Daemon helps running an application as a daemon.

%description -l zh_CN.UTF-8
以守护程序的方式启动应用程序。

%prep
%setup -q -n App-Daemon-%{version}
chmod 644 eg/*
sed -i -e 's!/usr/local!/usr!' eg/*

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*
magic_rpm_clean.sh

%check


%files
%doc Changes README eg
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Nov 02 2015 Liu Di <liudidi@gmail.com> - 0.22-4
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.22-3
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.22-2
- 为 Magic 3.0 重建

* Thu Apr 23 2015 Liu Di <liudidi@gmail.com> - 0.22-1
- 更新到 0.22

* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 0.14-17
- 为 Magic 3.0 重建

* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 0.14-16
- 为 Magic 3.0 重建

* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 0.14-15
- 为 Magic 3.0 重建

* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 0.14-14
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.14-13
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.14-12
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.14-11
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.14-10
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.14-9
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 0.14-8
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 0.14-7
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.14-6
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.14-5
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.14-4
- 为 Magic 3.0 重建

* Sat Jan 28 2012 Liu Di <liudidi@gmail.com> - 0.14-3
- 为 Magic 3.0 重建

* Fri Jan 27 2012 Liu Di <liudidi@gmail.com> - 0.14-2
- 为 Magic 3.0 重建

* Thu Jan 05 2012 Iain Arnell <iarnell@gmail.com> 0.14-1
- update to latest upstream version

* Sat Jul 23 2011 Iain Arnell <iarnell@gmail.com> 0.13-2
- Perl mass rebuild

* Sat Jul 23 2011 Iain Arnell <iarnell@gmail.com> 0.13-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.11-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.11-2
- 661697 rebuild for fixing problems with vendorach/lib

* Sun Aug 29 2010 Iain Arnell <iarnell@gmail.com> 0.11-1
- update to latest upstream

* Thu Apr 29 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.09-2
- Mass rebuild with perl-5.12.0

* Sun Apr 11 2010 Iain Arnell <iarnell@gmail.com> 0.09-1
- update to latest upstream version
- use perl_default_filter and DESTDIR

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.08-2
- rebuild against perl 5.10.1

* Sat Nov 07 2009 Iain Arnell <iarnell@gmail.com> 0.08-1
- update to latest upstream version

* Sun Oct 18 2009 Iain Arnell <iarnell@gmail.com> 0.07-1
- update to latest upstream (fixes rt#50326)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Apr 10 2009 Iain Arnell 0.06-1
- Specfile autogenerated by cpanspec 1.77.
- remove explicit requires
- add eg to docs
