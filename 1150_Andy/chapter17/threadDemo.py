"""
Mark Porraz, 5/11/2023. thread demo.py
"""
import threading, time
print('Start of program.')  # first print out start

def takeANap():
    time.sleep(5)  # after 5 seconds the time.sleep() function will print wake up
    print('Wake up!')  # prints out last after 5 seconds


threadObj = threading.Thread(target=takeANap)  # we pass a target equal to take a nap, in the thread function
threadObj.start()  # the thread object should start


print('End of program.')  # secondly print out end of program
# note this program will not terminate until all the threads have terminated.
