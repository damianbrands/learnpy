# 3-Variables
# Up till now everything was just kind of basic calculations. Now we're going to jump into a big part of programming.
# A variable is a container to store data in. You create a variable by giving it a name and then assigning a value:

a = 12
b = "twelve"
c = 6

# After assigning a value to a variable, python will keep the variable in mind for you.
# You can call the value by using its name:

print("-------------------------")
print(a)
print("a equals 12 here")

# python reads your program file from top to bottom.
# So if you call the print(a) above but change the value of a later, you will not change the outcome of the print.
# You can also calculate with variables.

print("-------------------------")
a = a + 1
print(a)

# If you change the value of the initial 'a' variable you will see that it changes the second print statement too.
# (when you run the file again)

# You can put variables in strings by using what is known as an f-string:

print("-------------------------")
word = "world"
print(f"Hello {word}!")

