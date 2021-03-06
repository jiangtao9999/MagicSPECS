# %global         git_commit 1496e4d
Name:           libmm-qt
Version: 1.0.1
Release:        4%{?dist}
Epoch:          1
Summary:        Qt-only wrapper for ModemManager DBus API
Summary(zh_CN.UTF-8): ModemMoanager DBus API 的 Qt 接口

Group:          System Environment/Libraries
Group(zh_CN.UTF-8): 系统环境/库
License:        LGPLv2+
URL:            https://projects.kde.org/projects/extragear/libs/libmm-qt

Source0:        http://download.kde.org/unstable/modemmanager-qt/%{version}/src/%{name}-%{version}.tar.xz
# Package from git snapshots using releaseme scripts
# Source0:        %{name}-%{version}-git%{git_commit}.tar.bz2

BuildRequires:  cmake >= 2.6
BuildRequires:  pkgconfig(QtCore)
BuildRequires:  ModemManager-devel >= 1.0.0

Requires:  ModemManager >= 1.0.0

%description
Qt library for ModemManager

%description -l zh_CN.UTF-8
ModemManager 的 Qt 库

%package devel
Summary: Development files for %{name}
Summary(zh_CN.UTF-8): %{name} 的开发包
Group: Development/Libraries
Group(zh_CN.UTF-8): 开发/库
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}
%description devel
Qt libraries and header files for developing applications that use ModemManager

%description devel -l zh_CN.UTF-8
%{name} 的开发包。

%prep
%setup -qn %{name}-%{version}

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
rm -rf %{buildroot}

make install/fast  DESTDIR=%{buildroot} -C %{_target_platform}
magic_rpm_clean.sh

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc README
%{_libdir}/libModemManagerQt.so.*


%files devel
%{_libdir}/pkgconfig/ModemManagerQt.pc
%{_includedir}/ModemManagerQt/
%{_libdir}/libModemManagerQt.so

%changelog
* Mon Nov 09 2015 Liu Di <liudidi@gmail.com> - 1:1.0.1-4
- 为 Magic 3.0 重建

* Sat Oct 31 2015 Liu Di <liudidi@gmail.com> - 1:1.0.1-3
- 为 Magic 3.0 重建

* Tue Jul 22 2014 Liu Di <liudidi@gmail.com> - 1:1.0.1-2
- 更新到 1.0.1

* Thu Nov 21 2013 Jan Grulich <jgrulich@redhat.com> - 1:1.0.0-2
- Update to 1.0.0 (stable release)

* Wed Oct 9 2013 Jan Grulich <jgrulich@redhat.com> - 1:1.0.0-1.20131009git1496e4d
- Update to current git snapshot

* Mon Sep 16 2013 Jan Grulich <jgrulich@redhat.com> - 1:0.5.1-1
- Update to 0.5.1

* Tue Sep 10 2013 Jan Grulich <jgrulich@redhat.com - 1:0.5.0-1
- First stable release (0.5.0)

* Mon Aug 12 2013 Lukas Tinkl <ltinkl@redhat.com> - 0.6.0-4.20130812gitd84301
- Update to current git snapshot

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-3.20130613gitc5920e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 13 2013 Jan Grulich <jgrulich@redhat.com> - 0.6.0-2.20130613gitc5920e0
- Update to the current git snapshot

* Fri May 31 2013 Jan Grulich <jgrulich@redhat.com> - 0.6.0-1.20130422git657646b
- Initial package
- Based on git snapshot 657646bdc1eb9913e07a8307afd2b47b6225209b
