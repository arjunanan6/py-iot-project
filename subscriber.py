import paho.mqtt.client as paho
from publisher import topics

def on_message(mosq, obj, msg):
    print(msg.topic, " ", msg.qos, msg.payload.decode("utf-8"))

def on_publish(mosq, obj, mid):
    pass


if __name__ == '__main__':
    client = paho.Client()
    client.on_message = on_message
    client.on_publish = on_publish

    client.connect("127.0.0.1", 1883, 60)

    for topic in topics:
        client.subscribe(topic, 0)

    while client.loop() == 0:
        pass
