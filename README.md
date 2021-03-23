# Pi Env Monitor

Tool to monitor environment values (Temperature, Humidity [,Pressure]) from a raspberrypi zero, and upload it to farmos, google spreadsheets or (and) save it locally.

## Scripts:

- `dht22_get_env.py`

   Gets the temperature and humidity from a `DTH22` sensor connected to the Pi's `GPIO`.
   Outputs the measured values as `JSON` format to the `STDOUT`  *including timestamp?

   Configurations: *TODO: should they be in /etc/pi-env-monitor/dth22_config.py
   ```
   DHT22_DATA_PIN = "D4"         # Data pin in the GPIO where the DHT22 is connected
   DHT22_READ_TIMEOUT = 2        # Timeout in seconds
   DHT22_READ_MAX_ATTEMPTS = 5   #
   ```

 - `bme280_get_env.py`

    Gets the temperature, humidity and pressure from a `BME280` sensor connected to the Pi's `GPIO` (via `SPI` or `I2C`)
    Outputs the measured values as `JSON` format to the `STDOUT`

    Configurations: *TODO: should they be in /etc/pi-env-monitor/dth22.conf
    ```
    BME_CONNECTION = "spi" or "i2c" ??
    BME_CCONNECTION_PINS ??
    ...
    ```

 - `farmos_sensor_send.py`

    Gets values as JSON and sends them to a FarmOS Sensor API

    Configurations: *TODO: should they be in /etc/pi-env-monitor/farmos_config.py
    ```
    FARMOS_URL          = "https://myfarm.farmos.net"
    FARMOS_SENSOR_NAME  = "Greenhouse Sensor"                  #*maybe not needed
    FARMOS_API_PUB_KEY  = "a40b12d245a1cf13d3a9ba521389e669"
    FARMOS_API_PRIV_KEY = "a40b12d245a1cf13d3a9ba521389e669"
    ...
    ```


 ## TODO:
 - implement timestamp
 - error handling
    - printing errors into stderr
    - implement logger to /var/log/
 - configs as env variables?
    - Formatting the config files without spaces makes them python and bash compatible
 - Save data locally
    - append to a json file?
    - append to a csv file?
    - add to a sqlite?
    - enable this as an optional feature? -> argparse or from config file
    - lock the file when writing into it
 - send/update data from local file/db
    - does farmos support multiline json?: YES!!
    - check last written timestamp on target (GET) and then send data newer than that
    - then divide the data into chunks.

