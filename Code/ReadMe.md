# DIY Wordclock
DIY project to build a wall clock that displays time using natural language, similar to the original [QLOCKTWO](https://qlocktwo.com/).

TODO:
- Documentation
- Move remaining project files into repository

## Raspberry Pi startup script
To start the wordclock program when the Raspberry Pi boots it has to be setup in rc.local:
Edit the file using ´sudo nano /etc/rc.local´ and add line ´sudo /home/pi/WordClock/start.sh &´