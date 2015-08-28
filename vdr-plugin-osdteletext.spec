%define plugin	osdteletext

Summary:	VDR plugin: Displays teletext on the OSD
Name:		vdr-plugin-%plugin
Version:	0.8.3
Release:	5
Group:		Video
License:	GPL
URL:		http://projects.vdr-developer.org/projects/show/plg-osdteletext
Source:		vdr-%plugin-%version.tgz
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
Osd-Teletext displays the teletext directly on the OSD.
Both sound and video are played in the background.

%prep
%setup -q -n %plugin-%version
%vdr_plugin_prep

# check default cache dir
grep "\"%{vdr_plugin_cachedir}/vtx\"" txtrecv.c

perl -pi -e 's|../../man|.|' Makefile

%vdr_plugin_params_begin %{plugin}
# Directory for the teletext page cache.
# default: %{_vdr_plugin_cachedir}/vtx
var=DIRECTORY
param=--directory=DIRECTORY
# Maximum cache size in MB.
# default: a calculated value below 50 MB
var=MAX_CACHE
param=--max-cache=MAX_CACHE
# Cache system to be used:
# legacy: traditional one-file-per-page system
# packed: one-file-for-a-few-pages system
# default: packed
var=CACHE_SYSTEM
param=--cache-system=CACHE_SYSTEM
%vdr_plugin_params_end

%build
%vdr_plugin_build

%install
%vdr_plugin_install

install -d -m755 %{buildroot}%{vdr_plugin_cachedir}/vtx

%pre
if [ -d /var/cache/vdr/osdteletext ] && ! [ -d %{vdr_plugin_cachedir}/vtx ]; then
	mv /var/cache/vdr/osdteletext %{vdr_plugin_cachedir}/vtx || :
fi

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README* COPYING HISTORY
%attr(-,vdr,vdr) %{vdr_plugin_cachedir}/vtx




%changelog
* Sat Feb 06 2010 Anssi Hannula <anssi@mandriva.org> 0.8.3-1mdv2010.1
+ Revision: 501485
- new version, new URL
- remove patches, applied upstream
- use upstream cache directory

* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.5.1-20mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.5.1-19mdv2009.1
+ Revision: 359346
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.5.1-18mdv2009.0
+ Revision: 197958
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.5.1-17mdv2009.0
+ Revision: 197701
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- adapt to gettext i18n of VDR 1.6 (semi-automatic patch)
- adapt for api changes of VDR 1.5.0 (P1 from e-tobi)

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.5.1-16mdv2008.1
+ Revision: 145158
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.5.1-15mdv2008.1
+ Revision: 103176
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.5.1-14mdv2008.0
+ Revision: 50026
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.5.1-13mdv2008.0
+ Revision: 42112
- rebuild for new vdr

* Tue May 15 2007 Anssi Hannula <anssi@mandriva.org> 0.5.1-12mdv2008.0
+ Revision: 27093
- rebuild

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.5.1-11mdv2008.0
+ Revision: 22764
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.5.1-10mdv2007.0
+ Revision: 90952
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.5.1-9mdv2007.1
+ Revision: 74064
- rebuild for new vdr
- Import vdr-plugin-osdteletext

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.5.1-8mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.5.1-7mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.5.1-6mdv2007.0
- rebuild for new vdr

* Thu Jul 27 2006 Anssi Hannula <anssi@mandriva.org> 0.5.1-5mdv2007.0
- rebuild for new vdr

* Tue Jul 25 2006 Anssi Hannula <anssi@mandriva.org> 0.5.1-4mdv2007.0
- fix instance of wrong macro name

* Tue Jun 20 2006 Anssi Hannula <anssi@mandriva.org> 0.5.1-3mdv2007.0
- use _ prefix for system path macros

* Mon Jun 05 2006 Anssi Hannula <anssi@mandriva.org> 0.5.1-2mdv2007.0
- rebuild for new vdr

* Fri Jun 02 2006 Anssi Hannula <anssi@mandriva.org> 0.5.1-1mdv2007.0
- initial Mandriva release

