# ====================
# Python Basics
# ====================

# This file contains my Python practice while learning programming.

# Topics Covered:
# Variables 
# String Operations (str) 
#   - String Concatenation (+) vs Comma (,) 
# Integer Variables (int)
#   - Arithmetic Operators (+,-,*,//,/,%,**)
#   - Augmented Assignment Operators(+=,-=,*=,//=,/=,%=,**=)
#   - Printing Integers: '+' vs ','
# Floating-Point Numbers (float) 
#   - Printing Floats: '+' vs ','
# Boolean Values (bool)
# Multiple Assignment
# Built-in Functions for Strings
# Common String Methods
# Typecasting
# Errors and Fixes


# ===========
# Variables
# ===========

# ========================
# String Operations (str)
# ========================

name = "Calm"

print(name)                                    # Calm   
print("Hello " + name)                         # Hello Calm
print(type(name))                              # <class 'str'>

first_name = "Calm"
last_name = "Mind"

full_name = first_name + " " + last_name

print("Hello " + full_name)                    # Hello Calm Mind

# String Concatenation (+) vs Comma (,) 

print("Python" + "is" + "fun")                 # Pythonisfun
print("Python" , "is" , "fun")                 # Python is fun

# ========================
# Integer Variables (int)
# ========================

# Arithmetic Operators (+ , - , * , // , / , % , **)

age = 25

age = age + 1
print(age)                 # 26

age = age - 5
print(age)                 # 21

age = age * 3
print(age)                 # 63

age = age // 7
print(age)                 # 9

age = age / 3
print(age)                 # 3.0

age = age % 2
print(age)                 # 1.0

age = age ** 4
print(age)                 # 1.0

# Augmented Assignment Operators(+= , -= , *= , //= , /= , %= , **=)

age = 25

age += 8
print(age)                 # 33

age -= 3
print(age)                 # 30

age *= 8
print(age)                 # 240

age //= 4
print(age)                 # 60

age /= 2
print(age)                 # 30.0

age %= 7
print(age)                 # 2.0

age **= 2
print(age)                 # 4.0

# Printing Integers: '+' vs ','

age = 25

print("Age: " + str(age))              # Age: 25
print("Age:" , age)                    # Age: 25

# =================================
# Floating-Point Numbers (float)
# =================================

height = 165.5
print(height)                          # 165.5
print(type(height))                    # <class 'float'>

# Printing Floats: '+' vs ','

print("Your height is: " + str(height) + " cm")      # Your height is: 165.5 cm
print("Your height is:", height , "cm")              # Your height is: 165.5 cm

# =======================
# Boolean Values (bool)
# =======================

human = False
print(human)                 # False
print(type(human))           # <class 'bool'>

human = True
print("Are you a human: " + str(human))              # Are you a human: True

# =====================
# Multiple Assignment
# =====================

name , age , human = "Calm" , 25 , True
print(name , age , human)                            # Calm 25 True
 
violet = indigo = blue = green = 10
print(violet , indigo , blue , green)                # 10 10 10 10

# ===============================
# Built-in Functions for Strings
# ===============================

# Length 

name = "Calm Mind"

print(len(name))                     # 9

# ========================
# Common String Methods
# ========================

name = "Calm Mind"

#  Find Index

print(name.find("a"))               # 1

print(name.find("M"))               # 5

print(name.find("k"))               # -1

print(name.find("b"))               # -1

print("strawberry".find("r"))       # 2


# Capitalize

print(name.capitalize())            # Calm mind

print("strawberry".capitalize())    # Strawberry

# Title

print(name.title())                 # Calm Mind

print("strawberry".title())         # Strawberry

# Upper

print(name.upper())                 # CALM MIND

print("strawberry".upper())         # STRAWBERRY

# Lower

print("CALM MIND".lower())          # calm mind

print("Strawberry".lower())         # strawberry

# is digit

print(name.isdigit())               # False

print("12345".isdigit())            # True

print("Python3".isdigit())          # False

# is alpha

print(name.isalpha())               # False

print("strawberry".isalpha())       # True

print("Sun Shine".isalpha())        # False

print("Python3".isalpha())          # False

# Count

print(name.count("m"))              # 1

print("strawberry".count("r"))      # 3

print("python".count("z"))          # 0

# Replace

print(name.replace("m" , "l"))      # Call Mind

print("strawberry".replace("r" , "c"))         # stcawbeccy

# String Multiplication

name = "Calm"

print(name * 3)             # CalmCalmCalm

print("12345" * 3)          # 123451234512345

print("Hi " * 3)            # Hi Hi Hi

# =============
# Typecasting
# =============

# Integer to String

age = 25
print(type(age))         # <class 'int'>

age = str(age)           
print(type(age))         # <class 'str'>

# Integer to Float

age = 25

age = float(age)
print(type(age))         # <class 'float'>

# Float to Integer

height = 165.5

height = int(height)
print(height)            # 165
print(type(height))      # <class 'int'>

print("I am " + str(height) + " cm tall.")        # I am 165 cm tall.

# ===================
# Errors and Fixes
# ===================

# --------------
# SyntaxError
# --------------

# print("Hello"                  # Missing closing parenthesis

# --------------
# NameError
# --------------

# print(Hello)                   # Missing quotation marks

# --------------
# TypeError
# --------------

# age = 25
# print("Age: " + age)           # Cannot concatenate str and int

# --------------
# ValueError
# --------------

# size = "1.0"
# size = int(size)              # ValueError
# size = int(float(size))       # right

# -------------------
# ZeroDivisionError
# -------------------

# print(10 / 0)                 # ZeroDivisionError

