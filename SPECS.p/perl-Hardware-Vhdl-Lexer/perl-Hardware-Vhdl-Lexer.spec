Name:           perl-Hardware-Vhdl-Lexer
Version:        1.00
Release:        18%{?dist}
Summary:        Split VHDL code into lexical tokens
License:        GPL+ or Artistic

Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Hardware-Vhdl-Lexer/
Source0:        http://www.cpan.org/authors/id/M/MY/MYKL/Hardware-Vhdl-Lexer-%{version}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  perl(Class::Std)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Readonly) >= 1.03
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::Pod)

Requires:       perl(Readonly) >= 1.03
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# %%dir %%{perl_vendorlib}/Hardware/Vhdl/ is owned by perl-Hardware-Vhdl-Parser
Requires:       perl-Hardware-Vhdl-Parser


%description
Hardware::Vhdl::Lexer splits VHDL code into lexical tokens. To use it, you
need to first create a lexer object, passing in something which will supply
chunks of VHDL code to the lexer. Repeated calls to the get_next_token
method of the lexer will then return VHDL tokens (in scalar context) or a
token type code and the token (in list context). get_next_token returns
undef when there are no more tokens to be read.


%prep
%setup -q -n Hardware-Vhdl-Lexer-%{version}

# rpmlint : line endings spurious-executable-perm
for i in Changes README lib/Hardware/Vhdl/Lexer.pm ; do
  echo "Fixing wrong-file-end-of-line-encoding : $i"
  %{__sed} 's/\r//' $i > $i.rpmlint
  touch -r $i $i.rpmlint;
  %{__mv} $i.rpmlint $i
  echo "Fixing perms : $i"
  chmod 0644 $i
done

# workaround for bug in rpmbuild
# disables the Requires of modules in commented code
%{__sed} "s|use regexp-generating|#use regexp-generating|" \
  lib/Hardware/Vhdl/Lexer.pm > Lexer.pm
touch -r lib/Hardware/Vhdl/Lexer.pm Lexer.pm;
%{__mv} Lexer.pm lib/Hardware/Vhdl/Lexer.pm

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*


%check



%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/Hardware/Vhdl/Lexer.pm
%{_mandir}/man3/*

%changelog
* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 1.00-18
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 1.00-17
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.00-16
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.00-15
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.00-14
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.00-13
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 1.00-12
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 1.00-11
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.00-9
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 17 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.00-7
- 661697 rebuild for fixing problems with vendorach/lib

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.00-6
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.00-5
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Dec 21 2008 Chitlesh GOORAH <chitlesh [AT] fedoraproject DOT org> 1.00-2
- updated as suggestion on review RHBZ 477515#c2

* Sun Dec 14 2008 Chitlesh GOORAH <chitlesh [AT] fedoraproject DOT org> 1.00-1
- Specfile autogenerated by cpanspec 1.77.
