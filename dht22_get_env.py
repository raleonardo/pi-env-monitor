#!/usr/bin/env python3

# import settings
import sys
sys.path.append('/etc/pi-env-monitor/')
from dht22_config import *

import time
import board
import adafruit_dht
import json

dht22 = adafruit_dht.DHT22( getattr(board, DHT22_DATA_PIN) )

for i in range (DHT22_READ_MAX_ATTEMPTS):
    try:
        meas = {}
        meas['temperature'] = dht22.temperature
        time.sleep(0.1)
        meas['humidity']    = dht22.humidity

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        #print(error.args[0])  # TODO: log this to stderr or log
        time.sleep(DHT22_READ_TIMEOUT)
        #continue
    except Exception as error:
        dht22.exit()
        raise error
    else:
        # print ( "Temperature: {0}C  Humidity: {1}%".format( meas['temperature'], meas['humidity'] ))
        print (json.dumps(meas))
        break

"""
TODO:
- include timespamp in json
- optionally update a local json file
"""
