Name:           herdr-core
Version:        0.1.22
Release:        %autorelease
Summary:        Headless terminal runtime and background server for AI coding agents
License:        Apache-2.0
URL:            https://github.com/herdrdev/herdr-core
ExclusiveArch:  x86_64 aarch64
Source0:        https://releases.herdr.dev/core/%{version}/herdr-core-linux-x86_64.tar.gz
Source1:        https://releases.herdr.dev/core/%{version}/herdr-core-linux-aarch64.tar.gz

%global debug_package %{nil}

%description
herdr-core (hc) is the headless terminal runtime and local background server for
Herdr. It runs programs and AI coding agents inside persistent terminals that
stay alive across client disconnects, app restarts, and SSH drops, and supports
agent-to-agent spawning and communication.

%prep
%setup -q -c -T
%ifarch x86_64
tar -xzf %{SOURCE0}
%endif
%ifarch aarch64
tar -xzf %{SOURCE1}
%endif

%install
install -D -m 0755 herdr-core %{buildroot}%{_bindir}/herdr-core
ln -s herdr-core %{buildroot}%{_bindir}/hc

%files
%license LICENSE
%doc THIRD-PARTY-NOTICES
%{_bindir}/herdr-core
%{_bindir}/hc

%changelog
%autochangelog
