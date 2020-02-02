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
import hashlib, _sha256, uuid, binascii


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
# data = ['Jane Doe, 03/30/1956', 'Jim Davis, 4/15/1983', 'Mindy Watkins, 8/21/1977']

data = []

# Printing the data values, while making the heading bold using class color; also underlining using variables
print(startBold + startGreen + startUnderline + "\nData:" + endColor, data)

# Printing the hash table, while using the termcolor library to make the heading blue and the python color class assigned
# variables to make the heading bold
print(startBold + startUnderline + colored("\nEmpty hash table:", "blue") + endColor, data)

# Ensuring the object (string) is hashed, before adding 'salt' to avoid collision
# reference: https://www.pythoncentral.io/hashing-strings-with-python/
# Side note: 'b' is buffer of bytes
hash_object = hashlib.sha256(b"Jane Doe")

# Adding 'salt' to the hash
# references: https://stackoverflow.com/questions/9594125/salt-and-hash-a-password-in-python
# https://docs.python.org/2/library/uuid.html
salt = uuid.uuid4().hex

hashedString = hash_object.hexdigest()
print("\nHashed string: ", hashedString)

newhash = hashedString + salt
print("\nHashed string concatenated with salt: ", newhash)

print("\n---------------------Trying the Key Derivation method--------------------------------\n")
# reference: https://python.readthedocs.io/en/latest/library/hashlib.html

# Derived-Key (dk)
# Password-based key derivation function 2
# (hash_name, password, salt, iterations, dklen)  side note: at least 100,000 iterations of SHA-256 are suggested
dk = hashlib.pbkdf2_hmac('sha256', b'password', b'salt', 100000)
print("\n", dk)

# reference: https://www.journaldev.com/17357/python-hash-function
# https://stackoverflow.com/questions/114830/is-a-python-dictionary-an-example-of-a-hash-table

class hashClass():

    def _init_(self, lastName, firstName, empNum, dob):
        self.lastName = lastName
        self.firstName = firstName
        self.empNum = empNum
        self.dob = dob

    def _updatedInfo_(self):

        dk1 = hashlib.pbkdf2_hmac('sha256', b'w', b'salt', 100000)
        dk2 = hashlib.pbkdf2_hmac('sha256', b'x', b'salt', 100000)
        dk3 = hashlib.pbkdf2_hmac('sha256', b'y', b'salt', 100000)
        dk4 = hashlib.pbkdf2_hmac('sha256', b'z', b'salt', 100000)

        self.lastName = input("\nPlease enter your last name: ")

        self.firstName = input("\nPlease enter your first name: ")

        self.empNum = input("\nPlease enter your employee number: ")

        self.newDOB = input("\nPlease enter your date-of-birth(DD-MMM-YYYY: ")

        w = self.lastname
        x = self.firstName
        y = self.empNum
        z = self.newDOB

        my_table = {"my_key": (binascii.hexlify(dk1), binascii.hexlify(dk2),
                               binascii.hexlify(dk3), binascii.hexlify(dk4))}

        return my_table


hashClass()

def _main_(self):

    theHash = hashClass()


    theHash.__init__()
    theHash._updatedInfo_()





















