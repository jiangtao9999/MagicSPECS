# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name hinotify

Name:           ghc-%{pkg_name}
Version:        0.3.7
Release:        2%{?dist}
Summary:        Haskell binding to inotify

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-unix-devel
# End cabal-rpm deps

%description
This library provides a wrapper to the Linux Kernel's inotify feature, allowing
applications to subscribe to notifications when a file is accessed or modified.


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
%doc README.md


%changelog
* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 19 2015 Jens Petersen <petersen@redhat.com> - 0.3.7-1
- update to 0.3.7

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 05 2013 Jens Petersen <petersen@redhat.com> - 0.3.5-3
- update to new simplified Haskell Packaging Guidelines

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Nov 07 2012 Jens Petersen <petersen@redhat.com> - 0.3.5-1
- update to 0.3.5

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Jens Petersen <petersen@redhat.com> - 0.3.2-4
- change prof BRs to devel

* Sun Mar 18 2012 Jens Petersen <petersen@redhat.com> - 0.3.2-3
- update to cabal2spec-0.25

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-2.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 24 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.3.2-1.3
- rebuild with new gmp without compat lib

* Fri Oct 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.3.2-1.2
- rebuild with new gmp without compat lib

* Tue Oct 11 2011 Peter Schiffer <pschiffe@redhat.com> - 0.3.2-1.1
- rebuild with new gmp

* Mon Jul 25 2011 Ben Boeckel <mathstuf@gmail.com> - 0.3.2-1
- Update to 0.3.2
- Update to cabal2spec-0.24

* Thu Jun 23 2011 Jens Petersen <petersen@redhat.com> - 0.3.1-11
- BR ghc-Cabal-devel instead of ghc-prof and use ghc_arches (cabal2spec-0.23.2)
- don't build via-C since it breaks assembler on x86_64 (#715799)

* Wed May 11 2011 Ben Boeckel <mathstuf@gmail.com> - 0.3.1-10
- Update to cabal2spec-0.22.7

* Thu Mar 10 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.3.1-9
- Enable build on sparcv9

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 15 2011 Ben Boeckel <mathstuf@gmail.com> - 0.3.1-7
- Update to cabal2spec-0.22.4
- Rebuild

* Sun Nov 28 2010 Ben Boeckel <mathstuf@gmail.com> - 0.3.1-6
- Rebuild for GHC7

* Sun Nov 07 2010 Ben Boeckel <mathstuf@gmail.com> - 0.3.1-5
- Rebuild

* Wed Sep 01 2010 Ben Boeckel <mathstuf@gmail.com> - 0.3.1-4
- Ship the readme as well

* Tue Aug 31 2010 Ben Boeckel <mathstuf@gmail.com> - 0.3.1-3
- Update to new cabal2spec

* Wed Jun 30 2010 Ben Boeckel <mathstuf@gmail.com> - 0.3.1-2
- Merge with cabal2spec-0.22.1 spec

* Thu May 20 2010 Ben Boeckel <mathstuf@gmail.com> - 0.3.1-1
- Initial version

* Thu May 20 2010 Fedora Haskell SIG <haskell-devel@lists.fedoraproject.org> - 0.3.1-0
- initial packaging for Fedora automatically generated by cabal2spec-0.21.3
