#define svn_number rc1
%define real_name ktorrent

%define kde4_enable_final_bool OFF

%define libktorrentver 1.3.1

Name: kde4-ktorrent
Summary: BitTorrent client for KDE
Summary(zh_CN.UTF-8): Ktorrent 是一款 KDE 下的 BT 客户端
License: GPL v2 or Later
Group: Applications/Internet
Group(zh_CN.UTF-8): 应用程序/互联网
URL: http://ktorrent.org
Version:	4.3.1
Release: 3%{?dist}
Source0: http://ktorrent.pwsp.net/downloads/%{version}/%{real_name}-%{version}.tar.bz2

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: cmake >= 2.6.2
BuildRequires: gettext
BuildRequires: libkdelibs4-devel >= 4.0.82
BuildRequires: kde4-libktorrent-devel >= %{libktorrentver}

Requires:      kde4-libktorrent >= %{libktorrentver}

%description
KTorrent is a BitTorrent program for KDE. You can use it to 
download and upload files on the BitTorrent network. 

%description -l zh_CN.UTF-8
KTorrent 是一个 KDE 下的 BT 下载程序。它的主要特性有：
下载 torrent 文件；
上传速度控制；
使用 BT 网页搜索引擎进行互联网搜索；
支持 UDP Tracker 等。

%package devel
Summary: Development files for %{name}
Summary(zh_CN.UTF-8): %{name} 的开发文件
Group: Development/Libraries
Group(zh_CN.UTF-8): 开发/库
Requires: %{name} = %{version}-%{release}

%description devel
Contains the development files.

%description devel -l zh_CN.UTF-8
%{name} 的开发文件。包含 libbtcore 的开发文件。

%prep
%setup -q -n %{real_name}-%{version}

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
%clean_kde4_notifyrc_files
%adapt_kde4_notifyrc_files

%clean
rm -rf %{buildroot} %{_builddir}/%{buildsubdir}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING
%{kde4_bindir}/*
%{kde4_plugindir}/*
%{kde4_libdir}/*.so.*
%{kde4_appsdir}/ktorrent
%{kde4_iconsdir}/hicolor/*
%{kde4_xdgappsdir}/ktorrent.desktop
%{kde4_servicesdir}/*
%{kde4_servicetypesdir}/*
%{kde4_localedir}/*
#%{kde4_kcfgdir}/*
%{kde4_htmldir}/en/*

%if 0
%files devel
%defattr(-,root,root,-)
%{kde4_libdir}/*.so
%endif
%changelog
* Mon Nov 09 2015 Liu Di <liudidi@gmail.com> - 4.3.1-3
- 为 Magic 3.0 重建

* Fri Oct 30 2015 Liu Di <liudidi@gmail.com> - 4.3.1-2
- 为 Magic 3.0 重建

* Tue Jun 03 2014 Liu Di <liudidi@gmail.com> - 4.3.1-1
- 更新到 4.3.1

* Fri Dec 07 2012 Liu Di <liudidi@gmail.com> - 4.3.0-2
- 为 Magic 3.0 重建

* Tue Aug 11 2009 Ni Hui <shuizhuyuanluo@126.com> - 3.2.3-1mgc
- 更新至 3.2.3
- 拆出开发包
- 己丑  六月廿一
