Name:          gupnp-av
Version:	0.12.7
Release:       4%{?dist}
Summary:       A collection of helpers for building UPnP AV applications
Summary(zh_CN.UTF-8): 构建 UPnP 音视频程序的帮助程序

Group:         System Environment/Libraries
Group(zh_CN.UTF-8): 系统环境/库
License:       LGPLv2+
URL:           http://www.gupnp.org/
%define majorver %(echo %{version} | awk -F. '{print $1"."$2}')
Source0:       http://download.gnome.org/sources/gupnp-av/%{majorver}/%{name}-%{version}.tar.xz
Patch0:        gupnp-av-fixdso.patch

BuildRequires: glib2-devel
BuildRequires: gtk-doc
BuildRequires: gssdp-devel >= 0.14.0
BuildRequires: gupnp-devel >= 0.20.0
BuildRequires: gobject-introspection-devel >= 1.36.0
BuildRequires: libxml2-devel
BuildRequires: libsoup-devel

%description
GUPnP is an object-oriented open source framework for creating UPnP
devices and control points, written in C using GObject and libsoup.
The GUPnP API is intended to be easy to use, efficient and flexible.

GUPnP-AV is a collection of helpers for building AV (audio/video) 
applications using GUPnP.

%description -l zh_CN.UTF-8
构建 UPnP 音视频程序的帮助程序。

%package devel
Summary: Development package for %{name}
Summary(zh_CN.UTF-8): %{name} 的开发包
Group: Development/Libraries
Group(zh_CN.UTF-8): 开发/库
Requires: %{name} = %{version}-%{release}
Requires: gssdp-devel
Requires: gupnp-devel
Requires: pkgconfig

%description devel
Files for development with %{name}.

%description devel -l zh_CN.UTF-8
%{name} 的开发包。

%package docs
Summary: Documentation files for %{name}
Summary(zh_CN.UTF-8): %{name} 的文档
Group: Development/Libraries
Group(zh_CN.UTF-8): 开发/库
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description docs
This package contains developer documentation for %{name}.

%description docs -l zh_CN.UTF-8
%{name} 的文档。

%prep
%setup -q
%patch0 -p1 -b .fixdso

%build
%configure --disable-static
make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot}

#Remove libtool archives.
find %{buildroot} -name '*.la' -exec rm -f {} ';'
magic_rpm_clean.sh

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS COPYING README
%{_libdir}/libgupnp-av-1.0.so.*
%{_libdir}/girepository-1.0/GUPnPAV-1.0.typelib
%{_datadir}/%{name}

%files devel
%{_includedir}/gupnp-av-1.0
%{_libdir}/pkgconfig/gupnp-av-1.0.pc
%{_libdir}/libgupnp-av-1.0.so
%{_datadir}/gir-1.0/GUPnPAV-1.0.gir
%{_datadir}/vala/vapi/gupnp-av-1.0.*

%files docs
%{_datadir}/gtk-doc/html/%{name}

%changelog
* Sun Nov 08 2015 Liu Di <liudidi@gmail.com> - 0.12.7-4
- 为 Magic 3.0 重建

* Fri Oct 30 2015 Liu Di <liudidi@gmail.com> - 0.12.7-3
- 更新到 0.12.7

* Tue Apr 15 2014 Liu Di <liudidi@gmail.com> - 0.12.5-2
- 为 Magic 3.0 重建

* Tue Feb  4 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.12.5-1
- 0.12.5 release
- http://ftp.gnome.org/pub/GNOME/sources/gupnp-av/0.12/gupnp-av-0.12.5.news

* Mon Nov 18 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.12.4-1
- 0.12.4 release
- http://ftp.gnome.org/pub/GNOME/sources/gupnp-av/0.12/gupnp-av-0.12.4.news

* Wed Oct 16 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.12.3-1
- 0.12.3 release
- http://ftp.gnome.org/pub/GNOME/sources/gupnp-av/0.12/gupnp-av-0.12.3.news

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 30 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.12.2-1
- 0.12.2 release
- http://ftp.gnome.org/pub/GNOME/sources/gupnp-av/0.12/gupnp-av-0.12.2.news

* Sun May 12 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.12.1-2
- Move xsd files to main rpm (RHBZ 962166)

* Tue Mar 19 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.12.1-1
- 0.12.1 release
- http://ftp.gnome.org/pub/GNOME/sources/gupnp-av/0.12/gupnp-av-0.12.1.news

* Thu Feb 21 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.12.0-1
- 0.12.0 release
- http://ftp.gnome.org/pub/GNOME/sources/gupnp-av/0.12/gupnp-av-0.12.0.news

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec 14 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.11.6-1
- 0.11.6 release
- http://ftp.gnome.org/pub/GNOME/sources/gupnp-av/0.11/gupnp-av-0.11.6.news

* Thu Dec  6 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.11.5-1
- 0.11.5 release
- http://ftp.gnome.org/pub/GNOME/sources/gupnp-av/0.11/gupnp-av-0.11.5.news

* Sat Dec  1 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.11.4-1
- 0.11.4 release
- http://ftp.gnome.org/pub/GNOME/sources/gupnp-av/0.11/gupnp-av-0.11.4.news

* Mon Nov 19 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.11.3-1
- 0.11.3 release
- http://ftp.gnome.org/pub/GNOME/sources/gupnp-av/0.11/gupnp-av-0.11.3.news

