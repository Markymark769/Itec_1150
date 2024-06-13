"""
Mark Porraz, 5/4/2023, prettifiedStopwatch.py

This program tracks the amount of time elapsed between presses of the
enter key, with each key press starting a new “lap” on the timer.
it also prints the lap number, total time, and lap time.
"""

import time
import pyperclip

def main():
    lapTimes = []
    lapNum = 0
    lastTime = 0
    startTime = time.time()
    print('Press ENTER to begin. Afterward, press ENTER TO "CLICK" the stopwatch. Press Ctrl-C to quit:')
    try:
        while True:
            input()
            lapTime, totalTime, lastTime = inputs(lastTime, startTime)
            lapNum += 1
            formatted = processing(lapNum, totalTime, lapTime)
            outputs(lapTimes, formatted)
    except KeyboardInterrupt:
        print('\nDone.')
        pyperclip.copy('\n'.join(lapTimes))
# TODO: install a quit option
def inputs(lastTime, startTime):
    lapTime = round(time.time() - lastTime, 2)
    totalTime = round(time.time() - startTime, 2)
    return lapTime, totalTime, time.time()

def processing(lapNum, totalTime, lapTime):
    # Format lap.
    lap = f'Lap #{lapNum}: '
    ttime = str(totalTime).rjust(7)
    ttimeSep = ' ('
    ltime = str(lapTime).rjust(7)
    ltimeSep = ')'
    formatted = f'{lap}{ttime}{ttimeSep}{ltime}{ltimeSep}'

    return formatted

def outputs(lapTimes, formatted):
    print(formatted, end='')
    lapTimes.append(formatted)  # Add to list of saved laps

main()