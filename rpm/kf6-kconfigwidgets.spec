%global  kf_version 6.6.0

Name:    kf6-kconfigwidgets
Version: 6.6.0
Release: 0%{?dist}
Summary: KDE Frameworks 6 Tier 3 addon for creating configuration dialogs

# The following licenses are in LICENSES but go unused: BSD-3-Clause, MIT
License: CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/kconfigwidgets
Source0:    %{name}-%{version}.tar.bz2

BuildRequires:  cmake
BuildRequires:  clang
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  kf6-kcodecs-devel
BuildRequires:  kf6-kcolorscheme-devel
BuildRequires:  kf6-kconfig-devel
BuildRequires:  kf6-kcoreaddons-devel
BuildRequires:  kf6-kguiaddons-devel
BuildRequires:  kf6-ki18n-devel
BuildRequires:  kf6-kwidgetsaddons-devel
BuildRequires:  pkgconfig(xkbcommon)

%description
KConfigWidgets provides easy-to-use classes to create configuration dialogs, as
well as a set of widgets which uses KConfig to store their settings.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf6-kauth-devel
Requires:       kf6-kcodecs-devel
Requires:       kf6-kcolorscheme-devel
Requires:       kf6-kconfig-devel
Requires:       kf6-kwidgetsaddons-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.


%prep
%autosetup -n %{name}-%{version}/upstream -p1


%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name} --with-man --all-name

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_libdir}/libKF6ConfigWidgets.so.*
%{_datadir}/locale/*/kf6_entry.desktop
%{_kf6_datadir}/qlogging-categories6/kconfigwidgets*

%files devel
%{_kf6_includedir}/KConfigWidgets/
%{_kf6_libdir}/libKF6ConfigWidgets.so
%{_kf6_libdir}/cmake/KF6ConfigWidgets/
%{_kf6_libdir}/qt6/plugins/designer/kconfigwidgets6widgets.so
%{_qt6_docdir}/*.tags

%files doc
%{_qt6_docdir}/*.qch
