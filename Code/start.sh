#! /bin/sh
echo "Starting WordClock"
datetime=$(date '+%Y_%m_%d__%H:%M:%S');

# change working directory to script folder
cd $(dirname -- "$0";)

python main.py > logs/log_${datetime}.txt
echo "Program stopped"

shutdown now
