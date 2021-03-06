
Name:          jackson-parent
Version:       2.4.1
Release:       4%{?dist}
Summary:       Parent pom for all Jackson components
License:       ASL 2.0
URL:           https://github.com/FasterXML/jackson-parent
Source0:       https://github.com/FasterXML/jackson-parent/archive/%{name}-%{version}.tar.gz
# jackson-parent package don't include the license file
# reported @ https://github.com/FasterXML/jackson-parent/issues/1
Source1:       http://www.apache.org/licenses/LICENSE-2.0.txt
%if %{?fedora} > 20
BuildRequires: mvn(com.fasterxml:oss-parent:pom:)
%else
BuildRequires: mvn(com.fasterxml:oss-parent)
%endif
BuildRequires: mvn(junit:junit)
BuildRequires: maven-local
BuildRequires: replacer
BuildArch:     noarch

%description
Project for parent pom for all Jackson components.

%prep
%setup -q -n %{name}-%{name}-%{version}

cp -p %{SOURCE1} .
sed -i 's/\r//' LICENSE-2.0.txt

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-2.0.txt README.md

%changelog
* Sun Nov 08 2015 Liu Di <liudidi@gmail.com> - 2.4.1-4
- 为 Magic 3.0 重建

* Fri Oct 30 2015 Liu Di <liudidi@gmail.com> - 2.4.1-3
- 为 Magic 3.0 重建

* Thu Aug 14 2014 Liu Di <liudidi@gmail.com> - 2.4.1-2
- 为 Magic 3.0 重建

* Wed Jul 02 2014 gil cattaneo <puntogil@libero.it> 2.4.1-1
- initial rpm
