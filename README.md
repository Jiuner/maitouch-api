# maitouch-api

A Python-based open-source gateway for receiving RS-485 data and publishing to MQTT, designed for m'AI Touch sensor integration in smart building applications.

## Features
- RS-485 serial data acquisition
- Real-time JSON conversion
- MQTT publishing for IoT integration
- Includes example for robot-to-elevator communication

## Usage
1. Configure `config.json` for your device and broker.
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `python rs485_receiver.py`
4. Use `robot_mqtt_example.py` to test elevator commands via MQTT.

## Contact
For API access or MQTT broker credentials, please contact m'AI Touch Technology Co., Ltd.
