%global framework kmediaplayer

Name:           kf5-%{framework}
Version:        5.17.0
Release:        2%{?dist}
Summary:        KDE Frameworks 5 Tier 3 module with interface for media player features

License:        MIT
URL:            http://www.kde.org

%global versiondir %(echo %{version} | cut -d. -f1-2)
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/frameworks/%{versiondir}/portingAids/%{framework}-%{version}.tar.xz


BuildRequires:  kf5-rpm-macros >= %{version}
BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  qt5-qtbase-devel

BuildRequires:  kf5-kparts-devel >= %{version}
BuildRequires:  kf5-kxmlgui-devel >= %{version}

Requires:       kf5-filesystem >= %{version}

%description
KDE Frameworks 5 Tier 3 module with plugin interfaces for media player features.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-kparts-devel >= %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{framework}-%{version}

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc LICENSE README.md
%{_kf5_libdir}/libKF5MediaPlayer.so.*
%{_kf5_datadir}/kservicetypes5/*.desktop

%files devel
%{_kf5_includedir}/kmediaplayer_version.h
%{_kf5_includedir}/KMediaPlayer
%{_kf5_libdir}/libKF5MediaPlayer.so
%{_kf5_libdir}/cmake/KF5MediaPlayer
%{_kf5_datadir}/dbus-1/interfaces/*.xml


%changelog
* Sat Dec 19 2015 Liu Di <liudidi@gmail.com> - 5.17.0-2
- 为 Magic 3.0 重建

* Sun Nov 08 2015 Daniel Vrátil <dvratil@fedoraproject.org> - 5.16.0-1
- KDE Frameworks 5.16.0

* Thu Oct 08 2015 Daniel Vrátil <dvratil@redhat.com> - 5.15.0-1
- KDE Frameworks 5.15.0

* Wed Sep 16 2015 Daniel Vrátil <dvratil@redhat.com> - 5.14.0-1
- KDE Frameworks 5.14.0

* Wed Aug 19 2015 Daniel Vrátil <dvratil@redhat.com> - 5.13.0-1
- KDE Frameworks 5.13.0

* Wed Aug 19 2015 Daniel Vrátil <dvratil@redhat.com> - 5.13.0-1
- KDE Frameworks 5.13.0

* Tue Aug 11 2015 Daniel Vrátil <dvratil@redhat.com> - 5.13.0-0.1
- KDE Frameworks 5.13

* Fri Jul 17 2015 Daniel Vrátil <dvratil@redhat.com> - 5.12.0-1
- KDE Frameworks 5.12.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Daniel Vrátil <dvratil@redhat.com> - 5.11.0-1
- KDE Frameworks 5.11.0

* Mon May 11 2015 Daniel Vrátil <dvratil@redhat.com> - 5.10.0-1
- KDE Frameworks 5.10.0

* Tue Apr 07 2015 Daniel Vrátil <dvratil@redhat.com> - 5.9.0-1
- KDE Frameworks 5.9.0

* Mon Mar 16 2015 Daniel Vrátil <dvratil@redhat.com> - 5.8.0-1
- KDE Frameworks 5.8.0

* Fri Feb 27 2015 Daniel Vrátil <dvratil@redhat.com> - 5.7.0-2
- Rebuild (GCC 5)

* Mon Feb 16 2015 Daniel Vrátil <dvratil@redhat.com> - 5.7.0-1
- KDE Frameworks 5.7.0

* Mon Feb 09 2015 Daniel Vrátil <dvratil@redhat.com> - 5.7.0-1
- KDE Frameworks 5.7.0

* Thu Jan 08 2015 Daniel Vrátil <dvratil@redhat.com> - 5.6.0-1
- KDE Frameworks 5.6.0

* Mon Dec 08 2014 Daniel Vrátil <dvratil@redhat.com> - 5.5.0-1
- KDE Frameworks 5.5.0

* Mon Nov 03 2014 Daniel Vrátil <dvratil@redhat.com> - 5.4.0-1
- KDE Frameworks 5.4.0

* Tue Oct 07 2014 Daniel Vrátil <dvratil@redhat.com> - 5.3.0-1
- KDE Frameworks 5.3.0

* Mon Sep 15 2014 Daniel Vrátil <dvratil@redhat.com> - 5.2.0-1
- KDE Frameworks 5.2.0

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Aug 06 2014 Daniel Vrátil <dvratil@redhat.com> - 5.1.0-1
- KDE Frameworks 5.1.0

* Wed Jul 09 2014 Daniel Vrátil <dvratil@redhat.com> - 5.0.0-1
- KDE Frameworks 5.0.0

* Mon Jul 07 2014 Daniel Vrátil <dvratil@redhat.com> - 4.100.0-2
- fixed license
- fixed Source0 URL

* Tue Jun 03 2014 Daniel Vrátil <dvratil@redhat.com> - 4.100.0-1
- KDE Frameworks 4.100.0

* Mon May 05 2014 Daniel Vrátil <dvratil@redhat.com> - 4.99.0
- KDE Frameworks 4.99.0

* Mon Mar 31 2014 Jan Grulich <jgrulich@redhat.com> 4.98.0-1
- Update to KDE Frameworks 5 Beta 1 (4.98.0)

* Wed Mar 05 2014 Jan Grulich <jgrulich@redhat.com> 4.97.0-1
- Update to KDE Frameworks 5 Alpha 1 (4.97.0)

* Wed Feb 12 2014 Daniel Vrátil <dvratil@redhat.com> 4.96.0-1
- Update to KDE Frameworks 5 Alpha 1 (4.96.0)

* Wed Feb 05 2014 Daniel Vrátil <dvratil@redhat.com> 4.96.0-0.1.20140205git
- Update to pre-relase snapshot of 4.96.0

* Thu Jan 09 2014 Daniel Vrátil <dvratil@redhat.com> 4.95.0-1
- Update to KDE Frameworks 5 TP1 (4.95.0)

* Mon Jan  6 2014 Daniel Vrátil <dvratil@redhat.com>
- initial version
