# ----------------------Operators---------------------------
# Operators is a symbol that performs certain operation
# python provie following set of operators :-
# 1. Arithmetic operators
# 2. Relational operators or Comparision operators
# 3. Logical operators
# 4. Bitwise operators
# 5. Assignment operators
# 6. Special operators        *******
#       a. Identity operators
#       b. Membership operators

# ----------------------Arithmetic operators----------------

# +,- ,*,/,%,//,**

# Note :- +, * work with string also

# num1 = 10
# num2 = 2
# print(num1+num2)

# a = "Prem"
# b = "python"

# print(a+" "+b)
# print(num1-num2)
# print(a-b)     xxxxxxxxxx

# print(num1 * num2)  # 20
# print(a*num1)       # premprem
# print(a*b)          # error

# print(num1/num2)  # 5
# print(a/num1)  # error

#print(num1 % num2)
# num1 = 5
# num2 = 2
# print(num1//num2)   # 2

# num1 = 5
# num2 = 2.1
# print(num1/num2)  # 2.5
# print(num1//num2)  # 2.0
# print(num1//num2)  # 2.0

# num1 = 5
# num2 = 5

# print(num1**num2)  # 5*5*5*5*5

# Note :- /  ---> operators always perform floating point
# // --->   can perform both float and int
# if both the argument is int then it will return int
# if any one argument is float then return float

# print("Prem"+10)  #Error
# print("Prem"+"10")
# print(2*"prem")
# print("prem"*2.5)
# print("Prem"+2.5)

# -------------------------Relational operators or Comparision operators--------------------------
# >,<,>=,<=,==,!=
# Return only True or False


# num1 = 10
# num2 = 10

# print(num1 > num2)  # 0
# print(num1 < num2)  # 0
# print(num1 >= num2)  # 1
# print(num1 <= num2)  # 1
# print(num1 == num2)  # 1
# print(num1 != num2)  # 0

# print(True > True)  # 0
# print(True >= True)  # 1
# print(10 > True)  # 1
# print(False > True)  # 0
# print(10 > "python")  # xxxxxxx

# Chaining of relational operator is possible

# print(10 < 20 < 30 < 40)  #1
# print(10 < 20 > 30 > 40)  #0

#print(20 == 20 == 30)
#print(20 == 20 == 20)

# -----------------Logical Operators-----------------
# and , or ,not

# and--> if both arguments are True then return True
# or--> if at least one arguments are True then return True
# not --> Complement 1-->0

# print(True and False)  # 0
# print(True or False)  # 1
# print(True and True)  # 1
# print(not True)  # 0

# print(0 and True)  # 0

# print(1 or False)  # 1

# print(not 1)  # 0


# Note--> and--> if first argument is zero or false then result is 1st value else 2nd value

# Note--> or--> if first argument is True or zero then return 1st value else 2nd value

# print("" and 0)  # ""
# print(not None)  # 1
# print([] and 0)  #
# print([1, 2] and "Prem")  #


# print(5 or 6)  # 5
# print('' or "Cool")  # Cool
# print("you are in right direction." or "Data scientist coming soon")  # 1st
# print(True or False)  # 1
# print(1 or 0)    # 1


# ----------------------------Bitwise operators----------------------
# ---->   & , | , ~ , ^ , << , >>

# We can apply these operators bitwise.(10101)
# Note--> There operators are applicable only for int and boolean type
# By mistake if we trying to apply for any other type then we will get error..

#print(5 & 2)
# print(4 & 3)
# print(7 & 2)

# 000   0
# 001   1
# 010   2
# 011   3
# 100   4
# 101   5
# 110   6
# 111   7

# print(7 | 6)  # 7
# print(3 & 2)  # 2
# print(4 | 5)  # 5
# print(0 | 7)  # 7
# print(6 | 4)  # 6
# print(3 & 3)  # 3


# 010 --->101   -->5 -->-3
# 011--->100 -->011 1st complement -->- 011 +1 -->

# Note :-
# The most significant bit acts as sign bit ..0 value represent +ve and 1 is represent -ve

# The positive number will represent directly in the memory where as -ve number will be
# represent indirectly in 2s complement

# print(~7)  # --> -8
# print(~-7)  # --> 6
# print(~4)  # ---> -5
# print(~-2)  # ---> 1

# Shift operators

# left shift --->    <<
# shift the bit from left and after shifting cell we have to add zero from right side

# print(10 << 2)

# 00001010  ---> 00101000

# <----------------00101000-->40

# print(5 << 3)

# 00000101  ---> 00101000  -->40

# print(32 << 3)

# 00100000  ---> 00000000-->256  #**

# print(21 << 2)

# 00010101 --->01010100

# Right shift --->    >>
# shift the bit from right and after shifting cell we have to add zero from left side

# print(4 >> 2)

# # 00000100 ---> 00000001

# print(4 >> 3)

# # 00000100 ---> 00000000

# print(17 >> 2)

# # 00010001 --> 00000100

#
# print(True & False)  # F
# print(True | False)  # T
# print(~True)  # -2


# ----------------------------Assignment operators-----------------------
# We can use assignment operator to assign value to a variable
# ---> =,+=,-=,/=,//=,**=,*=,%=,&=,|=,>>=,<<=

# num1 = 10

# num1=num1+2
# num1 += 2
# print(num1)

#num1 = num1**5
# num1 **= 5
# print(num1)


# --------------------------Ternary operator-------------------------

# e.g  :- firstvalue if condition else sendvalue
# Nesting of ternary operator is possbile

# a, b = 10, 20

# x = 30 if a > b else 40 if a > b else 90

# print(x)

# 6. Special operators
#       a. Identity operators
#       b. Membership operators

# a. Identity operators --> is , is not
# We can use identity operator for address comparison.

num1 = 10
num2 = 10
# print(id(num1))
# print(id(num2))
print(num1 != num2)
print(num1 is not num2)
# print(num1 == num2)  # value
# print(num1 is num2)  # memory  # True

# num1 = [10, 20]
# print(id(num1))
# num2 = [10, 20]
# print(id(num2))


# num1 = [10, 20]
# print(id(num1))
# num2 = [10, 20]
# print(id(num2))

# print(num1 != num2)
# print(num1 is not num2)
