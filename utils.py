import random

def sanitize(topic: str) -> str:
    return topic.split('/')[0]

def get_random_payload(device_versions):
    device = random.choice(list(device_versions.keys()))
    payload = random.choice(["online", "offline"])
    return device, payload