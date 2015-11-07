%if 0%{!?_with_xfce:1} && 0%{!?_without_xfce:1}
%if 0%{?rhel}
%global _with_xfce 0
%else
%global _with_xfce 1
%endif
%endif

Name:		im-chooser
Version:	1.6.4
Release:	5%{?dist}
License:	GPLv2+ and LGPLv2+
URL:		http://fedorahosted.org/im-chooser/
%{?_with_gtk2:BuildRequires:	gtk2-devel}
%{!?_with_gtk2:BuildRequires:	gtk3-devel}
BuildRequires:	libSM-devel imsettings-devel >= 1.3.0
%if 0%{?_with_xfce}
BuildRequires:	libxfce4util-devel
%endif
BuildRequires:	desktop-file-utils intltool gettext

Source0:	http://fedorahosted.org/releases/i/m/%{name}/%{name}-%{version}.tar.bz2

Summary:	Desktop Input Method configuration tool
Group:		Applications/System
Obsoletes:	im-chooser-gnome3 < 1.4.2-2
Provides:	im-chooser-gnome3 = %{version}-%{release}
Requires:	%{name}-common = %{version}-%{release}

%description
im-chooser is a GUI configuration tool to choose the Input Method
to be used or disable Input Method usage on the desktop.

%package	common
Summary:	Common files for im-chooser subpackages
Group:		Applications/System
Requires:	imsettings >= 1.3.0
Obsoletes:	im-chooser < 1.5.0.1
## https://fedorahosted.org/fpc/ticket/174
Provides:	bundled(egglib)

%description	common
im-chooser is a GUI configuration tool to choose the Input Method
to be used or disable Input Method usage on the desktop.

This package contains the common libraries/files to be used in
im-chooser subpackages.

%if 0%{?_with_xfce}
%package	xfce
Summary:	XFCE settings panel for im-chooser
Group:		Applications/System
Requires:	%{name}-common = %{version}-%{release}
Obsoletes:	im-chooser < 1.5.0.1

%description	xfce
im-chooser is a GUI configuration tool to choose the Input Method
to be used or disable Input Method usage on the desktop.

This package contains the XFCE settings panel for im-chooser.
%endif


%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="/usr/bin/install -p"

desktop-file-install \
%if 0%{?fedora} && 0%{?fedora} < 19
	--vendor=fedora				\
%endif
	--add-category=X-GNOME-PersonalSettings			\
	--delete-original					\
	--dir=$RPM_BUILD_ROOT%{_datadir}/applications		\
	$RPM_BUILD_ROOT%{_datadir}/applications/im-chooser.desktop
%if 0%{?_with_xfce}
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/xfce4-im-chooser.desktop
%endif
#%%{!?_with_gtk2:desktop-file-validate $RPM_BUILD_ROOT%%{_datadir}/applications/im-chooser-panel.desktop}

rm -rf $RPM_BUILD_ROOT%{_libdir}/libimchooseui.{so,la,a}
#%%{!?_with_gtk2:rm -rf $RPM_BUILD_ROOT%%{_libdir}/control-center-1/panels/libim-chooser.{a,la}}

# disable panel so far
rm -rf $RPM_BUILD_ROOT%{_libdir}/control-center-1/panels/libim-chooser.so
rm -rf $RPM_BUILD_ROOT%{_datadir}/applications/im-chooser-panel.desktop

%find_lang %{name}


%post	common
/sbin/ldconfig
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun	common
/sbin/ldconfig
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans	common
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files
%{_bindir}/im-chooser
%if 0%{?fedora} && 0%{?fedora} < 19
%{_datadir}/applications/fedora-im-chooser.desktop
%else
%{_datadir}/applications/im-chooser.desktop
%endif
%{_mandir}/man1/im-chooser.1*

