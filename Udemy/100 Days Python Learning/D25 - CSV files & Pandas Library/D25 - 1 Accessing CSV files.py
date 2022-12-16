"""Accessing the RAW csv files"""
# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

"""Accessing CSV files with CSV modules"""
import csv

with open("weather_data.csv") as file:
    data = csv.reader(file)
    #print(data)  # <_csv.reader object at 0x000000EC9FC1E320>
    for x in data:  # iterating each CSV values as a single value row
        temperatures = []
        for temp in x:
            if temp.isnumeric():
                temperatures.append(temp)
        print(temperatures)
