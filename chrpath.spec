Summary: 	Dynamic library load path (rpath) alterer
Name: 		chrpath
Version: 	0.13
Release: 	12
Group: 		Development/Other
License: 	GPLv2
Url:		http://www.tux.org/pub/X-Windows/ftp.hungry.com/chrpath/
Source0:	http://www.tux.org/pub/X-Windows/ftp.hungry.com/chrpath/%{name}-%{version}.tar.bz2

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

