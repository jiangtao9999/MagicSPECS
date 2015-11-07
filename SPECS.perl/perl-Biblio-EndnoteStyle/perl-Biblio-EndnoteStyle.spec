Name:           perl-Biblio-EndnoteStyle
Version:        0.05
Release:        10%{?dist}
Summary:        Reference formatting using Endnote-like templates
Summary(zh_CN.UTF-8): 采用类尾注模板的参考格式
License:        GPL+ or Artistic
Group:          Development/Libraries
Group(zh_CN.UTF-8): 开发/库
URL:            http://search.cpan.org/dist/Biblio-EndnoteStyle/
Source0:        http://www.cpan.org/authors/id/M/MI/MIRK/Biblio-EndnoteStyle-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This small module provides a way of formatting bibliographic references
using style templates similar to those used by the popular reference
management software Endnote (http://www.endnote.com/). The API is
embarrassingly simple: a formatter object is made using the class's
constructor, the new() method; format() may then be repeatedly called on
this object, using the same or different templates.

%description -l zh_CN.UTF-8
采用类尾注模板的参考格式。

%prep
%setup -q -n Biblio-EndnoteStyle-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*
magic_rpm_clean.sh

%check


%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_bindir}/*

%changelog
* Mon Nov 02 2015 Liu Di <liudidi@gmail.com> - 0.05-10
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.05-9
- 为 Magic 3.0 重建

* Fri Apr 24 2015 Liu Di <liudidi@gmail.com> - 0.05-8
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.05-7
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 0.05-6
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.05-5
- 为 Magic 3.0 重建

* Sat Jan 28 2012 Liu Di <liudidi@gmail.com> - 0.05-4
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue May 31 2011 Nicholas van Oudtshoorn <vanoudt@gmail.com> 0.05-2
- Added perl(Test::More) BuildRequires
- Removed superfluous spec file tags
- Undid the nastiness of moving the script to /usr/sbin; it's back where it belongs
* Thu Apr 28 2011 Nicholas van Oudtshoorn 0.05-1
- Specfile autogenerated by cpanspec 1.78.
- Specfile fixed by hand
- Moved Script from /usr/bin to /usr/sbin
- License is described here: https://rt.cpan.org/Public/Bug/Display.html?id=44211
