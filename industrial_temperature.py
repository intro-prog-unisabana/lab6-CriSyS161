def trigger_alarm(temperatures, threshold = 80):
    triggered_sensors = []
    for sensor, temp in temperatures.items():

