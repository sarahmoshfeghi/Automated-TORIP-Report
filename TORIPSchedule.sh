#!/bin/bash

# Run Python from virtual environment
source /etc/venv/bin/activate
python3 /pathtoipblock/TORIP-Finder.py

ip_count=$(cat ip-block.csv | wc -l)

if [ $ip_count -gt 0 ]; then
    echo "Please Block these IP"
else
    echo "File ip-block.csv has no new ip ."
fi
