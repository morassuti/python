
# Calculator

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y


print ("\n Select an operation number: \n" )

print ("1- Addition ")
print ("2- Subtraction ")
print ("3- Multiply ")
print ("4- Division ")

option = input("Type your option (1/2/3/4): ")

num1 = int(input("Type first number: "))
num2 = int(input("Type second number: "))

if option == '1':
    print("\n")
    print(num1, " + ", num2, "=", add(num1,num2) )
    print("\n")

if option == '2':
    print("\n")
    print(num1, " - ", num2, "=", subtract(num1,num2) )
    print("\n")

if option == '3':
    print("\n")
    print(num1, " * ", num2, "=", multiply(num1,num2) )
    print("\n")

if option == '4':
    print("\n")
    print(num1, " / ", num2, "=", divide(num1,num2) )
    print("\n")

else:
    print("\n")
    print("Invalid option" )
    print("\n")





