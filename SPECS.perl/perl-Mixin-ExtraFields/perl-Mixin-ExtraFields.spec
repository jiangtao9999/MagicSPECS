Name:           perl-Mixin-ExtraFields
Version:	0.140002
Release:	1%{?dist}
Summary:        Add extra stashes of data to your objects
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Mixin-ExtraFields/
Source0:        http://www.cpan.org/authors/id/R/RJ/RJBS/Mixin-ExtraFields-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Sub::Exporter) => 0.972
BuildRequires:  perl(Sub::Install)
BuildRequires:  perl(String::RewritePrefix)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
Mixin::ExtraFields provides a simple way to add an arbitrary number of stashes
for named data.  These data can be stored in the object, in a database, or
anywhere else.  The storage mechanism is abstracted away from the provided
interface, so one storage mechanism can be easily swapped for another.
Multiple ExtraFields stashes can be mixed into one class, using one or many
storage mechanisms.

%prep
%setup -q -n Mixin-ExtraFields-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.140002-1
- 更新到 0.140002

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.100971-9
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.100971-8
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.100971-7
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.100971-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 29 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.100971-5
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.100971-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.100971-3
- 661697 rebuild for fixing problems with vendorach/lib

* Mon May 03 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.100971-2
- Mass rebuild with perl-5.12.0

* Sun Apr 11 2010 Iain Arnell <iarnell@gmail.com> 0.100971-1
- update to latest upstream version

* Sun Feb 21 2010 Iain Arnell <iarnell@gmail.com> 0.008-1
- Specfile autogenerated by cpanspec 1.78.
- use perl_default_filter and DESTDIR
- tweak {build,}requires
