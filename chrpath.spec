Name: 		chrpath
Version: 	0.13
Release: 	%mkrel 6
Group: 		Development/Other
Summary: 	Dynamic library load path (rpath) alterer
Url:		http://www.tux.org/pub/X-Windows/ftp.hungry.com/chrpath/
Source:		%Url/%name-%version.tar.bz2
License: 	GPL
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot

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
rm -rf $RPM_BUILD_ROOT
%makeinstall 
rm -fr $RPM_BUILD_ROOT/usr/doc

%clean
rm -rf $RPM_BUILD_ROOT;

%files 
%defattr (-, root, root,755)
%doc AUTHORS ChangeLog COPYING NEWS README
%_bindir/chrpath
%_mandir/man1/chrpath.1*

