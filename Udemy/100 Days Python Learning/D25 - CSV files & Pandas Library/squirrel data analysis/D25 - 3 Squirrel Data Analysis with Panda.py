import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

"""Extracting the squirrel based on colour"""
cin_sqr = data[data["Primary Fur Color"] == "Cinnamon"]
gr_sqr = data[data["Primary Fur Color"] == "Gray"]
blk_sqr = data[data["Primary Fur Color"] == "Black"]

"""Counting the squirrel based on color"""
cin_sqr_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
gr_sqr_count = len(gr_sqr)
blk_sqr_count = len(blk_sqr)

"""Constructing the dataframe"""
# Define the dictionary
sqr_dataframe = {
    "Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gr_sqr_count, cin_sqr_count, blk_sqr_count]
}

# Converting into Dataframe
sqr_df = pandas.DataFrame(sqr_dataframe)

# Exporting into new files
sqr_df.to_csv("squirrel_count")




# Debugging for check the script
# print(cin_sqr_count)
# print(cin_sqr_count)
# print(gr_sqr_count)