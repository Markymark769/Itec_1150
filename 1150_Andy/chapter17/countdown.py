"""
Mark Porraz, 5/5/2023, countdown.py
 a simple countdown script
"""

import time, subprocess

timeLeft = 60
while timeLeft > 0:
    print(timeLeft, end=' ')
    time.sleep(1)
    timeLeft = timeLeft - 1

subprocess.Popen(['start', 'alarm.wab'], shell=True)

