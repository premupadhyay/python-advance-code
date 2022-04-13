# IN python the following data types are consider as fundamental data types

# int
# float
# complex
# bool
# str


# ------------ int----------> float,string(only int number),bool
#number = 34.5
#number = "10"
# number = "10ab"    xxxxx
# number = "10.5"     xxxxx
#number = True
#number = False
#number = "True"
# number = 5+3j    XXXXXXX

# print(type(number))

# number_int = int(number)

# print(number_int)

# print(type(number_int))

# ------------Float----------> int,string with any number,bool,
#number = 123
# number = 1+5j  XXXXX
#number = "12"
#number = "12.5"
#number = True
#number = False
# number = "True"  # XXXXXX


# print(type(number))
# number_float = float(number)
# print(number_float)
# print(type(number_float))


# ------------Complex----------> int,float,bool,string with any number
#number = 10
#number = 10.5
#number = True
#number = "10"
#number = "10.5"
#number = "Ten"


# print(type(number))
# number_float = complex(number)
# print(number_float)
# print(type(number_float))


# ------------bool---------->int(except -->0),string (except---> ""),float (except-->0.0)
# complex (except -->0)

# number = 12  # Note--> anything in python treated as True except(0,"",empty,[],0+0j)
#number = "Prem"
#number = 12.3
#number = 0+0j
#number = ""
#number = 0
#number = 0.0
#number = []
#number = "This is python144453.35454"
# print(type(number))
# number_float = bool(number)
# print(number_float)
# print(type(number_float))

# or --> if your first value is true then your output will be first value else 2nd
# print(5 or 6)  # ----> 5,5,5
# print('' or "Cool")  # -->cool
# # --->"you are in right direction."
# print("you are in right direction." or "Data scientist coming soon")
# print(True or False)  # --->True
# print(1 or 0)  # ----> 1
