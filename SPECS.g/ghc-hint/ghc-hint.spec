# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name hint

# failing on ARM
%ifarch %{ix86} x86_64
%bcond_without tests
%endif

Name:           ghc-%{pkg_name}
Version:        0.4.2.1
Release:        5%{?dist}
Summary:        Runtime Haskell interpreter

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-extensible-exceptions-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-ghc-devel
BuildRequires:  ghc-ghc-mtl-devel
BuildRequires:  ghc-ghc-paths-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-utf8-string-devel
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
%endif
# End cabal-rpm deps
# needs GHC.setContext, GHC.compileExpr, etc (#1121624)
ExclusiveArch:  %{ghc_arches_with_ghci}


%description
This library defines an 'Interpreter' monad. It allows to load Haskell modules,
browse them, type-check and evaluate strings with Haskell expressions and even
coerce them into values. The library is thread-safe and type-safe (even the
coercion of expressions to values). It is, essentially, a huge subset of the
GHC API wrapped in a simpler API.


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
%doc LICENSE
%{_docdir}/%{name}-%{version}/LICENSE

%files devel -f %{name}-devel.files
%doc AUTHORS README examples


%changelog
* Fri Dec 04 2015 Liu Di <liudidi@gmail.com> - 0.4.2.1-5
- 为 Magic 3.0 重建

* Sun Nov 08 2015 Liu Di <liudidi@gmail.com> - 0.4.2.1-4
- 为 Magic 3.0 重建

* Sun Sep 20 2015 Liu Di <liudidi@gmail.com> - 0.4.2.1-3
- 为 Magic 3.0 重建

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 19 2015 Jens Petersen <petersen@redhat.com> - 0.4.2.1-1
- update to 0.4.2.1

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Jens Petersen <petersen@redhat.com> - 0.4.2.0-2
- requires ghci libHSghc to compile (#1121624)

* Mon May 19 2014 Jens Petersen <petersen@redhat.com> - 0.4.2.0-1
- spec file generated by cabal-rpm-0.8.11
- disable tests on arm for now
