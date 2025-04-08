"""
Robot → Elevator MQTT Communication Script
-------------------------------------------
This script demonstrates how a robot can send commands to an elevator system via MQTT protocol
using a secure WebSocket connection. For actual deployment, please configure MQTT credentials
and broker address securely through environment variables or a separate config file.
"""

import time
import logging
import ssl
import json
import paho.mqtt.client as mqtt

BROKER_ADDRESS = "your-broker-address"
BROKER_PORT = 8883
MQTT_TOPIC = "elevator/control"
MQTT_USERNAME = "your-username"
MQTT_PASSWORD = "your-password"
MQTT_CLIENT_ID = f"robot-elevator-client-{int(time.time())}"

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        logging.info("Successfully connected to MQTT broker.")
    else:
        logging.error(f"Failed to connect, return code {rc}")

def on_publish(client, userdata, mid):
    logging.info(f"Message published. MID: {mid}")

client = mqtt.Client(client_id=MQTT_CLIENT_ID, transport="websockets")
client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
client.tls_set(cert_reqs=ssl.CERT_NONE)
client.tls_insecure_set(True)

client.on_connect = on_connect
client.on_publish = on_publish
client.connect(BROKER_ADDRESS, BROKER_PORT, keepalive=60)
client.loop_start()

def send_elevator_command(command_code):
    if isinstance(command_code, int) and 1 <= command_code <= 15:
        payload = json.dumps({"command": command_code})
        result = client.publish(MQTT_TOPIC, payload, qos=2)
        logging.info(f"Command {command_code} sent with result: {result.rc}")
    else:
        logging.warning("Invalid command. Must be integer from 1 to 15.")

if __name__ == '__main__':
    time.sleep(2)
    send_elevator_command(5)  # go to 5F
    send_elevator_command(2)  # open door
