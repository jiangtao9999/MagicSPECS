%if 0%{?fedora} || 0%{?rhel} >= 7
%global ruby_archdir   %{ruby_vendorarchdir}
%else
%global ruby_archdir   %(ruby -rrbconfig -e 'puts RbConfig::CONFIG["sitearchdir"]')
%endif

Name:           ruby-shadow
Version:        1.4.1
Release:        30%{?dist}
Summary:        Ruby bindings for shadow password access
Group:          System Environment/Libraries
License:        Public Domain
URL:            http://ttsky.net/
Source0:        http://ttsky.net/src/ruby-shadow-%{version}.tar.gz
Patch0:         0001-Add-ruby-1.9-support.patch
Patch1:         ruby-shadow-1.4.1-cflags.patch
Patch2:         ruby-shadow-2.2.0-Add-support-for-ruby-2.0.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  ruby-devel
%if 0%{?fedora} || 0%{?rhel} >= 7
Requires:       ruby(release)
%else
Requires:       ruby(abi) = 1.8
%endif
Provides:       ruby(shadow) = %{version}-%{release}

%description
Ruby bindings for shadow password access

%prep
%setup -q -n shadow-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%{_bindir}/iconv -f EUCJP -t utf8 -o README.ja README.euc

%build
ruby extconf.rb --with-cflags="$RPM_OPT_FLAGS"
make

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} sitearchdir=%{buildroot}%{ruby_archdir} install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc HISTORY README README.ja
%{ruby_archdir}/shadow.so

%changelog
* Fri Nov 13 2015 Liu Di <liudidi@gmail.com> - 1.4.1-30
- 为 Magic 3.0 重建

* Wed Nov 04 2015 Liu Di <liudidi@gmail.com> - 1.4.1-29
- 为 Magic 3.0 重建

* Thu Sep 24 2015 Liu Di <liudidi@gmail.com> - 1.4.1-28
- 为 Magic 3.0 重建

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jan 17 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.1-26
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_2.2

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 31 2014 Sam Kottler <skottler@fedoraproject.org> - 1.4.1-23
- Fix conditional so shadow.so gets installed to the proper location (BZ#1094046)

* Mon Apr 28 2014 Vít Ondruch <vondruch@redhat.com> - 1.4.1-22
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1

* Thu Jan 23 2014 Orion Poplawski <orion@cora.nwra.com> - 1.4.1-21
- Update ruby requires conditionals for EPEL7

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 18 2013 Vít Ondruch <vondruch@redhat.com> - 1.4.1-19
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 20 2012 Todd Zullinger <tmz@pobox.com> - 1.4.1-16
- Add ruby-1.9 support

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 10 2008 Kostas Georgiou <k.georgiou@imperial.ac.uk> - 1.4.1-11
- Rebuild for GCC 4.3

* Wed Aug 29 2007 Kostas Georgiou <k.georgiou@imperial.ac.uk> - 1.4.1-10
- Increase version to fix wrong tag

* Wed Aug 29 2007 Kostas Georgiou <k.georgiou@imperial.ac.uk> - 1.4.1-9
- Clean up of the "sh: ruby: command not found" added by the automated rebuild
  in the spec file

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 1.4.1-8
- Rebuild for selinux ppc32 issue.

* Wed Jul 18 2007 David Lutterkort <dlutter@redhat.com> - 1.4.1-7
- Remove dependency on ruby{,io}.h from depend - makes builds on RHEL4 fail, 
  and doesn't provide anything for proper rpm builds

* Fri May 25 2007 Kostas Georgiou <k.georgiou@imperial.ac.uk> 1.4.1-6
Removed _smp_mflags from install since it was causing problems

* Fri May 18 2007 Kostas Georgiou <k.georgiou@imperial.ac.uk> 1.4.1-5
Removed the ruby abi macro since it doesn't work in mock

* Tue May 15 2007 Kostas Georgiou <k.georgiou@imperial.ac.uk> 1.4.1-4
Cleaner ruby abi macro

* Tue May 15 2007 Kostas Georgiou <k.georgiou@imperial.ac.uk> 1.4.1-3
Fixed struct defines (0 != NULL in C) 
Calculate ruby abi at runtime instead of a hard coded version

* Tue May 15 2007 Kostas Georgiou <k.georgiou@imperial.ac.uk> 1.4.1-2
Converted README.euc to utf8 README.ja
Patched extconf.rb to use provided CFLAGS

* Mon May 14 2007 Kostas Georgiou <k.georgiou@imperial.ac.uk> 1.4.1-1
Initial rpm release
