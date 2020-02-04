# importing 'hashlib' to create a hash table, and 'uuid' to salt the hash and prevent collision
# Other reference for possible future ideas:
# For checking integrity of the data and user-entries: https://www.pythoncentral.io/hashing-strings-with-python/
import hashlib
import pandas as pd
from openpyxl.workbook import Workbook
from openpyxl import load_workbook
import xlrd
import xlwt
from xlutils.copy import copy
import xlsxwriter


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
        dk1 = hashlib.pbkdf2_hmac('sha256', b'w', b'salt', 100000)
        dk2 = hashlib.pbkdf2_hmac('sha256', b'x', b'salt', 100000)
        dk3 = hashlib.pbkdf2_hmac('sha256', b'y', b'salt', 100000)
        dk4 = hashlib.pbkdf2_hmac('sha256', b'z', b'salt', 100000)

        # Creating a variable called k (for key), to add all of the hashes together to create an
        # individual hashtable key and reference for all of the actual data
        k = dk1 + dk2 + dk3 + dk4

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
        # reference: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_excel.html

        ### my_table_DataFrame.to_excel("MyEmployeeHashTable.xlsx", sheet_name='AllData', engine='xlsxwriter')

        # reference: https://www.youtube.com/watch?v=38XhSpmuXQw

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

