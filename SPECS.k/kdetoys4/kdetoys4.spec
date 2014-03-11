%define rversion %{kde4_kdelibs_version}
%define release_number 1
%define real_name kdetoys


Name: kdetoys4
Summary: The KDE Toy Components
Summary(zh_CN.UTF-8): KDE 小玩具组件
License: LGPL v2 or later
Group: System/GUI/KDE
Group(zh_CN.UTF-8): 系统/GUI/KDE
URL: http://www.kde.org/
Version: %{rversion}
Release: %{release_number}%{?dist}
Source0: http://mirror.bjtu.edu.cn/kde/stable/%{rversion}/src/%{real_name}-%{rversion}.tar.xz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: libkdelibs4-devel
BuildRequires: libkdepimlibs4-devel
BuildRequires: kdebase4-workspace-devel
BuildRequires: strigi-devel >= 0.6.3

Requires: %{name}-amor = %{version}-%{release}
Requires: %{name}-kteatime = %{version}-%{release}
Requires: %{name}-ktux = %{version}-%{release}
#Requires: %{name}-kweather = %{version}-%{release}

%description
The KDE Toy Components.

%description -l zh_CN.UTF-8
KDE 小玩具组件。

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#     <--- amor
%package -n %{name}-amor
Group: System/GUI/KDE
Group(zh_CN.UTF-8): 系统/GUI/KDE
Summary: amor

%description -n %{name}-amor
amor.

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#     <--- kteatime
%package -n %{name}-kteatime
Group: System/GUI/KDE
Group(zh_CN.UTF-8): 系统/GUI/KDE
Summary: kteatime

%description -n %{name}-kteatime
kteatime.

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#     <--- ktux
%package -n %{name}-ktux
Group: System/GUI/KDE
Group(zh_CN.UTF-8): 系统/GUI/KDE
Summary: ktux

%description -n %{name}-ktux
ktux.

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#     <--- kweather
#%package -n %{name}-kweather
#Group: System/GUI/KDE
#Group(zh_CN.UTF-8): 系统/GUI/KDE
#Summary: kweather
#
#%description -n %{name}-kweather
#kweather.
#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#%package -n %{name}-devel
#Group: System/GUI/KDE
#Group(zh_CN.UTF-8): 系统/GUI/KDE
#Summary: KDE Toy Libraries: Build Environment
#Requires: libkdelibs4-devel
#Requires: %{name} = %{version}
#
#%description -n %{name}-devel
#This package contains all necessary include files and libraries needed
#to develop KDE Toy applications.
#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
%prep
%setup -q -n %{real_name}-%{rversion}

%build
mkdir build
cd build
%cmake_kde4 ..

make %{?_smp_mflags}


%install
cd build
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install


%clean_kde4_desktop_files
%clean_kde4_notifyrc_files
%adapt_kde4_notifyrc_files
magic_rpm_clean.sh

%clean
rm -rf %{buildroot} %{_builddir}/%{buildsubdir}

#%files -n %{name}-devel
#%defattr(-,root,root)
#%doc COPYING COPYING.LIB
#%{kde4_includedir}/*
#%{kde4_libdir}/*.so
#%exclude %{kde4_libdir}/libkdeinit4_*.so

%files
%defattr(-,root,root)

%files -n %{name}-amor
%defattr(-,root,root)
%{kde4_bindir}/amor
%{kde4_appsdir}/amor/*
%{kde4_dbus_interfacesdir}/org.kde.amor.xml
%{kde4_iconsdir}/hicolor/*/apps/amor.*
%{kde4_xdgappsdir}/amor.desktop
%{kde4_mandir}/man6/amor.6*
%doc %lang(en) %{kde4_htmldir}/en/amor

%files -n %{name}-kteatime
%defattr(-,root,root)
%{kde4_bindir}/kteatime
%{kde4_appsdir}/kteatime/*
%{kde4_iconsdir}/hicolor/*/apps/kteatime.*
%{kde4_xdgappsdir}/kteatime.desktop
%doc %lang(en) %{kde4_htmldir}/en/kteatime

%files -n %{name}-ktux
%defattr(-,root,root)
%{kde4_bindir}/ktux
%{kde4_appsdir}/ktux/*
%{kde4_iconsdir}/hicolor/*/apps/ktux.*
%{kde4_servicesdir}/ScreenSavers/ktux.desktop

#%files -n %{name}-kweather
#%defattr(-,root,root)
#%{kde4_bindir}/kweather*
#%{kde4_libdir}/libkdeinit4_kweatherreport.so
#%{kde4_plugindir}/kcm_weather*.so
#%{kde4_appsdir}/kweather*/*
#%{kde4_dbus_interfacesdir}/org.kde.kweather*.xml
#%{kde4_iconsdir}/hicolor/*/apps/kweather.*
#%{kde4_servicesdir}/kcmweather*.desktop
#%{kde4_servicesdir}/kweather*.desktop
#%doc %lang(en) %{kde4_htmldir}/en/kweather


