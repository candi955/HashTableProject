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

# Examples to use for assigning color class variables:
# Reference: https://stackoverflow.com/questions/8924173/how-do-i-print-bold-text-in-python
# class color:
   #PURPLE = '\033[95m'
   #CYAN = '\033[96m'
   #DARKCYAN = '\033[36m'
   #DARKCYAN = '\033[36m'
   #BLUE = '\033[94m'
   #GREEN = '\033[92m'
   #YELLOW = '\033[93m'
   #RED = '\033[91m'
   #BOLD = '\033[1m'
   #UNDERLINE = '\033[4m'
   #END = '\033[0m'
# Ex: print(color.BOLD + 'Hello World !' + color.END)

# importing 'hashlib' to create a hash table, and 'uuid' to salt the hash and prevent collision
import hashlib, uuid

# importing termcolor to color some of the text in the program
# reference: https://www.programcreek.com/python/example/78943/termcolor.colored
from termcolor import colored

# Using the color class in python, in assigned variable form, to make the headings bold
startBold = "\033[1m"
endBold = "\033[0;0m"

startUnderline = '\033[4m'
endUnderline = "\033[0;0m"

# Creating the data values
data = ['Jane Doe, 03/30/1956', 'Jim Davis, 4/15/1983', 'Mindy Watkins, 8/21/1977']

# Printing the data values, while making the heading bold using class color; also underlining using variables
print(startBold, startUnderline, "\nData:\n", endBold, endUnderline, data)

# Creating the table
hash_table = [None] * 20

# Printing the hash table, while using the termcolor library to make the heading blue and the python color class assigned
# variables to make the heading bold
print(startBold, colored("\nEmpty hash table:\n", "blue"), endBold, hash_table)





