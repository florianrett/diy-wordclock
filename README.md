# diy-wordclock

my attempt to build a cheaper version of the [QLOCKTWO](https://qlocktwo.com/)

repository contains planning files, "engineering" files and the actual clock code

## Raspberry Pi startup script
To start the wordclock program when the Raspberry Pi boots it has to be setup in rc.local:
Edit the file using ´sudo nano /etc/rc.local´ and add line ´sudo /home/pi/WordClock/start.sh &´
