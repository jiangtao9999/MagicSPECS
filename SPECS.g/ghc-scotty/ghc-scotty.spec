# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name scotty

%bcond_with tests

Name:           ghc-%{pkg_name}
Version:        0.9.0
Release:        6%{?dist}
Summary:        Haskell web framework inspired by Ruby's Sinatra

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-blaze-builder-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-case-insensitive-devel
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-monad-control-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-regex-compat-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-transformers-base-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-wai-devel
BuildRequires:  ghc-wai-extra-devel
BuildRequires:  ghc-warp-devel
%if %{with tests}
BuildRequires:  ghc-hspec-wai-devel
BuildRequires:  ghc-hspec2-devel
BuildRequires:  ghc-lifted-base-devel
%endif
# End cabal-rpm deps

%description
A Haskell web framework inspired by Ruby's Sinatra, using WAI and Warp.

Scotty is the cheap and cheerful way to write RESTful, declarative web
applications.

* A page is as simple as defining the verb, url pattern, and Text content.
* It is template-language agnostic. Anything that returns a Text value will do.
* Conforms to WAI Application interface.
* Uses very fast Warp webserver by default.

As for the name: Sinatra + Warp = Scotty.


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
cabal-tweak-dep-ver data-default '>= 0.5.3' '>= 0.5.1'


%build
%ghc_lib_build


%install
%ghc_lib_install

rm %{buildroot}%{ghc_pkgdocdir}/LICENSE


%check
%if %{with tests}
%cabal test
%endif


%post devel
%ghc_pkg_recache


%postun devel
%ghc_pkg_recache


%files -f %{name}.files
%license LICENSE


%files devel -f %{name}-devel.files
%doc README.md examples


%changelog
* Sun Nov 08 2015 Liu Di <liudidi@gmail.com> - 0.9.0-6
- 为 Magic 3.0 重建

* Sun Sep 20 2015 Liu Di <liudidi@gmail.com> - 0.9.0-5
- 为 Magic 3.0 重建

* Mon Sep  7 2015 Jens Petersen <petersen@redhat.com> - 0.9.0-4
- use license macro

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar  4 2015 Jens Petersen <petersen@fedoraproject.org> - 0.9.0-2
- cblrpm refresh

* Mon Sep 08 2014 Jens Petersen <petersen@redhat.com> - 0.9.0-1
- update to 0.9.0

* Mon Sep 01 2014 Jens Petersen <petersen@redhat.com> - 0.8.2-1
- update to 0.8.2
- refresh to cblrpm-0.8.11

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May  8 2014 Jens Petersen <petersen@redhat.com> - 0.5.0-4
- enable ARM

* Wed Jan 22 2014 Jens Petersen <petersen@redhat.com> - 0.5.0-3
- rebuild

* Thu Nov 21 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.5.0-2
- Skip ARM for now.

* Mon Nov 18 2013 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.5.0
- spec file generated by cabal-rpm-0.8.6
