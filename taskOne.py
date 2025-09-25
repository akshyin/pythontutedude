#Take an indicator for error happened in input
errorfound=False
#Take the first number as input from user and assign it to firstnumber variable
firstnumber=input("Enter the first number: ")
#Take the second number as input from the user and assign it to secondnumber variable.
secondnumber=input("Enter the second number: ")
#Convert firstnumber into integer
try:
    firstnumber=int(firstnumber)
except ValueError:
    errorfound=True
    print("Error in reading first number")
#Convert secondnumber into integer
try:
    secondnumber=int(secondnumber)
except ValueError:
    errorfound=True
    print("Error in reading second number")
#Add a new line
print('')
#Print Addition
if not errorfound:
    try:
        print("Addition: ",firstnumber+secondnumber)
    except:
        print("Addition can not be done with ", firstnumber,secondnumber)
    #Print Subtraction
    try:
        print("Subtraction: ",firstnumber-secondnumber)
    except:
        print("Subtraction can not be done with ",firstnumber,secondnumber)
    #Print Multiplication
    try:
        print("Multiplication: ",firstnumber*secondnumber)
    except:
        print("Multiplication can not be done with ",firstnumber,secondnumber)
    #Print Division
    if secondnumber==0:
        print("Division Error: Not able to divide by zero")
    else:
        try:
            print("Division: ",firstnumber/secondnumber)
        except:
            print("Division can not be done with ",firstnumber,secondnumber)

