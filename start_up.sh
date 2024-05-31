#!/usr/bin/bash

## journalctl -u mosquitos_start.service
## precisa navegar até o script para executar

ls

sudo ntpdate -u pool.ntp.org

cd /home/bgbc1/proc_local

./frame.out

#!/bin/bash

# Define the threshold time (24-hour format)
HOUR_THRESHOLD=23
MINUTE_THRESHOLD=50

# Get the current hour and minute
CURRENT_HOUR=$(date +%H)
CURRENT_MINUTE=$(date +%M)

# Define the scripts to execute
SCRIPT_BEFORE="./fotos_temp.sh"
SCRIPT_AFTER="./coleta_aqua.sh"

# Check if the current time is past the threshold
if [ "$CURRENT_HOUR" -gt "$HOUR_THRESHOLD" ] || { [ "$CURRENT_HOUR" -eq "$HOUR_THRESHOLD" ] && [ "$CURRENT_MINUTE" -ge "$MINUTE_THRESHOLD" ]; }; then
    echo "It's past the threshold time. Executing coleta_aqua.sh."
    bash "$SCRIPT_AFTER"
else
    echo "It's before the threshold time. Executing ./fotos_temp.sh ."
    bash "$SCRIPT_BEFORE"
fi
