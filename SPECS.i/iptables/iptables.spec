# enable systemd for Fedora-16 and RHEL-7
%bcond_without systemd

# install init scripts to /usr/libexec with systemd
%if %{with systemd}
    %define script_path %{_libexecdir}
%else
    %define script_path /etc/rc.d/init.d
%endif

Name: iptables
Summary: Tools for managing Linux kernel packet filtering capabilities
Version: 1.4.12.2
Release: 5%{?dist}
Source: http://www.netfilter.org/projects/iptables/files/%{name}-%{version}.tar.bz2
Source1: iptables.init
Source2: iptables-config
Source3: iptables.service
Patch5: iptables-1.4.11-cloexec.patch
Group: System Environment/Base
URL: http://www.netfilter.org/
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
License: GPLv2
BuildRequires: kernel-headers
Conflicts: kernel < 2.4.20
%if %{with systemd}
BuildRequires: systemd-units
Requires(post): systemd-units
Requires(post): systemd-sysv
Requires(preun): systemd-units
Requires(postun): systemd-units
Conflicts: systemd < 38
Conflicts: filesystem < 3
%else
Requires(post): chkconfig
Requires(preun): chkconfig
%endif
# provide also ipv6 sub package
Provides: %{name}-ipv6 = %{version}-%{release}
Obsoletes: %{name}-ipv6 < %{version}-%{release}

%ifarch x86_64
Provides: libxtables.so.6()(64bit)
%else
Provides: libxtables.so.6
%endif


%description
The iptables utility controls the network packet filtering code in the
Linux kernel. If you need to set up firewalls and/or IP masquerading,
you should install this package.

%package devel
Summary: Development package for iptables
Group: System Environment/Base
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
iptables development headers and libraries.

The iptc interface is upstream marked as not public. The interface is not 
stable and may change with every new version. It is therefore unsupported.

%prep
%setup -q
%patch5 -p1 -b .cloexec

%build
CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing " \
./configure --enable-devel --enable-libipq --bindir=%{_bindir} --sbindir=%{_sbindir} --sysconfdir=/etc --libdir=%{_libdir} --libexecdir=%{_libdir} --mandir=%{_mandir} --includedir=%{_includedir} --with-kernel=/usr --with-kbuild=/usr --with-ksource=/usr

# do not use rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

rm -f include/linux/types.h