%files	common -f %{name}.lang
%doc AUTHORS COPYING ChangeLog README
%{_libdir}/libimchooseui.so.*
%{_datadir}/icons/hicolor/*/apps/im-chooser.png
%dir %{_datadir}/imchooseui
%{_datadir}/imchooseui/imchoose.ui

%if 0%{?_with_xfce}
%files	xfce
%{_bindir}/xfce4-im-chooser
%{_datadir}/applications/xfce4-im-chooser.desktop
%endif

%changelog
* Fri Oct 30 2015 Liu Di <liudidi@gmail.com> - 1.6.4-5
- 为 Magic 3.0 重建

* Sat Oct 24 2015 Liu Di <liudidi@gmail.com> - 1.6.4-4
- 为 Magic 3.0 重建

* Fri Oct 23 2015 Liu Di <liudidi@gmail.com> - 1.6.4-3
- 为 Magic 3.0 重建

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 11 2013 Akira TAGOH <tagoh@redhat.com> - 1.6.4-1
- New upstream release.
- Remove BR: docbook2X

* Tue May 28 2013 Akira TAGOH <tagoh@redhat.com> - 1.6.3-1
- New upstream release.
  - Add a link to the log file in the error dialog (#950488)
  - Fix a crash issue (#859624)

* Sat Feb 23 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 1.6.2-3
- Remove --vendora from desktop-file-utils in F19+ https://fedorahosted.org/fesco/ticket/1077

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 23 2012 Akira TAGOH <tagoh@redhat.com> - 1.6.2-1
- New upstream release.
- the spec file cleanup.
- Correct License field
- Add Provides: bundled(egglib) to im-chooser-common since
  it actually contains things in libimchooseui.so.0

* Fri Nov  2 2012 Akira TAGOH <tagoh@redhat.com> - 1.6.1-1
- New upstream release.
  Translation updates. (#863375)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jul 14 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.6.0-2
- Add ldconfig calls to -common scriptlets.

* Thu Jul 12 2012 Akira TAGOH <tagoh@redhat.com> - 1.6.0-1
- New upstream release.

* Sun Jun 24 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.5.2.2-3
- Own the %%{_datadir}/imchooseui dir.

* Wed May 23 2012 Akira TAGOH <tagoh@redhat.com> - 1.5.2.2-2
- Conditionally build XFCE support for RHEL.

* Wed Apr 18 2012 Akira TAGOH <tagoh@redhat.com> - 1.5.2.2-1
- New upstream release.
  - Update translations (#801232)

* Fri Apr 06 2012 Kevin Fenzi <kevin@scrye.com> - 1.5.2.1-2
- Rebuild for Xfce 4.10

* Mon Mar 19 2012 Akira TAGOH <tagoh@redhat.com> - 1.5.2.1-1
- New upstream release.

* Fri Mar  2 2012 Akira TAGOH <tagoh@redhat.com> - 1.5.2-3
- Update po files.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 16 2011 Akira TAGOH <tagoh@redhat.com> - 1.5.2-1
- New upstream release.
  - Fix the logout button behaved shutting down on KDE. (#741497)

* Fri Sep  9 2011 Akira TAGOH <tagoh@redhat.com> - 1.5.1-1
- New upstream release.

* Tue Aug  2 2011 Akira TAGOH <tagoh@redhat.com> - 1.5.0.1-2
- Add some Obsoletes for upgrading path.

* Tue Aug  2 2011 Akira TAGOH <tagoh@redhat.com> - 1.5.0.1-1
- New upstream release.
- Add im-chooser-xfce subpackage.

* Tue May 10 2011 Akira TAGOH <tagoh@redhat.com> - 1.4.2-2
- Disable capplet. (#693809)

* Wed Mar 30 2011 Akira TAGOH <tagoh@redhat.com> - 1.4.2-1
- New upstream release.

* Thu Feb 23 2011 Akira TAGOH <tagoh@redhat.com> - 1.4.1-7
- Rebuild again.

* Mon Feb 21 2011 Akira TAGOH <tagoh@redhat.com> - 1.4.1-6
- Rebuild against latest imsettings.

* Fri Feb 11 2011 Matthias Clasen <mclasen@redhat.com> 1.4.1-5
- Rebuild against newer gtk

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  2 2011 Matthias Clasen <mclasen@redhat.com> - 1.4.1-3
- Rebuild against newer gtk

* Sun Jan  9 2011 Matthias Clasen <mclasen@redhat.com> - 1.4.1-2
- Rebuild against newer gtk3

* Thu Jan  6 2011 Akira TAGOH <tagoh@redhat.com> - 1.4.1-1
- New upstream release.

* Fri Dec  3 2010 Matthias Clasen <mclasen@redhat.com> - 1.4.0-2
- Rebuild against newer gtk3

* Thu Nov 25 2010 Akira TAGOH <tagoh@redhat.com> - 1.4.0-1
- New upstream release.
  - Improve the window title (#607502)
  - Move none state from checkbox to selector (#628420)
  - GNOME3 support

* Wed Sep  8 2010 Akira TAGOH <tagoh@redhat.com> - 1.3.2-1
- New upstream release.
  - Improve UI (#607513)

* Mon Jun 21 2010 Akira TAGOH <tagoh@redhat.com> - 1.3.1-1
- New upstream release.
  - Fallback to the themed icon if no icons are installed
    on the specified path. (#604482)

* Wed May 12 2010 Akira TAGOH <tagoh@redhat.com> - 1.3.0-1
- New upstream release.
  - GTK+ stock icon support. (#528850)

* Tue May  4 2010 Jens Petersen <petersen@redhat.com> - 1.2.7-2
- add new gnome-icon-theme style icons by Lapo Calamandrei and Jakub Steiner
  (mizmo, #587712)
- add scriptlets for icon cache

* Mon Sep 14 2009 Akira TAGOH <tagoh@redhat.com> - 1.2.7-1
- New upstream release.
  - translation updates only.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon May 25 2009 Akira TAGOH <tagoh@redhat.com> - 1.2.6-3
- Disable the status icon check box.

* Thu Feb 26 2009 Akira TAGOH <tagoh@redhat.com> - 1.2.6-2
- Fix a typo in xfce4-im-chooser.desktop. (#487275)

* Mon Feb 23 2009 Akira TAGOH <tagoh@redhat.com> - 1.2.6-1
- New upstream release.

* Wed Oct 22 2008 Akira TAGOH <tagoh@redhat.com> - 1.2.5-1
- New upstream release.

* Tue Oct 14 2008 Akira TAGOH <tagoh@redhat.com> - 1.2.4-1
- New upstream release.

* Wed Sep 17 2008 Akira TAGOH <tagoh@redhat.com> - 1.2.3-1
- New upstream release.

* Fri Aug 29 2008 Akira TAGOH <tagoh@redhat.com> - 1.2.2-1
- New upstream release.

* Tue Jul 29 2008 Akira TAGOH <tagoh@redhat.com> - 1.2.1-1
- New upstream release.
  - Display IM icon in the list. (#454371)

* Tue Jul  8 2008 Akira TAGOH <tagoh@redhat.com> - 1.2.0-1
- New upstream release.

* Fri Jun 27 2008 Akira TAGOH <tagoh@redhat.com> - 1.1.1-1
- New upstream release.
  - Fix a segfault when no Input Method installed. (#452997)

* Thu Jun 12 2008 Akira TAGOH <tagoh@redhat.com> - 1.1.0-1
- New upstream release.

* Mon May 26 2008 Akira TAGOH <tagoh@redhat.com> - 0.99.6-5
- Fix a typo in the package group of imsettings-xfce. (#448037)

* Wed May 14 2008 Akira TAGOH <tagoh@redhat.com> - 0.99.6-4
- im-chooser-fix-window-border.patch: Display the progress window with
  the certain window border. (#444818)
- imsettings-ignore-error-on-check-running.patch: Fix a crash issue when
  the pidfile doesn't exist. (#445129)

* Tue Apr 29 2008 Akira TAGOH <tagoh@redhat.com> - 0.99.6-3
- im-chooser-0.99.6-sanity-check-on-dbus-conn.patch: Do not abort even if
  getting the bus is failed. (#444494)
- im-chooser-0.99.6-validate-pid.patch: Validate the pid. (#443765)

* Wed Apr 23 2008 Akira TAGOH <tagoh@redhat.com> - 0.99.6-2
- im-chooser-0.99.6-check-if-im-is-running.patch: Do not turn on the check box
  if IM isn't really running. (#443765)
- im-chooser-0.99.6-correct-build-order.patch: Apply to correct the build order.

* Tue Apr  8 2008 Akira TAGOH <tagoh@redhat.com> - 0.99.6-1
- New upstream release.
  - translation updates.
- Remove unnecessary patches:
  - im-chooser-0.99.5-no-xinputrc-update.patch
  - im-chooser-0.99.5-no-crash-on-no-im.patch

* Mon Apr  7 2008 Akira TAGOH <tagoh@redhat.com> - 0.99.5-3
- im-chooser-0.99.5-no-crash-on-no-im.patch: Fix a crash when no IM
  available. (#440519)
- Invoke ReloadConfig to apply changes on DBus services in %%post and %%postun.

* Fri Mar 28 2008 Akira TAGOH <tagoh@redhat.com> - 0.99.5-2
- im-chooser-0.99.5-no-xinputrc-update.patch: real fix for #437732
- ensure invoking xinput.sh after the session bus is established. (#436284)

* Wed Mar 19 2008 Akira TAGOH <tagoh@redhat.com> - 0.99.5-1
- New upstream release.
  - Fix an issue always create .xinputrc at the startup time. (#437732)
  - Add Xfce support.

* Tue Mar 11 2008 Akira TAGOH <tagoh@redhat.com> - 0.99.4-1
- New upstream release.
  - Compress im-chooser.png icon. (#330441)

* Thu Feb 21 2008 Akira TAGOH <tagoh@redhat.com>
- Run ldconfig on scriptlet of imsettings-libs.

* Wed Feb 20 2008 Akira TAGOH <tagoh@redhat.com> - 0.99.3-1
- New upstream release.
  - Fix taking too much CPU power. (#433575)
  - Fix not parsing the multiple command line options in xinput
    script. (#433578)

* Tue Feb 19 2008 Akira TAGOH <tagoh@redhat.com> - 0.99.2-1
- New upstream release.
  - Fix not working the user own .xinputrc properly.

* Fri Feb  8 2008 Akira TAGOH <tagoh@redhat.com> - 0.99.1-1
- New upstream release.
  - Fix some memory leaks and clean up the code. (#431167)
  - Fix the handling of the user own .xinputrc. (#431291)

* Fri Feb  1 2008 Akira TAGOH <tagoh@redhat.com> - 0.99-1
- New upstream release.
  - IMSettings is now enabled. you don't need to restart your desktop after
    changing IM for GTK+ applications. but still need to do for others so far.

* Thu Dec 27 2007 Akira TAGOH <tagoh@redhat.com> - 0.5.5-1
- New upstream release.
  - Rename sr@Latn to sr@latin. (#426540)

* Fri Nov 16 2007 Akira TAGOH <tagoh@redhat.com> - 0.5.4-1
- New upstream release.
  - Improve .desktop file for GNOME HIG compliant (#330431)
  - Improve English label on GUI (#302491)
- Remove the dead link. (#330391)
- Improve a package description. (#330421)

* Mon Oct 15 2007 Akira TAGOH <tagoh@redhat.com>
- Remove the obsolete Norwegian (no) translation. (#332131)

* Thu Oct 11 2007 Akira TAGOH <tagoh@redhat.com> - 0.5.3-1
- New upstream release.
  - Fix an issue that looks like IM can't be disabled on im-chooser. (#324231)

* Tue Oct  2 2007 Akira TAGOH <tagoh@redhat.com> - 0.5.2-3
- Revert the previous change.

* Fri Sep 21 2007 Akira TAGOH <tagoh@redhat.com> - 0.5.2-2
- Bring up IM by default again, except the session is on Live CD. (#250226)

* Tue Sep 18 2007 Akira TAGOH <tagoh@redhat.com> - 0.5.2-1
- New upstream release.
  - Fix to allow users disabling IM.

* Fri Sep 14 2007 Akira TAGOH <tagoh@redhat.com> - 0.5.1-2
- Add README into the package.

* Mon Sep 10 2007 Akira TAGOH <tagoh@redhat.com> - 0.5.1-1
- New upstream release.

* Thu Sep  6 2007 Akira TAGOH <tagoh@redhat.com> - 0.5.0-1
- New upstream release.

* Wed Aug  8 2007 Akira TAGOH <tagoh@redhat.com>
- Update License tag.

* Mon Aug  6 2007 Akira TAGOH <tagoh@redhat.com> - 0.4.1-3
- Own /etc/X11/xinit/xinput.d (#250960)

* Mon Jul 30 2007 Akira TAGOH <tagoh@redhat.com> - 0.4.1-2
- Update Require for xorg-x11-xinit

* Wed Jul 25 2007 Akira TAGOH <tagoh@redhat.com> - 0.4.1-1
- New upstream release.
  - xinput.sh has been moved from xorg-x11-xinit.

* Tue Jan 30 2007 Akira TAGOH <tagoh@redhat.com> - 0.3.4-1
- Translations update release.

* Wed Jan 24 2007 Matthias Clasen <mclasen@redhat.com> - 0.3.3-3
- Add X-GNOME-PersonalSettings to the desktop file categories (#224159)
- Use desktop-file-install

* Mon Oct  2 2006 Akira TAGOH <tagoh@redhat.com> - 0.3.3-2
- added Assamese, Greek and Marathi translation. (#208258)

* Mon Oct  2 2006 Akira TAGOH <tagoh@redhat.com> - 0.3.3-1
- Translations update release. (#208258, #208512)

* Fri Sep  8 2006 Akira TAGOH <tagoh@redhat.com> - 0.3.2-1
- New upstream release.
  - added an icon. (#199337)
- removed the unnecessary patches:
  - im-chooser-r49.patch
  - im-chooser-r53.patch

* Tue Aug 29 2006 Akira TAGOH <tagoh@redhat.com> - 0.3.1-3
- im-chooser-r53.patch: take care of the suffix to appears current selection.
  (#204433)

* Fri Aug 25 2006 Akira TAGOH <tagoh@redhat.com> - 0.3.1-2
- im-chooser-r49.patch: removed MimeType field from .desktop file. (#203982)

* Tue Aug 15 2006 Akira TAGOH <tagoh@redhat.com> - 0.3.1-1
- New upstream release.

* Mon Jul 24 2006 Akira TAGOH <tagoh@redhat.com> - 0.3.0-2
- New upstream release.
- add libgnomeui-devel to BR.
- im-chooser-suffix-r40.patch: applied to support the recent change
  in the xinput files.

* Thu Jul 20 2006 Akira TAGOH <tagoh@redhat.com> - 0.2.2-2
- rebuilt

* Wed Jul 12 2006 Akira TAGOH <tagoh@redhat.com> - 0.2.2-1
- New upstream release.

* Mon Jul 10 2006 Akira TAGOH <tagoh@redhat.com> - 0.2.1-3
- New upstream release.
- improved the package summary and description.
- added intltool to BuildReq.
- added gettext to BuildReq.

* Fri Jul  7 2006 Akira TAGOH <tagoh@redhat.com> - 0.2.0-1
- New upstream release.
- use dist tag.
- registered xinputrc alternatives for none and xim.
- removed the empty docs.
- add Requires: xorg-x11-xinit >= 1.0.2-5.fc6 for new xinput.sh.

* Wed Jun  7 2006 Akira TAGOH <tagoh@redhat.com> - 0.1.1-1
- Initial package.

