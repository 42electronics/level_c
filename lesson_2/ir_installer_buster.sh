#!/bin/bash
#Installation script created by modifying Adafruit's pi-eyes.sh installer script located at
#https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/pi-eyes.sh
#This installer is for the Buster version of Raspbian

if [ $(id -u) -ne 0 ]; then
	echo "Installer must be run as root."
	echo "Try 'sudo bash $0'"
	exit 1
fi

clear
echo "EXISTING INSTALLATION, IF ANY, WILL BE OVERWRITTEN."
echo "This script installs the lirc IR package and makes"
echo "the needed changes to config and startup files to"
echo "allow for IR input on GPIO23 and output on GPIO22."
echo "The default lirc config file is overwritten with"
echo "one that has been pre-programmed with the values"
echo "for a generic 17-button remote similar to"
echo "https://www.amazon.com/WINGONEER-Infrared-Wireless-Control-Arduino/dp/B06XHGJG7Q"
echo
echo -n "CONTINUE? [y/N] "
read
if [[ ! "$REPLY" =~ ^(yes|y|Y)$ ]]; then
	echo "Canceled."
	exit 0
fi

reconfig() {
	grep $2 $1 >/dev/null
	if [ $? -eq 0 ]; then
		# Pattern found; replace in file
		sed -i "s|$2|$3|g" $1 >/dev/null
		echo "$1 updated"
	else
		# Not found; show error
		echo "Line to modify not found, $1 not changed"
	fi
}

apt-get install -y --force-yes lirc

curl -LO https://raw.githubusercontent.com/42electronics/level_c/master/lesson_2/lircd.conf
mv lircd.conf /etc/lirc/lircd.conf
curl -LO https://raw.githubusercontent.com/42electronics/level_c/master/lesson_2/lirc_options.conf
mv lirc_options.conf /etc/lirc/lirc_options.conf

apt-get install -y --force-yes lirc

reconfig /boot/config.txt "#dtoverlay=gpio-ir,gpio_pin=17" "dtoverlay=gpio-ir,gpio_pin=23"

# PROMPT FOR REBOOT --------------------------------------------------------

echo "Done."
echo
echo "Settings take effect on next boot."
echo
echo -n "REBOOT NOW? [y/N] "
read
if [[ ! "$REPLY" =~ ^(yes|y|Y)$ ]]; then
	echo "Exiting without reboot."
	exit 0
fi
echo "Reboot started..."
reboot
exit 0