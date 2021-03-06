Summary: Internationalized Domain Name support library
Summary(zh_CN.UTF-8): 国际化域名支持库
Name: libidn
Version: 1.32
Release: 5%{?dist}
URL: http://www.gnu.org/software/libidn/
License: LGPLv2+ and GPLv3+ and GFDL
Source0: http://ftp.gnu.org/gnu/libidn/libidn-%{version}.tar.gz
Group: System Environment/Libraries
Group(zh_CN.UTF-8): 系统环境/库
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: pkgconfig, gettext
Requires(post): /usr/sbin/install-info /usr/sbin/ldconfig
Requires(preun): /usr/sbin/install-info
Requires(postun): /usr/sbin/ldconfig

%description
GNU Libidn is an implementation of the Stringprep, Punycode and
IDNA specifications defined by the IETF Internationalized Domain
Names (IDN) working group, used for internationalized domain
names.

%description -l zh_CN.UTF-8
国际化域名支持库。

%package devel
Summary: Development files for the libidn library
Summary(zh_CN.UTF-8): %{name} 的开发包
Group: Development/Libraries
Group(zh_CN.UTF-8): 开发/库
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
This package includes header files and libraries necessary for
developing programs which use the GNU libidn library.

%description devel -l zh_CN.UTF-8
%{name} 的开发包。

%package -n emacs-%{name}
Summary: GNU Emacs libidn support files
Summary(zh_CN.UTF-8): GNU Emacs libidn 支持文件
License: GPLv3+
BuildRequires: emacs
Requires: %{name} = %{version}-%{release}
Requires: emacs(bin) >= %{_emacs_version}
BuildArch: noarch

%description -n emacs-%{name}
This package includes libidn support files for GNU Emacs.

%description -n emacs-%{name} -l zh_CN.UTF-8
GNU Emacs libidn 支持文件。

%prep
%setup -q

# Name directory sections consistently in the info file, #209491
sed -i '/^INFO-DIR-SECTION/{s/GNU Libraries/Libraries/;s/GNU utilities/Utilities/;}' doc/libidn.info

iconv -f ISO-8859-1 -t UTF-8 doc/libidn.info > iconv.tmp
mv iconv.tmp doc/libidn.info

%build
%configure --disable-csharp --disable-static --libdir=%{_libdir} --with-lispdir=%{_emacs_sitelispdir}/%{name}
make %{?_smp_mflags}

%if 0%{?with_check}
%check
make %{?_smp_mflags} -C tests check
%endif

%install
rm -rf %{buildroot}
make install DESTDIR=$RPM_BUILD_ROOT pkgconfigdir=%{_libdir}/pkgconfig

# provide more examples
make %{?_smp_mflags} -C examples distclean

# clean up docs
find doc -name "Makefile*" | xargs rm
rm -rf $RPM_BUILD_ROOT%{_datadir}/info/dir

