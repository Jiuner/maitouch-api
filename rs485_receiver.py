import serial
import json
import time
import logging
from mqtt_publisher import publish_to_mqtt

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def parse_rs485_data(line):
    try:
        data = dict(item.split(":") for item in line.split(";"))
        return json.dumps(data)
    except Exception as e:
        logging.warning(f"Data parsing error: {e}")
        return None

def main():
    try:
        with open("config.json") as f:
            config = json.load(f)

        ser = serial.Serial(config["serial_port"], config["baudrate"], timeout=1)
        logging.info("RS-485 receiver started...")

        while True:
            try:
                line = ser.readline().decode("utf-8").strip()
                if line:
                    logging.debug(f"Raw data: {line}")
                    json_data = parse_rs485_data(line)
                    if json_data:
                        publish_to_mqtt(json_data)
            except Exception as e:
                logging.error(f"Unexpected error: {e}")
            time.sleep(0.1)

    except serial.SerialException as e:
        logging.critical(f"Serial port error: {e}")
    except Exception as e:
        logging.critical(f"Initialization error: {e}")

if __name__ == "__main__":
    main()
