#A simulation of the minor project's working of the hardware
#Using MQTT protocol, sending the cylinder's calibrated reading to the MQTT
#MQTT is Message Query Telematry Transport Protocol
#The cylinder data is published, the subscriber will receive it's signal.
# Use sudo pip3 install paho-mqtt
#Check readings @ http://www.hivemq.com/demos/websocket-client/
import paho.mqtt.client as paho #paho library of Python
import time
import random

client = paho.Client("Cylinder Data") #Client Broker
client.connect("broker.hivemq.com") #Connecting to MQTT
random.seed(100)

while(True):
    cylinder_weight=random.randint(20,40) #Randomly generating values
    client.publish("CYLINDER WEIGHT:",cylinder_weight) #Publishing the values
    print("Printed value - "+str(cylinder_weight)) #Reference
    print("----------------------------")
    time.sleep(5)