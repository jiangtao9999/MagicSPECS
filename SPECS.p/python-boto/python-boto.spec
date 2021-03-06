%if 0%{?fedora}
%bcond_without python3
%bcond_without unittests
%else
%bcond_with python3
%bcond_with unittests
%endif

# Boto's sample executables became doc files in F23
%if 0%{?fedora} >= 23
%bcond_with executables
%else
%bcond_without executables
%endif


%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%if %{with python3}
%{!?__python3: %global __python3 /usr/bin/python3}
%{!?python3_sitelib: %global python3_sitelib %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%endif  # with python3

Summary:        A simple, lightweight interface to Amazon Web Services
Summary(zh_CN.UTF-8): Amazon 网页服务的简单轻量级接口
Name:           python-boto
Version:        2.38.0
Release:        6%{?dist}
License:        MIT
Group:          Development/Languages
Group(zh_CN.UTF-8): 开发/语言
URL:            https://github.com/boto/boto
Source0:        http://pypi.python.org/packages/source/b/boto/boto-%{version}.tar.gz
# Taken from sourcecode 2014-07-31
Source1:        boto-mit-license.txt

# Unbundle python-six
# https://github.com/boto/boto/pull/3086
Patch1:         boto-2.37.0-devendor.patch

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-six
%if %{with python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
%endif  # with python3

%if %{with unittests}
BuildRequires:  python-argparse
BuildRequires:  python-httpretty
BuildRequires:  python-mock
BuildRequires:  python-nose
BuildRequires:  python-requests
%if %{with python3}
BuildRequires:  python3-httpretty
BuildRequires:  python3-mock
BuildRequires:  python3-nose
BuildRequires:  python3-requests
%endif  # with python3
%endif  # with unittests

Requires:       python-requests
Requires:       python-rsa
Requires:       python-six

Provides:       python2-boto = %{version}-%{release}

BuildArch:      noarch


%description
Boto is a Python package that provides interfaces to Amazon Web Services.
It supports over thirty services, such as S3 (Simple Storage Service),
SQS (Simple Queue Service), and EC2 (Elastic Compute Cloud) via their
REST and Query APIs.  The goal of boto is to support the full breadth
and depth of Amazon Web Services.  In addition, boto provides support
for other public services such as Google Storage in addition to private
cloud systems like Eucalyptus, OpenStack and Open Nebula.

%description -l zh_CN.UTF-8
Amazon 网页服务的简单轻量级接口。

%if %{with python3}
%package -n python3-boto
Summary:        A simple, lightweight interface to Amazon Web Services
Summary(zh_CN.UTF-8): Amazon 网页服务的简单轻量级接口

Requires:       python3-requests
Requires:       python3-six
%if 0%{?fedora} > 20
# python3-rsa was introduced in python-rsa-3.1.1-6.fc21.
# If it is backported to F20 please file a bug to request a rebuild
# without this condition.
Requires:       python3-rsa
%endif  # fedora > 20


%description -n python3-boto
Boto is a Python package that provides interfaces to Amazon Web Services.
It supports over thirty services, such as S3 (Simple Storage Service),
SQS (Simple Queue Service), and EC2 (Elastic Compute Cloud) via their
REST and Query APIs.  The goal of boto is to support the full breadth
and depth of Amazon Web Services.  In addition, boto provides support
for other public services such as Google Storage in addition to private
cloud systems like Eucalyptus, OpenStack and Open Nebula.

%description -n python3-boto -l zh_CN.UTF-8
Amazon 网页服务的简单轻量级接口。
%endif  # with python3


%prep
%setup -q -n boto-%{version}

%if ! 0%{?el7}
# python-six-1.3.0-4.el7 is too old, causes ImportErrors
# https://bugzilla.redhat.com/show_bug.cgi?id=1185409
%patch1 -p1
rm -r boto/vendored
%endif

cp -p %{SOURCE1} .

rm -r boto.egg-info


%build
%{__python2} setup.py build
%if %{with python3}
%{__python3} setup.py build
%endif  # with python3


%install
%if %{with python3}
# Scripts only work with python2
%{__python3} setup.py install --skip-build --root $RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT/%{_bindir}/*
%endif  # with python3

%{__python2} setup.py install --skip-build --root $RPM_BUILD_ROOT

%if %{without executables}
# Make executables doc files instead
chmod -x $RPM_BUILD_ROOT/%{_bindir}/*
mv $RPM_BUILD_ROOT/%{_bindir} examples
%endif
magic_rpm_clean.sh

%check
%if %{with unittests}
%{__python2} tests/test.py default
%if %{with python3}
%{__python3} tests/test.py default
%endif  # with python3
%endif  # with unittests


%files
# For some reason this definition really does have to go in this section.
%{!?_licensedir: %global license %%doc}
%license boto-mit-license.txt
%doc README.rst
%{python2_sitelib}/boto*

%if %{with executables}
%{_bindir}/*
%else
%doc examples
%endif


%if %{with python3}
%files -n python3-boto
%license boto-mit-license.txt
%{python3_sitelib}/boto*
%endif  # with python3


%changelog
* Thu Nov 12 2015 Liu Di <liudidi@gmail.com> - 2.38.0-6
- 为 Magic 3.0 重建

* Mon Nov 02 2015 Liu Di <liudidi@gmail.com> - 2.38.0-5
- 为 Magic 3.0 重建

* Wed Aug 19 2015 Liu Di <liudidi@gmail.com> - 2.38.0-4
- 为 Magic 3.0 重建

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.38.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun  9 2015 Garrett Holmstrom <gholms@fedoraproject.org> - 2.38.0-2
- Fixed ImportErrors on RHEL 7 (RH #1229863)

* Fri Apr 10 2015 Garrett Holmstrom <gholms@fedoraproject.org> - 2.38.0-1
- Updated to 2.38.0
- Added BuildRequires for python-six
- Made sample executables doc files in F23

* Wed Apr  8 2015 Garrett Holmstrom <gholms@fedoraproject.org> - 2.37.0-1
- Updated to 2.37.0 (RH #1180861)
- Dropped executables in F23
- Unbundled python-six (boto #3086)
- Enabled unit tests on Fedora (RH #1072946)

* Sun Nov  9 2014 Garrett Holmstrom <gholms@fedoraproject.org> - 2.34.0-4
- Fixed python3 requires

* Fri Nov  7 2014 Garrett Holmstrom <gholms@fedoraproject.org> - 2.34.0-3
- Re-fix executables (RH #1152444)

* Fri Nov  7 2014 Garrett Holmstrom <gholms@fedoraproject.org> - 2.34.0-2
- Added missing python-requests and python-rsa dependencies
- Disabled unit tests due to rawhide/F21 python regression (RH #1161166:c4)

* Fri Nov  7 2014 Garrett Holmstrom <gholms@fedoraproject.org> - 2.34.0-1
- Updated to 2.34.0 (RH #1072925, RH #1072928, RH #1161229)
- Made executables point to python2 (RH #1152444)
- Enabled unit tests on Fedora (RH #1072946)

* Thu Aug 21 2014 Garrett Holmstrom <gholms@fedoraproject.org> - 2.32.1-1
- Updated to 2.32.1 (RH #1126056, RH #1132348)
- Added python3-boto (RH #1024363)
- Added (but did not enable) unit tests (RH #1072946, RH #1072923)

* Thu Jul 31 2014 Tom Callaway <spot@fedoraproject.org> - 2.27.0-3
- fix license handling

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.27.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 21 2014 Garrett Holmstrom <gholms@fedoraproject.org> - 2.27.0-1
- Updated to 2.27.0

* Wed Feb 12 2014 Garrett Holmstrom <gholms@fedoraproject.org> - 2.25.0-2
- Fixed roboto parameter type conversion (boto #2094, RH #1064550)

* Mon Feb 10 2014 Garrett Holmstrom <gholms@fedoraproject.org> - 2.25.0-1
- Updated to 2.25.0
- This update makes s3.get_bucket use HEAD instead of GET

* Mon Jan 20 2014 Garrett Holmstrom <gholms@fedoraproject.org> - 2.23.0-1
- Updated to 2.23.0
- Fixed auth for anonymous S3 requests (boto #1988)

* Thu Sep 26 2013 Garrett Holmstrom <gholms@fedoraproject.org> - 2.13.3-1
- Updated to 2.13.3
- Note that this version changes register_image's virtualization_type parameter
- Fixed auto-scaling PropagateAtLaunch parsing (#1011682)

* Mon Jul 29 2013 Garrett Holmstrom <gholms@fedoraproject.org> - 2.9.9-2
- Re-fixed autoscaling policy parsing (boto #1538)

* Thu Jul 25 2013 Orion Poplawski <orion@cora.nwra.com> - 2.9.9-1
- Update to 2.9.9

* Fri Jun 21 2013 Garrett Holmstrom <gholms@fedoraproject.org> - 2.9.6-2
- Rebuilt after merge

* Fri Jun 21 2013 Garrett Holmstrom <gholms@fedoraproject.org> - 2.9.6-1
- Updated to 2.9.6
- Fixed autoscaling policy parsing (boto #1538)

* Thu May  9 2013 Orion Poplawski <orion@cora.nwra.com> - 2.9.2-1
- Update to 2.9.2 (bug #948714)
- Spec cleanup

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan  8 2013 Garrett Holmstrom <gholms@fedoraproject.org> - 2.5.2-3
- Fixed parsing of current/previous instance state data (boto #881)

* Wed Nov 21 2012 Garrett Holmstrom <gholms@fedoraproject.org> - 2.6.0-2
- Updated to 2.6.0 (#876517)
- Note that this version enables SSL cert verification by default.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jul  6 2012 Garrett Holmstrom <gholms@fedoraproject.org> - 2.5.2-1
- Updated to 2.5.2
- Fixed failure when metadata is empty (#838076)

* Thu Jun 14 2012 Garrett Holmstrom <gholms@fedoraproject.org> - 2.5.1-1
- Updated to 2.5.1 (last-minute upstream bugfix)

* Wed Jun 13 2012 Garrett Holmstrom <gholms@fedoraproject.org> - 2.5.0-1
- Updated to 2.5.0 (#828912)

* Wed Mar 21 2012 Robert Scheck <robert@fedoraproject.org> 2.3.0-1
- Upgrade to 2.3.0 (#786301 #c10)

* Tue Mar 13 2012 Robert Scheck <robert@fedoraproject.org> 2.2.2-1
- Upgrade to 2.2.2 (#786301, thanks to Bobby Powers)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 15 2011 Robert Scheck <robert@fedoraproject.org> 2.0-1
- Upgrade to 2.0 (#723088)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9b-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 02 2011 Robert Scheck <robert@fedoraproject.org> 1.9b-6
- Added a patch for python 2.4 support (#656446, #661233)

* Thu Dec 02 2010 Lubomir Rintel <lubo.rintel@gooddata.com> 1.9b-5
- Apply a patch for python 2.7 support (#659248)

* Thu Nov 18 2010 Robert Scheck <robert@fedoraproject.org> 1.9b-4
- Added patch to fix parameter of build_list_params() (#647005)

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 1.9b-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Feb 09 2010 Robert Scheck <robert@fedoraproject.org> 1.9b-2
- Backported upstream patch for image registration (#561216)

* Sat Jan 09 2010 Robert Scheck <robert@fedoraproject.org> 1.9b-1
- Upgrade to 1.9b

* Fri Jul 24 2009 Robert Scheck <robert@fedoraproject.org> 1.8d-1
- Upgrade to 1.8d (#513560)

* Wed Jun 03 2009 Luke Macken <lmacken@redhat.com> 1.7a-2
- Add python-setuptools-devel to our build requirements, for egg-info

* Thu Apr 16 2009 Robert Scheck <robert@fedoraproject.org> 1.7a-1
- Upgrade to 1.7a

* Mon Feb 23 2009 Robert Scheck <robert@fedoraproject.org> 1.5c-2
- Rebuild against rpm 4.6

* Sun Dec 07 2008 Robert Scheck <robert@fedoraproject.org> 1.5c-1
- Upgrade to 1.5c

* Fri Dec 05 2008 Jeremy Katz <katzj@redhat.com> 1.2a-2
- Rebuild for python 2.6

* Wed May 07 2008 Robert Scheck <robert@fedoraproject.org> 1.2a-1
- Upgrade to 1.2a

* Sat Feb 09 2008 Robert Scheck <robert@fedoraproject.org> 1.0a-1
- Upgrade to 1.0a

* Sat Dec 08 2007 Robert Scheck <robert@fedoraproject.org> 0.9d-1
- Upgrade to 0.9d

* Thu Aug 30 2007 Robert Scheck <robert@fedoraproject.org> 0.9b-1
- Upgrade to 0.9b
- Initial spec file for Fedora and Red Hat Enterprise Linux
