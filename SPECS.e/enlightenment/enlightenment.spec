Name:           enlightenment
Version:        0.17.5
Release:        2%{?dist}
License:        BSD
Summary:        Enlightenment window manager
Url:            http://enlightenment.org
Source:         http://download.enlightenment.org/releases/%{name}-%{version}.tar.bz2

BuildRequires:  alsa-lib-devel
BuildRequires:  dbus-devel 
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  e_dbus-devel  >= 1.7.9
BuildRequires:  ecore-devel >= 1.7.9
BuildRequires:  edje-devel >= 1.7.9
BuildRequires:  eet-devel >= 1.7.9
BuildRequires:  eeze-devel >= 1.7.9
BuildRequires:  efreet-devel >= 1.7.9
BuildRequires:  eio-devel >= 1.7.9
BuildRequires:  embryo >= 1.7.9
BuildRequires:  emotion-devel >= 1.7.9
BuildRequires:  evas-devel >= 1.7.9
BuildRequires:  libXext-devel 
BuildRequires:  libeina-devel 
BuildRequires:  pam-devel
BuildRequires:  xcb-util-keysyms-devel
Requires:       %{name}-data = %{version}-%{release}
Requires:       emotion >= 1.7.9
Requires:       elementary >= 1.7.9
Requires:       ethumb >= 1.7.9
Requires:       evas-generic-loaders >= 1.7.9
Requires:       magic-menus
Provides:       firstboot(windowmanager) = enlightenment

%description
Enlightenment window manager is a lean, fast, modular and very extensible window 
manager for X11 and Linux. It is classed as a "desktop shell" providing the 
things you need to operate your desktop (or laptop), but is not a whole '
application suite. This covered launching applications, managing their windows 
and doing other system tasks like suspending, reboots, managing files etc. 

%package        data
Summary:        Enlightenment data files
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description data
Contains data files for Enlightenment

%package        devel
Summary:        Enlightenment headers, documentation and test programs

%description devel
Headers,  test programs and documentation for enlightenment

%prep
%setup -q

%build
%configure --disable-static --disable-rpath
make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot}

find %{buildroot} -name '*.la' -delete

%find_lang %{name}
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop

%files
%doc AUTHORS COPYING README NEWS
%{_sysconfdir}/xdg/menus/enlightenment.menu
%{_sysconfdir}/enlightenment/sysactions.conf
%{_bindir}/enlightenment
%{_bindir}/enlightenment_filemanager
%{_bindir}/enlightenment_imc
%{_bindir}/enlightenment_open
%{_bindir}/enlightenment_remote
%{_bindir}/enlightenment_start
%{_libdir}/enlightenment

%files data -f %{name}.lang
%{_datadir}/xsessions/enlightenment.desktop
%{_datadir}/enlightenment
%{_datadir}/applications/*.desktop

%files devel
%{_libdir}/pkgconfig/*.pc
%{_includedir}/enlightenment

%changelog
* Tue Nov 12 2013 Dan Mashal <dan.mashal@fedoraproject.org> 0.17.5-2
- Add emotion-devel to BRs

* Thu Nov 07 2013 Dan Mashal <dan.mashal@fedoraproject.org> 0.17.5-1
- Update to 0.17.5

* Mon Oct 07 2013 Dan Mashal <dan.mashal@fedoraproject.org> 0.17.4-4
- Add hard runtime requirements so one package can install the entire stack.

* Sun Oct 06 2013 Dan Mashal <dan.mashal@fedoraproejct.org> 0.17.4-3
- Add versioned build deps.

* Sun Oct 06 2013 Dan Mashal <dan.mashal@fedoraproejct.org> 0.17.4-2
- Update spec as per package review #1014619

* Tue Sep 24 2013 Dan Mashal <dan.mashal@fedoraproject.org> 0.17.4-1
- Update to 0.17.4
- Clean up spec file
- Update license from MIT to BSD

* Wed Jan 02 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 0.17.0-1
- initial spec
