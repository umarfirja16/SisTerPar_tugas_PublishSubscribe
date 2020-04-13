import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("message received", str(message.payload.decode("utf-8")))
    #print("message topic = ", message.topic)
    #print("message qos = ", message.qos)
    #print("message retain flag = ", message.retrain)

broker_address="localhost"

print("creating new instance")
client = mqtt.Client("P1")

client.on_message = on_message

print("connecting to broker")

client.connect(broker_address, port = 1883)

client.loop_start()

print("subscribing to topic","house/bulbs/bulb1")
client.subscribe("house/bulbs/bulb1")

print("publishing message to topic","house/bulbs/bulb1")
client.publish("house/bulbs/bulb1","OFF")

time.sleep(1)
client.loop_stop()

