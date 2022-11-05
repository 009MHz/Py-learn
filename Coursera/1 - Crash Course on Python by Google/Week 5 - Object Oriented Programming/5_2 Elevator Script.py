""""The code below defines an Elevator class. The elevator has a current floor, it also has a top and a bottom floor
that are the minimum and maximum floors it can go to. Fill in the blanks to make the elevator go through the floors
requested. """
class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        pass

    def up(self):
        """Makes the elevator go up one floor."""
        pass

    def down(self):
        """Makes the elevator go down one floor."""
        pass

    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        pass


elevator = Elevator(-1, 10, 0)
elevator.up()

elevator.current #should output 1
elevator.down()

elevator.go_to(10)
elevator.current #should output 10

"""If you get a NameError message, be sure to run the Elevator class definition code block first. If you get an 
AttributeError message, be sure to initialize self.current in your Elevator class. Once you've made the above methods 
output 1, 0 and 10, you've successfully coded the Elevator class and its methods. """

# Go to the top floor. Try to go up, it should stay. Then go down.
elevator.go_to(10)
elevator.up()
elevator.down()
print(elevator.current) # should be 9

# Go to the bottom floor. Try to go down, it should stay. Then go up.
elevator.go_to(-1)
elevator.down()
elevator.down()
elevator.up()
elevator.up()
print(elevator.current) # should be 1

"""Now add the str method to your Elevator class definition above so that when printing the elevator using the print( 
) method, we get the current floor together with a message. For example, in the 5th floor it should say "Current 
floor: 5 """
elevator.go_to(5)
print(elevator)