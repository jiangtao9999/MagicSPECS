#define git_number rc1
%define real_name picmi

%define kde4_enable_final_bool ON

Name: kde4-%{real_name}
Summary: A nonogram logic game
Summary(zh_CN.UTF-8): 一个古日本拼图逻辑游戏
Group: User Interface/Desktops
Group(zh_CN.UTF-8): 用户界面/桌面
Version: 4.14.3
Release: 3%{?dist}
License: GPLv2+ and GFDL
URL:     https://projects.kde.org/projects/kde/kdegames/%{name}
Source0: http://download.kde.org/stable/%{version}/src/%{real_name}-%{version}.tar.xz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: gettext
BuildRequires: cmake >= 2.6.2
BuildRequires: gettext
BuildRequires: libkdelibs4-devel >= 4.0.82

BuildRequires: desktop-file-utils
BuildRequires: kde4-libkdegames-devel >= %{version}

Requires: kde4-libkdegames%{?_isa} >= %{_kde4_version}

%description
Picmi is a single player puzzle game.  The object of the game is to
color cells according to numbers given at the side of the board.

%description -l zh_CN.UTF-8
Nonogram是一种逻辑游戏，以猜谜的方式绘画位图。在一个网格中，每一行和列
都有一组数，玩家需根据它们来填满或留空格子，最后就可以由此得出一幅图画。

例如，“4 8 3”的意思就是指该行或列上有三条独立的线，分别占了4、8和3格，而
每条线最少要由一个空格分开。传统上，玩家是以黑色填满格子，和以“×”号标记
一定不需要填充的格子。就此来看，这和踩地雷十分相似。但跟踩地雷不同的是，
即使填错了格子，也不会即时出局。Nonogram是一个NP完全的问题。

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

%clean
rm -rf %{buildroot} %{_builddir}/%{buildsubdir}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING
%{kde4_bindir}/*
#%{kde4_plugindir}/*
#%{kde4_libdir}/*.so.*
%{kde4_appsdir}/*
#%{kde4_configdir}/*
%{kde4_xdgappsdir}/*.desktop
#%{kde4_servicesdir}/*
#%{kde4_servicetypesdir}/*
#%{kde4_kcfgdir}/*
%{kde4_htmldir}/en/*
#%{kde4_mandir}/*
#%{kde4_libdir}/*.so
%{kde4_iconsdir}/*/*/a*/*

%changelog
* Mon Nov 09 2015 Liu Di <liudidi@gmail.com> - 4.14.3-3
- 为 Magic 3.0 重建

* Fri Oct 30 2015 Liu Di <liudidi@gmail.com> - 4.14.3-2
- 为 Magic 3.0 重建

* Wed Dec 31 2014 Liu Di <liudidi@gmail.com> - 4.14.3-1
- 更新到 4.14.3

* Fri Oct 31 2014 Liu Di <liudidi@gmail.com> - 4.14.2-1
- 更新到 4.14.2

* Fri Jul 18 2014 Liu Di <liudidi@gmail.com> - 4.13.3-1
- 更新到 4.13.3

* Thu Jun 19 2014 Liu Di <liudidi@gmail.com> - 4.13.2-1
- 更新到 4.13.2

* Wed Jun 04 2014 Liu Di <liudidi@gmail.com> - 4.13.1-1
- 更新到 4.13.1

* Mon Apr 28 2014 Liu Di <liudidi@gmail.com> - 4.13.0-2
- 为 Magic 3.0 重建

* Fri Dec 07 2012 Liu Di <liudidi@gmail.com> - 4.9.3-2
- 为 Magic 3.0 重建

* Tue Aug 11 2009 Ni Hui <shuizhuyuanluo@126.com> - 3.2.3-1mgc
- 更新至 3.2.3
- 拆出开发包
- 己丑  六月廿一
