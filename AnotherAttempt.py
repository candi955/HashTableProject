# importing 'hashlib' to create a hash table, and 'uuid' to salt the hash and prevent collision
import hashlib, _sha256, uuid, binascii

class hashClass():

    # Creating the hashClass() constructor
    def _init_(self, lastName, firstName, empNum, newDOB):
        self.lastName = lastName
        self.firstName = firstName
        self.empNum = empNum
        self.newDOB = newDOB

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

        dk1 = hashlib.pbkdf2_hmac('sha256', b'w', b'salt', 100000)
        dk2 = hashlib.pbkdf2_hmac('sha256', b'x', b'salt', 100000)
        dk3 = hashlib.pbkdf2_hmac('sha256', b'y', b'salt', 100000)
        dk4 = hashlib.pbkdf2_hmac('sha256', b'z', b'salt', 100000)

        # Using tuple to represent value of a key
        k = dk1 + dk2 + dk3 + dk4

        # reference for tuple information:
        # https://www.quora.com/In-the-Python-dictionary-can-1-key-hold-more-than-1-value
        my_table = {k: (self.lastName, self.firstName, self.empNum, self.newDOB)}

        # reference (ideas for the below key assignment for variable k, the input hashes added all together):
        # https://stackoverflow.com/questions/40477899/create-dict-from-tuples-with-tuple-variable-names-as-keys-in-python
        for k in my_table:
            key = k

        print(my_table)

hashClass()

def main():
    # Creating a variable to call the hashClass(), and using that to call the hashClass functions
    theHash = hashClass()

    # Calling the hashClass() function _updatedInfo_
    theHash._updatedInfo_()

main()