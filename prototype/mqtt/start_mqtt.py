import random
from paho.mqtt import client as mqtt_client

# broker = 'localhost'
broker = "10.7.129.102"
port = 1883
topic = "/control_camera"
# Generate a Client ID with the subscribe prefix.
client_id = f"subscribe-{random.randint(0, 100)}"


# username = 'emqx'
# password = 'public'
def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION1, client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        global _await
        if msg.payload.decode("utf-8") == "done":
            _await = True
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message
