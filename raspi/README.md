# Raspberry Pi 

Developed for a Pi Zero W, but should work on the others as well. Just make 
sure any kind of internet connectivity is available.

## Install instructions

Used a Raspian image. 

to describe:

* enable SSH
* enable WiFi
* enable W1
* (depending on kernel version, use GPIO4 and GPIO17 for W1)

### Enable one wire on startup

The script `raspi/scripts/enable_w1.sh` enables W1 on GPIO 4 and 17. Start it on each startup, eg. via cronjob

```sh
crontab -e
@reboot /home/pi/temperature-sensor/raspi/scripts/enable_w1.sh
```
Adjust the path, if you cloned the repo somewhere else.

## Connect

On the same network, search for the Raspi:

```bash
arp -a
```

Connect with SSH:

```bash
ssh pi@<RASPI IP GOES HERE>
```


