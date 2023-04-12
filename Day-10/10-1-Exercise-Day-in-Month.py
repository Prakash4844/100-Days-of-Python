def days_in_month(month=2, year=2023):
    """This function return the number of days in a month while also considering if year is leap or not."""
    if month > 12 or month < 1:
        return "Invalid Month!"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year):
        if month == 2:
            return
        return month_days[month-1]
    else:
        return month_days[month-1]


def is_leap(year):
    """This function check if a year is leap year or not. it returns True, if year is leap. And
    False, if year is not a leap year."""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# 🚨 Do NOT change any of the code below
u_year = int(input("Enter a year: "))
u_month = int(input("Enter a month: "))

days = days_in_month(u_month, u_year)

print(days)
