states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america[2]) #jika command ini memanggil data urutan ke 3 dari start (0=data nomor 1 di python) maka bisa menggunakan "-" untuk memanggil data urutan dari end (kanan)
print(states_of_america[-4]) #akan memeanggil data no 4 dari end yaitu "New Mexico"

states_of_america[1] = "Pennysvania" #command ini akan mengubah data akhir jika ada command yang memanggil "Pennsylvania" maka dia akan terpanggil sebagai "Pennysvania" tanpa mengubah main database

states_of_america.append("Transylvania") #command ini akan menambah Transylvania ke dalam main database yang diletakkan di akhir urutan (setelah Hawaii) tanpa mengubah main database

states_of_america.extend(["Carribean", "Tortuga", "Havana"]) #sama seperti line 8 namun data yang ditambahkan bisa lebih dari 1 item
#list command reference: https://docs.python.org/3/tutorial/datastructures.html
print(states_of_america)

dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

