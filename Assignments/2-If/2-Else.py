# Elif/Else statements: these work together with If statements. This way you can check on multiple conditions in a
# single function

def firstassignment():
    a = 8
    b = 3

    # Add a condition between the parentheses after 'if' using the variables and make sure this condition is NOT true.
    # That way the code after the 'else' will run.
    if ():
        print("Unexpected output")
    else:
        print("A is greater than B")

    # Expected output: "A is greater than B"

def secondassignment():
    # There is also the possibility to check on multiple conditions with the use of 'elif'.
    # This is essentially just an if statement that comes after another if statement and checks a different condition.
    a = "Hello World!"
    b = "Hello Mars!"


    if (a == b):
        print("B and A are the same")
    # Add a condition between the parentheses after 'elif'
    elif ():
        print("B and A are not the same")

    # Expected output: "B and A are not the same"


firstassignment()
secondassignment()
