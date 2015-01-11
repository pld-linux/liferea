Summary:	A RSS feed reader
Summary(pl.UTF-8):	Program do pobierania informacji w formacie RSS
Name:		liferea
Version:	1.10.13
Release:	1
License:	GPL v2+
Group:		X11/Applications/Networking
Source0:	http://github.com/lwindolf/liferea/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	9f1d952ff670f48aa92f5cf2983e928e
Patch0:		%{name}-desktop.patch
URL:		http://liferea.sourceforge.net/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.11
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	gsettings-desktop-schemas-devel
BuildRequires:	gtk+3-devel >= 3.4.0
BuildRequires:	gtk-webkit3-devel
BuildRequires:	intltool >= 0.40.0
BuildRequires:	json-glib-devel
BuildRequires:	libnotify-devel >= 0.7.0
BuildRequires:	libpeas-devel >= 1.0.0
BuildRequires:	libpeas-gtk-devel >= 1.0.0
BuildRequires:	libsoup-devel >= 2.28.2
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.27
BuildRequires:	libxslt-devel >= 1.1.19
BuildRequires:	pango-devel >= 1:1.4.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	sqlite3-devel >= 3.7.0
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	glib2 >= 1:2.26.0
Suggests:	liferea-plugin-gnome-keyring
Suggests:	liferea-plugin-media-player
Obsoletes:	liferea-gtkhtml
Obsoletes:	liferea-mozilla
Obsoletes:	liferea-webkit
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Liferea is a GTK+ clone of FeedReader.

%description -l pl.UTF-8
Liferea jest klonem, napisanym za pomocą biblioteki GTK+, programu
FeedReader.

%package plugin-gnome-keyring
Summary:	Liferea GNOME Keyring plugin
Requires:	%{name} = %{version}-%{release}
Requires:	python-pygobject3

%description plugin-gnome-keyring
Allow Liferea to use GNOME keyring as password store.

%package plugin-media-player
Summary:	Liferea media player plugin
Requires:	%{name} = %{version}-%{release}
Requires:	python-pygobject3

%description plugin-media-player
Play music and videos directly from Liferea.

%prep
%setup -q
%patch0 -p1

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
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%post
%glib_compile_schemas
%update_icon_cache hicolor
%update_desktop_database_post

%postun
%glib_compile_schemas
%update_icon_cache hicolor
%update_desktop_database_post

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/liferea
%attr(755,root,root) %{_bindir}/liferea-add-feed
%dir %{_libdir}/liferea
%dir %{_libdir}/liferea/girepository-1.0
%{_libdir}/liferea/girepository-1.0/Liferea-3.0.typelib
%dir %{_libdir}/liferea/plugins
%{_datadir}/appdata/liferea.appdata.xml
%{_datadir}/glib-2.0/schemas/net.sf.liferea.gschema.xml
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%{_datadir}/%{name}
%{_desktopdir}/liferea.desktop
%{_mandir}/man1/liferea.1*
%{_mandir}/pl/man1/liferea.1*

%files plugin-gnome-keyring
%defattr(644,root,root,755)
%{_libdir}/liferea/plugins/gnome-keyring.plugin
%{_libdir}/liferea/plugins/gnome-keyring.py

%files plugin-media-player
%defattr(644,root,root,755)
%{_libdir}/liferea/plugins/media-player.plugin
%{_libdir}/liferea/plugins/media-player.py
