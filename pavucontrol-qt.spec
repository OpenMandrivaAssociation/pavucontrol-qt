Summary:	Volume control for Pulseaudio sound server for Linux, Qt port
Name:		pavucontrol-qt
Version:	0.14.1
Release:	1
License:	GPLv2+
Group:		Sound
Url:		https://github.com/lxde/pavucontrol-qt
Source0:	https://github.com/lxde/pavucontrol-qt/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:	%{name}-16.png
Source2:	%{name}-32.png
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libpulse-mainloop-glib)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	cmake(lxqt)
BuildRequires:	cmake(lxqt-build-tools)
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	qmake5
Requires:	pulseaudio
Requires(post,postun):	desktop-file-utils
Provides:	pulseaudio-volume-control

%description
Pulseaudio Volume Control (pavucontrol) is a simple 
Qt based volume control tool for the Pulseaudio sound 
server. In contrast to classic mixer tools this one allows 
you to control both the volume of hardware devices and of 
each playback stream separately.

%prep
%setup -q
%autopatch -p1
%cmake_qt5 -DPULL_TRANSLATIONS:BOOL=OFF -G Ninja

%build
%ninja -C build

%install
%ninja_install -C build

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

ln -s %{name} %{buildroot}%{_bindir}/pavucontrol
%find_lang %{name} --with-qt --all-name

%files -f %{name}.lang
%doc LICENSE
%{_bindir}/pavucontrol
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
