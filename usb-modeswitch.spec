Summary: usb-modeswitch is  a mode switching tool for controlling "flip flop" (multiple device) USB gear
Name: usb-modeswitch
Version: 2.6.0
Release: alt1
License: GPL-2.0-or-later

Group: System/Configuration/Hardware
Url: http://www.draisberghof.de/usb_modeswitch/

Source: %name-%version.tar

# is needed service >= 0.5.24 (sd_booted is used)
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
#patch1 -p2

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

%package with-sysvinit-checkinstall
Summary: install %name together with sysvinit (to check comaptibility)
Group: Other
BuildArch: noarch
Requires: sysvinit
Requires: %name = %EVR
%files with-sysvinit-checkinstall
%description with-sysvinit-checkinstall
%summary.

We are afraid that some scripts included in %name would produce
auto-dependencies on some systemd-specific utilities, which would
be incompatible with a SysV init system. Such dependencies of
%name package would be incorrect, since the use of such utilities
by %name is optional (i.e., only for the case when used in a system
where systemd is active).

Checking that this package can be susccessfully installed (as done
by Girar) would detect such packaging errors.

%package with-systemd-checkinstall
Summary: install %name together with systemd (to check comaptibility)
Group: Other
BuildArch: noarch
Requires: systemd
Requires: %name = %EVR
%files with-systemd-checkinstall
%description with-systemd-checkinstall
%summary.

Checking that this package can be successfully installed (as done by Girar)
would detect some packaging errors of %name that could be an obstacle
for using %name in a system with systemd.

%package without-systemd-utils-checkinstall
Summary: install %name without systemd-utils (to check for excessive deps)
Group: Other
BuildArch: noarch
Conflicts: systemd-utils
Requires: %name = %EVR
%files without-systemd-utils-checkinstall
%description without-systemd-utils-checkinstall
%summary.

A dependency of %name on systemd-utils would be excessive, since these
specifc uitilities are optionally used by %name (in the specific case
when systemd is active in the system). So, it would be unwanted for some
use cases to have such a dependency. (Even though installing systemd-utils
doesn't imply having systemd installed, some may consider systemd-utils
to be an excessive package in their systemd-free system.)

Checking that this package can be successfully installed (as done by Girar)
would confirm that there is no such dependency.

%changelog
* Mon Feb 10 2020 Sergey Y. Afonin <asy@altlinux.org> 2.6.0-alt1
- 2.6.0 (ALT #33493)
- updated License tag to SPDX syntax
- updated systemd-detection.patch

* Thu May 12 2016 Mikhail Efremov <sem@altlinux.org> 2.3.0-alt2
- Fix systemd-detection.patch.

* Thu May 05 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 2.3.0-alt1
- 2.3.0

* Wed Nov 05 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2.2.0-alt1
- 2.2.0

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