* Mon Oct 29 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.11.2-1
- 0.11.2 release
- http://ftp.gnome.org/pub/GNOME/sources/gupnp-av/0.11/gupnp-av-0.11.2.news

* Sun Oct  7 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.11.0-1
- 0.11.0 release
- http://ftp.gnome.org/pub/GNOME/sources/gupnp-av/0.11/gupnp-av-0.11.0.news

* Sun Aug 19 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.10.3-1
- 0.10.3 release
- http://ftp.gnome.org/pub/GNOME/sources/gupnp-av/0.10/gupnp-av-0.10.3.news

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Apr 21 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.10.2-1
- 0.10.2 release
- http://ftp.gnome.org/pub/GNOME/sources/gupnp-av/0.10/gupnp-av-0.10.2.news

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep  5 2011 Zeeshan Ali <zeenix@redhat.com> - 0.10.1-2
- Push a new release to build against latest gssdp and gupnp.

* Mon Sep  5 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.10.1-1
- 0.10.1 release
- http://ftp.gnome.org/pub/GNOME/sources/gupnp-av/0.10/gupnp-av-0.10.1.news

* Fri Sep  2 2011 Zeeshan Ali <zeenix@redhat.com> - 0.10.0-1
- 0.10.0 release
- http://ftp.acc.umu.se/pub/GNOME/sources/gupnp-av/0.10/gupnp-av-0.10.0.news

* Thu Jun 16 2011 Peter Robinson <pbrobinson@gmail.com> - 0.9.1-1
- 0.9.1 release

* Thu Jun 16 2011 Peter Robinson <pbrobinson@gmail.com> - 0.9.0-1
- 0.9.0 release

* Sat Apr  9 2011 Peter Robinson <pbrobinson@gmail.com> - 0.8.0-1
- 0.8.0 stable release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec  2 2010 Peter Robinson <pbrobinson@gmail.com> 0.7.1-1
- Update to 0.7.1

* Mon Nov  8 2010 Peter Robinson <pbrobinson@gmail.com> 0.7.0-1
- Update to 0.7.0

* Wed Sep 29 2010 Peter Robinson <pbrobinson@gmail.com> 0.6.1-1
- Update to 0.6.1

* Wed Sep 22 2010 Matthias Clasen <mclasen@redhat.com> 0.6.0-2
- Rebuild against newer gobject-introspection

* Fri Sep 17 2010 Peter Robinson <pbrobinson@gmail.com> 0.6.0-1
- Update to 0.6.0

* Tue Aug 17 2010 Peter Robinson <pbrobinson@gmail.com> 0.5.9-2
- Update source URL

* Sat Aug 14 2010 Peter Robinson <pbrobinson@gmail.com> 0.5.9-1
- Update to 0.5.9

* Tue Aug  3 2010 Peter Robinson <pbrobinson@gmail.com> 0.5.8-2
- Add patch to fix dso linking issues

* Mon Aug  2 2010 Peter Robinson <pbrobinson@gmail.com> 0.5.8-1
- Update to 0.5.8

* Thu Jul 15 2010 Colin Walters <walters@verbum.org> - 0.5.7-2
- Rebuild with new gobject-introspection

* Fri Jun 25 2010 Peter Robinson <pbrobinson@gmail.com> 0.5.7-1
- Update to 0.5.7

* Mon Jun 21 2010 Peter Robinson <pbrobinson@gmail.com> 0.5.6-1
- Update to 0.5.6

* Fri Apr  9 2010 Peter Robinson <pbrobinson@gmail.com> 0.5.5-1
- Update to 0.5.5

* Fri Feb  5 2010 Peter Robinson <pbrobinson@gmail.com> 0.5.4-1
- Update to 0.5.4

* Sat Nov 21 2009 Peter Robinson <pbrobinson@gmail.com> 0.5.2-1
- Update to 0.5.2

* Thu Sep 17 2009 Bastien Nocera <bnocera@redhat.com> 0.5.1-1
- Update to 0.5.1

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun  9 2009 Peter Robinson <pbrobinson@gmail.com> 0.4.1-1
- New upstream release

* Sun Apr 12 2009 Peter Robinson <pbrobinson@gmail.com> 0.4-1
- New upstream release

* Wed Mar 4  2009 Peter Robinson <pbrobinson@gmail.com> 0.3.1-3
- Move docs to noarch subpackage

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 3  2009 Peter Robinson <pbrobinson@gmail.com> 0.3.1-1
- New upstream release

* Thu Dec 18 2008 Peter Robinson <pbrobinson@gmail.com> 0.3-1
- New upstream release

* Thu Dec 18 2008 Peter Robinson <pbrobinson@gmail.com> 0.2.1-7
- Add gtk-doc build req

* Mon Dec 1 2008 Peter Robinson <pbrobinson@gmail.com> 0.2.1-6
- Fix directory ownership

* Sat Nov 22 2008 Peter Robinson <pbrobinson@gmail.com> 0.2.1-5
- Update package summary

* Mon Oct 20 2008 Peter Robinson <pbrobinson@gmail.com> 0.2.1-4
- Add some requires for the devel package

* Fri Aug 29 2008 Peter Robinson <pbrobinson@gmail.com> 0.2.1-3
- Some spec file cleanups

* Tue Jun 17 2008 Peter Robinson <pbrobinson@gmail.com> 0.2.1-2
- Fix build on rawhide

* Tue Jun 17 2008 Peter Robinson <pbrobinson@gmail.com> 0.2.1-1
- Initial release