%changelog
* Tue Aug 4 2009 Ni Hui <shuizhuyuanluo@126.com> - 4.3.0-1mgc
- 更新至 4.3.0
- 己丑  六月十四

* Tue Jun 30 2009 Ni Hui <shuizhuyuanluo@126.com> - 4.2.95-1mgc
- 更新至 4.2.95(KDE 4.3 RC1)
- 己丑  闰五月初八

* Sat Jun 13 2009 Ni Hui <shuizhuyuanluo@126.com> - 4.2.91-1mgc
- 更新至 4.2.91
- 己丑  五月廿一

* Sun May 17 2009 Ni Hui <shuizhuyuanluo@126.com> - 4.2.85-1mgc
- 更新至 4.2.85(KDE 4.3 beta1)
- 己丑  四月廿三

* Sat Apr 4 2009 Ni Hui <shuizhuyuanluo@126.com> - 4.2.2-1mgc
- 更新至 4.2.2
- 己丑  三月初九  [清明]

* Sun Mar 8 2009 Ni Hui <shuizhuyuanluo@126.com> - 4.2.1-0.1mgc
- 更新至 4.2.1
- 己丑  二月十二

* Sun Jan 25 2009 Ni Hui <shuizhuyuanluo@126.com> - 4.2.0-0.1mgc
- 更新至 4.2.0
- 戊子  十二月三十

* Wed Jan 14 2009 Ni Hui <shuizhuyuanluo@126.com> - 4.1.96-0.1mgc
- 更新至 4.1.96(KDE 4.2 RC1)
- relwithdeb 编译模式
- 戊子  十二月十九

* Sun Dec 14 2008 Ni Hui <shuizhuyuanluo@126.com> - 4.1.85-0.1mgc
- 更新至 4.1.85(KDE 4.2 Beta2)
- 戊子  十一月十七

* Fri Nov 07 2008 Ni Hui <shuizhuyuanluo@126.com> - 4.1.3-0.1mgc
- 更新至 4.1.3
- 戊子  十月初十  [立冬]

* Mon Sep 29 2008 Ni Hui <shuizhuyuanluo@126.com> - 4.1.2-0.1mgc
- 更新至 4.1.2
- 戊子  九月初一

* Sat Aug 30 2008 Ni Hui <shuizhuyuanluo@126.com> - 4.1.1-0.1mgc
- 更新至 4.1.1
- 戊子  七月三十

* Fri Jul 25 2008 Liu Di <liudidi@gmail.com> - 4.1.0-1mgc
- 更新到 4.1.0(KDE 4.1 正式版)

* Fri Jul 11 2008 Ni Hui <shuizhuyuanluo@126.com> - 4.0.98-0.1mgc
- 更新至 4.0.98(KDE 4.1 RC1)
- 戊子  六月初九

* Sat Jun 28 2008 Ni Hui <shuizhuyuanluo@126.com> - 4.0.84-0.1mgc
- 更新至 4.0.84
- 戊子  五月廿五

* Thu Jun 19 2008 Ni Hui <shuizhuyuanluo@126.com> - 4.0.83-0.1mgc
- 更新至 4.0.83-try1(第一次 tag 4.1.0-beta2 内部版本)
- 戊子  五月十六

* Thu Jun 12 2008 Ni Hui <shuizhuyuanluo@126.com> - 4.0.82-0.1mgc
- 更新至 4.0.82
- 戊子  五月初九

* Wed Jun 4 2008 Ni Hui <shuizhuyuanluo@126.com> - 4.0.81-0.1mgc
- 更新至 4.0.81
- 戊子  五月初一

* Sat May 24 2008 Ni Hui <shuizhuyuanluo@126.com> - 4.0.80-0.1mgc
- 更新至 4.0.80(try1 内部版本)
- 戊子  四月二十

* Sat Apr 26 2008 Ni Hui <shuizhuyuanluo@126.com> - 4.0.71-0.1mgc
- 更新至 4.0.71
- 定义 kde4 路径
- 戊子  三月廿一

* Sun Feb 10 2008 Ni Hui <shuizhuyuanluo@126.com> - 4.0.1-0.1mgc
- 更新至 4.0.1

* Fri Jan 18 2008 Ni Hui <shuizhuyuanluo@126.com> - 4.0.0-0.1mgc
- 更新至 4.0.0

* Sat Nov 24 2007 Ni Hui <shuizhuyuanluo@126.com> - 3.96.0-0.1mgc
- 更新至 3.96.0 (KDE4-RC1)

* Sat Oct 20 2007 Ni Hui <shuizhuyuanluo@126.com> - 3.94.0-0.1mgc
- 首次生成 rpm 包
