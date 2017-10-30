Summary: usb-modeswitch is  a mode switching tool for controlling "flip flop" (multiple device) USB gear
Name: usb-modeswitch
Version: 2.2.0
Release: alt0.M70C.1
License: GPL

Group: System/Configuration/Hardware
Url: http://www.draisberghof.de/usb_modeswitch/

Source: %name-%version.tar

Patch: usb_modeswitch_dispatcher-old-kernels.patch
Patch1: systemd-detection.patch

Requires: usb-modeswitch-data
BuildRequires: tcl libusb-devel
Provides: usb_modeswitch
Obsoletes: usb_modeswitch

%description
USB_ModeSwitch is (surprise!) a mode switching tool for controlling
"flip flop" (multiple device) USB gear.
Several new USB devices (especially high-speed wireless WAN stuff, there
seems to be a chipset from Qualcomm offering that feature) have their
MS Windows drivers onboard; when plugged in for the first time they act
like a flash storage and start installing the driver from there.
After that (and on every consecutive plugging) this driver switches the
mode internally, the storage device vanishes (in most cases), and a new
device (like a USB modem) shows up. The WWAN gear maker Option calls
that feature "ZeroCD (TM)".

Needed for MTS (and others) branded e1550 modems.

%prep
%setup
%patch
%patch1 -p2

%build
%make

%install
DESTDIR=%buildroot make install

%files
%doc ChangeLog README
%_sbindir/*
%_man1dir/*
%_sysconfdir/*
/lib/udev/*
%_localstatedir/usb_modeswitch
%_unitdir/*

%changelog
* Mon Oct 30 2017 Lenar Shakirov <snejok@altlinux.ru> 2.2.0-alt0.M70C.1
- Backport to C7

* Wed Nov 05 2014 Andrey Cherepanov <cas@altlinux.org> 2.2.0-alt0.M70P.1
- Backport new version to p7 branch

* Wed Nov 05 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Mon May 05 2014 Andrey Cherepanov <cas@altlinux.org> 2.1.1-alt0.M70P.1
- Backport to p7 branch

* Mon May 05 2014 Andrey Cherepanov <cas@altlinux.org> 2.1.1-alt1
- New version

* Wed Jan 15 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2.0.1-alt1
- 2.0.1

* Fri Nov 16 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.2.5-alt1
- 1.2.5

* Mon Oct 22 2012 Lenar Shakirov <snejok@altlinux.ru> 1.2.4-alt2
- turn on findreq and findprov

* Mon Oct 22 2012 Lenar Shakirov <snejok@altlinux.ru> 1.2.4-alt1
- 1.2.4

* Mon Oct 22 2012 Lenar Shakirov <snejok@altlinux.ru> 1.2.3-alt3
- %_localstatedir/usb_modeswitch packaged (ALT #27874)

* Mon Oct 22 2012 Lenar Shakirov <snejok@altlinux.ru> 1.2.3-alt2
- make work on old kernels (older than 2.6.27)

* Thu Aug 09 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.2.3-alt1
- 1.2.3

* Fri Jul 01 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.1.8-alt1
- 1.1.8 by manowar@

* Mon Feb 21 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.1.6-alt1
- 1.1.6

* Fri Dec 17 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.1.5-alt2
- 1.1.5

* Mon Sep 20 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.1.4-alt2
- dependence on usb-modeswitch-data added
- provides & obsoletes

* Fri Sep 17 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.1.4-alt1
- first build

