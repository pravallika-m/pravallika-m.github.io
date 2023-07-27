# write function to call linux ls command every 4 hours

import os
import time
import schedule

def list_files():
    os.system("ls -l")

# schedule every 5 seconds
schedule.every(5).seconds.do(list_files)