make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make install DESTDIR=%{buildroot} 
# remove la file(s)
rm -f %{buildroot}/%{_libdir}/*.la

# install ip*tables.h header files
install -m 644 include/ip*tables.h %{buildroot}%{_includedir}/
install -d -m 755 %{buildroot}%{_includedir}/iptables
install -m 644 include/iptables/internal.h %{buildroot}%{_includedir}/iptables/

# install ipulog header file
install -d -m 755 %{buildroot}%{_includedir}/libipulog/
install -m 644 include/libipulog/*.h %{buildroot}%{_includedir}/libipulog/

# install init scripts and configuration files
install -d -m 755 %{buildroot}%{script_path}
install -c -m 755 %{SOURCE1} %{buildroot}%{script_path}/iptables.init
sed -e 's;iptables;ip6tables;g' -e 's;IPTABLES;IP6TABLES;g' < %{SOURCE1} > ip6tables.init
install -c -m 755 ip6tables.init %{buildroot}%{script_path}/ip6tables.init
install -d -m 755 %{buildroot}/etc/sysconfig
install -c -m 755 %{SOURCE2} %{buildroot}/etc/sysconfig/iptables-config
sed -e 's;iptables;ip6tables;g' -e 's;IPTABLES;IP6TABLES;g' < %{SOURCE2} > ip6tables-config
install -c -m 755 ip6tables-config %{buildroot}/etc/sysconfig/ip6tables-config

%if %{with systemd}
# install systemd service files
install -d -m 755 %{buildroot}/%{_unitdir}
install -c -m 755 %{SOURCE3} %{buildroot}/%{_unitdir}
sed -e 's;iptables;ip6tables;g' -e 's;IPv4;IPv6;g' < %{SOURCE3} > ip6tables.service
install -c -m 755 ip6tables.service %{buildroot}/%{_unitdir}
%endif

magic_rpm_clean.sh

%clean
rm -rf %{buildroot}

%if %{with systemd}

%post
/usr/sbin/ldconfig
if [ $1 -eq 1 ] ; then # Initial installation
   /usr/bin/systemctl daemon-reload >/dev/null 2>&1 || :
%if 0%{?fedora} < 17 && 0%{?rhel} < 7
   /usr/bin/systemctl enable iptables.service >/dev/null 2>&1 || :
   /usr/bin/systemctl enable ip6tables.service >/dev/null 2>&1 || :
%endif
fi

%preun
if [ $1 -eq 0 ]; then # Package removal, not upgrade
   /usr/bin/systemctl --no-reload disable iptables.service > /dev/null 2>&1 || :
   /usr/bin/systemctl --no-reload disable ip6tables.service > /dev/null 2>&1 || :
   /usr/bin/systemctl stop iptables.service > /dev/null 2>&1 || :
   /usr/bin/systemctl stop ip6tables.service > /dev/null 2>&1 || :
fi

%postun
/usr/sbin/ldconfig
/usr/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then # Package upgrade, not uninstall
   /usr/bin/systemctl try-restart iptables.service >/dev/null 2>&1 || :
   /usr/bin/systemctl try-restart ip6tables.service >/dev/null 2>&1 || :
fi

%triggerun -- iptables < 1.4.11.1-3
# To apply saved runlevel, use systemd-sysv-convert --apply iptables
%{_bindir}/systemd-sysv-convert --save iptables >/dev/null 2>&1 ||:

# Autostart
%if 0%{?fedora} < 17 && 0%{?rhel} < 7
/usr/bin/systemctl --no-reload enable iptables.service >/dev/null 2>&1 ||:
%endif

# Delete from sysv management, try to restart service
/usr/sbin/chkconfig --del iptables >/dev/null 2>&1 || :
/usr/bin/systemctl try-restart iptables.service >/dev/null 2>&1 || :

%triggerun -- iptables-ipv6 < 1.4.11.1-3
# To apply saved runlevel, use systemd-sysv-convert --apply iptables
%{_bindir}/systemd-sysv-convert --save ip6tables >/dev/null 2>&1 ||:

# Autostart
%if 0%{?fedora} < 17 && 0%{?rhel} < 7
/usr/bin/systemctl --no-reload enable ip6tables.service >/dev/null 2>&1 ||:
%endif

# Delete from sysv management, try to restart service
/usr/sbin/chkconfig --del ip6tables >/dev/null 2>&1 || :
/usr/bin/systemctl try-restart ip6tables.service >/dev/null 2>&1 || :

%else # no systemd

%post
/usr/sbin/ldconfig
/usr/sbin/chkconfig --add iptables
/usr/sbin/chkconfig --add ip6tables

%preun
if [ $1 -eq 0 ]; then
   /usr/sbin/chkconfig --del iptables
   /usr/sbin/chkconfig --del ip6tables
fi

%postun -p /usr/sbin/ldconfig

%endif # systemd


%files
%defattr(-,root,root)
%doc COPYING INSTALL INCOMPATIBILITIES
%attr(0755,root,root) %{script_path}/iptables.init
%attr(0755,root,root) %{script_path}/ip6tables.init
%config(noreplace) %attr(0600,root,root) /etc/sysconfig/iptables-config
%config(noreplace) %attr(0600,root,root) /etc/sysconfig/ip6tables-config
%if %{with systemd}
%{_unitdir}/iptables.service
%{_unitdir}/ip6tables.service
%endif
%{_sbindir}/iptables*
%{_sbindir}/ip6tables*
%{_sbindir}/xtables-multi
%{_bindir}/iptables-xml
%{_mandir}/man1/iptables-xml*
%{_mandir}/man8/iptables*
%{_mandir}/man8/ip6tables*
%dir %{_libdir}/xtables
%{_libdir}/xtables/libipt*
%{_libdir}/xtables/libip6t*
%{_libdir}/xtables/libxt*
%{_libdir}/libip*tc.so.*
%{_libdir}/libipq.so.*
%{_libdir}/libxtables.so.*

%files devel
%defattr(-,root,root)
%dir %{_includedir}/iptables
%{_includedir}/iptables/*.h
%{_includedir}/*.h
%dir %{_includedir}/libiptc
%{_includedir}/libiptc/*.h
%dir %{_includedir}/libipulog
%{_includedir}/libipulog/*.h
%{_mandir}/man3/*
%{_libdir}/libip*tc.so
%{_libdir}/libipq.so
%{_libdir}/libxtables.so
%{_libdir}/pkgconfig/libipq.pc
%{_libdir}/pkgconfig/libiptc.pc
%{_libdir}/pkgconfig/libip4tc.pc
%{_libdir}/pkgconfig/libip6tc.pc
%{_libdir}/pkgconfig/xtables.pc

%changelog
* Fri Dec 07 2012 Liu Di <liudidi@gmail.com> - 1.4.12.2-5
- 为 Magic 3.0 重建

* Wed Feb 29 2012 Harald Hoyer <harald@redhat.com> 1.4.12.2-4
- install everything in /usr
  https://fedoraproject.org/wiki/Features/UsrMove

* Thu Feb 16 2012 Thomas Woerner <twoerner@redhat.com> 1.4.12.2-3
- fixed auto enable check for Fedora > 16 and added rhel > 6 check

* Wed Feb 15 2012 Thomas Woerner <twoerner@redhat.com> 1.4.12.2-2
- disabled autostart and auto enable for iptables.service and ip6tables.service
  for Fedora > 16

* Mon Jan 16 2012 Thomas Woerner <twoerner@redhat.com> 1.4.12.2-1
- new version 1.4.12.2 with new pkgconfig/libip4tc.pc and pkgconfig/libip6tc.pc
  - build: make check stage not fail when building statically
  - build: restore build order of modules
  - build: scan for unreferenced symbols
  - build: sort file list before build
  - doc: clarification on the meaning of -p 0
  - doc: document iptables-restore's -T option
  - doc: fix undesired newline in ip6tables-restore(8)
  - ip6tables-restore: implement missing -T option
  - iptables: move kernel version find routing into libxtables
  - libiptc: provide separate pkgconfig files
  - libipt_SAME: set PROTO_RANDOM on all ranges
  - libxtables: Fix file descriptor leak in xtables_lmap_init on error
  - libxt_connbytes: fix handling of --connbytes FROM
  - libxt_CONNSECMARK: fix spacing in output
  - libxt_conntrack: improve error message on parsing violation
  - libxt_NFQUEUE: fix --queue-bypass ipt-save output
  - libxt_RATEEST: link with -lm
  - libxt_statistic: link with -lm
  - Merge branch 'stable'
  - Merge branch 'stable' of git://dev.medozas.de/iptables
  - nfnl_osf: add missing libnfnetlink_CFLAGS to compile process
  - xtoptions: fill in fallback value for nvals
  - xtoptions: simplify xtables_parse_interface

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 12 2011 Thomas Woerner <twoerner@redhat.com> 1.4.12.1-1
- new version 1.4.12.1 with new pkgconfig/libipq.pc
  - build: abort autogen on subcommand failure
  - build: strengthen check for overlong lladdr components
  - build: workaround broken linux-headers on RHEL-5
  - doc: clarify libxt_connlimit defaults
  - doc: fix typo in libxt_TRACE
  - extensions: use multi-target registration
  - libip6t_dst: restore setting IP6T_OPTS_LEN flag
  - libip6t_frag: restore inversion support
  - libip6t_hbh: restore setting IP6T_OPTS_LEN flag
  - libipq: add pkgconfig file
  - libipt_ttl: document that negation is available
  - libxt_conntrack: fix --ctproto 0 output
  - libxt_conntrack: remove one misleading comment
  - libxt_dccp: fix deprecated intrapositional ordering of !
  - libxt_dccp: fix random output of ! on --dccp-option
  - libxt_dccp: provide man pages options in short help too
  - libxt_dccp: restore missing XTOPT_INVERT tags for options
  - libxt_dccp: spell out option name on save
  - libxt_dscp: restore inversion support
  - libxt_hashlimit: default htable-expire must be in milliseconds
  - libxt_hashlimit: observe new default gc-expire time when saving
  - libxt_hashlimit: remove inversion from hashlimit rev 0
  - libxt_owner: restore inversion support
  - libxt_physdev: restore inversion support
  - libxt_policy: remove superfluous inversion
  - libxt_set: put differing variable names in directly
  - libxt_set: update man page about kernel support on the feature
  - libxt_string: define _GNU_SOURCE for strnlen
  - libxt_string: escape the escaping char too
  - libxt_string: fix space around arguments
  - libxt_string: replace hex codes by char equivalents
  - libxt_string: simplify hex output routine
  - libxt_tcp: always print the mask parts
  - libxt_TCPMSS: restore build with IPv6-less libcs
  - libxt_TOS: update linux kernel version list for backported fix
  - libxt_u32: fix missing allowance for inversion
  - src: remove unused IPTABLES_MULTI define
  - tests: add negation tests for libxt_statistic
  - xtoptions: flag use of XTOPT_POINTER without XTOPT_PUT
- removed include/linux/types.h before build to be able to compile

* Tue Jul 26 2011 Thomas Woerner <twoerner@redhat.com> 1.4.12-2
- dropped temporary provide again

* Tue Jul 26 2011 Thomas Woerner <twoerner@redhat.com> 1.4.12-1.1
- added temporary provides for libxtables.so.6 to be able to rebuild iproute,
  which is part of the standard build environment

* Mon Jul 25 2011 Thomas Woerner <twoerner@redhat.com> 1.4.12-1
- new version 1.4.12 with support of all new features of kernel 3.0
  - build: attempt to fix building under Linux 2.4
  - build: bump soversion for recent data structure change
  - build: install modules in arch-dependent location
  - doc: fix group range in libxt_NFLOG's man
  - doc: fix version string in ip6tables.8
  - doc: include matches/targets in manpage again
  - doc: mention multiple verbosity flags
  - doc: the -m option cannot be inverted
  - extensions: support for per-extension instance global variable space
  - iptables-apply: select default rule file depending on call name
  - iptables: consolidate target/match init call
  - iptables: Coverity: DEADCODE
  - iptables: Coverity: NEGATIVE_RETURNS
  - iptables: Coverity: RESOURCE_LEAK
  - iptables: Coverity: REVERSE_INULL
  - iptables: Coverity: VARARGS
  - iptables: restore negation for -f
  - libip6t_HL: fix option names from ttl -> hl
  - libipt_LOG: fix ignoring all but last flags
  - libxtables: ignore whitespace in the multiaddress argument parser
  - libxtables: properly reject empty hostnames
  - libxtables: set clone's initial data to NULL
  - libxt_conntrack: move more data into the xt_option_entry
  - libxt_conntrack: restore network-byte order for v1,v2
  - libxt_hashlimit: use a more obvious expiry value by default
  - libxt_rateest: abolish global variables
  - libxt_RATEEST: abolish global variables
  - libxt_RATEEST: fix userspacesize field
  - libxt_RATEEST: use guided option parser
  - libxt_state: fix regression about inversion of main option
  - option: remove last traces of intrapositional negation
- complete changelog:
  http://www.netfilter.org/projects/iptables/files/changes-iptables-1.4.12.txt

* Thu Jul 21 2011 Thomas Woerner <twoerner@redhat.com> 1.4.11.1-4
- merged ipv6 sub package into main package
- renamed init scripts to /usr/libexec/ip*tables.init

* Fri Jul 15 2011 Thomas Woerner <twoerner@redhat.com> 1.4.11.1-3
- added support for native systemd file (rhbz#694738)
  - new iptables.service file
  - additional requires
  - moved sysv init scripts to /usr/libexec
  - added new post, preun and postun scripts and triggers

* Tue Jul 12 2011 Thomas Woerner <twoerner@redhat.com> 1.4.11.1-2
- dropped temporary provide again
- enabled smp build

* Tue Jul 12 2011 Thomas Woerner <twoerner@redhat.com> 1.4.11.1-1.1
-  added temporary provides for libxtables.so.5 to be able to rebuild iproute,
   which is part of the standard build environment

* Mon Jul 11 2011 Thomas Woerner <twoerner@redhat.com> 1.4.11.1-1
- new version 1.4.11.1, bug and doc fix release for 1.4.11

* Tue Jun  7 2011 Thomas Woerner <twoerner@redhat.com> 1.4.11-1
- new version 1.4.11 with all new features of 2.6.37-39 (not usable)
  - lots of changes and bugfixes for base and extensions
  - complete changelog:
    http://www.netfilter.org/projects/iptables/files/changes-iptables-1.4.11.txt

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 10 2011 Thomas Woerner <twoerner@redhat.com> 1.4.10-1
- new version 1.4.10 with all new features of 2.6.36
  - all: consistent syntax use in struct option
  - build: fix static linking
  - doc: let man(1) autoalign the text in xt_cpu
  - doc: remove extra empty line from xt_cpu
  - doc: minimal spelling updates to xt_cpu
  - doc: consistent use of markup
  - extensions: libxt_quota: don't ignore the quota value on deletion
  - extensions: REDIRECT: add random help
  - extensions: add xt_cpu match
  - extensions: add idletimer xt target extension
  - extensions: libxt_IDLETIMER: use xtables_param_act when checking options
  - extensions: libxt_CHECKSUM extension
  - extensions: libipt_LOG/libip6t_LOG: support macdecode option
  - extensions: fix compilation of the new CHECKSUM target
  - extensions: libxt_ipvs: user-space lib for netfilter matcher xt_ipvs
  - iptables-xml: resolve compiler warnings
  - iptables: limit chain name length to be consistent with targets
  - libiptc: add Libs.private to pkgconfig files
  - libiptc: build with -Wl,--no-as-needed
  - xtables: remove unnecessary cast
- dropped xt_CHECKSUM, added upstream

* Tue Oct 12 2010 Thomas Woerner <twoerner@redhat.com> 1.4.9-2
- added xt_CHECKSUM patch from Michael S. Tsirkin (rhbz#612587)

* Wed Aug  4 2010 Thomas Woerner <twoerner@redhat.com> 1.4.9-1
- new version 1.4.9 with all new features of 2.6.35
  - doc: xt_hashlimit: fix a typo
  - doc: xt_LED: nroff formatting requirements
  - doc: xt_string: correct copy-and-pasting in manpage
  - extensions: add the LED target
  - extensions: libxt_quota.c: Support option negation
  - extensions: libxt_rateest: fix bps options for iptables-save
  - extensions: libxt_rateest: fix typo in the man page
  - extensions: REDIRECT: add random help
  - includes: sync header files from Linux 2.6.35-rc1
  - libxt_conntrack: do print netmask
  - libxt_hashlimit: always print burst value
  - libxt_set: new revision added
  - utils: add missing include flags to Makefile
  - xtables: another try at chain name length checking
  - xtables: remove xtables_set_revision function
  - xt_quota: also document negation
  - xt_sctp: Trace DATA chunk that supports SACK-IMMEDIATELY extension
  - xt_sctp: support FORWARD_TSN chunk type

* Fri Jul  2 2010 Thomas Woerner <twoerner@redhat.com> 1.4.8-1
- new version 1.4.8 all new features of 2.6.34 (rhbz#)
  - extensions: REDIRECT: fix --to-ports parser
  - iptables: add noreturn attribute to exit_tryhelp()
  - extensions: MASQUERADE: fix --to-ports parser
  - libxt_comment: avoid use of IPv4-specific examples
  - libxt_CT: add a manpage
  - iptables: correctly check for too-long chain/target/match names
  - doc: libxt_MARK: no longer restricted to mangle table
  - doc: remove claim that TCPMSS is limited to mangle
  - libxt_recent: add a missing space in output
  - doc: add manpage for libxt_osf
  - libxt_osf: import nfnl_osf program
  - extensions: add support for xt_TEE
  - CT: fix --ctevents parsing
  - extensions: add CT extension
  - libxt_CT: print conntrack zone in ->print/->save
  - xtables: fix compilation when debugging is enabled
  - libxt_conntrack: document --ctstate UNTRACKED
  - iprange: fix xt_iprange v0 parsing

* Wed Mar 24 2010 Thomas Woerner <twoerner@redhat.com> 1.4.7-2
- added default values for IPTABLES_STATUS_VERBOSE and
  IPTABLES_STATUS_LINENUMBERS in init script
- added missing lsb keywords Required-Start and Required-Stop to init script

* Fri Mar  5 2010 Thomas Woerner <twoerner@redhat.com> 1.4.7-1
- new version 1.4.7 with support for all new features of 2.6.33 (rhbz#570767)
  - libip4tc: Add static qualifier to dump_entry()
  - libipq: build as shared library
  - recent: reorder cases in code (cosmetic cleanup)
  - several man page and documentation fixes
  - policy: fix error message showing wrong option
  - includes: header updates
  - Lift restrictions on interface names
- fixed license and moved iptables-xml into base package according to review

* Wed Jan 27 2010 Thomas Woerner <twoerner@redhat.com> 1.4.6-2
- moved libip*tc and libxtables libs to /lib[64], added symlinks for .so libs
  to /usr/lib[64] for compatibility (rhbz#558796)

* Wed Jan 13 2010 Thomas Woerner <twoerner@redhat.com> 1.4.6-1
- new version 1.4.6 with support for all new features of 2.6.32
  - several man page fixes
  - Support for nommu arches
  - realm: remove static initializations
  - libiptc: remove unused functions
  - libiptc: avoid strict-aliasing warnings
  - iprange: do accept non-ranges for xt_iprange v1
  - iprange: warn on reverse range
  - iprange: roll address parsing into a loop
  - iprange: do accept non-ranges for xt_iprange v1 (log)
  - iprange: warn on reverse range (log)
  - libiptc: fix wrong maptype of base chain counters on restore
  - iptables: fix undersized deletion mask creation
  - style: reduce indent in xtables_check_inverse
  - libxtables: hand argv to xtables_check_inverse
  - iptables/extensions: make bundled options work again
  - CONNMARK: print mark rules with mask 0xffffffff as set instead of xset
  - iptables: take masks into consideration for replace command
  - doc: explain experienced --hitcount limit
  - doc: name resolution clarification
  - iptables: expose option to zero packet/byte counters for a specific rule
  - build: restore --disable-ipv6 functionality on system w/o v6 headers
  - MARK: print mark rules with mask 0xffffffff as --set-mark instead of --set-xmark
  - DNAT: fix incorrect check during parsing
  - extensions: add osf extension
  - conntrack: fix --expires parsing

* Thu Dec 17 2009 Thomas Woerner <twoerner@redhat.com> 1.4.5-2
- dropped nf_ext_init remains from cloexec patch

* Thu Sep 17 2009 Thomas Woerner <twoerner@redhat.com> 1.4.5-1
- new version 1.4.5 with support for all new features of 2.6.31
  - libxt_NFQUEUE: add new v1 version with queue-balance option
  - xt_conntrack: revision 2 for enlarged state_mask member
  - libxt_helper: fix invalid passed option to check_inverse
  - libiptc: split v4 and v6
  - extensions: collapse registration structures
  - iptables: allow for parse-less extensions
  - iptables: allow for help-less extensions
  - extensions: remove empty help and parse functions
  - xtables: add multi-registration functions
  - extensions: collapse data variables to use multi-reg calls
  - xtables: warn of missing version identifier in extensions
  - multi binary: allow subcommand via argv[1]
  - iptables: accept multiple IP address specifications for -s, -d
  - several build fixes
  - several man page fixes
- fixed two leaked file descriptors on sockets (rhbz#521397)

* Mon Aug 24 2009 Thomas Woerner <twoerner@redhat.com> 1.4.4-1
- new version 1.4.4 with support for all new features of 2.6.30
  - several man page fixes
  - iptables: replace open-coded sizeof by ARRAY_SIZE
  - libip6t_policy: remove redundant functions
  - policy: use direct xt_policy_info instead of ipt/ip6t
  - policy: merge ipv6 and ipv4 variant
  - extensions: add `cluster' match support
  - extensions: add const qualifiers in print/save functions
  - extensions: use NFPROTO_UNSPEC for .family field
  - extensions: remove redundant casts
  - iptables: close open file descriptors
  - fix segfault if incorrect protocol name is used
  - replace open-coded sizeof by ARRAY_SIZE
  - do not include v4-only modules in ip6tables manpage
  - use direct xt_policy_info instead of ipt/ip6t
  - xtables: fix segfault if incorrect protocol name is used
  - libxt_connlimit: initialize v6_mask
  - SNAT/DNAT: add support for persistent multi-range NAT mappings

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 15 2009 Thomas Woerner <twoerner@redhat.com> 1.4.3.2-1
- new version 1.4.3.2
- also install iptables/internal.h, needed for iptables.h and ip6tables.h

* Mon Mar 30 2009 Thomas Woerner <twoerner@redhat.com> 1.4.3.1-1
- new version 1.4.3.1
  - libiptc is now shared
  - supports all new features of the 2.6.29 kernel
- dropped typo_latter patch

* Thu Mar  5 2009 Thomas Woerner <twoerner@redhat.com> 1.4.2-3
- still more review fixes (rhbz#225906)
  - consistent macro usage
  - use sed instead of perl for rpath removal
  - use standard RPM CFLAGS, but also -fno-strict-aliasing (needed for libiptc*)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Thomas Woerner <twoerner@redhat.com> 1.4.2-1
- new version 1.4.2
- removed TOS value mask patch (upstream)
- more review fixes (rhbz#225906)
- install all header files (rhbz#462207)
- dropped nf_ext_init (rhbz#472548)

* Tue Jul 22 2008 Thomas Woerner <twoerner@redhat.com> 1.4.1.1-2
- fixed TOS value mask problem (rhbz#456244) (upstream patch)
- two more cloexec fixes

* Tue Jul  1 2008 Thomas Woerner <twoerner@redhat.com> 1.4.1.1-1
- upstream bug fix release 1.4.1.1
- dropped extra patch for 1.4.1 - not needed anymore

* Tue Jun 10 2008 Thomas Woerner <twoerner@redhat.com> 1.4.1-1
- new version 1.4.1 with new build environment
- additional ipv6 network mask patch from Jan Engelhardt
- spec file cleanup
- removed old patches

* Fri Jun  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.4.0-5
- use normal kernel headers, not linux/compiler.h
- change BuildRequires: kernel-devel to kernel-headers
- We need to do this to be able to build for both sparcv9 and sparc64 
  (there is no kernel-devel.sparcv9)

* Thu Mar 20 2008 Thomas Woerner <twoerner@redhat.com> 1.4.0-4
- use O_CLOEXEC for all opened files in all applications (rhbz#438189)

* Mon Mar  3 2008 Thomas Woerner <twoerner@redhat.com> 1.4.0-3
- use the kernel headers from the build tree for iptables for now to be able to 
  compile this package, but this makes the package more kernel dependant
- use s6_addr32 instead of in6_u.u6_addr32

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.4.0-2
- Autorebuild for GCC 4.3

* Mon Feb 11 2008 Thomas Woerner <twoerner@redhat.com> 1.4.0-1
- new version 1.4.0
- fixed condrestart (rhbz#428148)
- report the module in rmmod_r if there is an error
- use nf_ext_init instead of my_init for extension constructors

* Mon Nov  5 2007 Thomas Woerner <twoerner@redhat.com> 1.3.8-6
- fixed leaked file descriptor before fork/exec (rhbz#312191)
- blacklisting is not working, use "install X /bin/(true|false)" test instead
- return private exit code 150 for disabled ipv6 support
- use script name for output messages

* Tue Oct 16 2007 Thomas Woerner <twoerner@redhat.com> 1.3.8-5
- fixed error code for stopping a already stopped firewall (rhbz#321751)
- moved blacklist test into start

* Wed Sep 26 2007 Thomas Woerner <twoerner@redhat.com> 1.3.8-4.1
- do not start ip6tables if ipv6 is blacklisted (rhbz#236888)
- use simpler fix for (rhbz#295611)
  Thanks to Linus Torvalds for the patch.

* Mon Sep 24 2007 Thomas Woerner <twoerner@redhat.com> 1.3.8-4
- fixed IPv6 reject type (rhbz#295181)
- fixed init script: start, stop and status
- support netfilter compiled into kernel in init script (rhbz#295611)
- dropped inversion for limit modules from man pages (rhbz#220780)
- fixed typo in ip6tables man page (rhbz#236185)

* Wed Sep 19 2007 Thomas Woerner <twoerner@redhat.com> 1.3.8-3
- do not depend on local_fs in lsb header - this delayes start after network
- fixed exit code for initscript usage

* Mon Sep 17 2007 Thomas Woerner <twoerner@redhat.com> 1.3.8-2.1
- do not use lock file for condrestart test

* Thu Aug 23 2007 Thomas Woerner <twoerner@redhat.com> 1.3.8-2
- fixed initscript for LSB conformance (rhbz#246953, rhbz#242459)
- provide iptc interface again, but unsupported (rhbz#216733)
- compile all extension, which are supported by the kernel-headers package
- review fixes (rhbz#225906)

* Tue Jul 31 2007 Thomas Woerner <twoerner@redhat.com>
- reverted ipv6 fix, because it disables the ipv6 at all (rhbz#236888)

* Fri Jul 13 2007 Steve Conklin <sconklin@redhat.com> - 1.3.8-1
- New version 1.3.8

* Mon Apr 23 2007 Jeremy Katz <katzj@redhat.com> - 1.3.7-2
- fix error when ipv6 support isn't loaded in the kernel (#236888)

* Wed Jan 10 2007 Thomas Woerner <twoerner@redhat.com> 1.3.7-1.1
- fixed installation of secmark modules

* Tue Jan  9 2007 Thomas Woerner <twoerner@redhat.com> 1.3.7-1
- new verison 1.3.7
- iptc is not a public interface and therefore not installed anymore
- dropped upstream secmark patch

* Thu Sep 19 2006 Thomas Woerner <twoerner@redhat.com> 1.3.5-2
- added secmark iptables patches (#201573)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.3.5-1.2.1
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.3.5-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.3.5-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Thu Feb  2 2006 Thomas Woerner <twoerner@redhat.com> 1.3.5-1
- new version 1.3.5
- fixed init script to set policy for raw tables, too (#179094)

* Tue Jan 24 2006 Thomas Woerner <twoerner@redhat.com> 1.3.4-3
- added important iptables header files to devel package

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Nov 25 2005 Thomas Woerner <twoerner@redhat.com> 1.3.4-2
- fix for plugin problem: link with "gcc -shared" instead of "ld -shared" and 
  replace "_init" with "__attribute((constructor)) my_init"

* Fri Nov 25 2005 Thomas Woerner <twoerner@redhat.com> 1.3.4-1.1
- rebuild due to unresolved symbols in shared libraries

* Fri Nov 18 2005 Thomas Woerner <twoerner@redhat.com> 1.3.4-1
- new version 1.3.4
- dropped free_opts patch (upstream fixed)
- made libipq PIC (#158623)
- additional configuration options for iptables startup script (#172929)
  Thanks to Jan Gruenwald for the patch
- spec file cleanup (dropped linux_header define and usage)

* Mon Jul 18 2005 Thomas Woerner <twoerner@redhat.com> 1.3.2-1
- new version 1.3.2 with additional patch for the misplaced free_opts call
  from Marcus Sundberg

* Wed May 11 2005 Thomas Woerner <twoerner@redhat.com> 1.3.1-1
- new version 1.3.1

* Fri Mar 18 2005 Thomas Woerner <twoerner@redhat.com> 1.3.0-2
- Remove unnecessary explicit kernel dep (#146142)
- Fixed out of bounds accesses (#131848): Thanks to Steve Grubb
  for the patch
- Adapted iptables-config to reference to modprobe.conf (#150143)
- Remove misleading message (#140154): Thanks to Ulrich Drepper
  for the patch

* Mon Feb 21 2005 Thomas Woerner <twoerner@redhat.com> 1.3.0-1
- new version 1.3.0

* Thu Nov 11 2004 Thomas Woerner <twoerner@redhat.com> 1.2.11-3.2
- fixed autoload problem in iptables and ip6tables (CAN-2004-0986)

* Fri Sep 17 2004 Thomas Woerner <twoerner@redhat.com> 1.2.11-3.1
- changed default behaviour for IPTABLES_STATUS_NUMERIC to "yes" (#129731)
- modified config file to match this change and un-commented variables with
  default values

* Thu Sep 16 2004 Thomas Woerner <twoerner@redhat.com> 1.2.11-3
- applied second part of cleanup patch from (#131848): thanks to Steve Grubb
  for the patch

* Wed Aug 25 2004 Thomas Woerner <twoerner@redhat.com> 1.2.11-2
- fixed free bug in iptables (#128322)

* Tue Jun 22 2004 Thomas Woerner <twoerner@redhat.com> 1.2.11-1
- new version 1.2.11

* Thu Jun 17 2004 Thomas Woerner <twoerner@redhat.com> 1.2.10-1
- new version 1.2.10

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Feb 26 2004 Thomas Woerner <twoerner@redhat.com> 1.2.9-2.3
- fixed iptables-restore -c fault if there are no counters (#116421)

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Sun Jan  25 2004 Dan Walsh <dwalsh@redhat.com> 1.2.9-1.2
- Close File descriptors to prevent SELinux error message

* Wed Jan  7 2004 Thomas Woerner <twoerner@redhat.com> 1.2.9-1.1
- rebuild

* Wed Dec 17 2003 Thomas Woerner <twoerner@redhat.com> 1.2.9-1
- vew version 1.2.9
- new config options in ipXtables-config:
  IPTABLES_MODULES_UNLOAD
- more documentation in ipXtables-config
- fix for netlink security issue in libipq (devel package)
- print fix for libipt_icmp (#109546)

* Thu Oct 23 2003 Thomas Woerner <twoerner@redhat.com> 1.2.8-13
- marked all messages in iptables init script for translation (#107462)
- enabled devel package (#105884, #106101)
- bumped build for fedora for libipt_recent.so (#106002)

* Tue Sep 23 2003 Thomas Woerner <twoerner@redhat.com> 1.2.8-12.1
- fixed lost udp port range in ip6tables-save (#104484)
- fixed non numeric multiport port output in ipXtables-savs

* Mon Sep 22 2003 Florian La Roche <Florian.LaRoche@redhat.de> 1.2.8-11
- do not link against -lnsl

* Wed Sep 17 2003 Thomas Woerner <twoerner@redhat.com> 1.2.8-10
- made variables in rmmod_r local

* Tue Jul 22 2003 Thomas Woerner <twoerner@redhat.com> 1.2.8-9
- fixed permission for init script

* Sat Jul 19 2003 Thomas Woerner <twoerner@redhat.com> 1.2.8-8
- fixed save when iptables file is missing and iptables-config permissions

* Tue Jul  8 2003 Thomas Woerner <twoerner@redhat.com> 1.2.8-7
- fixes for ip6tables: module unloading, setting policy only for existing 
  tables

* Thu Jul  3 2003 Thomas Woerner <twoerner@redhat.com> 1.2.8-6
- IPTABLES_SAVE_COUNTER defaults to no, now
- install config file in /etc/sysconfig
- exchange unload of ip_tables and ip_conntrack
- fixed start function

* Wed Jul  2 2003 Thomas Woerner <twoerner@redhat.com> 1.2.8-5
- new config option IPTABLES_SAVE_ON_RESTART
- init script: new status, save and restart
- fixes #44905, #65389, #80785, #82860, #91040, #91560 and #91374

* Mon Jun 30 2003 Thomas Woerner <twoerner@redhat.com> 1.2.8-4
- new config option IPTABLES_STATUS_NUMERIC
- cleared IPTABLES_MODULES in iptables-config

* Mon Jun 30 2003 Thomas Woerner <twoerner@redhat.com> 1.2.8-3
- new init scripts

* Sat Jun 28 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- remove check for very old kernel versions in init scripts
- sync up both init scripts and remove some further ugly things
- add some docu into rpm

* Thu Jun 26  2003 Thomas Woerner <twoerner@redhat.com> 1.2.8-2
- rebuild

* Mon Jun 16 2003 Thomas Woerner <twoerner@redhat.com> 1.2.8-1
- update to 1.2.8

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Jan 13 2003 Bill Nottingham <notting@redhat.com> 1.2.7a-1
- update to 1.2.7a
- add a plethora of bugfixes courtesy Michael Schwendt <mschewndt@yahoo.com>

* Fri Dec 13 2002 Elliot Lee <sopwith@redhat.com> 1.2.6a-3
- Fix multilib

* Wed Aug 07 2002 Karsten Hopp <karsten@redhat.de>
- fixed iptables and ip6tables initscript output, based on #70511
- check return status of all iptables calls, not just the last one
  in a 'for' loop.

* Mon Jul 29 2002 Bernhard Rosenkraenzer <bero@redhat.com> 1.2.6a-1
- 1.2.6a (bugfix release, #69747)

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Mar  4 2002 Bernhard Rosenkraenzer <bero@redhat.com> 1.2.5-3
- Add some fixes from CVS, fixing bug #60465

* Tue Feb 12 2002 Bernhard Rosenkraenzer <bero@redhat.com> 1.2.5-2
- Merge ip6tables improvements from Ian Prowell <iprowell@prowell.org>
  #59402
- Update URL (#59354)
- Use /usr/sbin/chkconfig rather than chkconfig in %%postun script

* Fri Jan 11 2002 Bernhard Rosenkraenzer <bero@redhat.com> 1.2.5-1
- 1.2.5

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Nov  5 2001 Bernhard Rosenkraenzer <bero@redhat.com> 1.2.4-2
- Fix %%preun script

* Tue Oct 30 2001 Bernhard Rosenkraenzer <bero@redhat.com> 1.2.4-1
- Update to 1.2.4 (various fixes, including security fixes; among others:
  #42990, #50500, #53325, #54280)
- Fix init script (#31133)

* Mon Sep  3 2001 Bernhard Rosenkraenzer <bero@redhat.com> 1.2.3-1
- 1.2.3 (5 security fixes, some other fixes)
- Fix updating (#53032)

* Mon Aug 27 2001 Bernhard Rosenkraenzer <bero@redhat.com> 1.2.2-4
- Fix #50990
- Add some fixes from current CVS; should fix #52620

* Mon Jul 16 2001 Bernhard Rosenkraenzer <bero@redhat.com> 1.2.2-3
- Add some fixes from the current CVS tree; fixes #49154 and some IPv6
  issues

* Tue Jun 26 2001 Bernhard Rosenkraenzer <bero@redhat.com> 1.2.2-2
- Fix iptables-save reject-with (#45632), Patch from Michael Schwendt
  <mschwendt@yahoo.com>

* Tue May  8 2001 Bernhard Rosenkraenzer <bero@redhat.com> 1.2.2-1
- 1.2.2

* Wed Mar 21 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- 1.2.1a, fixes #28412, #31136, #31460, #31133

* Thu Mar  1 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Yet another initscript fix (#30173)
- Fix the fixes; they fixed some issues but broke more important
  stuff :/ (#30176)

* Tue Feb 27 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix up initscript (#27962)
- Add fixes from CVS to iptables-{restore,save}, fixing #28412

* Fri Feb 09 2001 Karsten Hopp <karsten@redhat.de>
- create /etc/sysconfig/iptables mode 600 (same problem as #24245)

* Mon Feb 05 2001 Karsten Hopp <karsten@redhat.de>
- fix bugzilla #25986 (initscript not marked as config file)
- fix bugzilla #25962 (iptables-restore)
- mv chkconfig --del from postun to preun

* Thu Feb  1 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Fix check for ipchains

* Mon Jan 29 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Some fixes to init scripts

* Wed Jan 24 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Add some fixes from CVS, fixes among other things Bug #24732

* Wed Jan 17 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Add missing man pages, fix up init script (Bug #17676)

* Mon Jan 15 2001 Bill Nottingham <notting@redhat.com>
- add init script

* Mon Jan 15 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- 1.2
- fix up ipv6 split
- add init script
- Move the plugins from /usr/lib/iptables to /lib/iptables.
  This needs to work before /usr is mounted...
- Use -O1 on alpha (compiler bug)

* Sat Jan  6 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- 1.1.2
- Add IPv6 support (in separate package)

* Thu Aug 17 2000 Bill Nottingham <notting@redhat.com>
- build everywhere

* Tue Jul 25 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 1.1.1

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Tue Jun 27 2000 Preston Brown <pbrown@redhat.com>
- move iptables to /sbin.
- excludearch alpha for now, not building there because of compiler bug(?)

* Fri Jun  9 2000 Bill Nottingham <notting@redhat.com>
- don't obsolete ipchains either
- update to 1.1.0

* Mon Jun  4 2000 Bill Nottingham <notting@redhat.com>
- remove explicit kernel requirement

* Tue May  2 2000 Bernhard Rosenkränzer <bero@redhat.com>
- initial package
