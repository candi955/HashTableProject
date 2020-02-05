# A program to fulfill the project requirements for Hash Table in class MS549: timing the duration
# of 100 random hash table entries, deletions, and removals

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
import numpy as np
import random
import xlrd
import hmac
import hashlib, uuid
import pandas as pd
from openpyxl import load_workbook
import numpy as np
import xlrd

# To get rid of future warnings, specifically from hashClass(), function _getInfo_():
# FutureWarning: elementwise comparison failed; returning scalar instead, but in the future will perform elementwise comparison
# res_values = method(rvalues)
# reference:  https://stackoverflow.com/questions/40659212/futurewarning-elementwise-comparison-failed-returning-scalar-but-in-the-futur
import warnings
with warnings.catch_warnings():
    warnings.simplefilter(action='ignore', category=FutureWarning)

dataEmpty = bytes([])
print("\nEmpty dataset:", dataEmpty)

def newNum():
    rand100 = random.sample(range(1, 101), 1)

    dataRandom = np.append(dataEmpty, [rand100])
    print("\nPlacing 100 random numbers into the dataset:\n", dataRandom)
    dataRandomBytes = bytearray(dataRandom)

    salt = uuid.uuid4().hex

    for item in dataRandomBytes:

        item1 = bytes(item)
        hash = hashlib.sha256()
        hash.update(item1)
        itemHashed = hash.hexdigest()
        itemHashed_and_Salted = itemHashed + ":" + salt


        #hashed = hashlib.sha256(item)
        #hashed.update(item)
        #hashed.hexdigest(item)
        # reference for using hmac library: https://stackoverflow.com/questions/43559332/python-3-hash-hmac-sha512
        #sign = hmac.new(item, dataRandomBytes, hashlib.sha256).hexdigest()


        print("\nAdding a hash to the 100 dataset numbers:\n", itemHashed_and_Salted)
        k = itemHashed_and_Salted
        my_hash_table = {k: (dataRandom)}

        myNewDataframe = pd.DataFrame.from_dict(my_hash_table, orient='index')
        writer = pd.ExcelWriter('MyHashTable.xlsx', engine='openpyxl')
        writer.book = load_workbook('MyHashTable.xlsx')
        writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
        reader = pd.read_excel(r'MyHashTable.xlsx')
        myNewDataframe.to_excel(writer, index=True, header=False, startrow=len(reader) + 1)
        writer.close()
        break

newNum()
# The hashes were all showing up as same hash and salt, so created the function and now calling the function 100 times
# reference: https://stackoverflow.com/questions/4264634/more-pythonic-way-to-run-a-process-x-times
# the range (99) is for 0 - 99, which would be 100 numbers
for _ in range(99):
    newNum()





