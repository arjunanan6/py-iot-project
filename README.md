# py-iot-project
A Python IoT mockup


A simple application that imitates the publish-subscribe model of IoT sensors.

## Components

- `Broker`: [Mosquitto](http://mosquitto.org/) is used as a message broker to interpret MQTT traffic to allow mocked publish/subscribes.
- `Broker`: [Mosquitto](http://mosquitto.org/) is used as a message broker to interpret MQTT traffic to allow mocked publish/subscribes.
- `subscriber.py`: Subscribes to a set of topics, in this case, deviceID/status. Once read, devices.json is updated with the last timestamp. devices.json here serves as a local database. The subscriber also logs this information to the console.
- `publisher.py`: Publishes anywhere between 1 or 5 topics on random.
- `web.py`: Simple page in Flask that reads from the json file and displays device information.

![image](https://github.com/arjunanan6/py-iot-project/assets/102953522/801c050c-0ac0-4a64-9eb8-2a50bf7bc69f)


## Usage
- Set up a python virtual environment and run: `make install` to install all requirements.
- Run mosquitto, subscriber.py, and then publisher.py
- Logs are generated in subscriber.py
- Run web.py, and visit http://127.0.0.1:5000/ to see a minimal UI showing status.

## Current Assumptions
- Only dynamic field on device state is: Online/Offline status.
- Software version remains static.


## Future improvements
- Switch from file based status updates to sqlite/duckDB, or any other lightweight database.
- Build a simple UI with fastAPI/django that reads off of the DB to show device list and status. 
- Save application logs to a physical file.
- Understand envryption standards.
