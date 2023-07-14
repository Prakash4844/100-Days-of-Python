##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
from random import randint
from smtplib import SMTP
import os
from email.mime.text import MIMEText

MY_EMAIL = "prakashsahu0518@gmail.com"
MY_PASSWORD = os.environ.get("SMTP_APP_PASSWORD")

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
# 2. Check if today matches a birthday in the birthdays.csv
if today_tuple in birthdays_dict:
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME]
    # with the person's actual name from birthdays.csv
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    # 4. Send the letter generated in step 3 to that person's email address.
    with SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        msg = MIMEText(contents)
        msg['Subject'] = "Happy Birthday!"
        msg['From'] = birthday_person["email"]
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"], msg=msg.as_string()
        )

        print(f"Birthday Message sent! to {birthday_person['name']}")
