import random
import json
import os
import time


def sanitize(topic: str) -> str:
    """Sanitize helper.

    Args:
        topic (str): Topic to be sanitized.
        Ex: "device1/status" 

    Returns:
        str: returns "device1"
    """
    return topic.split("/")[0]


def fetch_json() -> dict:
    """JSON -> dict helper.

    Returns:
        dict: Returns a dict of devices.
    """
    with open(
        os.path.dirname(os.path.abspath(__file__)) + "/devices.json", "r"
    ) as file:
        data = json.load(file)
    return data


def update_device_info(device_name, status):
    """Update .json file helper.

    Args:
        device_name (str): The device ID.
        status (str): online/offline.
    """
    with open(
        os.path.dirname(os.path.abspath(__file__)) + "/devices.json", "r"
    ) as file:
        data = json.load(file)

    if device_name in data:
        data[device_name]["last_status"] = status
        data[device_name]["last_notification"] = time.strftime("%Y-%m-%d %H:%M:%S")

    with open("devices.json", "w") as file:
        json.dump(data, file, indent=4)
