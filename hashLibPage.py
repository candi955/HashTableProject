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

start = "\033[1m"
end = "\033[0;0m"

data = ['Jane Doe, 03/30/1956', 'Jim Davis, 4/15/1983', 'Mindy Watkins, 8/21/1977']


print(start, "\nData:\n", end, data)

hash_table = [None] * 20


print(colored("\nEmpty hash table:\n", "blue"))
print(hash_table)




