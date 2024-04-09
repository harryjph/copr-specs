Name: stm8flash
Version: d91dc18d5c408304a84e0fcf8ef1fb74e3b39a69
Release: %autorelease
Summary: Program your STM8 devices with SWIM/STLinkV1/2
License: GPL-2.0-or-later
Url: https://github.com/vdudouyt/stm8flash
Source: https://github.com/vdudouyt/stm8flash/archive/%{version}.tar.gz
BuildRequires: gcc make libusb1-devel

%description
This is free and open-source software distributed under the terms of the GNU General Public License, either version 2 of the License, or (at your option) any later version.
For years, it was the only program that's able to communicate through the SWIM interface of ST-LINKs under Linux.
Since 2018, OpenOCD also offers the basic functionality, and also has support for on-target debugging. As of early 2018, stm8flash has wider device support, and better support for memory read/write operations.

%global debug_package %{nil}

%prep
%autosetup

%build
%make_build
strip stm8flash

%install
install -m 0755 stm8flash -D %{buildroot}/%{_bindir}/stm8flash

%files
%doc README.md
%license COPYING LICENSE-CHANGE
%{_bindir}/stm8flash

%changelog
%autochangelog
