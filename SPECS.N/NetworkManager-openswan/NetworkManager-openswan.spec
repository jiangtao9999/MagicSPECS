#%define nm_version        1:0.9.8

%define realversion 0.9.8.4

Summary:   NetworkManager VPN plug-in for openswan
Name:      NetworkManager-openswan
Version:   0.9.8.4
Release:   2%{?dist}
License:   GPLv2+
Group:     System Environment/Base
URL:       http://ftp.gnome.org/pub/GNOME/sources/NetworkManager-openswan/0.9/
Source0:   http://ftp.gnome.org/pub/GNOME/sources/NetworkManager-openswan/0.9/%{name}-%{realversion}.tar.xz
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Patch1:    0001-NM-openswan-was-missing-support-for-nm-openswan-auth.patch
Patch2:    0002-Fixed-gtk-label-max-width-issue-by-setting-it-to-35.patch
Patch3:    0003-Fixed-Networkmanager-and-related-lib-dependencies.patch
Patch4:    0004-Fixed-gnomekeyring-lib-dependencies.patch
Patch5:    0005-Fixed-dead-code-based-on-coverity-scan.patch
Patch6:    0006-Fix-prcoessing-of-nm-openswan-dialog.ui-file-and-add.patch
Patch7:    0007-openswan-libreswan-does-not-provide-tun0-interface-s.patch
Patch8:    0008-libreswan-related-fixes-as-some-macros-have-been-mod.patch
Patch9:    0009-Fixed-an-issue-where-writing-configuration-on-stdin-.patch
Patch10:   0010-Fixed-more-coverity-scan-issues.patch
Patch11:   0011-Fixed-the-current-code-as-it-does-not-set-the-defaul.patch
Patch12:   0012-Fixed-netmask-issue-when-sending-IP-information-to-t.patch
Patch13:   0013-Fixed-more-libreswan-related-changes.patch
Patch14:   0014-Fixed-an-issue-where-nm-openswan-service-is-searchin.patch
Patch15:   0015-Rewrite-pluto-watch-API-which-watches-the-pluto-proc.patch
Patch16:   0016-Fixed-defaults-values-for-more-parameters-to-help-th.patch
Patch17:   0017-Fixed-initiation-of-pluto-daemon-by-this-plugin-to-r.patch
Patch18:   0018-Fixed-various-debug-messages.patch
Patch19:   0019-Fixed-the-termination-operation-of-pluto-daemon-to-c.patch
Patch20:   0020-Fixed-an-issue-where-proper-network-stack-is-not-loa.patch
Patch21:   nm-openswan-1035786-1040924.patch

BuildRequires: gtk3-devel
BuildRequires: dbus-devel
BuildRequires: NetworkManager-devel
BuildRequires: NetworkManager-glib-devel
BuildRequires: NetworkManager-devel       >= %{nm_version}
BuildRequires: NetworkManager-glib-devel  >= %{nm_version}
%if 0%{?fedora} > 16 || 0%{?rhel} >= 7
BuildRequires: libgnome-keyring-devel
%else
BuildRequires: gnome-keyring-devel
%endif
BuildRequires: intltool gettext

Requires: NetworkManager   >= %{nm_version}
Requires: gnome-keyring
Requires: gtk3
Requires: dbus
Requires: libreswan
Requires: shared-mime-info
#Requires: nm-connection-editor

%global _privatelibs libnm-openswan-properties[.]so.*
%global __provides_exclude ^(%{_privatelibs})$
%global __requires_exclude ^(%{_privatelibs})$

%description
This package contains software for integrating the openswan VPN software
with NetworkManager and the GNOME desktop

%package -n NetworkManager-openswan-gnome
Summary: NetworkManager VPN plugin for openswan - GNOME files
Group:   System Environment/Base

Requires: NetworkManager-openswan = %{version}-%{release}
Requires: nm-connection-editor

