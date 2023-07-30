import requests
import datetime

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# latitude = response.json()["iss_position"]["latitude"]
# longitude = response.json()["iss_position"]["longitude"]
#
# iss_position = (latitude, longitude)
# print(iss_position)

MY_LAT = 28.7334  # Your latitude
MY_LONG = 77.2986  # Your longitude

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
response = response.json()
print(response["results"]["sunrise"])
print(response["results"]["sunset"])

sunrise = int(response["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(response["results"]["sunset"].split("T")[1].split(":")[0])

print(sunrise)
print(sunset)

time_now = datetime.datetime.now().hour
print(time_now)
