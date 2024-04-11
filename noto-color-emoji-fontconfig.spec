Name: noto-color-emoji-fontconfig
Version: 1.0.0
Release: %autorelease
Summary: Fontconfig to enable Noto Color Emoji fonts where emojis can be displayed
License: GPL
BuildArch: noarch
URL: https://aur.archlinux.org/packages/noto-color-emoji-fontconfig
Source: https://aur.archlinux.org/cgit/aur.git/snapshot/noto-color-emoji-fontconfig.tar.gz

%description
Fontconfig to enable Noto Color Emoji fonts where emojis can be displayed

%prep
%setup -n noto-color-emoji-fontconfig

%install
install -D -m644 75-noto-color-emoji.conf %{buildroot}/usr/share/fontconfig/conf.avail/75-noto-color-emoji.conf
mkdir -p %{buildroot}/etc/fonts/conf.d/
ln -sf /usr/share/fontconfig/conf.avail/75-noto-color-emoji.conf %{buildroot}/etc/fonts/conf.d/75-noto-color-emoji.conf

%files
/usr/share/fontconfig/conf.avail/75-noto-color-emoji.conf
/etc/fonts/conf.d/75-noto-color-emoji.conf

%changelog
%autochangelog
