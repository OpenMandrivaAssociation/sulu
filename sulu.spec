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



%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.17-6mdv2010.0
+ Revision: 434166
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.17-5mdv2009.0
+ Revision: 261216
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.17-4mdv2009.0
+ Revision: 253699
- rebuild
- drop old menu

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.17-2mdv2008.1
+ Revision: 140863
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
    - import sulu


* Tue Sep 05 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.17-2mdv2007.0
- XDG

* Mon Aug 29 2005 Austin Acton <austin@mandriva.org> 0.17-1mdk
- 0.17
- source URL

* Thu Feb 20 2004 Austin Acton <austin@mandrake.org> 0.16-3mdk
- rebuild

* Sat Aug 30 2003 Michael Scherer <scherer.michael@free.fr> 0.16-2mdk 
- BuildRequires popt-devel

* Mon Aug 25 2003 Austin Acton <aacton@yorku.ca> 0.16-1mdk
- 0.16

* Sat Mar 29 2003 Austin Acton <aacton@yorku.ca> 0.15-1mdk
- 0.15

* Mon Feb 24 2003 Austin Acton <aacton@yorku.ca> 0.11-1mdk
- 0.11

* Wed Feb 5 2003 Austin Acton <aacton@yorku.ca> 0.08-2mdk
- remove bad depends

* Sat Jan 11 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.08-1mdk
- 0.08

* Thu Dec 12 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.07-1mdk
- from Austin Acton <aacton@yorku.ca> :
	- initial build
