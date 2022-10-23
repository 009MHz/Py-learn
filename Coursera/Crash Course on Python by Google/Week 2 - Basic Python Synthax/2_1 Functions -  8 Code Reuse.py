"""identify the repeated pattern and replace it with a function called month_days, that receives the name of the
month and the number of days in that month as parameters. Adapt the rest of the code so that the result is the same.
Confirm your results by making a function call with the correct parameters for both months listed. """

# REPLACE THIS STARTER CODE WITH YOUR FUNCTION
june_days = 30
print("June has " + str(june_days) + " days.")
july_days = 31
print("July has " + str(july_days) + " days.")

"""This function to calculate the area of a rectangle is not very readable. Can you refactor it, and then call the 
function to calculate the area with base of 5 and height of 6? Tip: a function that calculates the area of a 
rectangle should probably be called rectangle_area, and if it's receiving base and height, that's what the parameters 
should be called. """


def f1(x, y):
    z = x * y  # the area is base*height
    print("The area is " + str(z))
