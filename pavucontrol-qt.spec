Summary:	Volume control for Pulseaudio sound server for Linux, Qt port
Name:		pavucontrol-qt
Version:	2.3.0
Release:	1
License:	GPLv2+
Group:		Sound
Url:		https://github.com/lxqt/pavucontrol-qt
Source0:	https://github.com/lxqt/pavucontrol-qt/releases/download/%{version}/pavucontrol-qt-%{version}.tar.xz
Source1:	%{name}-16.png
Source2:	%{name}-32.png
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libpulse-mainloop-glib)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	cmake(lxqt)
BuildRequires:	cmake(lxqt2-build-tools)
BuildRequires:	desktop-file-utils
Requires:	pulseaudio
Provides:	pulseaudio-volume-control
BuildSystem:	cmake
BuildOption:	-DPULL_TRANSLATIONS:BOOL=OFF

%description
Pulseaudio Volume Control (pavucontrol) is a simple 
Qt based volume control tool for the Pulseaudio sound 
server. In contrast to classic mixer tools this one allows 
you to control both the volume of hardware devices and of 
each playback stream separately.

%install -a
sed -i "s/^Icon=.*/Icon=%{name}/" %{buildroot}%{_datadir}/applications/%{name}.desktop

desktop-file-install --vendor="" \
	--add-category="Qt" \
	--add-category="X-MandrivaLinux-Multimedia-Sound" \
	--add-category="X-MandrivaLinux-CrossDesktop" \
	--remove-category="Application" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/%{name}.desktop

#icons install
install -D -m 0644 %{SOURCE1} %{buildroot}%{_miconsdir}/%{name}.png
install -D -m 0644 %{SOURCE2} %{buildroot}%{_iconsdir}/%{name}.png

%files -f %{name}.lang
%doc LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%dir %{_datadir}/pavucontrol-qt/translations
