Name:           perl-Data-Dump-Streamer
Version:	2.38
Release:	3%{?dist}
Summary:        Accurately serialize a data structure as Perl code
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Data-Dump-Streamer/
Source0:        http://search.cpan.org/CPAN/authors/id/Y/YV/YVES/Data-Dump-Streamer-%{version}.tar.gz
BuildRequires:  perl(Algorithm::Diff)
BuildRequires:  perl(B::Utils)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(PadWalker) >= 0.99
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Balanced)
Requires:       perl(Compress::Zlib)
Requires:       perl(PadWalker) >= 0.99
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter:
%filter_from_requires /::_::/d
%filter_from_provides /::_::/d
%perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}::_::
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}::_::

%description
Given a list of scalars or reference variables, writes out their contents
in perl syntax. The references can also be objects. The contents of each
variable is output using the least number of Perl statements as convenient,
usually only one. Self-referential structures, closures, and objects are
output correctly.

%prep
%setup -q -n Data-Dump-Streamer-%{version}
find . -type f | xargs chmod -x

%build
%{__perl} Build.PL DDS installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Data*
%{perl_vendorarch}/DDS.pm
%{_mandir}/man3/*

%changelog
* Mon Nov 02 2015 Liu Di <liudidi@gmail.com> - 2.38-3
- 为 Magic 3.0 重建

* Mon Sep 14 2015 Liu Di <liudidi@gmail.com> - 2.38-2
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 2.38-1
- 更新到 2.38

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 2.32-13
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 2.32-12
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 2.32-11
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 2.32-10
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 2.32-9
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 2.32-8
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 2.32-7
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 2.32-6
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.32-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Iain Arnell <iarnell@gmail.com> 2.32-4
- Perl mass rebuild

* Wed Jul 20 2011 Iain Arnell <iarnell@gmail.com> 2.32-3
- update filtering for rpm 4.9

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.32-2
- Perl mass rebuild

* Sun Feb 20 2011 Iain Arnell <iarnell@gmail.com> 2.32-1
- update to latest upstream version

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb 04 2011 Iain Arnell <iarnell@gmail.com> 2.31-1
- update to latest upstream version

* Sun Jan 30 2011 Iain Arnell <iarnell@gmail.com> 2.25-1
- update to latest upstream version

* Fri Jan 21 2011 Iain Arnell <iarnell@gmail.com> 2.23-1
- update to latest upstream version

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.22-2
- 661697 rebuild for fixing problems with vendorach/lib

* Sun Jul 18 2010 Iain Arnell <iarnell@gmail.com> 2.22-1
- update to 2.22
- enable DDS shortcut
- update spec for modern rpmbuild

* Wed Jun 23 2010 Iain Arnell <iarnell@gmail.com> 2.21-1
- update to latest upstream

* Mon Jun 14 2010 Iain Arnell <iarnell@gmail.com> 2.18-1
- update to latest upstream
- convert to Module::Build
- use filtering macros

* Tue Apr 06 2010 Iain Arnell <iarnell@gmail.com> 2.13-1
- update to latest upstream
- drop madness.t patch

* Mon Apr 05 2010 Iain Arnell <iarnell@gmail.com> 2.11-1
- update to 2.11 (perl 5.12 compatibility tweaks)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 2.09-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 12 2009 Iain Arnell <iarnell@gmail.com> 2.09-2
- fix FTBFS by patching t/madness.t (due to rt #44610)

* Sat Apr 04 2009 Iain Arnell <iarnell@gmail.com> 2.09-1
- update to latest upstream

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec 05 2008 Iain Arnell 2.08-1
- Specfile autogenerated by cpanspec 1.77.
- strip private provides/requires