%description -n NetworkManager-openswan-gnome
This package contains software for integrating VPN capabilities with
the openswan/libreswan server with NetworkManager (GNOME files).

%prep
%setup -q  -n NetworkManager-openswan-%{realversion}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1

%build
autoreconf
%configure --disable-static --enable-more-warnings=yes
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f %{buildroot}%{_libdir}/NetworkManager/lib*.la
rm -f %{buildroot}%{_libdir}/NetworkManager/lib*.a
mv  %{buildroot}%{_libexecdir}/nm-openswan-service-helper  %{buildroot}%{_libexecdir}/nm-libreswan-service-helper

%find_lang %{name}

%post
update-desktop-database &> /dev/null || :

%postun
update-desktop-database &> /dev/null || :

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-, root, root,-)
%doc AUTHORS ChangeLog COPYING
#%{_libdir}/NetworkManager/lib*.so*
%{_libexecdir}/nm-openswan-auth-dialog
%{_sysconfdir}/dbus-1/system.d/nm-openswan-service.conf
%{_sysconfdir}/NetworkManager/VPN/nm-openswan-service.name
%{_libexecdir}/nm-openswan-service
%{_libexecdir}/nm-libreswan-service-helper
%{_datadir}/applications/nm-openswan-auth-dialog.desktop
#%dir %{_datadir}/gnome-vpn-properties/openswan
#%{_datadir}/gnome-vpn-properties/openswan/nm-openswan-dialog.ui

%files -n NetworkManager-openswan-gnome
%doc AUTHORS ChangeLog COPYING
%{_libdir}/NetworkManager/lib*.so*
%dir %{_datadir}/gnome-vpn-properties/openswan
%{_datadir}/gnome-vpn-properties/openswan/nm-openswan-dialog.ui


%changelog
* Thu Dec 12 2013 Avesh Agarwal <avagarwa@redhat.com> - 0.9.8.4-2
- Fixes 1035786 (and its duplicate 1040924)

* Tue Dec 10 2013 Avesh Agarwal <avagarwa@redhat.com> - 0.9.8.4-1
- New upstream release 0.9.8.4
- Fixed 926225
- Fixed dependency to libreswan.
- Created a new sub package NetworkManager-openswan-gnome
- Various other spec file fixes.
- Additional code changes are as follows:
- Fixed an issue where proper network stack is not loaded unless
  _stackmanager is run before starting pluto daemon service.
- Fixed the termination operation of pluto daemon to comply with
  libreswan changes.
- Fixed various debug messages.
- Fixed initiation of pluto daemon by this plugin to reflect the
  changes in libreaswan.
- Fixed defaults values for more parameters to help the VPN
  connection stay more reliable.
- Rewrote pluto watch API which watches the pluto process for its status.
  Fixed memory leak issues as not all child processes were reaped correctly.
  Also g_spwan_close_pid was not being called after children were reaped.
  Also modified debugs and added more to help with debugging in the future.
- Fixed an issue where nm-openswan service is searching for ipsec binary in
  both /sbin and /usr/sbin leading to same operation twice, as /sbin is just
  symlink to /usr/sbin, so removed /sbin from the search paths.
- Fixed some libreswan related macro changes.
- Fixed netmask issue when sending IP information to the nm openswan
  plugin service.
- Fixed the current code as it does not set the default route field
  NM_VPN_PLUGIN_IP4_CONFIG_NEVER_DEFAULT when sending VPN information
  to nm-openswan plugin. This fix sets the field to TRUE.
- Fixed some issues found by coverity scan.
- Fixed an issue where writing configuration on stdin should not end with
  \n as it gives error. It used to work previously, but not with latest
  NetworkManager versions.
- libreswan related fixes, as some macros have been modified after forking
  to libreswan from openswan.
- openswan/libreswan does not provide tun0 interface, so fixed the code
  where it sends tun0 interface.
