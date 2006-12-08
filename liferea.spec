#
# Conditional build:
%bcond_without	dbus		# without DBUS support
%bcond_without	mozilla		# without mozilla
%bcond_without	gtkhtml		# without GtkHTML
%bcond_without	mozilla_firefox	# build with mozilla-firefox-devel
#
%define	pre	RC3
Summary:	A RSS feed reader
Summary(pl):	Program do pobierania informacji w formacie RSS
Name:		liferea
Version:	1.2
Release:	0.%{pre}.1
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/liferea/%{name}-%{version}-%{pre}.tar.gz
# Source0-md5:	30542c315370db12cc9598d3b809b2d5
Patch0:		%{name}-desktop.patch
URL:		http://liferea.sourceforge.net/
BuildRequires:	GConf2-devel >= 2.10.0
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_dbus:BuildRequires:	dbus-glib-devel >= 0.33}
BuildRequires:	gtk+2-devel >= 2:2.6.4
%{?with_gtkhtml:BuildRequires:	libgtkhtml-devel >= 2.6.3}
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.19
%if %{with mozilla}
%if %{with mozilla_firefox}
BuildRequires:	mozilla-firefox-devel
%else
BuildRequires:	mozilla-devel
%endif
%endif
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
Requires(post,preun):	GConf2
Requires:	%{name}-backend = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libgtkembedmoz.so libxpcom.so

%description
Liferea is a GTK+ clone of FeedReader.

%description -l pl
Liferea jest klonem, napisanym za pomoc± biblioteki GTK+, programu
FeedReader.

%package gtkhtml
Summary:	GtkHTML module for Liferea
Summary(pl):	Modu³ GtkHTML dla Liferea
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-backend = %{version}-%{release}

%description gtkhtml
GtkHTML module for Liferea.

%description gtkhtml -l pl
Modu³ GtkHTML dla Liferea.

%package mozilla
Summary:	Mozilla HTML browser module for Liferea
Summary(pl):	Modu³ przegl±darki HTML dla Liferea oparty na Mozilli
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
%if %{with mozilla_firefox}
%requires_eq	mozilla-firefox-libs
%else
Requires:	mozilla-embedded = %(rpm -q --qf '%{EPOCH}:%{VERSION}' --whatprovides mozilla-embedded)
%endif
Provides:	%{name}-backend = %{version}-%{release}

%description mozilla
Mozilla HTML browser module for Liferea.

%description mozilla -l pl
Modu³ przegl±darki HTML dla Liferea oparty na Mozilli.

%prep
%setup -q -n %{name}-%{version}-%{pre}
%patch0 -p1

%build
#%{__glib_gettextize}
%{__aclocal}
%{__libtoolize}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-schemas-install \
	%{!?with_dbus: --disable-dbus} \
	%{!?with_gtkhtml: --disable-gtkhtml2} \
	%{!?with_mozilla: --disable-gecko}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/lib*.la

%find_lang %{name}

%post
%gconf_schema_install liferea.schemas
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall liferea.schemas

%postun
%update_icon_cache hicolor

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*.so.*.*.*
%{_iconsdir}/hicolor/48x48/apps/liferea.png
%{_mandir}/pl/man1/liferea.1*
%{_sysconfdir}/gconf/schemas/*.schemas
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_mandir}/man1/liferea.1*

%if %{with gtkhtml}
%files gtkhtml
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/liblihtmlg.so*
%endif

%if %{with mozilla}
%files mozilla
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/liblihtmlm.so*
%endif
