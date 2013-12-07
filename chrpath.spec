Summary: 	Dynamic library load path (rpath) alterer
Name: 		chrpath
Version: 	0.15
Release: 	4
Group: 		Development/Other
License: 	GPLv2
Url:		https://alioth.debian.org/projects/chrpath/
Source0:	https://alioth.debian.org/frs/download.php/file/3648/%{name}-%{version}.tar.gz

%description
Chrpath allows you to modify the dynamic library load path (rpath) of
compiled programs.  Currently, only removing and modifying the rpath
is supported.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall 
rm -fr %{buildroot}/usr/doc

%files 
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/chrpath
%{_mandir}/man1/chrpath.1*

