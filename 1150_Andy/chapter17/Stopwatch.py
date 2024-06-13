
"""
Mark Porraz, 5/4/2023, Stopwatch.py

This program tracks the amount of time elapsed between presses of the
enter key, with each key press starting a new “lap” on the timer.
it also prints the lap number, total time, and lap time.
"""

import time

# Display the program's instructions.
print('Press ENTER to begin. Afterward, press ENTER TO "CLICK" the stopwatch. Press Ctrl-C to quit:')
input()  # press Enter to begin
print('Started.')
startTime = time.time()  # get the first lap's start time
lastTime = startTime
lapNum = 1


# Start tracking the lap times
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time()  #
except KeyboardInterrupt:
    print('\nDone.')
