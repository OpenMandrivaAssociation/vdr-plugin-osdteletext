
%define plugin	osdteletext
%define name	vdr-plugin-%plugin
%define version	0.5.1
%define rel	18

Summary:	VDR plugin: Displays teletext on the OSD
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.wiesweg-online.de/linux/
Source:		http://www.wiesweg-online.de/linux/vdr/vdr-%plugin-%version.tar.bz2
Patch0:		osdteletext-0.5.1-i18n-1.6.patch
Patch1:		91_osdteletext-1.5.0.dpatch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
Osd-Teletext displays the teletext directly on the OSD.
Both sound and video are played in the background.

%prep
%setup -q -n %plugin-%version
%patch0 -p1
%patch1 -p1
%vdr_plugin_prep

# fix default cache dir
perl -pi -e 's|"/vtx"|"%{_vdr_plugin_cachedir}/%{plugin}"|' txtrecv.c

perl -pi -e 's|../../man|.|' Makefile

%vdr_plugin_params_begin %{plugin}
# Directory for the teletext page cache.
# default: %{_vdr_plugin_cachedir}/%{plugin}
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
rm -rf %{buildroot}
%vdr_plugin_install

install -d -m755 %{buildroot}%{_vdr_plugin_cachedir}/%{plugin}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%clean
rm -rf %{buildroot}

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README* COPYING HISTORY
%attr(-,vdr,vdr) %{_vdr_plugin_cachedir}/%{plugin}


