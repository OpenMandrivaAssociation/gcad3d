%define		oname	gCAD3D

Name:		gcad3d
Version:	1.80
Release:	3
Summary:	A 3D CAD CAM application
Group:		Graphics
License:	Freeware
URL:		http://www.gcad3d.org/
# source is extracted from .deb packages in Downloads section
Source0:	%{name}-%{version}.tar.bz2
%rename		%{oname}

%description
gCAD3D is a 3D CAD CAM application that features an integrated 3D OpenGL
viewer, a program interpreter for geometry and NC-commands in 3D, an 
integrated NC-processor, and a programming interface for user programs.

It can
-Import and display data from Iges, Step, wire frame and solid objects 
-Create and modify wire frame elements
-Create surfaces
-Create simple solid bodies
-Assemble user-created ancillary programmes
-Export wire frame elements as DXF and Iges
-Export surfaces as Vrml-1, Vrml-2, obj, tw Iges

It cannot yet
-Blend or modify surfaces
-Create or modify complex solid bodies

%prep
%setup -q

%build
%__cat > %{name}.desktop <<@@@
[Desktop Entry]
Name=gCAD3D
Encoding=UTF-8
Exec=gCAD3D
Icon=/usr/share/pixmaps/gCAD3D.xpm
Comment=A 3D CAD CAM application
Type=Application
Categories=Graphics;
Terminal=false
@@@

%install
%__rm -rf %{buildroot}

%__mkdir_p %{buildroot}%{_prefix}
%ifarch x86_64
%__cp -r %{oname}-%{version}-64/* %{buildroot}/
%else
%__cp -r %{oname}-%{version}-32/* %{buildroot}/
%endif

%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<@@@
[Desktop Entry]
Name=gCAD3D
Exec=%{name}
Icon=%{_datadir}/%{name}/icons/%{oname}.xpm
Comment=A 3D CAD CAM application
Type=Application
Categories=Graphics;
Terminal=false
@@@

%__rm -rf %{buildroot}%{_datadir}/menu

%clean
%__rm -rf %{buildroot}

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_prefix}/lib/%{oname}
%{_docdir}/%{name}

