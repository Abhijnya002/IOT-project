import time
import random
import paho.mqtt.client as mqtt

# MQTT Broker and Credentials
BROKER = "mqtt3.thingspeak.com"
PORT = 1883
CLIENT_ID = "DDUQAgEZBwEnFRweJy8JAQE"
USERNAME = "DDUQAgEZBwEnFRweJy8JAQE"
PASSWORD = "D1JqNmT3rc4ossn6i0qWbpyu"
CHANNEL_ID = "2889202"

TOPIC = f"channels/{CHANNEL_ID}/publish"


mqtt_client = mqtt.Client(client_id=CLIENT_ID, protocol=mqtt.MQTTv311)
mqtt_client.username_pw_set(USERNAME, PASSWORD)
mqtt_client.connect(BROKER, PORT)

print("Connecting to ThingSpeak MQTT Broker...")
time.sleep(3)
print("Connection established! Ready to publish sensor data.")

while True:
    temp = round(random.uniform(-50, 50), 2)
    humidity_level = round(random.uniform(0, 100), 2)
    co2_level = random.randint(300, 2000)

    
    payload = f"field1={temp}&field2={humidity_level}&field3={co2_level}"

    result = mqtt_client.publish(TOPIC, payload)
    
    if result.rc == mqtt.MQTT_ERR_SUCCESS:
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        print(f"[{timestamp}] Data Published: Temperature = {temp}°C, Humidity = {humidity_level}%, CO2 = {co2_level} ppm")

        
        with open("sensor_log.txt", "a") as log_file:
            log_file.write(f"{timestamp},{temp},{humidity_level},{co2_level}\n")
    else:
        print("Data transmission failed. Retrying...")

    time.sleep(15)  
