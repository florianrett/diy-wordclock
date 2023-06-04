#! /bin/sh
echo "Starting WordClock"
datetime=$(date '+%Y_%m_%d__%H:%M:%S');
python main.py > log_${datetime}.txt
echo "Program stopped"

shutdown now