%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

%{!?_systemd_unitdir: %global _systemd_unitdir %(pkg-config systemd --variable=systemdsystemunitdir)}

%define debug_package %{nil}

Name:                wicd
Version:             1.7.2.4
Release:             5%{?dist}
Summary:             Wireless and wired network connection manager

Group:               System Environment/Base
License:             GPLv2+
URL:                 http://wicd.sourceforge.net/
Source0:             http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:             org.wicd.daemon.service

Patch0:              wicd-1.7.0-remove-WHEREAREMYFILES.patch
Patch1:              wicd-1.7.1-dbus-failure.patch
Patch2:              wicd-1.7.0-dbus-policy.patch
Patch3:              wicd-1.7.1-DaemonClosing.patch
Patch4:              wicd-1.7.2.4-unicode.patch

BuildRoot:           %{_tmppath}/%{name}-%{version}-%{release}-root-%(id -u -n)
BuildRequires:       babel
BuildRequires:       python2-devel
BuildRequires:       desktop-file-utils
BuildRequires:       pkgconfig
BuildRequires:       systemd-units

Requires:            pm-utils >= 1.2.4
Requires:            %{name}-common = %{version}-%{release}

%description
Wicd is designed to give the user as much control over behavior of network
connections as possible.  Every network, both wired and wireless, has its
own profile with its own configuration options and connection behavior.
Wicd will try to automatically connect only to networks the user specifies
it should try, with a preference first to a wired network, then to wireless.

This package provides the architecture-dependent components of wicd.

%package common
Summary:             Wicd common files
Group:               System Environment/Base
BuildArch:           noarch
Requires:            dbus
Requires:            dbus-python
Requires:            dhclient
Requires:            ethtool
Requires:            iproute
Requires:            logrotate
Requires:            net-tools
Requires:            wireless-tools
Requires:            wpa_supplicant
Requires:            pygobject2
Requires(post):      systemd-units
Requires(preun):     systemd-units
Requires(postun):    systemd-units

%description common
This package provides the main wicd daemon and the wicd-cli front-end.

%package curses
Summary:             Curses client for wicd
Group:               Applications/System
BuildArch:           noarch
Requires:            %{name}-common = %{version}-%{release}
Requires:            python-urwid >= 0.9.8.3
Requires:            %{name}-gtk = %{version}-%{release}

%description curses
Client program for wicd that uses a curses interface.

%package gtk
Summary:             GTK+ client for wicd
Group:               Applications/Internet
BuildArch:           noarch
Requires:            %{name}-common = %{version}-%{release}
Requires:            notify-python
Requires:            pygtk2-libglade >= 2.10

%description gtk
Client program for wicd that uses a GTK+ interface.

%prep
%setup -q

# Remove the WHEREAREMYFILES and resetting of ~/.wicd/WHEREAREMYFILES
# This is pointless.  The documentation can just provide WHEREAREMYFILES,
# which we do in this package.
%patch0 -p1

# Handle D-Bus connection failures a little better
%patch1 -p1

# Allow users at the console to control wicd
%patch2 -p1

# Work around bug in DaemonClosing() calls
%patch3 -p1

# Unicode string handling problems
%patch4 -p1

%build
rm -f po/ast.po
%{__python} setup.py configure \
    --distro redhat \
    --lib %{_libdir} \
    --share %{_datadir}/wicd \
    --etc %{_sysconfdir}/wicd \
    --bin %{_bindir} \
    --pmutils %{_libdir}/pm-utils/sleep.d \
    --log %{_localstatedir}/log \
    --systemd %{_systemd_unitdir} \
    --no-install-init
%{__python} setup.py build
%{__python} setup.py compile_translations

