# diy-wordclock

my attempt to build a cheaper version of the [QLOCKTWO](https://qlocktwo.com/)

repository contains planning files, "engineering" files and the actual clock code

## Raspberry Pi startup script
To start the wordclock program when the Raspberry Pi boots it needs both the start.sh script in the same folder as main.py and the wordclock.service (edited with adjusted path) installed and enabled with systemd.
This allows hotreloading clock code during live operation as well as shutting down the Pi when properly quitting via button 4