
import time, datetime


startTime = datetime.datetime(2029, 10, 31, 0, 0, 0)
while datetime.datetime.now() < startTime:
    time.sleep(1)


print('program now starting on Halloween 2029')

