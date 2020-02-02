# Practice page, with source code listed below

# Source code for learning hashing from Algorithms for Dummies book, authors John Paul Mueller and Luca Massaron:
# Source code reference from dummies.com:
# https://www.dummies.com/store/product/Algorithms-For-Dummies.productCd-1119330491,navId-322493,descCd-DOWNLOAD.html



#%% md

# Hashing

#%%

data = [22, 40, 102, 105, 23, 31, 6, 5]
hash_table = [None] * 15
tblLen = len(hash_table)

def hash_function(value, table_size):
    return value % table_size

for value in data:
    hash_table[hash_function(value, tblLen)] = value

print("\nHash table:\n",hash_table)

#%%

print("\nHash table function:\n",hash_table[hash_function(102, tblLen)])

#%% md

## Creating your own hash function

#%%

from hashlib import md5, sha1

def hash_f(element, i, length):
    """ Function to create many hash functions """
    h1 = int(md5(element.encode('ascii')).hexdigest(),16)
    h2 = int(sha1(element.encode('ascii')).hexdigest(),16)
    return (h1 + i*h2) % length

#%%

print ("\nHash table CAT 1:\n",hash_f("CAT", 1, 10**5))

#%%

print ("\nHash table CAT 2:\n", hash_f("CAT", 2, 10**5))
