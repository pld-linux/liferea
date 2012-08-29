Summary:	A RSS feed reader
Summary(pl.UTF-8):	Program do pobierania informacji w formacie RSS
Name:		liferea
Version:	1.8.6
Release:	2
License:	GPL v2+
Group:		X11/Applications/Networking
Source0:	http://downloads.sourceforge.net/liferea/%{name}-%{version}.tar.gz
# Source0-md5:	6e6be1f4a3b87babb71fa06e7d209728
Patch0:		%{name}-desktop.patch
Patch1:		automake-1.12.patch
URL:		http://liferea.sourceforge.net/
BuildRequires:	GConf2-devel >= 2.10.0
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.11
BuildRequires:	geoclue-devel
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.26.0
BuildRequires:	gstreamer-devel >= 0.10
BuildRequires:	gtk+2-devel >= 2:2.18.0
BuildRequires:	gtk-webkit-devel >= 1.2.2
BuildRequires:	intltool >= 0.40.0
BuildRequires:	json-glib-devel
BuildRequires:	libglade2-devel >= 1:2.0.0
BuildRequires:	libnotify-devel >= 0.7.0
BuildRequires:	libsoup-devel >= 2.28.2
BuildRequires:	libtool
BuildRequires:	libunique-devel
BuildRequires:	libxml2-devel >= 1:2.6.27
BuildRequires:	libxslt-devel >= 1.1.19
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	sqlite3-devel >= 3.7.0
BuildRequires:	xorg-lib-libSM-devel
Requires(post,preun):	GConf2
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	glib2 >= 1:2.26.0
Requires:	gtk+2 >= 2:2.18.0
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
%patch1 -p1

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
	--disable-silent-rules

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
