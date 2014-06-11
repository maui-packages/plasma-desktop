# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.22
# 
# >> macros
# << macros

Name:       kde5-plasma-desktop
Summary:    Plasma 5 desktop
Version:    4.97.0
Release:    1
Group:      System/Base
License:    GPLv2+
URL:        http://www.kde.org
Source0:    %{name}-%{version}.tar.xz
Source100:  kde5-plasma-desktop.yaml
Source101:  kde5-plasma-desktop-rpmlintrc
Requires:   kde5-filesystem
Requires:   kde5-plasma-workspace
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  pkgconfig(Qt5Declarative)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  kde5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-tools
BuildRequires:  libusb-devel
BuildRequires:  fontconfig-devel
BuildRequires:  libX11-devel
BuildRequires:  libxkbfile-devel
BuildRequires:  libxcb-devel
BuildRequires:  xcb-util-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  phonon-qt5-devel
BuildRequires:  kf5-umbrella
BuildRequires:  kf5-plasma-devel
BuildRequires:  kf5-kdoctools-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kcmutils-devel
BuildRequires:  kf5-knewstuff-devel
BuildRequires:  kf5-kdelibs4support-devel
BuildRequires:  kf5-knotifyconfig-devel
BuildRequires:  kf5-kdesu-devel
BuildRequires:  kf5-attica-devel
BuildRequires:  kf5-kwallet-devel
BuildRequires:  kf5-krunner-devel
BuildRequires:  kde5-libksysguard-devel
BuildRequires:  kde5-plasma-workspace-devel
BuildRequires:  kde5-kwin-devel
BuildRequires:  kf5-kactivities-libs-devel
BuildRequires:  desktop-file-utils


%description
Plasma 5 desktop



%package doc
Summary:    Documentation and user manuals for %{name}
Group:      Documentation
Requires:   %{name} = %{version}-%{release}

%description doc
Documentation and user manuals for %{name}



%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
%kde5_make
# << build pre



# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
%kde5_make_install
# << install pre

# >> install post
rm -vf %{buildroot}/%{_kde5_libdir}/libkfontinst{,ui}.so || true
# << install post
desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop









%files
%defattr(-,root,root,-)
%{_kde5_bindir}/kapplymousetheme
%{_kde5_bindir}/kaccess
%{_kde5_bindir}/kfontinst
%{_kde5_bindir}/kfontview
%{_kde5_bindir}/krdb
%{_kde5_libexecdir}/kcmdatetimehelper
%{_kde5_libexecdir}/fontinst
%{_kde5_libexecdir}/fontinst_helper
%{_kde5_libexecdir}/fontinst_x11
%{_kde5_libexecdir}/kfontprint
%{_kde5_libexecdir}/knetattach
%{_kde5_libdir}/qml/org/kde/plasma/private
%{_kde5_libdir}/attica_kde.so
%{_kde5_libdir}/libkdeinit5_kaccess.so
%{_kde5_libdir}/kconf_update_bin/*
%{_kde5_libdir}/libkfontinst.so.*
%{_kde5_libdir}/libkfontinstui.so.*
%{_kde5_plugindir}/*.so
%{_kde5_datadir}/plasma/*
%{_kde5_datadir}/kcminput
%{_kde5_datadir}/color-schemes
%{_kde5_datadir}/kconf_update/*
%{_kde5_datadir}/kthememanager
%{_kde5_datadir}/kdisplay
%{_kde5_datadir}/kcontrol
%{_kde5_datadir}/kcmkeys
%{_kde5_datadir}/kcm_componentchooser
%{_kde5_datadir}/kcmlocale
%{_kde5_datadir}/kcm_phonon
%{_kde5_datadir}/kfontinst
%{_kde5_datadir}/kfontview
%{_kde5_datadir}/kcmkeyboard
%{_kde5_datadir}/ksmserver
%{_kde5_datadir}/konqsidebartng/virtual_folders/services/fonts.desktop
%{_kde5_sysconfdir}/dbus-1/system.d/*.conf
%{_kde5_sysconfdir}/xdg/*.knsrc
%{_datadir}/kservices5/*.desktop
%{_datadir}/kservices5/ServiceMenus/installfont.desktop
%{_datadir}/kservices5/fonts.protocol
%{_datadir}/kservices5/kded/*.desktop
%{_datadir}/knotifications5/*.notifyrc
%{_datadir}/icons/*/*/*/*
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/dbus-1/system-services/*.service
%{_datadir}/polkit-1/actions/*.policy
# >> files
# << files


%files doc
%defattr(-,root,root,-)
%{_datadir}/doc/HTML/en/*
# >> files doc
# << files doc

