# 2-DataTypes
# In Python there are several DataTypes you can use.
# For now, we'll be going over some of the most important ones.
# Later you will get to know more of them.

# Here is a list of DataTypes:
# 'int' - a number without decimals for example: 2
# 'float' - a number with a decimals for example: 2.1 (Yes we use a dot for decimals not a comma)
# 'string' - text of some sort. To let python know you want to use a string write it like this: "word". Short form: str
# 'boolean' - True or False (The capital letter is necessary). Short form: bool
#   With booleans come new operators woohoo:
#   '==' equal to
#   '!=' not equal to
#   '>' greater than (returns bool) (You can add an '=' behind it to turn it into greater than or equal to x)
#   '<' smaller than (returns bool) (You can add an '=' behind it to turn it into smaller than or equal to x)
#   Both of these operators result in a boolean value so True or False

# Python automatically sets the datatype for you as long as you write it correctly
# You can see the datatype of a value by saying type(VALUE):

print("-------------------------")
print(type(2))
print(type(2 == 2))
print(type("Hello"))
print(type(2.0))

# Values with the same value but different DataType are NOT the same but ints and floats can still be the same.

print("-------------------------")
print("5" == 5)
print(True == (5 == 5))
print(5 == 5.00000)

# Booleans can have two values which are both ints. True = 1, False = 0.
# You can remember this by computers thinking in 0's and 1's.
# Knowing this you will realize that you can add booleans to ints:

print("-------------------------")
print(5 + True)
print(5 + False)
