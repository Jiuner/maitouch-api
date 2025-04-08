import paho.mqtt.client as mqtt
import json
import logging

logging.basicConfig(level=logging.INFO)

with open("config.json") as f:
    config = json.load(f)

client = mqtt.Client()
client.username_pw_set(config["mqtt_broker"], config.get("mqtt_password", ""))
client.connect(config["mqtt_broker"], 1883, 60)
client.loop_start()

def publish_to_mqtt(payload):
    logging.info(f"Publishing to {config['mqtt_topic']}: {payload}")
    client.publish(config["mqtt_topic"], payload)
