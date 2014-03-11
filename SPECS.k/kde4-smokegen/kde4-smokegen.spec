%define rversion %{kde4_kdelibs_version}
#define svn_number rc1
%define real_name smokegen

%define kde4_enable_final_bool OFF

Name: kde4-%{real_name}
Summary: Cantor for KDE Edu
Summary(zh_CN.UTF-8): KDE Edu 的数学组件 
License: GPL v2 or Later
Group: Applications/Internet
Group(zh_CN.UTF-8): 应用程序/互联网
URL: http://ktorrent.org
Version: %{rversion}
Release: 1%{?dist}
Source0: %{real_name}-%{rversion}.tar.bz2

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: cmake >= 2.6.2
BuildRequires: gettext
BuildRequires: libkdelibs4-devel >= 4.0.82


%description
Cantor is an application that lets you use your favorite mathematical 
applications from within a nice KDE-integrated Worksheet Interface. 
It offers assistant dialogs for common tasks and allows you to share 
your worksheets with others.

%description -l zh_CN.UTF-8
Cantor 是一个 KDE 集成程序，可以让你用你喜欢的数学程序做为后端进行
工作表处理。

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

%clean
rm -rf %{buildroot} %{_builddir}/%{buildsubdir}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING
%{kde4_bindir}/*
%{kde4_libdir}/*.so.*
%{kde4_libdir}/smokegen/*
#%{kde4_plugindir}/*
#%{kde4_iconsdir}/hicolor/*
#%{kde4_xdgappsdir}/*.desktop
#%{kde4_appsdir}/*
#%{kde4_kcfgdir}/*.kcfg
#%{kde4_servicesdir}/*
#%{kde4_servicetypesdir}/*
#%{kde4_configdir}/*
#%{kde4_htmldir}/en/*

%files devel
%defattr(-,root,root,-)
%{kde4_includedir}/*
%{kde4_libdir}/*.so
%{kde4_datadir}/smoke/cmake/*
%{kde4_datadir}/smokegen/*

%changelog
* Tue Aug 11 2009 Ni Hui <shuizhuyuanluo@126.com> - 3.2.3-1mgc
- 更新至 3.2.3
- 拆出开发包
- 己丑  六月廿一
