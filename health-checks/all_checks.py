#!/user/bin/env python3 
import os 
import shutil
import sys 

def check_rebooty():
    #Returns True if the computer has a pending reboot
    return os.path.exists("/run/reboot-required")

def check_disk_full(disk, min_gb, min_percent):
    #This function return True if there isn't enough disk space, False otherwise 
    du = shutil.disk_usage(disk)
    #Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    #Calculate how many free gigabytes
    gigabytes_free = 100 * du.free / du.total
    if percent_free < min_percent or gigabytes_free < min_gb:
        return True 
    return False 

def main():
    if check_rebooty():
        print("Reboot Pending")
        sys.exit(1) 
    if check_disk_full(disk="/", min_gb=2, min_percent=10):
        print("Disk Full.")
        sys.exit(1)

    print("Everything is Ok.")
    sys.exit(0)

main()

