# importing 'hashlib' to create a hash table, and 'uuid' to salt the hash and prevent collision
# Other reference for possible future ideas:
# For checking integrity of the data and user-entries: https://www.pythoncentral.io/hashing-strings-with-python/
# Hash compare online reference: http://onlinemd5.com/
import hashlib, binascii, uuid
import pandas as pd
from openpyxl import load_workbook



class hashClass():

    # Creating the hashClass() constructor
    # Received the idea from the following reference:
    # https://www.journaldev.com/17357/python-hash-function
    def _init_(self, lastName, firstName, empNum, newDOB):
        self.lastName = lastName
        self.firstName = firstName
        self.empNum = empNum
        self.newDOB = newDOB

    # Creating a function for the program user-inputs of employee information, and then to create the table
    # and individual hash keys, added together for an ultimate individual key.
    def _updatedInfo_(self):

        # Creating variables for user-input of employee information into the system
        self.lastName = input("\nPlease enter your last name: ")
        self.firstName = input("\nPlease enter your first name: ")
        self.empNum = input("\nPlease enter your employee number: ")
        self.newDOB = input("\nPlease enter your date-of-birth(DDMMMYYYY: ")

        # Showing the user their input entries for the hash table values
        print("Here are your entries: ", self.lastName, ", ", self.firstName, ", ", self.empNum, ", ", self.newDOB, "\n")

        w = self.lastName
        x = self.firstName
        y = self.empNum
        z = self.newDOB

        # reference for creating hashes with salt for all of the individual user-inputs
        # https: // python.readthedocs.io / en / latest / library / hashlib.html
        # reference for fixing error concerning hashing a variable (w, x, y, z):
        # https://stackoverflow.com/questions/24905062/how-to-hash-a-variable-in-python
        # reference for adding salt to the hash: https://gist.github.com/markito/30a9bc2afbbfd684b31986c2de305d20

        salt = uuid.uuid4().hex

        LastNameString = hashlib.sha256(w.encode('utf-8'))
        LastNameHashed = LastNameString.hexdigest() + ':' + salt

        dkFirstName = hashlib.pbkdf2_hmac('sha256', b'x', b'salt', 100000)
        dkFirstNameHex = binascii.hexlify(dkFirstName)

        dkEmpNum = hashlib.pbkdf2_hmac('sha256', b'y', b'salt', 100000)
        dkEmpNumHex = binascii.hexlify(dkEmpNum)

        dkDOB = hashlib.pbkdf2_hmac('sha256', b'z', b'salt', 100000)
        dkDOBHex = binascii.hexlify(dkDOB)

        # Creating a variable called k (for key), to add all of the hashes together to create an
        # individual hashtable key and reference for all of the actual data
        k = LastNameHashed ##+ dkFirstNameHex + dkEmpNumHex + dkDOBHex

        # reference for tuple information:
        # https://www.quora.com/In-the-Python-dictionary-can-1-key-hold-more-than-1-value
        my_table = {k: (self.lastName, self.firstName, self.empNum, self.newDOB)}

        print("\n", my_table)

        # ____________________________________________________________________
        # Attempting to create a dataframe to save the info to a pandas dataframe
        my_table_DataFrame = pd.DataFrame.from_dict(my_table, orient='index')

        # setting the dataframe to show the entire dataframe
        pd.set_option('display.max_rows', 500)
        pd.set_option('display.max_columns', 500)
        pd.set_option('display.width', 1000)

        # printing the dataframe
        print(my_table_DataFrame)

        #____________________________________________________
        # Create, write to and save a workbook
        # https://medium.com/better-programming/using-python-pandas-with-excel-d5082102ca27

        writer = pd.ExcelWriter('MyEmployeeHashTable.xlsx', engine='openpyxl')
        writer.book = load_workbook('MyEmployeeHashTable.xlsx')
        writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
        reader = pd.read_excel(r'MyEmployeeHashTable.xlsx')
        my_table_DataFrame.to_excel(writer, index=True, header=False, startrow=len(reader)+1)

        writer.close()






hashClass()

def main():
    # Creating a variable to call the hashClass(), and using that to call the hashClass functions
    theHash = hashClass()

    # Calling the hashClass() function _updatedInfo_
    theHash._updatedInfo_()


    tryAgain = input("Please enter 1 to make more entries, or 2 to exit: ")

    if tryAgain == "1":
        theHash._updatedInfo_()
    if tryAgain == "2":
        exit()
    else:
        exit()




main()

