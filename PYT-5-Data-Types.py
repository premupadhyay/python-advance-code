#-------- Data Types in python-----------#

# int
# float
# complex
# bool
# str
# bytes     --->****
# bytearray
# None

# -------collection---------------
# range
# list
# tuple
# set
# frozenset
# dict


# int data types  ---> long

# number =9
# print(number)
# print(type(number))

# Note : if you are using python3 there is no long type explicitly
# We can represent long value also by using int type only


# float data types   ---> double

# number = 34.5

# print(number)
# print(type(number))

# complex data type :

# number = 3+5j

# print(type(number))
# print(number)


# bool data type : (True and False)

# Python internally treat 1--> True and 0--->False

# number = True
# print(type(number))
# print(number)

# print(True + True) --->2

# print(True + False)  --->1

# ---------- str  data types------------------

# A String is a sequence of char enclosed withing in single or double quotes

# name = "Prem here for python "

# print(type(name))

# print(name)

# full_name = '''prem

# upadhyay'''

# print(full_name)
# print(type(full_name))

# data = '''the American" Standard's" Association'''

# print(data)
# doc string
'''This is string
in python
'''


# msg = '''23456789- were "#$%_&'()'''


# IN python the following data types are consider as fundamental data types

# int
# float
# complex
# bool
# str

# 1 byte --> 8 bit

# -----bytes data type----
# Represent a group of byte number just like array

# x = [10, 20, 30, 40]
# byte_number = bytes(x)

# print(byte_number)
# print(type(byte_number))

# print(byte_number[0])

# byte_number[0] = 12

# print(byte_number)

# range --> 0 to 256

# we cant change its value other wise it will give type error


# -----bytesarray data type----
# x = [10, 20, 30, 40]
# byte_number = bytearray(x)

# print(byte_number)
# print(type(byte_number))

# print(byte_number[0])

# byte_number[0] = 12

# print(byte_number)

# Note :- bytearray is exactly same as bytes data types but it allow element can we modified and assign
