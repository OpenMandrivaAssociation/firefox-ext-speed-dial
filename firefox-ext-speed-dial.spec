%define ff_epoch 0
%define ff_ver 3.0.7
%define realname speed_dial

%define _mozillapath %{_libdir}/firefox-%{ff_ver}
%define _mozillaextpath %{_mozillapath}/extensions

Summary: Speed dial extension for firefox
Name: firefox-ext-speed-dial
Version: 0.7.2.12
Release: %mkrel 2
License: MPLv1.1 or GPLv2+ or LGPLv2+
Group: Networking/WWW
URL: http://speeddial.uworks.net/
Source: http://speeddial.uworks.net/speed_dial-%version-fx.xpi
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: mozilla-firefox = %{ff_epoch}:%{ff_ver}

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

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_mozillaextpath}

hash="$(sed -n '/.*em:id="\(.*\)"/{s//\1/p;q}' install.rdf)"
if [ -z "$hash" ]; then
    hash="$(sed -n '/.*em:id>\(.*\)<\/em:id>.*/{s//\1/p;q}' install.rdf)"
fi
if [ -z "$hash" ]; then
    echo "Failed to find plugin hash."
    exit 1
fi
extdir="%{_mozillaextpath}/$hash"
mkdir -p "%{buildroot}$extdir"
cp -af * "%{buildroot}$extdir/"

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%dir %_mozillapath
%{_mozillaextpath}
