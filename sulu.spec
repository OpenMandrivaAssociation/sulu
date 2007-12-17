%define name sulu
%define version 0.17
%define release %mkrel 2

Name:		%{name}
Summary:	Interface for Samsung Uproar and Yepp
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Sound
URL:		http://www.cs.toronto.edu/~kal/sulu
Source:		http://www.cs.toronto.edu/~kal/sulu/%{name}-%{version}.tar.bz2
BuildRequires:	gtk-devel libusb-devel popt-devel

%description
Sulu is a GTK interface for transferring mp3's between your Samsung Uproar 
or Yepp and your Linux computer.

%prep
%setup -q

%build
make CFLAGS="$RPM_OPT_FLAGS" CPPFLAGS="$RPM_OPT_FLAGS"

%install
mkdir -p $RPM_BUILD_ROOT/%_bindir
cp %name $RPM_BUILD_ROOT/%_bindir

mkdir -p %{buildroot}%_menudir
cat << EOF > %{buildroot}%_menudir/%name
?package(sulu): \
  needs=x11 \
  section=Multimedia/Sound \
  title=Sulu \
  longtitle="GUI for Samsung Uproar and Yepp" \
  icon=sound_section.png \
  command=sulu \
  xdg="true"
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Sulu
Comment=GUI for Samsung Uproar and Yepp
Exec=%{_bindir}/sulu
Icon=sound_section
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Multimedia-Sound;AudioVideo;Audio;Player
EOF

%post
%update_menus

%postun 
%clean_menus

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc changelog COPYING README todo
%_bindir/%name
%_menudir/%name
%{_datadir}/applications/mandriva-%{name}.desktop

