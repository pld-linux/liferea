Summary:	A RSS feed reader
Summary(pl):	Program do pobierania informacji w formacie RSS
Name:		liferea
Version:	0.4.5
Release:	1
License:	GPL
Group:		Applications/Internet
Source0:	http://dl.sourceforge.net/liferea/%{name}-%{version}.tar.gz
# Source0-md5:	526b5fa11f5b6e5ab8ab863bd018d987
URL:		http://liferea.sourceforge.net/
BuildRequires:	GConf2-devel >= 2.0.0
BuildRequires:	gnome-vfs2-devel >= 2.0.0
BuildRequires:	gtk+2-devel
BuildRequires:	libxml2-devel >= 2.0.0
BuildRequires:	libgtkhtml-devel >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Liferea is a GTK+ clone of FeedReader.

%description -l pl
Liferea jest klonem, napisanym za pomoc± biblioteki GTK+, programu
FeedReader.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
#%{_desktopdir}/*
#%{_pixmapsdir}/*
