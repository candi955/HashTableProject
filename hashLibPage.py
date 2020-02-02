# A program to fulfill the project requirements for Hash Table in class MS549.

# In this project I not only practice hash tables, but also the use of color within my output, using both class color
# variable assignment, and the library 'termcolor'.

# reference: https://docs.python.org/3/library/hashlib.html
# https://pypi.org/project/hashlib/
# https://readthedocs.org/projects/hashlib/
# https://circuitpython.readthedocs.io/projects/hashlib/en/latest/
# https://github.com/adafruit/Adafruit_CircuitPython_hashlib
# https://www.pythoncentral.io/hashing-strings-with-python/
# Reference for uuid to add salt to hash to prevent collision:
# https://stackoverflow.com/questions/9594125/salt-and-hash-a-password-in-python
# https://docs.python.org/2/library/uuid.html

# Other references for hash tables in python:
# https://www.geeksforgeeks.org/python-hash-method/'
# https://www.geeksforgeeks.org/applications-of-hashing/
# side note from reference:  uuid4() creates a random UUID.

# importing 'hashlib' to create a hash table, and 'uuid' to salt the hash and prevent collision
import hashlib, uuid

# importing termcolor to color some of the text in the program
# reference: https://www.programcreek.com/python/example/78943/termcolor.colored
from termcolor import colored

# Using the color class in python, in assigned variable form, to make the headings bold, underline, and various colors
# reference: https://stackoverflow.com/questions/8924173/how-do-i-print-bold-text-in-python
endColor = "\033[0m"

startBold = "\033[1m"
startUnderline = '\033[4m'
startDarkCyan = '\033[36m'
startPurple = '\033[95m'
startCyan = '\033[96m'
startBlue = '\033[94m'
startGreen = '\033[92m'
startYellow = '\033[93m'
startRed = '\033[91m'


# Creating the data values
data = ['Jane Doe, 03/30/1956', 'Jim Davis, 4/15/1983', 'Mindy Watkins, 8/21/1977']

# Printing the data values, while making the heading bold using class color; also underlining using variables
print(startBold + startGreen + startUnderline + "\nData:" + endColor, data)

# Creating the table
hash_table = [None] * 20

# Printing the hash table, while using the termcolor library to make the heading blue and the python color class assigned
# variables to make the heading bold
print(startBold + startUnderline + colored("\nEmpty hash table:", "blue") + endColor, hash_table)





