"""Infinite Loop: A loop that keeps executing and never stops"""
# Infinite loop sample: ping -t di windows untuk mengetahui ping internet

"example 1: infinite loop"
x = 0
while x - 1 < 10:  # reason: 0 - 1 akan selalu dibawah 10
    # solutions: gimana caranya biar x bisa menyentuh angka 10
    x += 1
    print(x)

"example 2 infinite loop"
def print_range(start, end):
    # Loop through the numbers from start to end
    n = start
    while n <= end:
        print(n)


#print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line)

"Infinite loop solution: adding 'break' "
while True:
    do_something_cool()
    if user_requested_to_stop():
        break


"""Summary: Avoid the most common pitfalls on while loop
    1.  Initiate the variable for starting
    2. Check the loop is not creating infinite loop
"""