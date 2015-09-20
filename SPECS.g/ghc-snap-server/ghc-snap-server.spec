# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name snap-server

Name:           ghc-%{pkg_name}
Version:        0.9.4.6
Release:        2%{?dist}
Summary:        A fast, iteratee-based, epoll-enabled web server for the Snap Framework

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-MonadCatchIO-transformers-devel
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-attoparsec-enumerator-devel
BuildRequires:  ghc-blaze-builder-devel
BuildRequires:  ghc-blaze-builder-enumerator-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-case-insensitive-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-enumerator-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-old-locale-devel
BuildRequires:  ghc-snap-core-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-unix-compat-devel
BuildRequires:  ghc-unix-devel
# End cabal-rpm deps

%description
Snap is a simple and fast web development framework and server written in
Haskell. For more information, you can visit the Snap project website at
<http://snapframework.com/>.

The Snap HTTP server is a high performance, epoll-enabled, iteratee-based web
server library written in Haskell. Together with the 'snap-core' library upon
which it depends, it provides a clean and efficient Haskell programming
interface to the HTTP protocol.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development files.


%prep
%setup -q -n %{pkg_name}-%{version}


%build
%ghc_lib_build


%install
%ghc_lib_install


%post devel
%ghc_pkg_recache


%postun devel
%ghc_pkg_recache


%files -f %{name}.files
%doc LICENSE


%files devel -f %{name}-devel.files
%doc CONTRIBUTORS README.md README.SNAP.md


%changelog
* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jan 20 2015 Jens Petersen <petersen@redhat.com> - 0.9.4.6-1
- update to 0.9.4.6

* Mon Sep 01 2014 Jens Petersen <petersen@redhat.com> - 0.9.4.5-1
- update to 0.9.4.5

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 10 2014 Jens Petersen <petersen@redhat.com> - 0.9.3.4-3
- update to cblrpm-0.8.11

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Oct 16 2013 Jens Petersen <petersen@redhat.com> - 0.9.3.4-1
- 0.9.3.4
- add static provides to devel

* Thu Jun 27 2013 Jens Petersen <petersen@redhat.com> - 0.9.3.3-1
- minor description tweaks and add CONTRIBUTORS

* Thu Jun 27 2013 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.9.3.3-0
- spec file generated by cabal-rpm-0.8.2
