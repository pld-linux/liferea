Summary:	A RSS Feed reader
Summary(pl):	Program do pobierania feedu news w formacie RSS
Name:		liferea
Version:	0.3.8
Release:	1
License:	GPL
Group:		Applications/Internet
Source0:	http://dl.sourceforge.net/liferea/%{name}-%{version}.tar.gz
# Source0-md5:	505a6590a862e5144f28aea45866c60a
URL:		http://liferea.sourceforge.net/
BuildRequires:	GConf2-devel >= 2.0.0
BuildRequires:	gnome-vfs2-devel >= 2.0.0
BuildRequires:	gtk+2-devel
BuildRequires:	libxml2-devel >= 2.0.0
BuildRequires:	libgtkhtml-devel >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Liferea is a GTK clone of FeedReader.

%description -l pl
Liferea jest klonem FeedReadera korzystaj±cym z GTK.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
#%{_desktopdir}/*
#%{_pixmapsdir}/*
