# Python 3.0 --
# print > print(var)

hello = "Hello World" + '!!!!!!'    # Basic var = string (+ string is Concatenation)
print(hello)

# Changing the value of the hello var.

hello = "The var now changed because this line sets a new string for it."
print(hello)    # Will always print the last written var of hello

# Basic print(var) with operator
# Can't add a string to a var - print(days + 'in a month')
# Can multiply a string with a var

days = 31
print(days - 1)     # Subtracts 1 from days var
print(days * "!")   # Creates 31 "!"
print(9 * "!")      # Creates 9 "!"

# Basic math --

mul = 7 * 7
add = 7 + 7
sub = 7 - 7
div = 7 / 7

eq = mul * add + sub - div / mul    # 7*7 * 7+7 + 7-7 - 7/7 / 7*7 = 685.97~
print(eq - 100)     # above equation - 100


# Beginning of strings test --

print(hello[4])     # prints 3rd letter in hello, Index strings are always -1

       # 0123456789-
quote = "The end of a string"
print(quote.find("of"))     # Index's count spaces

print("line 26: " + quote[7])     # prints nothing because 7 is a space
print("line 27: " + quote[8])     # prints "o"

# Strings in strings ----
# Finding the string "is" in the string "Somewhere something is looking to be known."
# use .find() to get Index location - Starting point of "is"
# use <var>[:] to convert to a letter - Index 20 > "i"

some = "Somewhere something is looking to be known is."
print(some.find('is'))      # starts at index 20
print(some[20:22])      # [20:22] prints "is"
print(some.find("junk"))    # Returns -1, String "junk" can't be found in var some

# Finding with numbers --

print(some.find("is", 0))   # Finds first "is" string at the beginning of var some: Index 20
print("Line 56: " + some[20:22])
print(some.find("is", 21))  # Finds second "is" string at the end of var some: Index 43
print("Line 57: " + some[43:])

# Extra -- Does nothing, just for example
"west".find("test")     # Returns -1, .find() looks for exact match
"test".find("st")       # Works, .find() can find "st" in "test" at index 2
"Test".find("te")       # Returns -1, .find() is case sensitive.

# s.find(s + "!!!") + 1
#   s= "hi!"
#       s + "!!!" = "hi!!!!"
#           Can't find "hi!!!!" in "hi!" >,(yields) -1
#               + 1 = 0

base = 1000
des = 1000.     # returns a decimal due to the "." at the end
print(base)
print(des)

TheDragonTeam auto push test