%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --no-compile --root %{buildroot}
sed -i -e '/^#!\//, 1d'  %{buildroot}%{_datadir}/wicd/backends/be-external.py
sed -i -e '/^#!\//, 1d'  %{buildroot}%{_datadir}/wicd/backends/be-ioctl.py
sed -i -e '/^#!\//, 1d'  %{buildroot}%{_datadir}/wicd/cli/wicd-cli.py
sed -i -e '/^#!\//, 1d'  %{buildroot}%{_datadir}/wicd/curses/curses_misc.py
sed -i -e '/^#!\//, 1d'  %{buildroot}%{_datadir}/wicd/curses/netentry_curses.py
sed -i -e '/^#!\//, 1d'  %{buildroot}%{_datadir}/wicd/curses/prefs_curses.py
sed -i -e '/^#!\//, 1d'  %{buildroot}%{_datadir}/wicd/daemon/wicd-daemon.py
sed -i -e '/^#!\//, 1d'  %{buildroot}%{_datadir}/wicd/gtk/gui.py
sed -i -e '/^#!\//, 1d'  %{buildroot}%{_datadir}/wicd/gtk/prefs.py
sed -i -e '/^#!\//, 1d'  %{buildroot}%{_datadir}/wicd/gtk/wicd-client.py

rm -f %{buildroot}%{_localstatedir}/lib/wicd/WHEREAREMYFILES
rm -rf %{buildroot}%{_datadir}/doc
find %{buildroot} -type f -name ".empty_on_purpose" | xargs rm

