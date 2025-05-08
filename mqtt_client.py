import json
import django
import os
import paho.mqtt.client as mqtt

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mqtt_project.settings')
django.setup()

from sensor_data.models import SensorData
from datetime import datetime

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("iot/sensors/data")

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload)
        SensorData.objects.create(
            device_id=data["device_id"],
            timestamp=data["timestamp"],
            temperature=data["temperature"],
            humidity=data["humidity"],
            status=data["status"]
        )
        print("Data saved:", data)
    except Exception as e:
        print("Error:", e)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)
client.loop_forever()
