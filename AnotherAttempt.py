# importing 'hashlib' to create a hash table, and 'uuid' to salt the hash and prevent collision
import hashlib, _sha256, uuid

class hashClass():

    def _init_(self, lastName, firstName, empNum, newDOB):
        self.lastName = lastName
        self.firstName = firstName
        self.empNum = empNum
        self.newDOB = newDOB

    def _updatedInfo_(self):
        self.lastName = input("\nPlease enter your last name: ")

        self.firstName = input("\nPlease enter your first name: ")

        self.empNum = input("\nPlease enter your employee number: ")

        self.newDOB = input("\nPlease enter your date-of-birth(DDMMMYYYY: ")

        print(self.lastName, self.firstName, self.empNum, self.newDOB)

    def _table_(self):
        dk = hashlib.pbkdf2_hmac('sha256', b'password', b'salt', 100000)
        my_table = {"my_key": (self.lastName, self.firstName, self.empNum, self.newDOB)}

        print(dk(self.lastName, self.firstName, self.empNum, self.newDOB))


hashClass()

class Main():
    theHash = hashClass()

    theHash.__init__()
    theHash._updatedInfo_()
    theHash._table_()

Main()