for lib in %{buildroot}%{python_sitelib}/wicd/*.py ; do
    sed '/\/usr\/bin\/env/d' $lib > $lib.new &&
    touch -r $lib $lib.new &&
    mv $lib.new $lib
done

mkdir -p %{buildroot}%{_datadir}/dbus-1/system-services
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/dbus-1/system-services/org.wicd.daemon.service

mv %{buildroot}%{_sysconfdir}/logrotate.d/%{name}.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

desktop-file-install \
    --remove-category="Application" \
    --delete-original \
    --dir=%{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/wicd.desktop

desktop-file-install \
    --dir=%{buildroot}%{_sysconfdir}/xdg/autostart \
    %{buildroot}%{_sysconfdir}/xdg/autostart/wicd-tray.desktop

%find_lang %{name}

%clean
rm -rf %{buildroot}

%post common
%systemd_post wicd.service

%preun common
%systemd_preun wicd.service

%postun common
%systemd_post_with_restart wicd.service

%post gtk
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun gtk
if [ $1 -eq 0 ]; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans gtk
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%defattr(-,root,root,-)
%{_libdir}/pm-utils/sleep.d/55wicd

%files common -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS CHANGES LICENSE NEWS README other/WHEREAREMYFILES
%dir %{python_sitelib}/wicd
%dir %{_sysconfdir}/wicd
%dir %{_sysconfdir}/wicd/encryption
%dir %{_sysconfdir}/wicd/encryption/templates
%dir %{_sysconfdir}/wicd/scripts
%dir %{_sysconfdir}/wicd/scripts/postconnect
%dir %{_sysconfdir}/wicd/scripts/postdisconnect
%dir %{_sysconfdir}/wicd/scripts/preconnect
%dir %{_sysconfdir}/wicd/scripts/predisconnect
%{_sysconfdir}/acpi/resume.d/80-wicd-connect.sh
%{_sysconfdir}/acpi/suspend.d/50-wicd-suspend.sh
%config(noreplace) %{_sysconfdir}/logrotate.d/wicd
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/wicd.conf
%config(noreplace) %{_sysconfdir}/wicd/dhclient.conf.template.default
%config(noreplace) %{_sysconfdir}/wicd/encryption/templates/active
%config(noreplace) %{_sysconfdir}/wicd/encryption/templates/active_wired
%config(noreplace) %{_sysconfdir}/wicd/encryption/templates/eap
%config(noreplace) %{_sysconfdir}/wicd/encryption/templates/eap-tls
%config(noreplace) %{_sysconfdir}/wicd/encryption/templates/leap
%config(noreplace) %{_sysconfdir}/wicd/encryption/templates/peap
%config(noreplace) %{_sysconfdir}/wicd/encryption/templates/peap-tkip
%config(noreplace) %{_sysconfdir}/wicd/encryption/templates/psu
%config(noreplace) %{_sysconfdir}/wicd/encryption/templates/ttls
%config(noreplace) %{_sysconfdir}/wicd/encryption/templates/wep-hex
%config(noreplace) %{_sysconfdir}/wicd/encryption/templates/wep-passphrase
%config(noreplace) %{_sysconfdir}/wicd/encryption/templates/wep-shared
%config(noreplace) %{_sysconfdir}/wicd/encryption/templates/wired_8021x
%config(noreplace) %{_sysconfdir}/wicd/encryption/templates/wpa
%config(noreplace) %{_sysconfdir}/wicd/encryption/templates/wpa-psk
%config(noreplace) %{_sysconfdir}/wicd/encryption/templates/wpa-peap
%config(noreplace) %{_sysconfdir}/wicd/encryption/templates/wpa2-leap
%config(noreplace) %{_sysconfdir}/wicd/encryption/templates/wpa2-peap
%{_systemd_unitdir}/wicd.service
%{python_sitelib}/wicd/*
%{python_sitelib}/wicd-%{version}*.egg-info
%{_bindir}/wicd-cli
%{_bindir}/wicd-client
%{_sbindir}/wicd
%{_datadir}/applications/wicd.desktop
%{_datadir}/dbus-1/system-services/org.wicd.daemon.service
%{_datadir}/man/man1/wicd-client.1*
%{_datadir}/man/man5/wicd-manager-settings.conf.5*
%{_datadir}/man/man5/wicd-wired-settings.conf.5*
%{_datadir}/man/man5/wicd-wireless-settings.conf.5*
%{_datadir}/man/man8/wicd-cli.8*
%{_datadir}/man/man8/wicd.8*
%lang(nl) %{_datadir}/man/nl/man1/wicd-client.1*
%lang(nl) %{_datadir}/man/nl/man5/wicd-manager-settings.conf.5*
%lang(nl) %{_datadir}/man/nl/man5/wicd-wired-settings.conf.5*
%lang(nl) %{_datadir}/man/nl/man5/wicd-wireless-settings.conf.5*
%lang(nl) %{_datadir}/man/nl/man8/wicd.8*
%dir %{_datadir}/wicd
%dir %{_datadir}/wicd/backends
%dir %{_datadir}/wicd/cli
%dir %{_datadir}/wicd/daemon
%{_datadir}/wicd/backends/*
%{_datadir}/wicd/cli/*
%{_datadir}/wicd/daemon/*
%dir %{_localstatedir}/lib/wicd
%dir %{_localstatedir}/lib/wicd/configurations

%files curses
%defattr(-,root,root,-)
%dir %{_datadir}/wicd/curses
%{_datadir}/wicd/curses/*
%{_bindir}/wicd-curses
%{_datadir}/man/man8/wicd-curses.8*
%lang(nl) %{_datadir}/man/nl/man8/wicd-curses.8*

%files gtk
%defattr(-,root,root,-)
%dir %{_datadir}/wicd/gtk
%dir %{_datadir}/pixmaps/wicd
%{_sysconfdir}/xdg/autostart/wicd-tray.desktop
%{_datadir}/autostart/wicd-tray.desktop
%{_datadir}/wicd/gtk/*
%{_datadir}/pixmaps/wicd/*
%{_datadir}/pixmaps/wicd-gtk.xpm
%{_bindir}/wicd-gtk
%{_datadir}/icons/hicolor/*/apps/wicd-gtk.png
%{_datadir}/icons/hicolor/scalable/apps/wicd-gtk.svg

