import paho.mqtt.publish as publish


def send_message(direction, speed):
    host = "10.7.129.102"
    publish.single(
        topic="/control_camera", payload=f"{direction} {speed}", hostname=host
    )
