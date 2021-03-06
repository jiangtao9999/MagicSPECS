# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name primitive

Name:           ghc-%{pkg_name}
Version:        0.5.2.1
Release:        4%{?dist}
Summary:        Primitive memory-related operations

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros

%description
This package provides various primitive memory-related operations.


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


%changelog
* Sun Nov 08 2015 Liu Di <liudidi@gmail.com> - 0.5.2.1-4
- 为 Magic 3.0 重建

* Sun Sep 20 2015 Liu Di <liudidi@gmail.com> - 0.5.2.1-3
- 为 Magic 3.0 重建

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug  8 2014 Jens Petersen <petersen@redhat.com> - 0.5.2.1-1
- update to 0.5.2.1

* Thu Jun 19 2014 Jens Petersen <petersen@redhat.com> - 0.5.0.1-5
- update packaging to cblrpm-0.8.11

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 04 2013 Jens Petersen <petersen@redhat.com> - 0.5.0.1-3
- update to new simplified Haskell Packaging Guidelines

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 27 2012 Jens Petersen <petersen@redhat.com> - 0.5.0.1-1
- update to 0.5.0.1

* Sat Nov 17 2012 Jens Petersen <petersen@redhat.com>
- update with cabal-rpm

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Jens Petersen <petersen@redhat.com> - 0.4.1-2
- change prof BRs to devel

* Thu Mar 22 2012 Jens Petersen <petersen@redhat.com> - 0.4.1-1
- update to 0.4.1

* Wed Jan  4 2012 Jens Petersen <petersen@redhat.com> - 0.4.0.1-1
- update to 0.4.0.1 and cabal2spec-0.25.2

* Mon Oct 24 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.3.1-2.1
- rebuild with new gmp without compat lib

* Tue Sep 13 2011 Jens Petersen <petersen@redhat.com> - 0.3.1-2
- rebuild against newer ghc-rpm-macros

* Thu Sep  8 2011 Jens Petersen <petersen@redhat.com> - 0.3.1-1
- BSD license

* Thu Sep  8 2011 Fedora Haskell SIG <haskell-devel@lists.fedoraproject.org> - 0.3.1-0
- initial packaging for Fedora automatically generated by cabal2spec-0.24.1
