Summary: WebQQ 2.0 tray
Name: webqq
Version: 0.2
Release: 2%{dist}
License: GPL
URL: http://ftp.magiclinux.org.cn/haulm
Group: Applications/Internet
Group(zh_CN): 应用程序/互联网
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot-%(%{__id_u} -n)
Source0: %{name}-%{version}.tar.gz
Source1: %{name}.desktop
Prefix: %{_prefix}
Requires: qt4-webkit
Packager: haulm<haulm@126.com>, Magic Group
Autoreqprov: 0
%description
 WebQQ 2.0 tray program.

%description -l zh_CN
WebQQ 2.0 Magic 托盘管理程序

%prep

%setup -q -n webqq

%Build
qmake-qt4
make
lrelease qq_cn.ts
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/opt/webqq
mkdir -p %{buildroot}/usr/bin/
mkdir -p %{buildroot}/usr/share/applications/
install -m 755 ./webqq %{buildroot}/opt/webqq
install -m 644 ./qq_cn.qm %{buildroot}/opt/webqq
cp %{SOURCE1} %{buildroot}/usr/share/applications/
cp webqq.png %{buildroot}/opt/webqq/
ln -s /opt/webqq/webqq %{buildroot}/usr/bin/webqq
%clean
rm -rf %{buildroot} %{_builddir}/%{buildsubdir}
%files
%defattr(-,root,root)
/opt/webqq
/usr/share/applications/
/usr/bin
%changelog
* Sun Dec 09 2012 Liu Di <liudidi@gmail.com> - 0.2-2
- 为 Magic 3.0 重建


