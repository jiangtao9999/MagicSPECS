
%{!?_licensedir:%global license %%doc}

Name:    libkgeomap
Summary: A wrapper around different world-map components, to browse and arrange photos over a map
Summary(zh_CN.UTF-8): 不同的世界地图组件的包装器，可以在地图上浏览和安排图像
Version: 15.12.1
Release: 1%{?dist}

License: GPLv2+
URL:     https://projects.kde.org/projects/kde/kdegraphics/libs/libkgeomap
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: kdelibs4-devel >= 4.14

%{?kdelibs4_requires}

%description
%{summary}.

%description -l zh_CN.UTF-8
不同的世界地图组件的包装器，可以在地图上浏览和安排图像。

%package devel
Summary:  Development files for %{name}
Summary(zh_CN.UTF-8): %{name} 的开发包
License: GPLv2+ and LGPLv2+ and BSD
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: kdelibs4-devel 
%description devel
%{summary}.
%description devel -l zh_CN.UTF-8
%{name} 的开发包。

%prep
%setup -q


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
magic_rpm_clean.sh

%check
export PKG_CONFIG_PATH=%{buildroot}%{_libdir}/pkgconfig
pkg-config --modversion libkgeomap


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc AUTHORS README TODO
%license COPYING
%{_kde4_appsdir}/libkgeomap/
%{_kde4_libdir}/libkgeomap.so.2*

%files devel
%license COPYING.LIB
%{_kde4_includedir}/libkgeomap/
%{_kde4_libdir}/libkgeomap.so
%{_kde4_libdir}/pkgconfig/libkgeomap.pc
%license COPYING-CMAKE-SCRIPTS
%{_kde4_appsdir}/cmake/modules/*.cmake


%changelog
* Mon Nov 09 2015 Liu Di <liudidi@gmail.com> - 15.08.2-2
- 为 Magic 3.0 重建

* Sun Apr 19 2015 Rex Dieter <rdieter@fedoraproject.org> 15.04.0-2
- rebuild (marble)

* Mon Apr 13 2015 Rex Dieter <rdieter@fedoraproject.org> 15.04.0-1
- 15.04.0

* Sat Apr 11 2015 Rex Dieter <rdieter@fedoraproject.org> 15.03.97-2
- switch to publically-available 15.03.97
- fix missing %%description
- -devel: %%license COPYING.LIB COPYING-CMAKE_SCRIPTS

* Sat Apr 11 2015 Rex Dieter <rdieter@fedoraproject.org> 15.04.0-1
- 15.04.0

