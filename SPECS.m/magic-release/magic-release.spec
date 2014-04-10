Summary: magic-release
Summary(zh_CN.UTF-8): MagicLinux的发行文件
Name: magic-release
Version: 3.0
Release: 5%{?dist}
Group: System Environment/Base
Group(zh_CN.UTF-8): 系统环境/基本
License: GPL
Source: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root
Packager: lovewilliam<williamlovecyl@hotmail.com>
# Following are optional fields
URL: http://www.magiclinux.org
Distribution: Magic Linux
BuildArch: noarch

%description
magic-release
for system Version

%description -l zh_CN.UTF-8
描述系统版本的发行文件

%define fedora_version 21
%define dist_version 30

%prep
%setup -q
#%patch

%build

%install
mkdir -p ${RPM_BUILD_ROOT}/etc
cp etc/* ${RPM_BUILD_ROOT}/etc
mkdir -p ${RPM_BUILD_ROOT}/usr/share/doc/magic-release-3.0-Kaibao
cp releasedoc/* ${RPM_BUILD_ROOT}/usr/share/doc/magic-release-3.0-Kaibao
ln -s magic-release $RPM_BUILD_ROOT/etc/redhat-release
ln -s magic-release $RPM_BUILD_ROOT/etc/system-release

# Set up the dist tag macros
install -d -m 755 $RPM_BUILD_ROOT/etc/rpm
cat >> $RPM_BUILD_ROOT/etc/rpm/macros.dist << EOF
# dist macros.

%%fedora                %{fedora_version}
%%dist          	mgc%{dist_version}
%%fc%{fedora_version}             1
EOF

magic_rpm_clean.sh

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root,-)
/etc/*
/usr/*

%changelog
* Wed Apr 09 2014 Liu Di <liudidi@gmail.com> - 3.0-5
- 修改以符合 LSB 标准

* Fri May 17 2013 Liu Di <liudidi@gmail.com> - 3.0-4
- 重新编译

* Fri Dec 07 2012 Liu Di <liudidi@gmail.com> - 3.0-3
- 为 Magic 3.0 重建

* Tue Jul 31 2012 Liu Di <liudidi@gmail.com> - 3.0-2
- 为 Magic 3.0 重建

* Fri Apr 22 2011 Liu Di <liudidi@gmail.com> - 3.0-0.1
- 2.9999

* Fri Jul 08 2005 lovewilliam <williamlovecyl@hotmail.com>
- 2.0

* Tue Jul 05 2005 lovewilliam <williamlovecyl@hotmail.com>
- update to 1.9 genius

* Sat Jun 04 2005  lovewilliam<williamlovecyl@hotmail.com>
- Initial spec
