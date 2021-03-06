# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name control-monad-free

Name:           ghc-%{pkg_name}
Version:        0.6.1
Release:        6%{?dist}
Summary:        Free monads and monad transformers

License:        Public Domain
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-prelude-extras-devel
BuildRequires:  ghc-transformers-devel
# End cabal-rpm deps

%description
This package provides datatypes to construct Free monads, Free monad
transformers, and useful instances. In addition it provides the constructs to
avoid quadratic complexity of left associative bind, as explained in:

Janis Voigtlander, Asymptotic Improvement of Computations over Free Monads,
MPC'08/. http://www.janis-voigtlaender.eu/Voi08d.html


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development
files.


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


%files devel -f %{name}-devel.files


%changelog
* Sun Nov 08 2015 Liu Di <liudidi@gmail.com> - 0.6.1-6
- 为 Magic 3.0 重建

* Sun Sep 20 2015 Liu Di <liudidi@gmail.com> - 0.6.1-5
- 为 Magic 3.0 重建

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Feb 27 2015 Ben Boeckel <mathstuf@gmail.com> - 0.6.1-3
- patch is for the wrong spec...

* Thu Feb 26 2015 Ben Boeckel <mathstuf@gmail.com> - 0.6.1-2
- cherry-pick patch to support control-monad-free 0.6

* Tue Feb 24 2015 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.6.1-1
- spec file generated by cabal-rpm-0.9.3
