#Take an indicator for error happened in input
errorfound=False
#Take the first number as input from user and assign it to x variable
x=input("Enter the first number: ")
#Take the second number as input from the user and assign it to y variable.
y=input("Enter the second number: ")
#Convert x into integer
try:
    x=int(x)
except ValueError:
    errorfound=True
    print("Error in reading first number")
#Convert y into integer
try:
    y=int(y)
except ValueError:
    errorfound=True
    print("Error in reading second number")
#Add a new line
print('')
#Print Addition
if not errorfound:
    try:
        print("Addition: ",x+y)
    except:
        print("Addition can not be done with ", x,y)
    #Print Subtraction
    try:
        print("Subtraction: ",x-y)
    except:
        print("Subtraction can not be done with ",x,y)
    #Print Multiplication
    try:
        print("Multiplication: ",x*y)
    except:
        print("Multiplication can not be done with ",x,y)
    #Print Division
    if y==0:
        print("Division Error: Not able to divide by zero")
    else:
        try:
            print("Division: ",x/y)
        except:
            print("Division can not be done with ",x,y)

