# Todo 0: importing necessary modul
import psutil
import shutil

# Todo 1: define a check_disk_usage function
def check_disk_usage(disk):
    du = shutil.disk_usage(disk)  # variable to check the path
    free = du.free / du.total  # checking the free size ratio vs total size
    return free > 20  # return as True when the free size > 20 % (healthy size)


# Todo 2: define check_cpu_usage function to check the interval in whole seconds
def check_cpu_usage():
    usage = psutil.cpu_percent(1)  # check the CPU usage in 1 second interval
    return usage < 75  # return as True when the usage is less from 75 (healthy load)


# Todo 3: Check if those two values returning false (not in good shape)
if not check_disk_usage('/') or not check_cpu_usage():
    print("WARNING !")
else:
    print("Verifying PASSED!")


# Todo 4:
"""
- Extract the code as python file or txt file
- Run with local console
"""