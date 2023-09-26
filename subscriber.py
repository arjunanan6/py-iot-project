import paho.mqtt.client as paho
from publisher import topics
from utils import fetch_json, sanitize, update_device_info
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(filename)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def on_message(mosq, obj, msg):
    payload = msg.payload.decode("utf-8")
    logging.debug(f"{msg.topic} {msg.qos} {payload}")

    # Extract device name from the topic (assuming it's in the format "device_name/status")
    device_name = sanitize(msg.topic)

    # Update device information with the received status
    update_device_info(device_name, payload)

    # Fetch the latest device information
    device_data = fetch_json().get(device_name, {})
    software_version = device_data.get("software_version", "")
    last_status = device_data.get("last_status", "")
    last_notification = device_data.get("last_notification", "")

    # Log the latest device information with DEBUG level
    logger.info(f"Device ID: {device_name}")
    logger.info(f"Software Version: {software_version}")
    logger.info(f"Last Status: {last_status}")
    logger.info(f"Last Notification: {last_notification}")


if __name__ == "__main__":
    client = paho.Client()
    client.on_message = on_message

    client.connect("127.0.0.1", 1883, 60)

    for topic in topics:
        client.subscribe(topic, 0)

    while client.loop() == 0:
        pass
