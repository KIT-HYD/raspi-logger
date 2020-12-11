#!/bin/sh -e
#
# This File is not used anymore!
# Use the cli with sudo to enable pins like:
#
# python3 -m raspi_logger enable_w1 --gpio=[4,17]
#
# This script should be run on each system startup.
# You can define a cronjob:
#
# >> crontab -e
# >> @reboot /path/to/enable_w1.sh
#

# enable GPIO 4 and GPIO 17 for W1
dtoverlay w1-gpio gpiopin=4 pullup=0
dtoverlay w1-gpio gpiopin=17 pullup=0

exit 0
