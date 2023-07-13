import datetime as dt

# Get current date and time
now = dt.datetime.now()
print(now)
print(type(now))

# Get current year
print(now.year)

# Get current month
print(now.month)

# Get current day
print(now.day)

# Our own datetime object
birthday = dt.datetime(2002, 5, 18)
print(birthday)
