Name:           kf5
Version:        5.13.0
Release:        3%{?dist}
Summary:        Filesystem and RPM macros for KDE Frameworks 5
Summary(zh_CN.UTF-8): KDE 框架 5 使用的文件系统和 RPM 宏
License:        BSD
URL:            http://www.kde.org

Source0:        macros.kf5

%description
Filesystem and RPM macros for KDE Frameworks 5

%description -l zh_CN.UTF-8
KDE 框架 5 使用的文件系统和 RPM 宏。

%package        filesystem
Summary:        Filesystem for KDE Frameworks 5
Summary(zh_CN.UTF-8): KDE 框架 5 使用的文件系统
# noarch -> arch transition
Obsoletes:      kf5-filesystem < 5.10.0-2
%description    filesystem
Filesystem for KDE Frameworks 5.
%description filesystem -l zh_CN.UTF-8
KDE 框架 5 使用的文件系统。

%package        rpm-macros
Summary:        RPM macros for KDE Frameworks 5
Summary(zh_CN.UTF-8): KDE 框架 5 使用的 RPM 宏
BuildArch: noarch
%description    rpm-macros
RPM macros for building KDE Frameworks 5 packages.
%description rpm-macros -l zh_CN.UTF-8
KDE 框架 5 使用的 RPM 宏。

%install
# See macros.kf5 where the directories are specified
mkdir -p %{buildroot}%{_prefix}/{lib,%{_lib}}/qt5/plugins/kf5/
mkdir -p %{buildroot}%{_includedir}/KF5
mkdir -p %{buildroot}%{_datadir}/{kconf_update,kf5}
mkdir -p %{buildroot}%{_libexecdir}/kf5
mkdir -p %{buildroot}%{_sysconfdir}/xdg/plasma-workspace/{env,shutdown}

install -Dpm644 %{_sourcedir}/macros.kf5 %{buildroot}%{_rpmconfigdir}/macros.d/macros.kf5
sed -i \
  -e "s|@@KF5_VERSION@@|%{version}|g" \
  %{buildroot}%{_rpmconfigdir}/macros.d/macros.kf5
magic_rpm_clean.sh

%files filesystem
%{_sysconfdir}/xdg/plasma-workspace/
%{_prefix}/lib/qt5/plugins/kf5/
%{_prefix}/%{_lib}/qt5/plugins/kf5/
%{_includedir}/KF5/
%{_libexecdir}/kf5/
%{_datadir}/kconf_update/
%{_datadir}/kf5/

%files rpm-macros
%{_rpmconfigdir}/macros.d/macros.kf5


%changelog
* Fri Oct 30 2015 Liu Di <liudidi@gmail.com> - 5.13.0-3
- 为 Magic 3.0 重建

* Fri Sep 11 2015 Liu Di <liudidi@gmail.com> - 5.13.0-2
- 为 Magic 3.0 重建

* Wed Aug 19 2015 Daniel Vrátil <dvratil@redhat.com> - 5.13.0-1
- KDE Frameworks 5.13.0

* Wed Aug 19 2015 Rex Dieter <rdieter@fedoraproject.org> 5.13.0-0.2
- macros.kf5: add %%_kf5_version

* Tue Aug 11 2015 Daniel Vrátil <dvratil@redhat.com> - 5.13.0-0.1
- KDE Frameworks 5.13

* Fri Jul 17 2015 Daniel Vrátil <dvratil@redhat.com> - 5.12.0
- KDE Frameworks 5.12.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Rex Dieter <rdieter@fedoraproject.org> 5.11.0-2
- own %%_datadir/kconf_update

* Wed Jun 10 2015 Daniel Vrátil <dvratil@redhat.com> - 5.11.0-1
- KDE Frameworks 5.11.0

* Wed Jun 03 2015 Rex Dieter <rdieter@fedoraproject.org> 5.10.0-2
- own %%{_datadir}/kf5, make -filesystem arch'd

* Mon May 11 2015 Daniel Vrátil <dvratil@redhat.com> - 5.10.0-1
- KDE Frameworks 5.10.0

* Tue Apr 07 2015 Daniel Vrátil <dvratil@redhat.com> - 5.9.0-1
- KDE Frameworks 5.9.0

* Mon Mar 16 2015 Daniel Vrátil <dvratil@redhat.com> - 5.8.0-1
- KDE Frameworks 5.8.0

* Tue Feb 10 2015 Daniel Vrátil <dvratil@redhat.com> - 5.7.0-2
- add %%find_lang_kf5 macro to macros.kf5 to workaround %%find_lang bugs

* Mon Feb 09 2015 Daniel Vrátil <dvratil@redhat.com> - 5.7.0-1
- KDE Frameworks 5.7.0

* Fri Jan 30 2015 Rex Dieter <rdieter@fedoraproject.org> 5.6.0-2
- own /etc/xdg/plasma-workspace/, /etc/xdg/plasma-workspace/{env,shutdown}

* Tue Jan 08 2015 Daniel Vrátil <dvratil@redhat.com> - 5.6.0-1
- KDE Frameworks 5.6.0

* Tue Jan 06 2015 Daniel Vrátil <dvratil@redhat.com> - 5.6.0-1
- KDE Frameworks 5.6.0

* Sat Dec 06 2014 Daniel Vrátil <dvratil@redhat.com> - 5.5.0-1
- KDE Frameworks 5.5.0

* Mon Nov 24 2014 Rex Dieter <rdieter@fedoraproject.org> 5.4.0-2
- macros.kf5: PATH, prepend %%_qt5_bindir instead of %%_kf5_bindir (ie, /usr/bin)

