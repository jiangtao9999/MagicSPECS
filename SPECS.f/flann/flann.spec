%if 0%{?rhel} < 6 && ! 0%{?fedora}
%{!?python_sitearch: %global python_sitearch %(/usr/bin/python26 -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%endif

Name:           flann
Version:        1.7.1
Release:        5%{?dist}
Summary:        Fast Library for Approximate Nearest Neighbors

Group:          Development/Libraries
License:        BSD
URL:            http://www.cs.ubc.ca/~mariusm/index.php/FLANN/FLANN
Source0:        http://www.cs.ubc.ca/~mariusm/uploads/FLANN/%{name}-%{version}-src.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# This patch fixes the library install path on 64-bit systems
Patch0:         flann-1.6.7.64bit.patch
# This patch adds a missing version and soversion to flann.
Patch1:         flann-1.6.9.fixsoname.patch
# Prevent the buildsysem from running setup.py, not submitted upstream
Patch2:         flann-1.6.11.fixpyflann.patch 
# Patch to fix detection of tbb.  Not submitted upstream
Patch3:         flann-1.7.1-tbb.patch
BuildRequires:  cmake
BuildRequires:  zlib-devel

%if 0%{?fedora}
BuildRequires:  hdf5-devel
BuildRequires:  gtest-devel
%ifarch %{ix86} x86_64 ia64 ppc ppc64
BuildRequires:  tbb-devel
%endif
%endif

%if 0%{?rhel} >= 6 || 0%{?fedora}
BuildRequires:  python-devel
%else
BuildRequires:  python26
BuildRequires:  python26-devel
%endif


%description
FLANN is a library for performing fast approximate nearest neighbor searches 
in high dimensional spaces. It contains a collection of algorithms found 
to work best for nearest neighbor search and a system for automatically 
choosing the best algorithm and optimum parameters depending on the data sets.

%package devel
Summary: Development headers and libraries for flann
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
# flann/flann_mpi.hpp requires boost/mpi.hpp, which is a convenience header
# inside of the boost-devel package
Requires: boost-devel

%description devel
Development headers and libraries for flann.

%package static
Summary: Static libraries for flann
Group: Development/Libraries
Requires: %{name}-devel = %{version}-%{release}

%description static
Static libraries for flann.

%package python
Summary: Python bindings for flann
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: numpy

%description python
Python bindings for flann

%prep
%setup -q -n %{name}-%{version}-src
%patch0 -p1 -b .64bit
%patch1 -p0 -b .fixsoname
%patch2 -p0 -b .fixpyflann
%patch3 -p0 -b .tbb

%build
mkdir %{_target_platform}
pushd %{_target_platform}
%cmake -DBUILD_MATLAB_BINDINGS=OFF  -DCMAKE_BUILD_TYPE=RelWithDebInfo -DBUILD_PYTHON_BINDINGS=ON ..
popd
make %{?_smp_mflags} -C %{_target_platform}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} -C %{_target_platform}
rm -rf %{buildroot}%{_datadir}/%{name}/python

# install the python bindings
cp %{_target_platform}/src/python/setup.py src/python
pushd src/python
%if 0%{?rhel} >= 6 || ! 0%{?rhel}
python setup.py install --prefix=/usr --root=%{buildroot} --install-lib=%{python_sitearch}
%else
python26 setup.py install --prefix=/usr --root=%{buildroot} --install-lib=%{python_sitearch}
%endif
popd
# get rid of duplicate shared libraries
rm -rf %{buildroot}%{python_sitearch}/pyflann/lib
# Remove example binaries
rm -rf %{buildroot}%{_bindir}*
# Remove installed documentation, we'll install it later with the doc macro
rm -rf %{buildroot}%{_datadir}/doc/flann

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc doc/manual.pdf
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/flann

%files static
%defattr(-,root,root,-)
%{_libdir}/*.a

%files python
%defattr(-,root,root,-)
%{python_sitearch}/pyflann
%{python_sitearch}/flann-%{version}*.egg-info

%changelog
* Wed Oct 10 2012 Dan Horák <dan[at]danny.cz> - 1.7.1-5
- TBB is available only on selected arches

* Fri Sep 28 2012 Rich Mattes <richmattes@gmail.com> - 1.7.1-4
- Enabled tbb support

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-2
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Rich Mattes <richmattes@gmail.com> - 1.7.1-1
- Update to release 1.7.1

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 19 2011 Rich Mattes <richmattes@gmail.com> - 1.6.11-1
- Update to release 1.6.11

* Fri May 13 2011 Rich Mattes <richmattes@gmail.com> - 1.6.9-1
- Update to 1.6.9
- Make flann-devel require boost-devel for boost/mpi.hpp

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Feb 05 2011 Dan Horák <dan[at]danny.cz> - 1.6.7-6
- further updates for 64-bit systems (s390x, sparc64)

* Fri Feb 04 2011 Rich Mattes <richmattes@gmail.com> - 1.6.7-5
- Fixed ppc64 library installation paths (675316)

* Thu Feb 03 2011 Rich Mattes <richmattes@gmail.com> - 1.6.7-4
- Disabled hdf and ctest requirements for el6
- Explicit python26 dependency for el5

* Wed Feb 02 2011 Rich Mattes <richmattes@gmail.com> - 1.6.7-3
- Added clean section, rm buildroot at beginning of install
- Switched to using buildroot macro throughout specfile

* Mon Jan 31 2011 Rich Mattes <richmattes@gmail.com> - 1.6.7-2
- Fix exit() in shared lib error

* Wed Dec 22 2010 - Rich Mattes <richmattes@gmail.com> - 1.6.7-1
- Initial build
