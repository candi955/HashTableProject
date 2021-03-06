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
import pandas as pd
import xlrd


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
print(startCyan, startBold, startUnderline + colored("\nHashed string:") + endColor, hashedString)

newhash = hashedString + salt
print(startPurple, startBold, startUnderline + colored("\nHashed string concatenated with salt:") + endColor, newhash)

print(startRed, colored("\n---------------------Trying the Key Derivation method--------------------------------\n") +
      endColor)
# reference: https://python.readthedocs.io/en/latest/library/hashlib.html

# Derived-Key (dk)
# Password-based key derivation function 2
# (hash_name, password, salt, iterations, dklen)  side note: at least 100,000 iterations of SHA-256 are suggested
dk = hashlib.pbkdf2_hmac('sha256', b'password', b'salt', 100000)
print("\n", dk)

print(startGreen, colored("\n---------------------Creating an SHA-256 Algorithm Hash With Salt--------------------------------\n") + endColor)

# reference: https://www.journaldev.com/17357/python-hash-function
# https://stackoverflow.com/questions/114830/is-a-python-dictionary-an-example-of-a-hash-table
# reference for creating hashes with salt for all of the individual user-inputs
# reference for fixing error concerning hashing a variable (w, x, y, z):
# https://stackoverflow.com/questions/24905062/how-to-hash-a-variable-in-python

# main reference: https: // python.readthedocs.io / en / latest / library / hashlib.html
data = []
print("Empty data table: ", data, "\n")

data= [b'Apples', b'Grapes ', b'oranges']
print("Data with Apples, Grapes, and Oranges added: ", data, "\n")

# reference for adding salt to the hash: https://gist.github.com/markito/30a9bc2afbbfd684b31986c2de305d20
salt = uuid.uuid4().hex

# variables for hashing the employee number and adding salt (which will be used in the initially set-up program


for item in data:
    addingHash = hashlib.sha256(bytes(item))
    updatedData = addingHash.hexdigest()
    updatedDataWithSalt = updatedData + ":" + salt
    # updating
    print(updatedDataWithSalt)

print(startPurple, colored("\n-----------------Creating Tables with the combined hash from items as a key " +
                           "(with salt), SHA-256 Algorithm----------------------------\n") + endColor)

print("\n___________Table 1___________\n")

a = b'Smith'
b = b'Andrew'
c = b'Soccor'
salt = uuid.uuid4().hex

# variables for hashing the employee number and adding salt (which will be used in the initially set-up program
hashedA= hashlib.sha256(a)
hashedSaltA = hashedA.hexdigest() + ':' + salt

hashedB = hashlib.sha256(b)
hashedSaltB = hashedB.hexdigest() + ':' + salt

hashedC = hashlib.sha256(c)
hashedSaltC = hashedC.hexdigest() + ':' + salt

k = hashedSaltA + hashedSaltB + hashedSaltC

my_table = {k: (a, b, c)}

print(my_table)

print("\n___________Table 2___________\n")

a = b'Casada'
b = b'Marcus'
c = b'Football'
salt = uuid.uuid4().hex

# variables for hashing the employee number and adding salt (which will be used in the initially set-up program
hashedA= hashlib.sha256(a)
hashedSaltA = hashedA.hexdigest() + ':' + salt

hashedB = hashlib.sha256(b)
hashedSaltB = hashedB.hexdigest() + ':' + salt

hashedC = hashlib.sha256(c)
hashedSaltC = hashedC.hexdigest() + ':' + salt

k = hashedSaltA + hashedSaltB + hashedSaltC

my_table2 = {k: (a, b, c)}

print(my_table2)

print("\n___________Table 3___________\n")

a = b"O'Riley"
b = b'Robert'
c = b'Tennis'
salt = uuid.uuid4().hex

# variables for hashing the employee number and adding salt (which will be used in the initially set-up program
hashedA= hashlib.sha256(a)
hashedSaltA = hashedA.hexdigest() + ':' + salt

hashedB = hashlib.sha256(b)
hashedSaltB = hashedB.hexdigest() + ':' + salt

hashedC = hashlib.sha256(c)
hashedSaltC = hashedC.hexdigest() + ':' + salt

k = hashedSaltA + hashedSaltB + hashedSaltC

my_table3 = {k: (a, b, c)}

print(my_table3)

print(startBlue, colored("\n___________The Hash Table Dataframe (with combined hashes as keys; SHA256, salt added___________\n") + endColor)

tableHashedKeyDataFrame = pd.DataFrame({'Table 1': (my_table),
                                        'Table 2': (my_table2),
                                        'Table 3': (my_table3)})


pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)

print(tableHashedKeyDataFrame)



























