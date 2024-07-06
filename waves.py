import requests
import numpy as np 
key = "CS9GvEpyo3eFy86sGgykX35SOcom5SEl"

csv = open('test.csv', 'r')
#add each line in file to a list
lines = csv.readlines()
#close the file
csv.close()

#open the file in write mode
csv = open('test.csv', 'w')



url = "https://api.windy.com/api/point-forecast/v2"



things = []
# -2,61 to 8,49
for line in lines:
    x = line.split(",")[0]
    y = line.split(",")[1]
    parms = {
        "lat": y,
        "lon": x,
        "model": "gfsWave",
        "parameters": ["waves"],
        "levels": ["surface"],
        "key": key
    }

    response = requests.post(url, json=parms)
    data = response.json()

    heights = data['waves_height-surface']
    directions = data['waves_direction-surface']
    periods = data['waves_period-surface']
    
    # Filter out None values (if any)
    heights_filtered = [x for x in heights if x is not None]
    directions_filtered = [x for x in directions if x is not None]
    periods_filtered = [x for x in periods if x is not None]
    
    # Calculate mean values using numpy.nanmean to handle potential NaN values gracefully
    mean_height = np.nanmean(heights_filtered)
    mean_direction = np.nanmean(directions_filtered)
    mean_period = np.nanmean(periods_filtered)
    

    # add to the line
    line = line+f",{mean_height},{mean_direction},{mean_period}"
    things.append(line)
    print(line)





# write all items to csv file
csv.write("\n".join(things))
csv.close()
