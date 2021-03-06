Summary:   GLib wrapper around libusb1
Summary(zh_CN.UTF-8): libusb1 的 GLib 接口
Name:      libgusb
Version:   0.2.7
Release:   5%{?dist}
License:   LGPLv2+
URL:       https://gitorious.org/gusb/
Source0:   http://people.freedesktop.org/~hughsient/releases/%{name}-%{version}.tar.xz

BuildRequires: glib2-devel >= 2.16.1
BuildRequires: libtool
BuildRequires: libgudev1-devel
BuildRequires: libusb1-devel
BuildRequires: gobject-introspection-devel
BuildRequires: vala-devel
BuildRequires: vala-tools

%description
GUsb is a GObject wrapper for libusb1 that makes it easy to do
asynchronous control, bulk and interrupt transfers with proper
cancellation and integration into a mainloop.

%description -l zh_CN.UTF-8
libusb1 的 GLib 接口。

%package devel
Summary: Libraries and headers for gusb
Summary(zh_CN.UTF-8): %{name} 的开发包
Requires: %{name} = %{version}-%{release}

%description devel
GLib headers and libraries for gusb.

%description devel -l zh_CN.UTF-8
%{name} 的开发包。

%prep
%setup -q

%build
%configure \
        --disable-static                \
        --enable-vala=yes               \
        --enable-introspection=yes      \
        --disable-gtk-doc               \
        --enable-gudev                  \
        --disable-dependency-tracking

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/libgusb.la
magic_rpm_clean.sh

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc README AUTHORS NEWS COPYING
%{_libdir}/libgusb.so.?
%{_libdir}/libgusb.so.?.0.*
%{_libdir}/girepository-1.0/GUsb-1.0.typelib

%files devel
%defattr(-,root,root,-)
%{_includedir}/gusb-1
%{_libdir}/libgusb.so
%{_libdir}/pkgconfig/gusb.pc
%{_datadir}/gtk-doc/html/gusb
%{_datadir}/gir-1.0/GUsb-1.0.gir
%{_datadir}/vala/vapi/gusb.vapi

%changelog
* Sat Nov 28 2015 Liu Di <liudidi@gmail.com> - 0.2.7-5
- 为 Magic 3.0 重建

* Mon Nov 09 2015 Liu Di <liudidi@gmail.com> - 0.1.6-4
- 为 Magic 3.0 重建

* Sat Oct 31 2015 Liu Di <liudidi@gmail.com> - 0.1.6-3
- 更新到 0.2.7

* Wed Jul 16 2014 Liu Di <liudidi@gmail.com> - 0.1.6-2
- 为 Magic 3.0 重建

* Tue Feb 06 2013 Richard Hughes <richard@hughsie.com> 0.1.6-1
- New upstream version
- Do not use deprecated GLib functionality
- Unref the GMainloop after it has been run, not when just quit

* Tue Feb 05 2013 Richard Hughes <richard@hughsie.com> 0.1.5-1
- New upstream version

* Tue Nov 06 2012 Richard Hughes <richard@hughsie.com> 0.1.4-1
- New upstream version
- Add GObject Introspection support
- Add Vala bindings

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 05 2011 Richard Hughes <richard@hughsie.com> 0.1.3-1
- New upstream version
- Add a missing error enum value

* Fri Nov 11 2011 Richard Hughes <richard@hughsie.com> 0.1.2-1
- New upstream version
- Ignore EBUSY when trying to detach a detached kernel driver

* Tue Nov 01 2011 Richard Hughes <richard@hughsie.com> 0.1.1-1
- New upstream version

* Thu Sep 15 2011 Richard Hughes <richard@hughsie.com> 0.1.0-1
- Initial version for Fedora package review
