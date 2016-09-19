#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /
cd home/pi/mfb_scripts_2016/print/
sudo python print_mfb.py
cd /
