print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇


first = input("\nWhich path will you choose? \"Left\" or \"Right\"? \n" ).lower()
if first == "left":
  print("You have sharp eye, stay safe on your journey.")
  print("\nThere's a dark forest up ahead!")
  forest = input('What will you do about it? "Circle" around or "Cross"? \n').lower()
  if forest == "cross":
    print("Good Job Adventurer, you may proceed")
    
    print("\nYou arrive at red boiling lake, and the destination is lies beyond it.")
    lake = input('What will you choose for this matter? "Wait", "Swim", or "Create" a Boat to cross? \n').lower()
    if lake == "swim":
      print("You're look exhausting but you managed it due your Vitality status.")
   
      print("\nNow you're at the main castle. Choose wisely about what will you do!")
      room = input('Which room you will enter? "black", "gold", "blue", "red"? \n').lower()
      if room == "red":
        print("Congratulations, here's your reward")
      elif room == "black":
        print("This is the room of torture, you will dead slaughtered by the room master")
      elif room == "gold":
        print("This is the fake treasure room, you'll died slowly by the poison trap from this room")
      else:
        print("I don't know why you choose this, but you have to try again from the start.")
    elif lake == "wait":
      print("There's a monster slaughter you because you're at their nest")
    else:
      print("Time's up you need to decide quickly next time")
  else:
    print("Only the true Adventurer may cross the path. Thank you for your participation.")
else:
  print("You can start again next time")