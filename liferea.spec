Summary:	A RSS Feed reader
Name:		liferea
Version:	0.2.7
Release:	0.1
License:	GPL
Group:		Applications/Internet
Source0:	http://umn.dl.sourceforge.net/sourceforge/liferea/liferea-0.2.7.tar.gz
# Source0-md5:	d092db3324c775160c5b1b1d5259f3fd
URL:		http://liferea.sourceforge.net/
BuildRequires:	gtk+2-devel
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