%changelog
* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 23 2012 David Cantrell <dcantrell@redhat.com> - 1.7.2.4-4
- Fix some Unicode string handling and display problems (#845749)

* Tue Oct 23 2012 David Cantrell <dcantrell@redhat.com> - 1.7.2.4-3
- Use new systemd macros in trigger scripts (#850367)

* Thu Aug 02 2012 David Cantrell <dcantrell@redhat.com> - 1.7.2.4-2
- Updated duplicate logrotate file fix (#820139)

* Thu Aug 02 2012 David Cantrell <dcantrell@redhat.com> - 1.7.2.4-1
- Upgrade to wicd-1.7.2.4
- Remove duplicate logrotate file (#820139)
- The curses package requires some code from the gtk module, so add explicit
  dependency (#831309)

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 13 2012 David Cantrell <dcantrell@redhat.com> - 1.7.2.1-1
- Upgrade to wicd-1.7.2.1 to fix CVE-2012-2095 (#811763)

* Mon Mar 26 2012 David Cantrell <dcantrell@redhat.com> - 1.7.1-5
- Remove our wicd.service file, this is provided by upstream now

* Mon Mar 26 2012 David Cantrell <dcantrell@redhat.com> - 1.7.1-4
- Make sure systemd unit files go to /usr/lib/systemd
- Stop mangling logfile.py so bytecompiling will actually work
- 91wicd -> 55wicd
- Pick up new encryption template files in the %%files list

* Thu Mar 22 2012 David Cantrell <dcantrell@redhat.com> - 1.7.1-3
- BR babel
- Remove po/ast.po because babel doesn't understand it

* Thu Mar 22 2012 David Cantrell <dcantrell@redhat.com> - 1.7.1-2
- Ensure wpath.etc is set to /etc/wicd, not /etc/dhcp (#754412)
- Initialize child_pid to None in wicd-daemon.py (#798692)
- Make wicd-gtk subpackage require notify-python (#748258)
- Work around no-op problem in DaemonClosing calls (#740317)

* Fri Feb 10 2012 David Cantrell <dcantrell@redhat.com> - 1.7.1-1
- Upgrade to wicd-1.7.1 final release (#789380)
- Have wicd-common require pygobject2 (#754416)
- Remove patches that have been incorporated upstream

* Fri Jan 27 2012 David Cantrell <dcantrell@redhat.com> - 1.7.1b2-0.3
- Fix CVE-2012-0813 (#785147)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-0.2.b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Aug 19 2011 David Cantrell <dcantrell@redhat.com> - 1.7.1b2-0.1
- Upgrade to wicd-1.7.1b2

* Fri Aug 19 2011 David Cantrell <dcantrell@redhat.com> - 1.7.0-9
- Initialize appGui._wired_showing in __init__ (#723553)
- Make sure check and message in wicd-cli are a lambda (#712435)
- Correct systemd unit file for wicd, add D-Bus service file (#699116)
- Move docs to the wicd-common subpackage
- Correct /etc/dbus-1/system.d/wicd.conf (#699116)

* Mon May 09 2011 Bill Nottingham <notting@redhat.com> - 1.7.0-8
- fix systemd scriptlets for upgrade

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 15 2011 David Cantrell <dcantrell@redhat.com> - 1.7.0-6
- Correct typo with _systemd_unitdir macro usage in spec file

* Sat Jan 15 2011 David Cantrell <dcantrell@redhat.com> - 1.7.0-5
- Replace existing init script with systemd unit file (#661226)

* Fri Oct 22 2010 David Cantrell <dcantrell@redhat.com> - 1.7.0-4
- Use cPickle instead of deepcopy in configmanager.py (#645251)

* Wed Aug 25 2010 David Cantrell <dcantrell@redhat.com> - 1.7.0-3
- Remove hard dependency on the base package by wicd-common.  The
  base package is arch-specific and contains optional components
  for wicd.  If it is present, wicd will make use of it, but it is
  not required for normal functionality.

* Fri Jul 30 2010 Thomas Spura <tomspur@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon Jun 21 2010 David Cantrell <dcantrell@redhat.com> - 1.7.0-1
- Initial package
