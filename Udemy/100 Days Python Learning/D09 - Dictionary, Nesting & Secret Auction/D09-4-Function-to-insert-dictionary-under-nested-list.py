travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(add_country,add_visit, add_cities): #2. Fungsi untuk memanggil point 1
    new_keys = {
        "country" : add_country,
        "visits" : add_visit,
        "cities" : add_cities
    } #3. key value yang berisikan input baru dari fungsi nomor 1
    travel_log.append(new_keys) #4. command untuk memasukkan data baru pada list yg sudah ada

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"]) #1. Merupakan format untuk pemanggilan function, oleh karena itu perlu membuat fungsi untuk memanggil add_new_country yang berisi pemanggilan country, visits, dan city
print(travel_log[2])



