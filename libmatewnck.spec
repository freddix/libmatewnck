Summary:	General Window Manager interfacing for MATE utilities
Name:		libmatewnck
Version:	1.6.1
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://pub.mate-desktop.org/releases/1.6/%{name}-%{version}.tar.xz
# Source0-md5:	30c96e0120b0c709b417d787b2aa3033
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk+-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	startup-notification-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
General Window Manager interfacing for MATE utilities. This library
is a part of the MATE platform.

%package devel
Summary:	Header files and documentation for libmatewnck
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header, docs and development libraries for libmatewnck.

%package apidocs
Summary:	libmatewnck API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libmatewnck API documentation.

%prep
%setup -q

# kill mate-common deps
%{__sed} -i -e '/MATE_COMPILE_WARNINGS.*/d'	\
    -i -e '/MATE_MAINTAINER_MODE_DEFINES/d'	\
    -i -e '/MATE_COMMON_INIT/d'		\
    -i -e '/MATE_DEBUG_CHECK/d' configure.ac

%build
%{__gtkdocize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/{ca@valencia,crh,en@shaw}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/matewnck-urgency-monitor
%attr(755,root,root) %{_bindir}/matewnckprop
%attr(755,root,root) %ghost %{_libdir}/libmatewnck.so.?
%attr(755,root,root) %{_libdir}/libmatewnck.so.*.*.*
%{_libdir}/girepository-1.0/Matewnck-1.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmatewnck.so
%{_includedir}/libmatewnck
%{_pkgconfigdir}/libmatewnck.pc
%{_datadir}/gir-1.0/Matewnck-1.0.gir

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libmatewnck

