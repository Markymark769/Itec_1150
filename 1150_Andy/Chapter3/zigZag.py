"""Mark Porraz, 2/19/2023, Zig zag
homework, chapter 3, Functions
This program describes a function structure.

"""

#### Press the STOP button or CTRL-C to exit
###########
import time, sys
indent = 0 # How many spaces to indent.
indentIncreasing = True # Whether the indentation is increasing or not.
try:
     while True: # The main program loop.
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # Pause for 1/10 of a second.
        if indentIncreasing:

            #Increases Indent
            indent = indent + 1
            if indent == 20:
                #Change direction:
                indentIncreasing = False
        else:
            #Decrease the number of spaces
            indent = indent - 1
            if indent == 0:
                #change direction
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()
##########
#### Press the STOP button or CTRL-C to exitw1      z