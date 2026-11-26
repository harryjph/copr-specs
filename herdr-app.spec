Name:           herdr-app
Version:        0.1.18
Release:        %autorelease
Summary:        Native desktop workspace for terminals and coding agents
License:        Apache-2.0
URL:            https://github.com/herdrdev/herdr-app
ExclusiveArch:  x86_64 aarch64
Source0:        https://releases.herdr.dev/app/%{version}/herdr-app-linux-%{_arch}.tar.gz

BuildRequires:  desktop-file-utils
Requires:       herdr-core >= 0.1.11
Requires:       hicolor-icon-theme
Requires:       libglvnd
Requires:       libwayland-client
Requires:       libxkbcommon-x11
Requires:       vulkan-loader

%global debug_package %{nil}

%description
Herdr is a native Rust/GPUI desktop workspace for running, monitoring, and
managing terminals and AI coding agents side by side. It connects to
herdr-core so terminal sessions and background agents keep running even when
the desktop window is closed.

%prep
%autosetup -n herdr-app

%install
install -D -m 0755 herdr-app %{buildroot}%{_bindir}/herdr-app
install -D -m 0644 herdr-app.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/herdr-app.svg

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/herdr-app.desktop <<'EOF'
[Desktop Entry]
Type=Application
Name=Herdr
Comment=Terminals and coding agents that keep running
Exec=herdr-app
Icon=herdr-app
Terminal=false
Categories=Development;
StartupWMClass=herdr-app
EOF
desktop-file-validate %{buildroot}%{_datadir}/applications/herdr-app.desktop

%files
%license LICENSE
%doc THIRD-PARTY-NOTICES
%{_bindir}/herdr-app
%{_datadir}/applications/herdr-app.desktop
%{_datadir}/icons/hicolor/scalable/apps/herdr-app.svg

%changelog
%autochangelog
