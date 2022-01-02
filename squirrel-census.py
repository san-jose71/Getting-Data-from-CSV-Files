import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")


grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(grey_squirrel_count)

data_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [grey_squirrel_count, black_squirrel_count, cinnamon_squirrel_count]
}

data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("squirrel_count.csv")

