from controll_start import *
import paho.mqtt.publish as publish
from mqtt.start_mqtt import *


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        command = msg.payload.decode("utf-8")
        print(f"received {command}")
        direction = command.split(" ")[0]
        if "left" in direction.contains():
            backwards(steps, hor)
        elif "right" in direction.contains():
            forward(steps, hor)
        elif "up" in direction.contains():
            forward(steps, ver)
        elif "down" in direction.contains():
            backwards(steps, ver)

        if "neutral" not in direction:
            host = "10.7.129.102"
            publish.single(topic="/control_camera", payload="done", hostname=host)

    client.subscribe(topic)
    client.on_message = on_message


client = connect_mqtt()
subscribe(client)
client.loop_start()

try:
    while True:
        pass
except KeyboardInterrupt:
    print("Encerrando...")
    client.loop_stop()
    client.disconnect()
    GPIO.cleanup()
