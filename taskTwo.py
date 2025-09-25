#take the first name from user and assign it to firstName
firstName=input("enter the first name: ")
#take the last name from the user and assign it to lastName
lastName=input("enter the last name: ")
#put two blank line as shown in output
print('')
print('')
#check the input x and y are non empty
if firstName=='':
    print("First Name can not be empty")
elif lastName=='':
    print("First Name can not be empty")
else:  
#use string print to show the welcome message to the user
#use string concatenation for including the name in welcome message.
#create a fullName variable and append firstName and lastName in it
    fullName=firstName+' '+lastName;
    print("Hello, "+fullName+"!, Welcome to the python program");

