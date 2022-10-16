# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ") #dalam command ini output yg dihasilkan akan selalu string
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
x = int(position[0]) #convert output string dari line 7 ke dalam int
y = int(position[1]) 
map[x -1][y-1] = "X" # -1 merubah urutan dari 0-2 menjadi 1-3, jadi hal ini menetralkan urutan yang tertanam pada python

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")