#!/bin/sh
# part of usb_modeswitch 2.6.0
device_in()
{
	if [ ! -e /var/lib/usb_modeswitch/$1 ]; then
		return 0
	fi
	while read line
	do
		if [ $(expr "$line" : "$2:$3") != 0 ]; then
			return 1
		fi
	done </var/lib/usb_modeswitch/$1
	if [ $(expr "$line" : "$2:$3") != 0 ]; then
		return 1
	fi
	return 0
}

if [ $(expr "$1" : "--.*") ]; then
	p_id=$4
	if [ -z $p_id ]; then
		prod=$5
		if [ -z $prod ]; then
			prod=$3
		fi
		prod=${prod%/*}
		v_id=0x${prod%/*}
		p_id=0x${prod#*/}
		if [ "$v_id" = "0x" ]; then
			v_id="0"
			p_id="0"
		fi
		v_id="$(printf %04x $(($v_id)))"
		p_id="$(printf %04x $(($p_id)))"
	else
		v_id=$3
	fi
fi
PATH=/sbin:/usr/sbin:$PATH
case "$1" in
	--driver-bind)
		# driver binding code removed
		exit 0
		;;
	--symlink-name)
		device_in "link_list" $v_id $p_id
		if [ "$?" = "1" ]; then
			if [ -e "/usr/sbin/usb_modeswitch_dispatcher" ]; then
				exec usb_modeswitch_dispatcher $1 $2 2>>/dev/null
			fi
		fi
		exit 0
		;;
esac

# ${1##*/} is the last component of the device "path";
# it must be a complete designation of the device.
# (usb_modeswitch_dispatcher cuts the --switch-mode parameter into parts
# delimited by ":" and takes the first one as the top part.
# The systemd service calls usb_modeswitch_dispatcher the same way as the last
# command here and passes the suffix of the service name as the parameter.)

PATH=/bin:/sbin:/usr/bin:/usr/sbin
if sd_booted; then
	exec systemctl --no-block restart usb_modeswitch@"${1##*/}".service
else
	# only old distros, new udev will kill all subprocesses
	exec 1<&- 2<&- 5<&- 7<&-
	exec usb_modeswitch_dispatcher --switch-mode "${1##*/}"
fi
