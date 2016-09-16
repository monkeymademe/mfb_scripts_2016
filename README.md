# mfb_scripts_2016
Makerfaire berlin scripts for 2016

## Setup launcher scripts

- Make launcher scripts
- 'mkdir logs' in /home/pi/
- run: sudo crontab -e
- insert this line: @reboot sh /home/pi/launcher.sh >/home/pi/logs/cronlog 2>&1

Done
