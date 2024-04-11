Name: jetbrains-mono-nerd-fonts
Version: 3.2.0
Release: %autorelease
Summary: The NerdFonts version of the JetBrains Mono font
License: OFL-1.1
BuildArch: noarch
Source: https://github.com/ryanoasis/nerd-fonts/releases/download/v%{version}/JetBrainsMono.tar.xz

%define fontdir /usr/share/fonts/%{name}

%description
Nerd Fonts is a project that patches developer targeted fonts with a high number of glyphs (icons).
Specifically to add a high number of extra glyphs from popular 'iconic fonts' such as Font Awesome, Devicons, Octicons, and others.

%prep
%setup -c

%install
install -m 0644 -D -t %{buildroot}%{fontdir} *.ttf

%files
%{fontdir}/*.ttf
%license OFL.txt
%doc README.md

%changelog
%autochangelog
