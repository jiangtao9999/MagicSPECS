#define svn_number rc1
%define real_name smokegen

%define kde4_enable_final_bool ON

Name: kde4-%{real_name}
Summary: Smoke Generator
Summary(zh_CN.UTF-8): Smoke 生成器 
License: GPL v2 or Later
Group: User Interface/Desktops
Group(zh_CN.UTF-8): 用户界面/桌面
URL: http://www.kde.org
Version: 4.13.1
Release: 1%{?dist}
Source0: http://download.kde.org/stable/%{version}/src/%{real_name}-%{version}.tar.xz

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

%files devel
%defattr(-,root,root,-)
%{kde4_includedir}/*
%{kde4_libdir}/*.so
%{kde4_datadir}/smoke/cmake/*
%{kde4_datadir}/smokegen/*

%changelog
* Wed May 28 2014 Liu Di <liudidi@gmail.com> - 4.13.1-1
- 更新到 4.13.1

* Tue Aug 11 2009 Ni Hui <shuizhuyuanluo@126.com> - 3.2.3-1mgc
- 更新至 3.2.3
- 拆出开发包
- 己丑  六月廿一
