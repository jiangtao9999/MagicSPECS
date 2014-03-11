Name: kde4-style-crystal
Summary: Crystal kwin decoration theme to KDE 4.x
Summary(zh_CN): KDE 4.x 的 Crystal 窗口装饰
Version: 2.0.5
Release: 3%{?dist}
Source0: http://www.kde-look.org/CONTENT/content-files/75140-crystal-%version.tar.bz2
Patch0: crystal-fix-compile.patch
URL: http://www.kde-look.org/content/show.php/crystal?content=75140
Group: Graphical desktop/KDE
Group(zh_CN):	用户界面/桌面
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License: GPLv2+
BuildRequires: kdebase4-workspace-devel
Obsoletes: kde4-kwin-style-crystal < %version-%release

%description
This is the port of the famous Crystal kwin decoration theme to KDE 4.x.

Main features:
* Choose the blending color of the buttons.
* You can define the title bar height and border size of the windows.
* Right click on minimize button toggles shade mode.
* Middle click on minimize button sends window to below.
* Double click on program symbol closes window.
* Support for button themes. Basic button theme is included, feel free
  to swamp me with cool themes.
* Can show a tooltip of the caption
* If kdocker is installed (http://kdocker.sf.net), right click on close
  button will send the window to the systemtray.

%description -l zh_CN
KDE 4.x 的 Crystal 窗口装饰。

%prep
%setup -q -n crystal-%version
%patch0

%build
pushd build
%cmake_kde4 ..
make 
popd

%install
%__rm -rf $RPM_BUILD_ROOT
pushd build
make install DESTDIR=$RPM_BUILD_ROOT
popd

%files
%defattr(-,root,root)
%doc AUTHORS README COPYING INSTALL
%{_kde4_libdir}/kde4/kwin3_crystal.so
%{_kde4_libdir}/kde4/kwin_crystal_config.so
%{_kde4_appsdir}/kwin/crystal.desktop


%changelog
* Fri Dec 07 2012 Liu Di <liudidi@gmail.com> - 2.0.5-3
- 涓� Magic 3.0 閲嶅缓

* Wed Dec 21 2011 Liu Di <liudidi@gmail.com> - 2.0.5-2
- 涓� Magic 3.0 閲嶅缓


