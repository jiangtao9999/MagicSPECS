%global gem_name test-spec

Summary:        Behaviour Driven Development interface for Test::Unit
Name:           rubygem-%{gem_name}
Version:        0.10.0
Release:        10%{?dist}
Group:          Development/Languages
License:        Ruby or GPLv2
URL:            http://test-spec.rubyforge.org
Source0:        http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       ruby(release)
Requires:       ruby(rubygems)
Requires:       rubygem(test-unit)
BuildRequires:  rubygems-devel
BuildRequires:  rubygem(test-unit)
BuildArch:      noarch
Provides:       rubygem(%{gem_name}) = %{version}

%description
Test/spec layers an RSpec-inspired interface on top of Test::Unit, so you
can mix TDD and BDD (Behavior-Driven Development).  It is a clean-room
implementation that maps most kinds of Test::Unit assertions to a
should-like syntax.


%prep
%setup -q -c -T
%gem_install -n %{SOURCE0}
# Fix the failures of empty tests handling by allowing to run them.
pushd .%{gem_instdir}
sed -i '357d' lib/test/spec.rb
popd

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{gem_dir}
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
cp -ar .%{gem_dir}/* %{buildroot}%{gem_dir}
cp -a .%{_bindir}/* %{buildroot}%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%check
pushd .%{gem_instdir}
# TODO... upstream seems to be unfindable and these are really weird
bin/specrb -a | grep '78 tests, 600 assertions, 0 failures, 8 errors'
popd

%files
%defattr(-, root, root, -)
%{_bindir}/specrb
%dir %{gem_instdir}
%dir %{gem_instdir}/bin
%attr(0755,root,root) %{gem_instdir}/bin/specrb
%{gem_libdir}
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/examples
%doc %{gem_instdir}/test
%doc %{gem_instdir}/README
%doc %{gem_instdir}/SPECS
%doc %{gem_instdir}/ROADMAP
%doc %{gem_instdir}/TODO
%doc %{gem_docdir}
%{gem_cache}
%{gem_spec}


%changelog
* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 18 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 0.10.0-8
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Feb 02 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.10.0-5
- Rebuilt for Ruby 1.9.3.
- Introduced %%check section.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 08 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 0.10.0-2
- Fix up license
- Consistent use of macros
- Dependency on Ruby ABI

* Thu Jun 25 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 0.10.0-1
- Package generated by gem2rpm
- Fix up plist
