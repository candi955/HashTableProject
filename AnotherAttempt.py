# importing 'hashlib' to create a hash table, and 'uuid' to salt the hash and prevent collision
# Other reference for possible future ideas:
# For checking integrity of the data and user-entries: https://www.pythoncentral.io/hashing-strings-with-python/
import hashlib
import pandas as pd

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

        # reference (ideas for the below key assignment for variable k, the input hashes added all together):
        # https://stackoverflow.com/questions/40477899/create-dict-from-tuples-with-tuple-variable-names-as-keys-in-python
        for k in my_table:
            key = k

        print("\n", my_table)

        # ____________________________________________________________________
        # Attempting to create a dataframe to save the info

        my_table_DataFrame = pd.DataFrame.from_dict(my_table, orient='index')
        print(my_table_DataFrame)

        # return

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
