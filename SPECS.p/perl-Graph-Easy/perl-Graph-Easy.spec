Name:           perl-Graph-Easy
Version:        0.71
Release:        5%{?dist}
Summary:        Convert or render graphs as ASCII, HTML, SVG or via Graphviz
License:        GPLv2+ and ASL 1.1
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Graph-Easy/
Source0:        http://www.cpan.org/authors/id/S/SH/SHLOMIF/Graph-Easy-%{version}.tar.gz
Patch0:         graph-easy-undefined-lc.patch
BuildArch:      noarch
BuildRequires:  perl >= 0:5.008002
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(Pod::Coverage)
BuildRequires:  perl(Scalar::Util) >= 1.13
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(utf8)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# avoid circular dependencies
%bcond_without bootstrap
%if %{without bootstrap}
BuildRequires:  perl(Graph::Easy::As_svg) >= 0.23
Requires:       perl(Graph::Easy::As_svg) >= 0.23
%endif

# filter unversioned provides
%{?filter_setup:
%filter_from_provides /^perl(Graph::Easy\(\|::Edge\|::Edge::Cell\|::Group\|::Node\))\s*$/d
%?perl_default_filter
}
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}perl\\(Graph::Easy\\)$
%global __provides_exclude %__provides_exclude|perl\\(Graph::Easy::(Edge|Edge::Cell|Group|Node)\\)$

%description
Graph::Easy lets you generate graphs consisting of various shaped nodes
connected by edges (with optional labels). It can read and write graphs in a
variety of formats, as well as render them via its own grid-based layouter.
Since the layouter works on a grid (manhattan layout), the output is most
useful for flow charts, network diagrams, or hierarchy trees.

%prep
%setup -q -n Graph-Easy-%{version}
%patch0 -p 1

chmod 0644 examples/*

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check


%files
%doc CHANGES LICENSE README TODO examples
%{_bindir}/*
%{_mandir}/man1/*
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.71-5
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.71-4
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.71-3
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.71-2
- 为 Magic 3.0 重建

* Fri Jan 06 2012 Iain Arnell <iarnell@gmail.com> 0.71-1
- update to latest upstream version
- update filtering for rpm 4.9

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.70-2
- Perl mass rebuild

* Sun Apr 24 2011 Iain Arnell <iarnell@gmail.com> 0.70-1
- Specfile autogenerated by cpanspec 1.79.
