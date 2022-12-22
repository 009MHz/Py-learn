import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

cin_sqr = data[data["Age"] == "Adult"]
print(cin_sqr)