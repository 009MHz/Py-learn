"""Accessing the RAW csv files"""
with open("weather_data.csv") as file:
    data = file.readlines()
    print(data)


"""Accessing CSV files with CSV modules"""
import csv
# my approaches
with open("weather_data.csv") as file:
    data = csv.reader(file)
    #print(data)  # <_csv.reader object at 0x000000EC9FC1E320>
    for x in data:  # iterating each CSV values as a single value row
        temperatures = []
        for temp in x:
            if temp.isnumeric():
                temperatures.append(temp)
        print(temperatures)

# course approaches
with open("weather_data.csv") as file:
    data = csv.reader(file)
    temperatures = []
    for x in data:
        if x[1] != "temp":  # condition to exclude row title
            temperatures.append(int(x[1]))  # inserting the values in the second row contents into empty list
    print(temperatures)


"""Accessing CSV files with pandas module"""
import pandas

data = pandas.read_csv("weather_data.csv")  # assign variable to read the CSV files
print(data)  # displaying the whole contents from CSV files

print(data["temp"])  # displaying specific contents by calling the title name