* Mon Nov 03 2014 Daniel Vrátil <dvratil@redhat.com> - 5.3.0-1
- KDE Frameworks 5.4.0

* Tue Oct 14 2014 Rex Dieter <rdieter@fedoraproject.org> 5.3.0-2
- macros.kf5: -DCMAKE_USE_RELATIVE_PATHS:BOOL=ON

* Wed Oct 08 2014 Daniel Vrátil <dvratil@redhat.com> - 5.3.0-1
- KDE Frameworks 5.3.0

* Mon Sep 15 2014 Daniel Vrátil <dvratil@redhat.com> - 5.2.0-1
- KDE Frameworks 5.2.0

* Wed Sep 03 2014 Rex Dieter <rdieter@fedoraproject.org> 5.1.0-3
- %%cmake_kf5: add -DKDE_INSTALL_USE_QT_SYS_PATHS=ON

* Thu Aug 21 2014 Daniel Vrátil <dvratil@redhat.com> - 5.1.0-2
- Add new KF5-specific variables to our CMake command

* Wed Aug 06 2014 Daniel Vrátil <dvratil@redhat.com> - 5.1.0-1
- KDE Frameworks 5.1.0

* Sat Jul 19 2014 Rex Dieter <rdieter@fedoraproject.org> 5.0.0-2
- Release: +%%{?dist}

* Wed Jul 09 2014 Daniel Vrátil <dvratil@redhat.com> - 5.0.0-1
- KDE Frameworks 5.0.0

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.99.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jun 04 2014 Daniel Vrátil <dvratil@redhat.com> 4.99.0-6
- Remove kf5 suffix from -DPLUGIN_INSTALL_DIR as packages now specify that on their own

* Wed Jun 04 2014 Daniel Vrátil <dvratil@redhat.com> 4.99.0-5
- Point -DLIBEXEC_INSTALL_DIR to %%{_libexecdir} to fix duplicated path

* Wed May 14 2014 Daniel Vrátil <dvratil@redhat.com> 4.99.0-4
- Make LIB_INSTALL_DIR relative, otherwise /usr/usr/lib64/... is generated by CMake

* Tue May 06 2014 Daniel Vrátil <dvratil@redhat.com> 4.99.0-3
- Define KF5_INCLUDE_INSTALL_DIR

* Mon May 05 2014 Daniel Vrátil <dvratil@redhat.com> 4.99.0-2
- Define KF5_LIBEXEC_INSTALL_DIR

* Mon May 05 2014 Daniel Vrátil <dvratil@redhat.com> 4.99.0-1
- KDE Frameworks 4.99.0

* Mon Apr 28 2014 Daniel Vrátil <dvratil@redhat.com> 4.98.0-8
- Remove INCLUDE_INSTALL_DIR, since we use the default one

* Tue Apr 22 2014 Daniel Vrátil <dvratil@redhat.com> 4.98.0-7
- Make DATA_INSTALL_DIR relative, so that CMake config files don't point to /usr/usr/share

* Tue Apr 22 2014 Daniel Vrátil <dvratil@redhat.com> 4.98.0-6
- Explicitly set BIN_INSTALL_DIR to be absolute, otherwise CMake complains

* Mon Apr 21 2014 Daniel Vrátil <dvratil@redhat.com> 4.98.0-5
- Fix _kf5_sysconfdir and set some install paths in cmake_kf5

* Wed Apr 16 2014 Daniel Vrátil <dvratil@redhat.com> 4.98.0-4
- Rename base package to kf5
- Create -filesystem, -rpm-macros subpackges

* Fri Apr 11 2014 Daniel Vrátil <dvratil@redhat.com> 4.98.0-3
- Fix build
- Use %%global instead of %%define
- Use install instead of cp

* Fri Apr 11 2014 Daniel Vrátil <dvratil@redhat.com> 4.98.0-2
- Fix some installation dirs in the macros.kf5 file

* Mon Mar 31 2014 Jan Grulich <jgrulich@redhat.com> 4.98.0-1
- Update to KDE Frameworks 5 Beta 1 (4.98.0)

* Wed Mar 05 2014 Jan Grulich <jgrulich@redhat.com> 4.97.0-1
- Update to KDE Frameworks 5 Alpha 2 (4.97.0)

* Thu Feb 13 2014 Daniel Vrátil <dvraitl@redhat.com> 4.96.0-2
- Remove unnecessary mkdirs

* Wed Feb 12 2014 Daniel Vrátil <dvratil@redhat.com> 4.96.0-1
- Update to KDE Frameworks 5 Alpha 1 (4.96.0)

* Wed Feb 05 2014 Daniel Vrátil <dvratil@redhat.com> 4.96.0-0.1.20140205git
- Update to pre-release snapshot of 4.96.0

* Thu Jan 16 2014 Daniel Vrátil <dvratil@redhat.com> 4.95.0-4
- fix definition of QT_PLUGIN_INSTALL_DIR in RPM macros

* Thu Jan 16 2014 Daniel Vrátil <dvratil@redhat.com> 4.95.0-2
- fix install dirs definitions in RPM macros

* Thu Jan 09 2014 Daniel Vrátil <dvratil@redhat.com> 4.95.0-1
- Update to KDE Frameworks 5 TP1 (4.95.0)

* Tue Jan  7 2014 Daniel Vrátil <dvratil@redhat.com>
- export XDG_DATA_DIRS

* Mon Jan  6 2014 Daniel Vrátil <dvratil@redhat.com>
- alter XDG_DATA_DIRS in cmake_kf5 RPM macro
- add _kf5_mandir RPM macro

* Sat Jan  4 2014 Daniel Vrátil <dvratil@redhat.com>
- initial version

