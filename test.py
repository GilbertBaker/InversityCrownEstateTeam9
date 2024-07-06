import requests
import json
import numpy as np
csv = open('test2.csv', 'w')

items = []
key = "TCQHk4cGQAZp4vQ8y6wEEXUtI0Zc2K28"
url = "https://api.windy.com/api/point-forecast/v2"

def calculate_means(data):
    try:
        waves_height_surface = data['waves_height-surface']
        waves_period_surface = data['waves_period-surface']
        waves_direction_surface = data['waves_direction-surface']

        # Calculate mean temperature
        mean_height = np.mean(waves_height_surface)

        # Calculate mean gust
        mean_period = np.mean(waves_period_surface)

        # Calculate wind speed from u and v components
        mean_direction = np.mean(waves_direction_surface)



        return mean_height, mean_period, mean_direction
    except:
        return 0,0,0

# -2,61 to 8,49
for x in range(-8,2):
    for y in range(49, 61):
        parms = {
            "lat": y,
            "lon": x,
            "model": "gfsWave",
            "parameters": ["waves"],
            "levels": ["surface"],
            "key": key
        }
        # request the params
        response = requests.post(url, json=parms)
        # get the json data
        mean_height, mean_period, mean_direction = calculate_means(response.json())
        # append the data to the items list
        print("DONE"+str(x)+","+str(y)+","+str(mean_height)+","+str(mean_period)+","+str(mean_direction))
        items.append(f"{x},{y},{mean_height},{mean_period},{mean_direction}")




# write all items to csv file
csv.write("\n".join(items))
csv.close()

