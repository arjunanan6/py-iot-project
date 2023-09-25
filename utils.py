import random
import json
import os
import time 

def sanitize(topic: str) -> str:
    return topic.split('/')[0]

def fetch_json() -> dict:
    with open(os.path.dirname(os.path.abspath(__file__))+"/devices.json", "r") as file:
        data = json.load(file)
    return data

def update_device_info(device_name, status):
    with open(os.path.dirname(os.path.abspath(__file__))+"/devices.json", "r") as file:
        data = json.load(file)
    
    if device_name in data:
        data[device_name]["last_status"] = status
        data[device_name]["last_notification"] = time.strftime("%Y-%m-%d %H:%M:%S")

    with open("devices.json", "w") as file:
        json.dump(data, file, indent=4)