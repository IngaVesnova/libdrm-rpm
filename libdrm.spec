%global debug_package %{nil}

Name:           libdrm
Version:        2.4.129
Release:        1%{?dist}
Summary:        Direct Rendering Manager runtime library

License:        MIT
URL:            https://dri.freedesktop.org/libdrm/
Source0:        https://dri.freedesktop.org/libdrm/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(pciaccess) >= 0.10
BuildRequires:  pkgconfig(libcjson)

%description
Direct Rendering Manager runtime library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}.

%prep
%autosetup

%build
%meson -Dudev=false
%meson_build

%install
%meson_install

%files
%license default_license.txt
%{_libdir}/libdrm*.so.*

%files devel
%{_includedir}/libdrm/
%{_includedir}/xf86*.h
%{_libdir}/libdrm*.so
%{_libdir}/pkgconfig/libdrm*.pc

%changelog
* Tue Aug 04 2026 Custom Maintainer - 2.4.129-1
- Update libdrm for MangoWM stack
