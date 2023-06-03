# with open("weather-data.csv") as file:
#     data = file.readlines()
#     print(data)

# import csv
#
# with open("weather-data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather-data.csv")

# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# print(round(data["temp"].mean(), 2))
# print(data["temp"].max())

# Get data in columns
# print(data["day"])
# print(data.day)

# Get data in rows
# print(data[data.day == "Monday"])
# print(data[data.temp == 12])
# print(data[data.condition == "Cloudy"])

# print(data[data.temp == data.temp.max()])

# def cal_to_Fahr(temp_cal):
#     """Convert Fahrenheit to Celsius
#
#     Return Celsius conversion of input"""
#
#     temp_cal = temp_cal * 1.8 + 32
#     return temp_cal
#
#
# monday = cal_to_Fahr(data[data.day == "Monday"].temp)
# print(monday)

# Create a dataframe from scratch
stu_data = {
    "students": ["Prakash", "Sonali", "Sagar"],
    "Scores": [75, 85, 70]
}

student_dataframe = pandas.DataFrame(stu_data)
print(student_dataframe)

student_dataframe.to_csv("Gang.csv", index=False) # Index=False is used to drop the index column
