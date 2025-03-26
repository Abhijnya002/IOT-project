# IoT Environmental Monitoring System

## Overview

This project simulates an IoT-based environmental monitoring system. It involves virtual sensors (temperature, humidity, and CO2) that periodically generate random data within specified ranges. The data is published using the MQTT protocol to a cloud-based platform, ThingSpeak, for storage and visualization.

## Features

- Virtual sensors that simulate environmental data:
  - **Temperature**: Range between -50°C to 50°C
  - **Humidity**: Range between 0% to 100%
  - **CO2**: Range between 300 ppm to 2000 ppm
- MQTT protocol for lightweight communication between sensors and cloud platform.
- Cloud-based data storage and monitoring via ThingSpeak.
- Real-time display of sensor data through a custom Python script.
- Query for the latest sensor data or data from the past 5 hours.

## Setup Instructions

### Prerequisites

- Python 3.x
- MQTT client library (`paho-mqtt`)
- ThingSpeak account and channel

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Abhijnya002/IOT-project.git
2. Install the required dependencies:
pip install paho-mqtt

3. Create an account on ThingSpeak and create a new channel.

4. Replace the username, password, and channel_id in the Python scripts (publisher.py and subscriber.py) with your ThingSpeak credentials.

### Running the System
To publish sensor data to ThingSpeak, run the publisher.py script:

python publisher.py

To view the latest sensor data or data from the last 5 hours, run the subscriber.py script:
python subscriber.py

### Project Structure
publisher.py: Simulates virtual sensors and publishes data to ThingSpeak.
subscriber.py: Queries and displays sensor data from ThingSpeak.
sensor_log.txt: Log file storing the sensor data with timestamps.

