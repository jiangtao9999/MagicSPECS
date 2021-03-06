# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name monad-control

Name:           ghc-%{pkg_name}
Version:        0.3.3.1
Release:        4%{?dist}
Summary:        Lift control operations through monad transformers

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-transformers-base-devel
BuildRequires:  ghc-transformers-compat-devel
BuildRequires:  ghc-transformers-devel
# End cabal-rpm deps

%description
This package defines the type class 'MonadBaseControl', a subset of 'MonadBase'
into which generic control operations such as 'catch' can be lifted from 'IO'
or any other base monad. Instances are based on monad transformers in
'MonadTransControl', which includes all standard monad transformers in the
'transformers' library except 'ContT'.

See the 'lifted-base' package which uses 'monad-control' to lift 'IO'
operations from the 'base' library (like 'catch' or 'bracket') into any monad
that is an instance of 'MonadBase' or 'MonadBaseControl'.


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
%{_docdir}/%{name}-%{version}/LICENSE


%files devel -f %{name}-devel.files
%doc README.markdown NEWS


%changelog
* Sun Nov 08 2015 Liu Di <liudidi@gmail.com> - 0.3.3.1-4
- 为 Magic 3.0 重建

* Sun Sep 20 2015 Liu Di <liudidi@gmail.com> - 0.3.3.1-3
- 为 Magic 3.0 重建

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar  3 2015 Jens Petersen <petersen@fedoraproject.org> - 0.3.3.1-1
- update to 0.3.3.1

* Tue Sep 16 2014 Jens Petersen <petersen@redhat.com> - 0.3.3.0-1
- update to 0.3.3.0
- refresh to cblrpm-0.8.11

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 10 2013 Jens Petersen <petersen@redhat.com> - 0.3.2.1-1
- update to 0.3.2.1
- update to new simplified Haskell Packaging Guidelines

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Nov 07 2012 Jens Petersen <petersen@redhat.com> - 0.3.1.4-1
- update to 0.3.1.4

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Jens Petersen <petersen@redhat.com> - 0.3.1.3-2
- rebuild

* Tue May  1 2012 Jens Petersen <petersen@redhat.com> - 0.3.1.3-1
- update to 0.3.1.3

* Thu Mar 22 2012 Jens Petersen <petersen@redhat.com> - 0.3.1-2
- add license to ghc_files

* Thu Jan 26 2012 Jens Petersen <petersen@redhat.com> - 0.3.1-1
- BSD license
- depends on base-unicode-symbols and transformers-base

* Thu Jan 26 2012 Fedora Haskell SIG <haskell-devel@lists.fedoraproject.org>
- spec file template generated by cabal2spec-0.25.4
