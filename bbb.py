import requests

key = "TCQHk4cGQAZp4vQ8y6wEEXUtI0Zc2K28"
parms = {
    "lat": 0.00,
    "lon": 0.00,
    "model": "gfs",
    "parameters": ["wind", "windGust", "temp"],
    "levels": ["surface", "surface", "surface"],
    "key": key
}

r = requests.post("https://api.windy.com/api/point-forecast/v2", json=parms)

print(r.json())