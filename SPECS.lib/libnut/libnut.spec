Summary: Library for creating and demuxing NUT files
Summary(zh_CN.UTF-8): 创建和重编码 NUT 文件的库
Name: libnut
Version: 0.0.0
Release: 6_r661%{?dist}
License: distributable
Group: FIXME
URL: http://www.nut-container.org/
Source0: %{name}-%{version}-r661.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Provides: libnut-devel = %{evr}

%description
NUT is a patent-free, multimedia container format originally conceived
by a few MPlayer and FFmpeg developers that were dissatisfied with the
limitations of all currently available multimedia container formats
such as AVI, Ogg or Matroska. It aims to be simple, flexible,
extensible, compact and error resistant (error resilient), thus
addressing most if not all of the shortcomings present in alternative
formats, like excessive CPU and size overhead, file size limits,
inability to allow fine grained seeking or restrictions on the type of
data they can contain.

libnut is a free library for creating and demuxing NUT files. It
supports frame accurate seeking for active streams, recovery from
errors and dynamic index generation during playback.

%description -l zh_CN.UTF-8
创建和重编码 NUT 文件的库。

%prep
%setup -q -n libnut
perl -pi -e's,\$\(prefix\)/lib,\$(DESTDIR)\$(libdir),g' Makefile
perl -pi -e's,\$\(prefix\)/include,\$(DESTDIR)\$(includedir),g' Makefile
perl -pi -e's,\$\(prefix\)/bin,\$(DESTDIR)\$(bindir),g' Makefile

%build
export CFLAGS="%{optflags} -fPIC"
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} \
  libdir=%{_libdir} includedir=%{_includedir} bindir=%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/*.a
%{_includedir}/*
%{_bindir}/nut*

%changelog
* Mon Nov 09 2015 Liu Di <liudidi@gmail.com> - 0.0.0-6_r661
- 为 Magic 3.0 重建

* Sat Oct 31 2015 Liu Di <liudidi@gmail.com> - 0.0.0-5_r661
- 为 Magic 3.0 重建

* Tue Jul 22 2014 Liu Di <liudidi@gmail.com> - 0.0.0-4_r661
- 为 Magic 3.0 重建

* Fri Dec 07 2012 Liu Di <liudidi@gmail.com> - 0.0.0-3_r661
- 为 Magic 3.0 重建

* Tue Jan 10 2012 Liu Di <liudidi@gmail.com> - 0.0.0-2_r661
- 为 Magic 3.0 重建

* Sat Nov 21 2009 Axel Thimm <Axel.Thimm@ATrpms.net>
- Initial build.

