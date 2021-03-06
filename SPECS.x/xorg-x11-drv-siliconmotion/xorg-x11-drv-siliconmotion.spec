%define tarball xf86-video-siliconmotion
%define moduledir %(pkg-config xorg-server --variable=moduledir )
%define driverdir	%{moduledir}/drivers

Summary:    Xorg X11 siliconmotion video driver
Summary(zh_CN.UTF-8): Xorg X11 siliconmotion 显卡驱动
Name:       xorg-x11-drv-siliconmotion
Version:	1.7.8
Release:	4%{?dist}
URL:        http://www.x.org
License:    MIT
Group:      User Interface/X Hardware Support
Group(zh_CN.UTF-8): 用户界面/X 硬件支持

Source0:    http://ftp.nara.wide.ad.jp/pub/X11/x.org/individual/driver/%{tarball}-%{version}.tar.bz2
Source2:    make-git-snapshot.sh
Source3:    commitid

ExcludeArch: s390 s390x %{?rhel:ppc ppc64}

BuildRequires: xorg-x11-server-devel >= 1.10.99.902

Requires: Xorg %(xserver-sdk-abi-requires ansic)
Requires: Xorg %(xserver-sdk-abi-requires videodrv)

%description 
X.Org X11 siliconmotion video driver.

%description -l zh_CN.UTF-8
Xorg X11 siliconmotion 显卡驱动。

%prep
%setup -q -n %{tarball}-%{version}

%build
autoreconf -fisv
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

# FIXME: Remove all libtool archives (*.la) from modules directory.  This
# should be fixed in upstream Makefile.am or whatever.
find $RPM_BUILD_ROOT -regex ".*\.la$" | xargs rm -f --

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{driverdir}/siliconmotion_drv.so
%{_mandir}/man4/siliconmotion.4*

%changelog
* Sun Nov 15 2015 Liu Di <liudidi@gmail.com> - 1.7.8-4
- 为 Magic 3.0 重建

* Fri Nov 06 2015 Liu Di <liudidi@gmail.com> - 1.7.8-3
- 为 Magic 3.0 重建

* Mon Oct 26 2015 Liu Di <liudidi@gmail.com> - 1.7.8-2
- 更新到 1.7.8

* Mon Jan 13 2014 Adam Jackson <ajax@redhat.com> - 1.7.7-13
- 1.15 ABI rebuild

* Tue Dec 17 2013 Adam Jackson <ajax@redhat.com> - 1.7.7-12
- 1.15RC4 ABI rebuild

* Wed Nov 20 2013 Adam Jackson <ajax@redhat.com> - 1.7.7-11
- 1.15RC2 ABI rebuild

* Wed Nov 06 2013 Adam Jackson <ajax@redhat.com> - 1.7.7-10
- 1.15RC1 ABI rebuild

* Fri Oct 25 2013 Adam Jackson <ajax@redhat.com> - 1.7.7-9
- ABI rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 07 2013 Peter Hutterer <peter.hutterer@redhat.com> - 1.7.7-7
- require xorg-x11-server-devel, not -sdk

* Thu Mar 07 2013 Peter Hutterer <peter.hutterer@redhat.com> - 1.7.7-6
- ABI rebuild

* Fri Feb 15 2013 Peter Hutterer <peter.hutterer@redhat.com> - 1.7.7-5
- ABI rebuild

* Fri Feb 15 2013 Peter Hutterer <peter.hutterer@redhat.com> - 1.7.7-4
- ABI rebuild

* Thu Jan 10 2013 Adam Jackson <ajax@redhat.com> - 1.7.7-3
- ABI rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 18 2012 Dave Airlie <airlied@redhat.com> 1.7.7-1
- siliconmotion 1.7.7

* Fri Apr 27 2012 Adam Jackson <ajax@redhat.com> 1.7.6-1
- siliconmotion 1.7.6

* Thu Apr 05 2012 Adam Jackson <ajax@redhat.com> - 1.7.5-10
- RHEL arch exclude updates

* Sat Feb 11 2012 Peter Hutterer <peter.hutterer@redhat.com> - 1.7.5-9
- ABI rebuild

* Fri Feb 10 2012 Peter Hutterer <peter.hutterer@redhat.com> - 1.7.5-8
- ABI rebuild

* Tue Jan 24 2012 Peter Hutterer <peter.hutterer@redhat.com> - 1.7.5-7
- ABI rebuild

* Wed Jan 04 2012 Peter Hutterer <peter.hutterer@redhat.com> - 1.7.5-6
- Rebuild for server 1.12

* Fri Dec 16 2011 Adam Jackson <ajax@redhat.com> - 1.7.5-5
- Drop xinf file

