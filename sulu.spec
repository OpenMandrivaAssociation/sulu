%define name sulu
%define version 0.17
%define release %mkrel 6

Name:		%{name}
Summary:	Interface for Samsung Uproar and Yepp
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Sound
URL:		http://www.cs.toronto.edu/~kal/sulu
Source:		http://www.cs.toronto.edu/~kal/sulu/%{name}-%{version}.tar.bz2
BuildRequires:	gtk-devel libusb-devel popt-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

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

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun 
%clean_menus
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc changelog COPYING README todo
%_bindir/%name
%{_datadir}/applications/mandriva-%{name}.desktop

