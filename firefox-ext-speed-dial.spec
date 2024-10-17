%define realname speed_dial

Summary: Speed dial extension for firefox
Name: firefox-ext-speed-dial
Version: 0.9.5.9
Release: 4
License: MPLv1.1 or GPLv2+ or LGPLv2+
Group: Networking/WWW
URL: https://speeddial.uworks.net/
Source: http://speeddial.uworks.net/speed_dial-%version-fx.xpi
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Requires: firefox >= %{firefox_version}
Obsoletes: %{name} < %{version}-%{release}
BuildRequires: firefox-devel

%description
With Speed Dial, you can easily access your most used websites. To show
the Speed Dial tab, use the Speed Dial button (which can be added to the
toolbar), or enter "chrome://speeddial/content" in your location bar.

To assign one website to Speed Dial, use the new "Set as Speed Dial"
option in the bookmarks menu, or right click on the tab you want to add,
and choose "Set as Speed Dial". That option is also available in the
contextual area menu.

%prep
%setup -q -c -n %{name}-%{version}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{firefox_extdir}

hash="$(sed -n '/.*em:id="\(.*\)"/{s//\1/p;q}' install.rdf)"
if [ -z "$hash" ]; then
    hash="$(sed -n '/.*em:id>\(.*\)<\/em:id>.*/{s//\1/p;q}' install.rdf)"
fi
if [ -z "$hash" ]; then
    echo "Failed to find plugin hash."
    exit 1
fi
extdir="%{firefox_extdir}/$hash"
mkdir -p "%{buildroot}$extdir"
cp -af * "%{buildroot}$extdir/"

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%{firefox_extdir}/*


%changelog
* Sun Mar 20 2011 Funda Wang <fwang@mandriva.org> 0.9.5.9-2mdv2011.0
+ Revision: 647133
- obsolete old package

* Fri Jan 28 2011 Funda Wang <fwang@mandriva.org> 0.9.5.9-1
+ Revision: 633597
- New version 0.9.5.9

* Wed Jan 05 2011 Thierry Vignaud <tv@mandriva.org> 0.9.5.1-5mdv2011.0
+ Revision: 628875
- rebuild for new firefox

* Sun Nov 14 2010 Thierry Vignaud <tv@mandriva.org> 0.9.5.1-4mdv2011.0
+ Revision: 597403
- rebuild for new firefox

  + Ahmad Samir <ahmadsamir@mandriva.org>
    - rebuild for firefox-3.6.8

* Tue Jul 27 2010 Funda Wang <fwang@mandriva.org> 0.9.5.1-3mdv2011.0
+ Revision: 561157
- rebuild for ff 3.6.8

* Mon Jun 28 2010 Frederic Crozat <fcrozat@mandriva.com> 0.9.5.1-2mdv2010.1
+ Revision: 549361
- rebuild with FF 3.6.6

* Sun Apr 04 2010 Funda Wang <fwang@mandriva.org> 0.9.5.1-1mdv2010.1
+ Revision: 531261
- update to new version 0.9.5.1

* Sun Apr 04 2010 Funda Wang <fwang@mandriva.org> 0.9.1.1-6mdv2010.1
+ Revision: 531094
- rebuild

* Wed Mar 24 2010 Funda Wang <fwang@mandriva.org> 0.9.1.1-5mdv2010.1
+ Revision: 527010
- rebuild

* Fri Jan 22 2010 Funda Wang <fwang@mandriva.org> 0.9.1.1-4mdv2010.1
+ Revision: 494801
- rebuild

* Sun Dec 20 2009 Funda Wang <fwang@mandriva.org> 0.9.1.1-3mdv2010.1
+ Revision: 480375
- rebuild for ff 3.6b5

* Tue Nov 10 2009 Funda Wang <fwang@mandriva.org> 0.9.1.1-2mdv2010.1
+ Revision: 463979
- rebuild for new ff

* Wed Sep 16 2009 Funda Wang <fwang@mandriva.org> 0.9.1.1-1mdv2010.0
+ Revision: 443395
- new version 0.9.1.1

* Tue Aug 18 2009 Gustavo De Nardin <gustavodn@mandriva.com> 0.9.1-2mdv2010.0
+ Revision: 417674
- buildrequire firefox-devel, which provides the new macros for building extensions
- make use of the firefox package macros
- rebuild for firefox 3.5.2

* Thu Aug 06 2009 Funda Wang <fwang@mandriva.org> 0.9.1-1mdv2010.0
+ Revision: 410561
- new version 0.9.1

* Wed Jul 22 2009 Raphaël Gertz <rapsys@mandriva.org> 0.9.0.8-2mdv2010.0
+ Revision: 398547
- Rebuild
- Update firefox version

* Sun Jun 14 2009 Funda Wang <fwang@mandriva.org> 0.9.0.8-1mdv2010.0
+ Revision: 385778
- New version 0.9.0.8

* Fri May 01 2009 Funda Wang <fwang@mandriva.org> 0.9.0.3-1mdv2010.0
+ Revision: 369815
- New version 0.9.0.3

* Sat Mar 28 2009 Gustavo De Nardin <gustavodn@mandriva.com> 0.7.2.12-3mdv2009.1
+ Revision: 361854
- rebuild for firefox 3.0.8

* Thu Mar 12 2009 Funda Wang <fwang@mandriva.org> 0.7.2.12-2mdv2009.1
+ Revision: 354099
- rebuild

* Wed Feb 04 2009 Funda Wang <fwang@mandriva.org> 0.7.2.12-1mdv2009.1
+ Revision: 337341
- New version 0.7.2.12

* Thu Dec 25 2008 Funda Wang <fwang@mandriva.org> 0.7.2.7-2mdv2009.1
+ Revision: 318917
- rebuild for new ff

* Sun Nov 16 2008 Funda Wang <fwang@mandriva.org> 0.7.2.7-1mdv2009.1
+ Revision: 303685
- new version 0.7.2.7

* Mon Sep 29 2008 Funda Wang <fwang@mandriva.org> 0.7.2-2mdv2009.0
+ Revision: 289173
- rebuild for new FF

* Tue Aug 05 2008 Funda Wang <fwang@mandriva.org> 0.7.2-1mdv2009.0
+ Revision: 263654
- import firefox-ext-speed-dial


