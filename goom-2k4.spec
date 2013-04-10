#
# Conditional build:
%bcond_without	static_libs	# static library
#
Summary:	GOOM! audio visualization version 2
Summary(pl.UTF-8):	Wizualizacja dźwięku GOOM! wersja 2
Name:		goom-2k4
Version:	0
Release:	1
License:	LGPL
Group:		Applications/Graphics
Source0:	http://downloads.sourceforge.net/goom/%{name}-%{version}-src.tar.gz
# Source0-md5:	8100dd07e0c6784fdf079eeaa53a5c7f
Patch0:		%{name}-link.patch
URL:		http://goom.sourceforge.net/
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	libtool
BuildRequires:	xmms-devel >= 0.9.5.1
Requires:	libgoom2 = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GOOM! audio visualization version 2.

%description -l pl.UTF-8
Wizualizacja dźwięku GOOM! wersja 2.

%package -n libgoom2
Summary:	Goom audio visualisation effects library
Summary(pl.UTF-8):	Biblioteka efektów wizualnych dźwięku Goom
Group:		Libraries

%description -n libgoom2
Goom audio visualisation effects library.

%description -n libgoom2 -l pl.UTF-8
Biblioteka efektów wizualnych dźwięku Goom.

%package -n libgoom2-devel
Summary:	Header files for Goom audio visualisation effects library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki efektów wizualnych dźwięku Goom
Group:		Development/Libraries
Requires:	libgoom2 = %{version}-%{release}

%description -n libgoom2-devel
Header files for Goom audio visualisation effects library.

%description -n libgoom2-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki efektów wizualnych dźwięku Goom.

%package -n libgoom2-static
Summary:	Goom audio visualisation effects static library
Summary(pl.UTF-8):	Statyczna biblioteka efektów wizualnych dźwięku Goom
Group:		Development/Libraries
Requires:	libgoom2-devel = %{version}-%{release}

%description -n libgoom2-static
Goom audio visualisation effects static library.

%description -n libgoom2-static -l pl.UTF-8
Statyczna biblioteka efektów wizualnych dźwięku Goom.

%package -n xmms-visualization-goom2
Summary:	Goom 2 visualization plugin for XMMS
Summary(pl.UTF-8):	Wtyczka wizualizacji Goom 2 dla XMMS-a
Group:		Applications/Multimedia
Requires:	libgoom2 = %{version}-%{release}
Requires:	xmms >= 0.9.5.1

%description -n xmms-visualization-goom2
Goom 2 visualization plugin for XMMS.

%description -n xmms-visualization-goom2 -l pl.UTF-8
Wtyczka wizualizacji Goom 2 dla XMMS-a.

%prep
%setup -q -n goom2k4-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	%{?with_static_libs:--enable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{xmms_visualization_plugindir}/*.la
%{?with_static_libs:%{__rm} $RPM_BUILD_ROOT%{xmms_visualization_plugindir}/*.a}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n libgoom2 -p /sbin/ldconfig
%postun	-n libgoom2 -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/goom2

%files -n libgoom2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgoom2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoom2.so.0

%files -n libgoom2-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgoom2.so
%{_libdir}/libgoom2.la
%{_includedir}/goom
%{_pkgconfigdir}/libgoom2.pc

%if %{with static_libs}
%files -n libgoom2-static
%defattr(644,root,root,755)
%{_libdir}/libgoom2.a
%endif

%files -n xmms-visualization-goom2
%defattr(644,root,root,755)
%attr(755,root,root) %{xmms_visualization_plugindir}/libxmmsgoom2.so
