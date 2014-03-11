%define rversion 1.4.1
%define release_number 1
%define real_name kdevplatform

%define kde4_enable_final_bool OFF

Name: kdevplatform
Summary: The KDE Develop Platform
License: LGPL v2 or later
Group: System/GUI/KDE
Group(zh_CN.UTF-8): 系统/GUI/KDE
URL: http://www.kde.org/
Version: %{rversion}
Release: %{release_number}%{?dist}.1
Source0: %{real_name}-%{rversion}.tar.bz2


BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: libkdelibs4-devel >= 4.1.60
BuildRequires: gettext
BuildRequires: boost-devel
BuildRequires: subversion-devel

# TODO: for kompare kpart support, please enable it in KDE 4.4.x  --- nihui
BuildRequires: kdesdk4-devel

%description
The KDE Develop Platform.

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#     <--- 开发包
%package -n %{name}-devel
Group: System/GUI/KDE
Group(zh_CN.UTF-8): 系统/GUI/KDE
Summary: KDE Develop Platforms: Build Environment
Requires: libkdelibs4-devel
Requires: %{name} = %{version}

%description -n %{name}-devel
This package contains all necessary include files and libraries needed
to develop KDE Develop Platforms.

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

magic_rpm_clean.sh

%clean_kde4_desktop_files


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot} %{_builddir}/%{buildsubdir}

%files -n %{name}-devel
%defattr(-,root,root)
%doc COPYING.*
%{kde4_includedir}/*
%{kde4_libdir}/*.so
# internal cmake modules
%{kde4_libdir}/cmake
#%{kde4_appsdir}/cmake

%files
%defattr(-,root,root)
%doc COPYING.*
%{kde4_bindir}/*
%{kde4_plugindir}/*.so
%{kde4_libdir}/*.so.*
%{kde4_appsdir}/*
#%exclude %{kde4_appsdir}/cmake
%{kde4_iconsdir}/*
%{kde4_servicesdir}/*
%{kde4_servicetypesdir}/*
%{kde4_localedir}/*

%changelog
* Fri Dec 07 2012 Liu Di <liudidi@gmail.com> - 1.2.3-1.1
- 为 Magic 3.0 重建

* Fri Aug 21 2009 Ni Hui <shuizhuyuanluo@126.com> - 0.9.95-1mgc
- 更新至 0.9.95
- 己丑  七月初二

* Tue Jun 30 2009 Ni Hui <shuizhuyuanluo@126.com> - 0.9.94-1mgc
- 更新至 0.9.94
- 己丑  闰五月初八

* Fri May 29 2009 Ni Hui <shuizhuyuanluo@126.com> - 0.9.93-1mgc
- 更新至 0.9.93
- 己丑  五月初六

* Sat Apr 4 2009 Ni Hui <shuizhuyuanluo@126.com> - 0.9.91-1mgc
- 更新至 0.9.91
- 己丑  三月初九  [清明]

* Thu Jan 15 2009 Ni Hui <shuizhuyuanluo@126.com> - 0.9.85-0.1mgc
- 更新至 0.9.85
- 去除 teamwork 插件支持(通不过编译)
- 戊子  十二月二十

* Sat Dec 13 2008 Ni Hui <shuizhuyuanluo@126.com> - 0.9.84-0.1mgc
- 首次生成 rpm 包
- 戊子  十一月十七