# Make multilib safe:
sed -i '/gnu compiler/d' $RPM_BUILD_ROOT%{_includedir}/idn-int.h

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la \
      $RPM_BUILD_ROOT%{_datadir}/info/*.png

#mkdir -p $RPM_BUILD_ROOT%{_libdir}
#mv $RPM_BUILD_ROOT/%{_lib}/libidn.so $RPM_BUILD_ROOT%{_libdir}

#lib=`echo $RPM_BUILD_ROOT/%{_lib}/libidn.so.*.*`
#ln -sf ../../%{_lib}/`basename ${lib}` $RPM_BUILD_ROOT%{_libdir}/libidn.so

# Fix the .pc file to reference the directory which contains the .so
sed -i 's,^libdir=.*$,libdir=%{_libdir},' \
    $RPM_BUILD_ROOT%{_libdir}/pkgconfig/libidn.pc

%{_emacs_bytecompile} $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{name}/*.el

magic_rpm_clean.sh 
%find_lang %{name} || touch %{name}.lang

%post
/usr/sbin/install-info %{_infodir}/%{name}.info.gz %{_infodir}/dir
/usr/sbin/ldconfig

%preun
if [ $1 = 0 ]; then
    /usr/sbin/install-info --delete %{_infodir}/%{name}.info.gz %{_infodir}/dir || :
fi

%postun -p /usr/sbin/ldconfig

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS NEWS FAQ README THANKS COPYING*
%{_bindir}/idn
%{_mandir}/man1/idn.1*
%{_libdir}/libidn.so.*
%{_infodir}/%{name}.info.gz

%files devel
%defattr(0644,root,root,755)
%doc doc/libidn.html examples
%{_libdir}/libidn.so
%{_includedir}/*.h
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*

%files -n emacs-%{name}
%defattr(-,root,root)
%{_emacs_sitelispdir}/%{name}

%changelog
* Mon Nov 09 2015 Liu Di <liudidi@gmail.com> - 1.32-5
- 为 Magic 3.0 重建

* Sat Oct 31 2015 Liu Di <liudidi@gmail.com> - 1.32-4
- 更新到 1.32

* Fri Jul 18 2014 Liu Di <liudidi@gmail.com> - 1.28-3
- 更新到 1.28

* Fri Dec 07 2012 Liu Di <liudidi@gmail.com> - 1.24-3
- 为 Magic 3.0 重建

* Wed Apr 18 2012 Liu Di <liudidi@gmail.com> - 1.24-2
- 为 Magic 3.0 重建

* Sun Jan 15 2012 Robert Scheck <robert@fedoraproject.org> - 1.24-1
- Update to 1.24 (#781379)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 25 2011 Miroslav Lichvar <mlichvar@redhat.com> - 1.23-1
- update to 1.23

* Tue May 31 2011 Ville Skyttä <ville.skytta@iki.fi> - 1.22-3
- Split emacs-libidn subpackage to avoid *.elc arch conflicts (#709136).

* Sun May 29 2011 Ville Skyttä <ville.skytta@iki.fi> - 1.22-2
- Byte compile Emacs lisp files, require emacs-filesystem for dir ownership.

* Thu May 05 2011 Miroslav Lichvar <mlichvar@redhat.com> - 1.22-1
- update to 1.22

* Tue Apr 26 2011 Miroslav Lichvar <mlichvar@redhat.com> - 1.21-1
- update to 1.21

* Thu Mar 03 2011 Miroslav Lichvar <mlichvar@redhat.com> - 1.20-1
- update to 1.20
- fix requires

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon May 24 2010 Joe Orton <jorton@redhat.com> - 1.19-1
- update to 1.19 (#595086)

* Tue Mar 30 2010 Joe Orton <jorton@redhat.com> - 1.18-2
- add GFDL to License

* Mon Mar 29 2010 Joe Orton <jorton@redhat.com> - 1.18-1
- update to 1.18
- fix Source0 to reference gnu.org repository

* Fri Jan 29 2010 Joe Orton <jorton@redhat.com> - 1.16-1
- update to 1.16

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 10 2009 Joe Orton <jorton@redhat.com> 1.9-4
- update to 1.9 (#302111)
- update License to reflect GPLv3+ binaries, LGPLv2+ library

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 29 2008 Kedar Sovani <kedars@marvell.com> 0.6.14-9
- fix the problem with #include_next

* Tue Jun 10 2008 Joe Orton <jorton@redhat.com> 0.6.14-8
- fix build with latest autoconf (#449440)

* Mon Mar 31 2008 Joe Orton <jorton@redhat.com> 0.6.14-7
- fix libidn.pc for correct libdir (#439549)

* Fri Mar  7 2008 Joe Orton <jorton@redhat.com> 0.6.14-6
- drop libidn.a
- move shared library to /lib{,64} (#283651)

* Thu Feb  7 2008 Joe Orton <jorton@redhat.com> 0.6.14-5
- fix DT_RPATH in /usr/bin/idn
- convert libidn.iconv to UTF-8 (Jon Ciesla, #226029)
- fix BuildRoot tag (Jon Ciesla, #226029)

* Tue Aug 21 2007 Joe Orton <jorton@redhat.com> 0.6.14-4
- drop contrib directory from docs

* Mon Aug 20 2007 Joe Orton <jorton@redhat.com> 0.6.14-3
- fix License

* Mon Jun 18 2007 Joe Orton <jorton@redhat.com> 0.6.14-2
- update to 0.6.14

* Mon Jan 29 2007 Joe Orton <jorton@redhat.com> 0.6.9-2
- update to 0.6.9
- make install-info use failsafe (Ville Skyttä, #223707)

* Wed Nov 15 2006 Joe Orton <jorton@redhat.com> 0.6.8-4
- use non-GNU section in info directory (#209491)

* Wed Nov 15 2006 Joe Orton <jorton@redhat.com> 0.6.8-3
- update to 0.6.8

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.6.5-1.1
- rebuild

* Fri Jul  7 2006 Joe Orton <jorton@redhat.com> 0.6.5-1
- update to 0.6.5

* Fri Jul  7 2006 Joe Orton <jorton@redhat.com> 0.6.4-1
- update to 0.6.4

* Thu Jun  1 2006 Joe Orton <jorton@redhat.com> 0.6.3-1
- update to 0.6.3
- fix some places where gettext() was not getting used

* Thu Jun  1 2006 Joe Orton <jorton@redhat.com> 0.6.2-4
- remove the libidn.la (#172639)

* Thu May 11 2006 Joe Orton <jorton@redhat.com> 0.6.2-3
- make idn-int.h multilib-safe

* Wed Feb 22 2006 Joe Orton <jorton@redhat.com> 0.6.2-2
- disable C# support (#182393)

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.6.2-1.1
- bump again for double-long bug on ppc(64)

* Mon Feb 06 2006 Florian La Roche <laroche@redhat.com>
- 0.6.1

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Sun Dec  4 2005 Joe Orton <jorton@redhat.com> 0.6.0-1
- update to 0.6.0

* Mon Oct 24 2005 Joe Orton <jorton@redhat.com> 0.5.20-1
- update to 0.5.20

* Mon Sep 19 2005 Joe Orton <jorton@redhat.com> 0.5.19-1
- update to 0.5.19

* Fri May 27 2005 Joe Orton <jorton@redhat.com> 0.5.17-1
- update to 0.5.17

* Fri May  6 2005 Joe Orton <jorton@redhat.com> 0.5.16-1
- update to 0.5.16

* Thu May  5 2005 Joe Orton <jorton@redhat.com> 0.5.15-2
- constify data tables in pr29.c
- clean up pre/post/postun requires

* Sun Mar 20 2005 Joe Orton <jorton@redhat.com> 0.5.15-1
- update to 0.5.15

* Fri Mar  4 2005 Joe Orton <jorton@redhat.com> 0.5.13-2
- rebuild

* Mon Jan 31 2005 Joe Orton <jorton@redhat.com> 0.5.13-1
- update to 0.5.13

* Sun Dec  5 2004 Joe Orton <jorton@redhat.com> 0.5.12-1
- update to 0.5.12

* Mon Nov 29 2004 Joe Orton <jorton@redhat.com> 0.5.11-1
- update to 0.5.11 (#141094)

* Tue Nov  9 2004 Joe Orton <jorton@redhat.com> 0.5.10-1
- update to 0.5.10
- buildroot cleanup fix (Robert Scheck)

* Mon Nov  8 2004 Joe Orton <jorton@redhat.com> 0.5.9-1
- update to 0.5.9 (#138296)

* Thu Oct  7 2004 Joe Orton <jorton@redhat.com> 0.5.6-1
- update to 0.5.6 (#134343)

* Thu Sep 30 2004 Miloslav Trmac <mitr@redhat.com> - 0.5.4-3
- Fix Group: (#134068)

* Tue Aug 31 2004 Joe Orton <jorton@redhat.com> 0.5.4-2
- move ldconfig from preun to postun (#131280)

* Sun Aug  8 2004 Joe Orton <jorton@redhat.com> 0.5.4-1
- update to 0.5.4 (#129341)

* Thu Jul 15 2004 Robert Scheck <redhat@linuxnetz.de> 0.5.2-1
- upgrade to 0.5.2, enabled i18n support and info files (#127906)

* Fri Jul  9 2004 Joe Orton <jorton@redhat.com> 0.5.1-1
- update to 0.5.1 (#127496)

* Mon Jun 28 2004 Joe Orton <jorton@redhat.com> 0.5.0-1
- update to 0.5.0 (#126836)

* Tue Jun 22 2004 Than Ngo <than@redhat.com> 0.4.9-2
- add prereq: /usr/sbin/ldconfig
- move la file in main package

* Tue Jun 15 2004 Robert Scheck <redhat@linuxnetz.de> 0.4.9-1
- upgrade to 0.4.9 (#126353)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Apr 29 2004 Joe Orton <jorton@redhat.com> 0.4.4-1
- update to 0.4.4; remove contrib from -devel docs

* Thu Apr 29 2004 Joe Orton <jorton@redhat.com> 0.4.3-1
- update to 0.4.3, remove -rpath patch

* Tue Jan 27 2004 Joe Orton <jorton@redhat.com> 0.3.7-1
- update to 0.3.7, simplify

* Wed Jan 07 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.3.6-1mdk
- 0.3.6

* Mon Dec 15 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 0.3.5-1mdk
- 0.3.5

* Sun Oct 19 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 0.3.3-2mdk
- drop the "soname fix" and use the correct way...

* Sat Oct 18 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 0.3.3-1mdk
- 0.3.3

* Mon Oct 13 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 0.3.2-1mdk
- initial cooker contrib
- used the package from PLD as a start point
