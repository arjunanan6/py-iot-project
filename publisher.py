import paho.mqtt.publish as publish
import random
import time
from devices import device_info


topics = [device_name + "/status" for device_name in device_info.keys()]

HOST = "localhost"


if __name__ == "__main__":
    while True:
        # Randomly send single or multiple messages.
        mode = random.choice(["single", "multiple"])
        if mode == "single":
            # Publish a single message
            random_topic = random.choice(topics)
            payload = random.choice(["online", "offline"])
            publish.single(topic=random_topic, payload=payload, hostname=HOST)

        elif mode == "multiple":
            # Randomly publish multiple messages and update device inventory.
            for topic in topics:
                payload = random.choice(["online", "offline"])
                publish.single(topic=topic, payload=payload, hostname=HOST)

        time.sleep(5)
