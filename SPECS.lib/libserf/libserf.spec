Name:           libserf
Version:        1.3.6
Release:        4%{?dist}
Summary:        High-Performance Asynchronous HTTP Client Library
Summary(zh_CN.UTF-8): 高性能的异步 HTTP 客户端库
License:        ASL 2.0
URL:            http://code.google.com/p/serf/
Source0:        http://serf.googlecode.com/svn/src_releases/serf-%{version}.tar.bz2
BuildRequires:  apr-devel, apr-util-devel
BuildRequires:  krb5-devel, openssl-devel, zlib-devel
BuildRequires:  scons, pkgconfig

%description
The serf library is a C-based HTTP client library built upon the Apache 
Portable Runtime (APR) library. It multiplexes connections, running the
read/write communication asynchronously. Memory copies and transformations are
kept to a minimum to provide high performance operation.

%description -l zh_CN.UTF-8
高性能的异步 HTTP 客户端库。

%package        devel
Summary:        Development files for %{name}
Summary(zh_CN.UTF-8): %{name} 的开发包
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       apr-devel%{?_isa}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%description devel -l zh_CN.UTF-8
%{name} 的开发包。

%prep
%setup -qn serf-%{version}

# Shared library versioning support in scons is worse than awful...
# minimally, here fix the soname to match serf-1.2.x.  Minor version
# handling should be fixed too; really requires better upstream support:
# http://scons.tigris.org/issues/show_bug.cgi?id=2869
sed -i '/SHLIBVERSION/s/MAJOR/0/' SConstruct

%build
scons \
      CFLAGS="%{optflags}" \
      PREFIX=%{_prefix} \
      LIBDIR=%{_libdir} \
      GSSAPI=%{_prefix} \
      %{?_smp_mflags}

%install
scons install --install-sandbox=%{buildroot}
find %{buildroot} -name '*.*a' -delete -print
magic_rpm_clean.sh

%check
scons %{?_smp_mflags} check || true

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc LICENSE NOTICE
%{_libdir}/*.so.*

%files devel
%doc CHANGES README design-guide.txt
%{_includedir}/serf-1/
%{_libdir}/*.so
%{_libdir}/pkgconfig/serf*.pc

%changelog
* Mon Nov 09 2015 Liu Di <liudidi@gmail.com> - 1.3.6-4
- 为 Magic 3.0 重建

* Sat Oct 31 2015 Liu Di <liudidi@gmail.com> - 1.3.6-3
- 为 Magic 3.0 重建

* Thu Jul 31 2014 Liu Di <liudidi@gmail.com> - 1.3.6-2
- 为 Magic 3.0 重建

* Thu Jul 31 2014 Liu Di <liudidi@gmail.com> - 1.3.6-1
- 升级到 1.3.6

* Tue Jun 17 2014 Liu Di <liudidi@gmail.com> - 1.3.5-3
- 为 Magic 3.0 重建

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 30 2014 Christopher Meng <rpm@cicku.me> - 1.3.5-1
- update to 1.3.5

* Mon Feb 17 2014 Joe Orton <jorton@redhat.com> - 1.3.4-1
- update to 1.3.4

* Tue Dec 10 2013 Joe Orton <jorton@redhat.com> - 1.3.3-1
- update to 1.3.3

* Wed Nov  6 2013 Joe Orton <jorton@redhat.com> - 1.3.2-1
- update to 1.3.2
- require krb5-devel for libgssapi (#1027011)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 17 2013 Christopher Meng <rpm@cicku.me> - 1.2.1-3
- SPEC cleanup.

* Thu Jun 13 2013 Christopher Meng <rpm@cicku.me> - 1.2.1-2
- Fix the permission of the library.

* Sun Jun 09 2013 Christopher Meng <rpm@cicku.me> - 1.2.1-1
- Initial Package.
