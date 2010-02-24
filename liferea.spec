#
# Conditional build:
%bcond_without	dbus		# without D-Bus support
%bcond_without	nm		# with NetworkManager support
#
Summary:	A RSS feed reader
Summary(pl.UTF-8):	Program do pobierania informacji w formacie RSS
Name:		liferea
Version:	1.7.4
Release:	1
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://downloads.sourceforge.net/liferea/%{name}-%{version}.tar.gz
# Source0-md5:	69ece60acc93a58cffb66e0e4f753704
Patch0:		%{name}-desktop.patch
URL:		http://liferea.sourceforge.net/
BuildRequires:	GConf2-devel >= 2.10.0
%{?with_nm:BuildRequires:	NetworkManager-devel}
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.6
%{?with_dbus:BuildRequires:	dbus-glib-devel >= 0.33}
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.18.0
BuildRequires:	gtk-webkit-devel >= 1.1.11
BuildRequires:	intltool >= 0.35.5
BuildRequires:	libglade2-devel >= 1:2.0.0
BuildRequires:	libnotify-devel >= 0.3.2
BuildRequires:	libsoup-devel >= 2.28.0
BuildRequires:	libtool
BuildRequires:	libunique-devel
BuildRequires:	libxml2-devel >= 1:2.6.27
BuildRequires:	libxslt-devel >= 1.1.19
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	sqlite3-devel >= 3.6.10
BuildRequires:	xorg-lib-libSM-devel
Requires(post,postun):	hicolor-icon-theme
Requires(post,preun):	GConf2
Requires:	gtk+2 >= 2.18.0
Obsoletes:	liferea-gtkhtml
Obsoletes:	liferea-mozilla
Obsoletes:	liferea-webkit
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Liferea is a GTK+ clone of FeedReader.

%description -l pl.UTF-8
Liferea jest klonem, napisanym za pomocą biblioteki GTK+, programu
FeedReader.

%prep
%setup -q
%patch0 -p1

%build
%{__glib_gettextize}
%{__intltoolize}
%{__aclocal}
%{__libtoolize}
%{__automake}
%{__autoheader}
%{__autoconf}
%configure \
	--disable-schemas-install \
	%{!?with_dbus: --disable-dbus} \
	%{!?with_nm: --disable-nm}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/liferea
%attr(755,root,root) %{_bindir}/liferea-add-feed
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%{_sysconfdir}/gconf/schemas/liferea.schemas
%{_datadir}/%{name}
%{_desktopdir}/liferea.desktop
%{_mandir}/man1/liferea.1*
%{_mandir}/pl/man1/liferea.1*
