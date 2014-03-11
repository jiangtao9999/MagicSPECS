Name:           lazarus
Version:        1.0.4
Release:        0
Summary:        Lazarus Component Library and IDE

Group:          Development/Languages
License:        GPL and modified LGPL
URL:            http://www.lazarus.freepascal.org/
Source0:        http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}-%{release}.tar.gz
Packager:       Mattias Gaertner
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  fpc, gtk2-devel, glibc-devel
Requires:       fpc-src, fpc, gtk2-devel, glibc-devel, binutils, gdb

Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%define _source_filedigest_algorithm 0
%define _binary_filedigest_algorithm 0

%description
Lazarus is a free and open source Rapid Application Development tool for
the FreePascal compiler using the Lazarus component library - LCL. The LCL
is included in this package.

%prep
%setup -c

%build
cd lazarus
MAKEOPTS="-Fl/opt/gnome/lib"
if [ -n "$FPCCfg" ]; then
  MAKEOPTS="$MAKEOPTS -n @$FPCCfg"
fi
#CHMHELP:MAKEOPTS="$MAKEOPTS -dUseCHMHelp"
make bigide OPT="$MAKEOPTS" USESVN2REVISIONINC=0
export LCL_PLATFORM=
strip lazarus
strip startlazarus
strip lazbuild
strip tools/lazres
strip tools/updatepofiles
strip tools/lrstolfm
strip tools/svn2revisioninc
if [ -f components/chmhelp/lhelp/lhelp ]; then
  strip components/chmhelp/lhelp/lhelp
fi

%install
[ %{buildroot} != "/" ] && ( rm -rf %{buildroot} )
LAZARUSDIR=%{_libdir}/%{name}
mkdir -p %{buildroot}$LAZARUSDIR
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/pixmaps
# mkdir -p %{buildroot}%{_datadir}/gnome/apps/Development
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/mime/packages
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_sysconfdir}/lazarus
cp -a lazarus/* %{buildroot}$LAZARUSDIR/
  install -m 644 lazarus/images/icons/lazarus128x128.png %{buildroot}%{_datadir}/pixmaps/lazarus.png
  install -m 644 lazarus/install/lazarus.desktop %{buildroot}%{_datadir}/applications/lazarus.desktop
  install -m 644 lazarus/install/lazarus-mime.xml $LazBuildDir%{buildroot}%{_datadir}/mime/packages/lazarus.xml
ln -sf $LAZARUSDIR/lazarus %{buildroot}%{_bindir}/lazarus-ide
ln -sf $LAZARUSDIR/startlazarus %{buildroot}%{_bindir}/startlazarus
ln -sf $LAZARUSDIR/lazbuild %{buildroot}%{_bindir}/lazbuild
cat lazarus/install/man/man1/lazbuild.1 | gzip > %{buildroot}%{_mandir}/man1/lazbuild.1.gz
cat lazarus/install/man/man1/lazarus-ide.1 | gzip > %{buildroot}%{_mandir}/man1/lazarus-ide.1.gz
cat lazarus/install/man/man1/startlazarus.1 | gzip > %{buildroot}%{_mandir}/man1/startlazarus.1.gz
  install lazarus/tools/install/linux/editoroptions.xml %{buildroot}%{_sysconfdir}/lazarus/editoroptions.xml
cat lazarus/tools/install/linux/environmentoptions.xml | sed -e "s#__LAZARUSDIR__#$LAZARUSDIR/#" -e "s#__FPCSRCDIR__#%{_datadir}/fpcsrc/#" > %{buildroot}%{_sysconfdir}/lazarus/environmentoptions.xml


%clean
[ %{buildroot} != "/" ] && ( rm -rf %{buildroot} )

%post
%{_libdir}/%{name}/tools/install/rpm/create_gtk1_links.sh
#update-desktop-database &> /dev/null ||:

%postun
update-desktop-database &> /dev/null ||:

%files
%defattr(-,root,root,-)
%{_libdir}/%{name}
%{_bindir}/*
  %{_datadir}/pixmaps/lazarus.png
  %{_datadir}/applications/lazarus.desktop
  %{_datadir}/mime/packages/lazarus.xml
  %{_sysconfdir}/lazarus/editoroptions.xml
  %{_sysconfdir}/lazarus/environmentoptions.xml
%{_mandir}/*/*

%changelog
* Mon Jun 21 2012 Mattias Gaertner <mattias@freepascal.org> 1.0-0
- 128x128 icon, chmhelp
* Sat Sep 9 2006 Mattias Gaertner <mattias@freepascal.org> 0.9.18-0
- Initial build.
* Wed Jul 20 2005 Joost van der Sluis <joost@cnoc.nl> 0.9.8-0.1
- Initial build.

