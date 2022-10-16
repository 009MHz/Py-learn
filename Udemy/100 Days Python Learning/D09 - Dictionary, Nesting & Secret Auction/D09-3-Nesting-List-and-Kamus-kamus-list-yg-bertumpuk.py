#Nesting 
#simple nesting => kamus = {key1:value1, key2: value2}
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#Nesting a List in a Dictionary
#kamus = {"KEY 1": [value 1a,value 1b, value 1c], "KEY 2":[value 2a, value 2b, value 2c]}
city_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting Dictionary in a Dictionary
# kamus = {
#     KEY1: {SUB key1: [sub1a,sub1b,sub1c], SUB key2:[sub2a,sub2b,sub2c]}, 
#     KEY2: {SUB key3: [sub3a,sub3b,sub3c]}, SUB key4: [sub4a,sub4b,sub4c] } }
travel_log = {
    "France": {"visited": ["Paris", "Lille", "Dijon"],"attempts": 12},
    "Japan": {"visited":["Tokyo", "Okinawa", "Hokaido"], "attempts":5}
}

#Nesting Dictionaries in Lists
# list = [
#     {KEY1: Value1, KEY2:[value2a,value2b,value2c], KEY3:Value3},
#     {KEY4: Value4, KEY5:[value5a,value5b,value5c], KEY6:Value6},
# ] namun bisa juga dibuat seperti contoh dibawah untuk mempermudah pembacaan
travel_log = [
    {
        "country": "France", 
        "visited": ["Paris", "Lille", "Dijon"],
        "attempts": 12
    },
    {
        "country":"Japan", 
        "visited":["Tokyo", "Okinawa", "Hokaido"], 
        "attempts": 5
    },
]
one = travel_log[1]['attempts']
print(one)
