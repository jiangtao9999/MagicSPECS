# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name system-fileio

%bcond_with tests

Name:           ghc-%{pkg_name}
Version:        0.3.16
Release:        3%{?dist}
Summary:        Consistent filesystem interaction across GHC versions

License:        MIT
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-system-filepath-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-unix-devel
%if %{with tests}
BuildRequires:  ghc-chell-devel
BuildRequires:  ghc-temporary-devel
BuildRequires:  ghc-transformers-devel
%endif
# End cabal-rpm deps

%description
This is a small wrapper around the "directory", "unix", and "Win32" packages,
for use with "system-filepath". It provides a consistent API to the various
versions of these packages distributed with different versions of GHC.

In particular, this library supports working with POSIX files that have paths
which can't be decoded in the current locale encoding.


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


%check
%if %{with tests}
%cabal test
%endif


%post devel
%ghc_pkg_recache


%postun devel
%ghc_pkg_recache


%files -f %{name}.files
%doc license.txt
%{_docdir}/%{name}-%{version}/license.txt

%files devel -f %{name}-devel.files
%doc README.md


%changelog
* Sun Sep 20 2015 Liu Di <liudidi@gmail.com> - 0.3.16-3
- 为 Magic 3.0 重建

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jan 20 2015 Jens Petersen <petersen@redhat.com> - 0.3.16-1
- update to 0.3.16

* Wed Aug 27 2014 Jens Petersen <petersen@redhat.com> - 0.3.14-1
- update to 0.3.14
- refresh to 0.8.11

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Jul 21 2013 Jens Petersen <petersen@redhat.com> - 0.3.11-1
- description

* Sun Jul 21 2013 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.3.11-0
- spec file generated by cabal-rpm-0.8.3
