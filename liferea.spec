Summary:	A RSS feed reader
Summary(pl):	Program do pobierania informacji w formacie RSS
Name:		liferea
Version:	0.5.2b
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/liferea/%{name}-%{version}.tar.gz
# Source0-md5:	320a3b93bbf9d105ba45e0ca6dedcefe
URL:		http://liferea.sourceforge.net/
BuildRequires:	GConf2-devel >= 2.4.0
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	libxml2-devel >= 2.0.0
BuildRequires:	libgtkhtml-devel >= 2.4.0
BuildRequires:	libstdc++-devel
BuildRequires:	mozilla-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libgtkembedmoz.so libxpcom.so

%description
Liferea is a GTK+ clone of FeedReader.

%description -l pl
Liferea jest klonem, napisanym za pomoc± biblioteki GTK+, programu
FeedReader.

%package mozilla
Summary:	Mozilla HTML browser module for Liferea
Summary(pl):	Modu³ przegl±darki HTML dla Liferea oparty na Mozilli
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}

%description mozilla
Mozilla HTML browser module for Liferea.

%description mozilla -l pl
Modu³ przegl±darki HTML dla Liferea oparty na Mozilli.

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

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/lib*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/liblihtmlg.so*
%{_datadir}/%{name}
%{_desktopdir}/*
%{_pixmapsdir}/*
%{_mandir}/man1/liferea.1*

%files mozilla
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/liblihtmlm.so*
