Name: 		chrpath
Version: 	0.13
Release: 	%mkrel 12
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



%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.13-10mdv2011.0
+ Revision: 663374
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 0.13-9mdv2011.0
+ Revision: 603830
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 0.13-8mdv2010.1
+ Revision: 518990
- rebuild

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.13-7mdv2010.0
+ Revision: 413235
- rebuild

* Fri Dec 19 2008 Oden Eriksson <oeriksson@mandriva.com> 0.13-6mdv2009.1
+ Revision: 316199
- rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0.13-5mdv2009.0
+ Revision: 220572
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.13-4mdv2008.1
+ Revision: 140693
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Oct 12 2006 Oden Eriksson <oeriksson@mandriva.com>
+ 2006-10-11 12:43:26 (63461)
- use the mkrel macro

* Thu Oct 12 2006 Oden Eriksson <oeriksson@mandriva.com>
+ 2006-10-11 12:41:34 (63460)
Import chrpath

* Sat May 13 2006 Stefan van der Eijk <stefan@eijk.nu> 0.13-3mdk
- rebuild for sparc

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 0.13-2mdk
- Rebuild

* Thu Dec 02 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.13-1mdk
- new release

* Mon Dec 15 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.11-1mdk
- new release

* Thu Dec 11 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.11-1mdk
- new release
- remove patch0 (merged upstream)

