import smtplib
import time

import requests
from datetime import datetime

MY_LAT = 28.7334  # Your latitude
MY_LONG = 77.2986  # Your longitude

MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# Your position is within +5 or -5 degrees of the ISS position.
def is_close():
    if MY_LAT - 5 < iss_latitude < MY_LAT + 5 and MY_LONG - 5 < iss_longitude < MY_LONG + 5:
        return True
    else:
        return False


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    res = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    res.raise_for_status()
    res_json = response.json()
    sunrise = int(res_json["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(res_json["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True
    else:
        return False


while True:
    # If the ISS is close to my current position
    if is_close() and is_dark():
        # Then send me an email to tell me to look up.
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up\n\nThe ISS is above you in the sky."
        )
        connection.close()
    else:
        print("ISS is not close")

    time.sleep(60)
