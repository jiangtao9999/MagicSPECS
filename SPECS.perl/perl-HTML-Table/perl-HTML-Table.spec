Name:           perl-HTML-Table
Version:        2.08a
Release:        13%{?dist}
Summary:        Create HTML tables using simple interface
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/HTML-Table/
Source0:        http://www.cpan.org/modules/by-module/HTML/HTML-Table-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))


%description
HTML::Table is used to generate HTML tables for CGI scripts.  By using the
methods provided fairly complex tables can be created, manipulated, then
 printed from Perl scripts.  The module also greatly simplifies creating
tables within tables from Perl.  It is possible to create an entire table
using the methods provided and never use an HTML tag.

HTML::Table also allows for creating dynamically sized tables via its addRow
and addCol methods.  These methods automatically resize the table if passed
more cell values than will fit in the current table grid.

Methods are provided for nearly all valid table, row, and cell tags specified
for HTML 3.0.


%prep
%setup -q -n HTML-Table-%{version}
for f in Changes lib/HTML/Table.pm
do
   iconv -f ISO-8859-1 -t UTF-8 -o ${f}.UTF-8 $f
   mv ${f}.UTF-8 $f
done


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check



%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 2.08a-13
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 2.08a-12
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 2.08a-11
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 2.08a-10
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.08a-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 15 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.08a-8
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.08a-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 17 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.08a-6
- 661697 rebuild for fixing problems with vendorach/lib

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.08a-5
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 2.08a-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.08a-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.08a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Sep 4 2008 Orion Poplawski <orion@cora.nwra.com> 2.08a-1
- Update to 2.08a

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.07b-2
Rebuild for new perl

* Wed Feb 27 2008 Orion Poplawski <orion@cora.nwra.com> 2.07b-1
- Update to 2.07b

* Tue Nov 20 2007 Orion Poplawski <orion@cora.nwra.com> 2.07-0.b2
- Update to 2.07-b2

* Tue Oct 16 2007 Tom "spot" Callaway <tcallawa@redhat.com> 2.05-1.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Thu May 17 2007 Orion Poplawski <orion@cora.nwra.com> 2.05-1
- Update to 2.05

* Tue Nov  7 2006 Orion Poplawski <orion@cora.nwra.com> 2.04a-1
- Update to 2.04a

* Wed Oct 12 2005 Orion Poplawski <orion@cora.nwra.com> 2.02-1
- Specfile autogenerated.