- Fix prcoessing of nm-openswan-dialog.ui file and added more error notifications.
- Fixed dead code based on coverity scan.
- Fixed gnomekeyring lib dependencies.
- Fixed Networkmanager and related lib dependencies.
- Fixed gtk label max width issue by setting it to 35.
- NM-openswan was missing support for nm-openswan-auth-dialog.desktop.in.in.
  So added a new nm-openswan-auth-dialog.desktop.in.in, and modified related
  Makefile and configure.ac files.

* Mon Aug 5 2013 Avesh Agarwal <avagarwa@redhat.com> - 0.9.8.0-1
- Rebase to latest upstream version 0.9.8.0
- Fixed several issues with the packaging

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3.995-6.git20120302
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3.995-5.git20120302
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 13 2012 Avesh Agarwal <avagarwa@redhat.com> - 0.9.3.995-4
Resolves: #845599, #865883

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3.995-3.git20120302
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 27 2012 Avesh Agarwal <avagarwa@redhat.com> - 0.9.3.995-2
- Ported changes from rhel to fedora

* Fri Mar  2 2012 Dan Williams <dcbw@redhat.com> - 0.9.3.995-1
- Update to 0.9.3.995 (0.9.4-beta1)
- ui: add support for external UI mode, eg GNOME Shell

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.9.0-2
- Rebuild for new libpng

* Fri Aug 26 2011 Dan Williams <dcbw@redhat.com> - 0.9.0-1
- Update to 0.9.0
- ui: translation fixes

* Thu Jul 21 2011 Dan Williams <dcbw@redhat.com> - 0.8.999-2.git20110721
- Update to git snapshot
- Fixes for secrets handling and saving

* Tue May 03 2011 Dan Williams <dcbw@redhat.com> - 0.8.999-1
- Update to 0.8.999 (0.9-rc2)
- Port to GTK 3.0 and GtkBuilder
- Fix some issues with secrets storage

* Sun Mar 27 2011 Christopher Aillon <caillon@redhat.com> - 0.8.0-9.20100411git
- Rebuild against NetworkManager 0.9

* Wed Feb 16 2011 Avesh Agarwal <avagarwa@redhat.com> - 0.8.0-8.20100411git
- fixes for compile time errors

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-7.20100411git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Sep 7 2010 Avesh Agarwal <avagarwa@redhat.com> - 0.8.0-6.20100411git
- Modified import and export interfaces to import_from_file and export_to_file, respectively,
  due to changes in NMVpnPluginUiInterface struct in NM (bz 631159). 

* Mon Jul 26 2010 Avesh Agarwal <avagarwa@redhat.com> - 0.8.0-5.20100411git
Resolves: #616910
- Support for reading phase1 and phase2 algorithms through GUI

* Tue Jul 13 2010 Avesh Agarwal <avagarwa@redhat.com> - 0.8.0-4.20100411git
- Modified fix for the bz 607352
- Fix to read connection configuration from stdin
- Fix to read Xauth user password from stdin
- Fix to delete the secret file as soon as read by Openswan

* Thu Jul 8 2010 Avesh Agarwal <avagarwa@redhat.com> - 0.8.0-3.20100411git
- Modified the patch so that it does not pass user password to 
  "ipsec whack" command.   

* Thu Jul 8 2010 Avesh Agarwal <avagarwa@redhat.com> - 0.8.0-2.20100411git
- Modified to initiate VPN connections with openswan whack interface
- Fixed the issue of world readable conf and secret files 
- Cleaned conf and secret files after VPN connection is stopped
- Fixed the issue of storing sensitive information like user 
  password in a file (rhbz# 607352)
- Changed PLUTO_SERVERBANNER to PLUTO_PEER_BANNER due
  to the same change in Openswan
- Modifed GUI to remove unused configuration boxes

* Tue Jun 15 2010 Avesh Agarwal <avagarwa@redhat.com> - 0.8.0-1.20100411git
- Initial build
