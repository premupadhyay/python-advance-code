

# Variable Identifiers

# 123total=1         W
# total123=1234      R
# java2share12=45    R
# ca$h =12           W
# _abc_abc_=123      R
# def =12            W
# if=13              W
# True=              W


# Rule of define the Variable in python:

# alphabet symbols
# digits(0 to 9)
# underscore symbol ( _ )

# you should not start with digit

# Variable name are case sensitive

# We can not use reserved word in python

# Note :- if identifiers start with _ then it indicates that is Private

# Note :- if identifiers start with __ then it indicates that is Strongly private

# Note :- if identifiers start with __ and end with __then it indicates that special method


import keyword

from numpy import byte
print(keyword.kwlist)


['False', 'None', 'True', '__peg_parser__', 'and', 'as',
 'assert', 'async', 'await', 'break', 'class', 'continue',
 'def', 'del', 'elif', 'else', 'except',
    'finally', 'for', 'from', 'global', 'if', 'import', 'in',
    'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
    'return', 'try', 'while', 'with', 'yield']


user_name = "Prem"

userName = "Prem"

# Data Types

# int
# float
# complex
# bool
# str
# bytes
# bytearray

# -------collection---------------
# range
# list
# tuple
# set
# frozenset
# dict
# None

number = 10

print(type(number))

print(id(number))

# 8 bit --> 1 byte


# abc_.123 = 345      W
Nonetest123 = 345     R
test &= "Hello"
# demo() = "Test"    W

print(Nonetest123)
print(test)
