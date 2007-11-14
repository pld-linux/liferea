# TODO: create subpackage -lua (?)
#
# Conditional build:
%bcond_without	dbus		# without DBUS support
%bcond_without	gtkhtml		# without GtkHTML
%bcond_without	xulrunner	# without XULRunner backend
%bcond_without	lua		# without LUA scripting support
%bcond_with	nm		# with NetworkManager support
#
%ifarch %{x8664}
%undefine	with_gtkhtml	# GtkHTML backend disabled on x86_64
%endif
Summary:	A RSS feed reader
Summary(pl.UTF-8):	Program do pobierania informacji w formacie RSS
Name:		liferea
Version:	1.4.7
Release:	1
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/liferea/%{name}-%{version}.tar.gz
# Source0-md5:	2d19a3ddc6ef2e2195383cbcd52c0dd3
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-xulrunner.patch
Patch2:		%{name}-lua51.patch
URL:		http://liferea.sourceforge.net/
BuildRequires:	GConf2-devel >= 2.10.0
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
%{?with_dbus:BuildRequires:	dbus-glib-devel >= 0.33}
BuildRequires:	gtk+2-devel >= 2:2.8.0
BuildRequires:	intltool >= 0.35.5
%{?with_gtkhtml:BuildRequires:	libgtkhtml-devel >= 2.6.3}
BuildRequires:	libnotify-devel >= 0.3.2
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.19
BuildRequires:	libxslt-devel >= 1.1.19
%{?with_lua:BuildRequires:	lua51-devel}
%{?with_nm:BuildRequires:	NetworkManager-devel}
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	sqlite3-devel
%{?with_xulrunner:BuildRequires:	xulrunner-devel}
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires(post,preun):	GConf2
Requires:	%{name}-backend = %{version}-%{release}
%ifarch %{x8664}
Obsoletes:	liferea-gtkhtml
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libgtkembedmoz.so libxpcom.so
# we have strict deps for it
%define		_noautoreq	libxpcom.so

%description
Liferea is a GTK+ clone of FeedReader.

%description -l pl.UTF-8
Liferea jest klonem, napisanym za pomocą biblioteki GTK+, programu
FeedReader.

%package gtkhtml
Summary:	GtkHTML module for Liferea
Summary(pl.UTF-8):	Moduł GtkHTML dla Liferea
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-backend = %{version}-%{release}

%description gtkhtml
GtkHTML module for Liferea.

%description gtkhtml -l pl.UTF-8
Moduł GtkHTML dla Liferea.

%package mozilla
Summary:	Mozilla HTML browser module for Liferea
Summary(pl.UTF-8):	Moduł przeglądarki HTML dla Liferea oparty na Mozilli
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
%requires_eq_to	xulrunner xulrunner-devel
Provides:	%{name}-backend = %{version}-%{release}

%description mozilla
Mozilla HTML browser module for Liferea.

%description mozilla -l pl.UTF-8
Moduł przeglądarki HTML dla Liferea oparty na Mozilli.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__glib_gettextize}
%{__intltoolize}
%{__aclocal}
%{__libtoolize}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-schemas-install \
	%{!?with_dbus: --disable-dbus} \
	%{!?with_gtkhtml: --disable-gtkhtml2} \
	%{!?with_lua: --disable-lua} \
	%{!?with_nm: --disable-nm} \
	%{!?with_xulrunner: --disable-xulrunner}
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
%{_sysconfdir}/gconf/schemas/liferea.schemas
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_mandir}/man1/liferea.1*
%if %{with lua}
%attr(755,root,root) %{_libdir}/%{name}/libliscrlua.so
%endif

%if %{with gtkhtml}
%files gtkhtml
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/liblihtmlg.so*
%endif

%if %{with xulrunner}
%files mozilla
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/liblihtmlx.so*
%endif
