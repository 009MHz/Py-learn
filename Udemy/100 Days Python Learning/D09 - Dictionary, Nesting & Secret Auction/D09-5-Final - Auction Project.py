import os
def cls():
    os.system('cls' if os.name =='nt' else 'clear')
# #HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

auctions = {} #1 key untuk awal kamus sebelum diisi value
max_bid = False
#auction process
while not max_bid:
    bidder = input("What's your name? ")
    price = int(input("How many your offer?: $")) #3 forcing text ke angka dengan int() => ["bidder": price]
    auctions[bidder] = price #2 key utk memasukkan value yg berupa [name] & offer => ["bidder":"price"]
    next = input("Is there any higher bid? Type 'yes' or 'no'.\n").lower()
    if next == "no":
        max_bid = True
    else:
        cls()
        print(f'Last bid is ${price}')

#highest bidder
max_bid = 0 #5 key awal parameter untuk memastikan price looping nnya 
for bidder in auctions: #4 looping "price" value dengan memanggil key nya (bidder) pada kamus (auctions)
    if auctions[bidder] > max_bid: #6 proses looping value harganya (auctions[bidder])
        bid = auctions[bidder] #7 replacing data no 6 ke price max dari semua data yang dicari
        winner = bidder.title() #8 replacing data key yg ada untuk mencari pemilik data (key) no 7
print(f'The auctions is winning by "{winner}" with ${bid}.')
