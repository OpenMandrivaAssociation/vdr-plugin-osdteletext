%define plugin	osdteletext

Summary:	VDR plugin: Displays teletext on the OSD
Name:		vdr-plugin-%plugin
Version:	0.9.4
Release:	1
Group:		Video
License:	GPLv2+
URL:		http://projects.vdr-developer.org/projects/show/plg-osdteletext
Source:		vdr-%plugin-%{version}.tgz
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
Osd-Teletext displays the teletext directly on the OSD.
Both sound and video are played in the background.

%prep
%setup -q -n %plugin-%{version}
%vdr_plugin_prep

# check default cache dir
grep "\"%{vdr_plugin_cachedir}/vtx\"" rootdir.c

perl -pi -e 's|../../man|.|' Makefile

%vdr_plugin_params_begin %{plugin}
# Directory for the teletext page cache.
# default: %{vdr_plugin_cachedir}/vtx
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
# Store top text pages at cache. (unviewable pages)
var=STORE_TOPTEXT
param=-t
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
%doc README* COPYING HISTORY
%attr(-,vdr,vdr) %{vdr_plugin_cachedir}/vtx
