#!/bin/sh -e
#
# Start One Wire protocol
#
# This script should can to the /etc/rc.local to be run
# on each system startup. Alternatively, define a cronjob:
#
# >> crontab -e
# >> @reboot /path/to/enable_w1.sh
#

# enable GPIO 4 and GPIO 17 for W1
dtoverlay w1-gpio gpiopin=4 pullup=0
dtoverlay w1-gpio gpiopin=17 pullup=0

exit 0
