#!/usr/bin/env bash
set -e

MEAS=$(/home/raleonardo/pi-env-monitor/dht22_get_env.py | jq '.' -Mc )
echo $MEAS

# setting farmos api variables
source /etc/pi-env-monitor/farmos_config.py

URL=${FARMOS_URL}/farm/sensor/listener/${FARMOS_API_PUB_KEY}?private_key=${FARMOS_API_PRIV_KEY}
#echo $URL

curl -H "Content-Type: application/json" -X POST -d $MEAS $URL

