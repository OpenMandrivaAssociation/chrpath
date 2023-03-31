Summary:	Dynamic library load path (rpath) alterer
Name:		chrpath
Version:	0.16
Release:	2
Group:		Development/Other
License:	GPLv2
Url:		https://alioth.debian.org/projects/chrpath/
Source0:	http://cdn-fastly.deb.debian.org/debian/pool/main/c/chrpath/%{name}_%{version}.orig.tar.gz

%description
Chrpath allows you to modify the dynamic library load path (rpath) of
compiled programs.  Currently, only removing and modifying the rpath
is supported.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install 
rm -fr %{buildroot}/usr/doc

%files 
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/chrpath
%{_mandir}/man1/chrpath.1*
