# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name webkit

Name:           ghc-%{pkg_name}
Version:        0.13.1.3
Release:        1%{?dist}
Summary:        Binding to the Webkit library

License:        LGPLv2+
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-cairo-devel
BuildRequires:  ghc-glib-devel
BuildRequires:  ghc-gtk-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-pango-devel
BuildRequires:  ghc-text-devel
BuildRequires:  gtk2hs-buildtools
BuildRequires:  pkgconfig(webkit-1.0)
# End cabal-rpm deps

%description
WebKit is a web content engine, derived from KHTML and KJS from KDE, and used
primarily in Apple's Safari browser. It is made to be embedded in other
applications, such as mail readers, or web browsers. It is able to display
content such as HTML, SVG, XML, and others. It also supports DOM,
XMLHttpRequest, XSLT, CSS, Javascript/ECMAscript and more.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}
Requires:       %{name}%{?_isa} = %{version}-%{release}
# Begin cabal-rpm deps:
Requires:       pkgconfig(webkit-1.0)
# End cabal-rpm deps

%description devel
This package provides the Haskell %{pkg_name} library development files.


%prep
%setup -q -n %{pkg_name}-%{version}


%build
%ghc_lib_build


%install
%ghc_lib_install

rm %{buildroot}%{ghc_pkgdocdir}/COPYING

# we include the demos in devel docdir
rm %{buildroot}%{_datadir}/%{pkg_name}-%{version}/{Makefile,Webkit.hs}


%post devel
%ghc_pkg_recache


%postun devel
%ghc_pkg_recache


%files -f %{name}.files
%license COPYING


%files devel -f %{name}-devel.files
%doc demo


%changelog
* Wed Jul 22 2015 Jens Petersen <petersen@redhat.com> - 0.13.1.3-1
- update to 0.13.1.3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 23 2015 Jens Petersen <petersen@redhat.com> - 0.13.1.1-1
- update to 0.13.1.1

* Tue Sep 16 2014 Jens Petersen <petersen@redhat.com> - 0.13.0.0-1
- update to 0.13.0.0
- refresh to cblrpm-0.8.11

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Dec 31 2013 Jens Petersen <petersen@redhat.com> - 0.12.5.1-1
- include demo sources in docdir

* Mon Dec 30 2013 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.12.5.1
- spec file generated by cabal-rpm-0.8.7
