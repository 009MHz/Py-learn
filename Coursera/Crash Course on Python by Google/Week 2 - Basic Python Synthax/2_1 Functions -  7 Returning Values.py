"""Use the get_seconds function to work out the amount of seconds in 2 hours and 30 minutes, then add this number to
the amount of seconds in 45 minutes and 15 seconds. Then print the result. """

def get_seconds(hours, minutes, seconds):
  return 3600*hours + 60*minutes + seconds

amount_a = get_seconds(___)
amount_b = get_seconds(___)
result = ___
print(result)


"Returning Values Using Functions"
"""Sometimes we don't want a function to simply run and finish. We may want a function to manipulate data we passed 
it and then return the result to us. This is where the concept of return values comes in handy. We use the return 
keyword in a function, which tells the function to pass data back. When we call the function, we can store the 
returned value in a variable. Return values allow our functions to be more flexible and powerful, so they can be 
reused and called multiple times. 

Functions can even return multiple values. Just don't forget to store all returned values in variables! You could 
also have a function return nothing, in which case the function simply exits. """