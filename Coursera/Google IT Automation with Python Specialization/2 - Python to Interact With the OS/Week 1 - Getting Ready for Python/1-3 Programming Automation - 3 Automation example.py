# Todo 0: importing necessary modul
import psutil
import shutil

# Todo 1: Check Disk usage
du = shutil.disk_usage('/')  # assigning root folder to check the usage
print(du)  # usage(total=245107195904, used=105283563520, free=139823632384)

# check the disk usage percentage
percent = du.free / du.total * 100
print(f"Disk usage: {round(percent, 2)} %")

# Todo 1: Check CPU usage
psutil.cpu_percent(0.1)  # verifying CPU usage in 0.1 s interval
