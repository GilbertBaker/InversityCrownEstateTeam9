import requests
import json
import numpy as np
csv = open('test.csv', 'w')

items = []
key = "TCQHk4cGQAZp4vQ8y6wEEXUtI0Zc2K28"
url = "https://api.windy.com/api/point-forecast/v2"

def calculate_means(data):
    wind_u = data['wind_u-surface']
    wind_v = data['wind_v-surface']
    gust = data['gust-surface']
    temp = data['temp-surface']
    
    # Calculate mean temperature
    mean_temp = np.mean(temp)
    
    # Calculate mean gust
    mean_gust = np.mean(gust)
    
    # Calculate wind speed from u and v components
    wind_speed = np.sqrt(np.array(wind_u)**2 + np.array(wind_v)**2)
    
    # Calculate mean wind speed
    mean_wind = np.mean(wind_speed)
    
    return mean_temp, mean_gust, mean_wind

# -2,61 to 8,49
for x in range(-8,2):
    for y in range(49, 61):
        parms = {
            "lat": y,
            "lon": x,
            "model": "gfs",
            "parameters": ["wind", "windGust", "temp"],
            "levels": ["surface", "surface", "surface"],
            "key": key
        }
        # request the params
        response = requests.post(url, json=parms)
        # get the json data
        mean_temp, mean_gust, mean_wind = calculate_means(response.json())
        # append the data to the items list
        print("DONE"+str(x)+","+str(y))
        items.append(f"{x},{y},{mean_temp},{mean_gust},{mean_wind}")




# write all items to csv file
csv.write("\n".join(items))
csv.close()