* Wed Nov 16 2011 Adam Jackson <ajax@redhat.com> 1.7.5-4
- ABI rebuild
- smi-1.7.5-vga.patch: Adapt to videoabi 12

* Thu Aug 18 2011 Adam Jackson <ajax@redhat.com> - 1.7.5-2
- Rebuild for xserver 1.11 ABI

* Tue Jun 21 2011 Adam Jackson <ajax@redhat.com> 1.7.5-1
- siliconmotion 1.7.5

* Wed May 11 2011 Peter Hutterer <peter.hutterer@redhat.com> - 1.7.3-9.20100122
- Rebuild for server 1.11

* Mon Feb 28 2011 Peter Hutterer <peter.hutterer@redhat.com> - 1.7.3-8.20100122
- Rebuild for server 1.10

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.3-7.20100122
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 02 2010 Adam Jackson <ajax@redhat.com> 1.7.3-6.20100122
- smi-1.7.3-pixmapprivate.patch: Update for new ABI.

* Wed Oct 27 2010 Adam Jackson <ajax@redhat.com> 1.7.3-5.20100122
- Add ABI requires magic (#542742)

* Mon Jul 05 2010 Peter Hutterer <peter.hutterer@redhat.com> - 1.7.3-4.20100122
- rebuild for X Server 1.9

* Fri Jan 22 2010 Peter Hutterer <peter.hutterer@redhat.com> 1.7.3-3.20100122
- Today's git snapshot

* Thu Jan 21 2010 Peter Hutterer <peter.hutterer@redhat.com> - 1.7.3-2
- Rebuild for server 1.8

* Wed Aug 05 2009 Dave Airlie <airlied@redhat.com> 1.7.3-1
- smi 1.7.3

* Tue Aug 04 2009 Adam Jackson <ajax@redhat.com> 1.7.2-3
- smi-1.7.2-dpms.patch: Fix for new DPMS headers.

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Adam Jackson <ajax@redhat.com> - 1.7.2-1.1
- ABI bump

* Thu Jul 02 2009 Adam Jackson <ajax@redhat.com> 1.7.2-1
- siliconmotion 1.7.2

* Thu Feb 26 2009 Adam Jackson <ajax@redhat.com> 1.7.0-1
- siliconmotion 1.7.0

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 20 2008 Dave Airlie <airlied@redhat.com> 1.6.0-1
- Update to latest upstream

* Mon Mar 10 2008 Dave Airlie <airlied@redhat.com> 1.5.1-5
- pciaccess conversion

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.5.1-4
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 Adam Jackson <ajax@redhat.com> - 1.5.1-3
- Rebuild for PPC toolchain bug

* Mon Jun 18 2007 Adam Jackson <ajax@redhat.com> 1.5.1-2
- Update Requires and BuildRequires.  Add Requires: hwdata.

* Mon Mar 19 2007 Adam Jackson <ajax@redhat.com> 1.5.1-1
- Update to 1.5.1

* Fri Feb 16 2007 Adam Jackson <ajax@redhat.com> 1.4.1-3
- ExclusiveArch -> ExcludeArch

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - sh: line 0: fg: no job control
- rebuild

* Tue May 23 2006 Adam Jackson <ajackson@redhat.com> 1.4.1-2
- Rebuild for 7.1 ABI fix.

* Sun Apr  9 2006 Adam Jackson <ajackson@redhat.com> 1.4.1-1
- Update to 1.4.1 from 7.1RC1.

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.3.1.5-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Jan 18 2006 Mike A. Harris <mharris@redhat.com> 1.3.1.5-1
- Updated xorg-x11-drv-siliconmotion to version 1.3.1.5 from X11R7.0

* Tue Dec 20 2005 Mike A. Harris <mharris@redhat.com> 1.3.1.4-1
- Updated xorg-x11-drv-siliconmotion to version 1.3.1.4 from X11R7 RC4
- Removed 'x' suffix from manpage dirs to match RC4 upstream.

* Wed Nov 16 2005 Mike A. Harris <mharris@redhat.com> 1.3.1.2-1
- Updated xorg-x11-drv-siliconmotion to version 1.3.1.2 from X11R7 RC2

* Fri Nov 4 2005 Mike A. Harris <mharris@redhat.com> 1.3.1.1-1
- Updated xorg-x11-drv-siliconmotion to version 1.3.1.1 from X11R7 RC1
- Fix *.la file removal.

* Tue Oct 4 2005 Mike A. Harris <mharris@redhat.com> 1.3.1-1
- Update BuildRoot to use Fedora Packaging Guidelines.
- Deglob file manifest.
- Limit "ExclusiveArch" to x86, x86_64

* Fri Sep 2 2005 Mike A. Harris <mharris@redhat.com> 1.3.1-0
- Initial spec file for siliconmotion video driver generated automatically
  by my xorg-driverspecgen script.
