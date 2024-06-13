"""
Mark Porraz
2/14/2024
Question 3: Windows 11 Install (10 points)

To install Windows 11, a computer must have 8GB of memory and 64GB of free
storage space, and be running Windows 10. (Source, Microsoft)

All three requirements must be met.

Write a windows_11_compatible function that takes three arguments, the amount
of memory, the free storage space, and current operating system.

In the windows_11_compatible function use conditions to figure out if the user's
computer can be upgraded to Windows 11 or not.

You'll need to check that the memory is at least 8, the free storage space is at
least 64, and the name of the current operating system equals 'Windows 10'

Your windows_11_compatible function should return one of the Boolean values
True (if the computer can be upgraded) or False (if it can't be upgraded).  The
can_upgrade function will not print anything.

Create a main function.  In the main function, ask the user for

The current memory in their computer, in GB.  (For example, a user with 8GB of memory would enter 8)
The amount of free storage space, in GB. (For example, a user with a 500GB of free space should enter 500)
The name of their current operating system. (For example, a user could enter Windows 10 or Windows 8
 or Windows 7 or Windows XP or Linux or MacOS...)
Call your windows_11_compatible function from main(), and use the return value to print a message
 to the user telling them if they can, or can't, upgrade.

Test your program with different combinations of memory, free storage space, and operating system.

"""