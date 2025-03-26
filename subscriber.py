from datetime import datetime, timedelta


CUTOFF_TIME = datetime.now() - timedelta(hours=5)


SENSOR_TYPE = input("Enter sensor type (temperature/humidity/co2): ").strip().lower()


valid_sensors = {"temperature", "humidity", "co2"}
if SENSOR_TYPE not in valid_sensors:
    print("Invalid sensor type! Please enter 'temperature', 'humidity', or 'co2'.")
    exit()


with open("sensor_log.txt", "r") as file:
    data_found = False 

    for line in file:
        timestamp_str, temp, hum, co2 = line.strip().split(",")
        timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")

        if timestamp >= CUTOFF_TIME:
            sensor_values = {"temperature": temp, "humidity": hum, "co2": co2}
            selected_value = sensor_values[SENSOR_TYPE]

            print(f"{timestamp.strftime('%Y-%m-%d %I:%M %p')} | {SENSOR_TYPE.upper()}: {selected_value}")
            data_found = True

    if not data_found:
        print(f"No recent {SENSOR_TYPE} data found in the last 5 hours.")
