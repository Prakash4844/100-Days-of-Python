import pandas

data = pandas.read_csv("Raw_Squirrel-Data.py")
# gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
#
# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
# }
#
# sdf = pandas.DataFrame(data_dict)
# sdf.to_csv("Squirrel_Count.csv")

# or use this:
(data["Primary Fur Color"].value_counts()).to_csv("Squirrel_Count.csv")
