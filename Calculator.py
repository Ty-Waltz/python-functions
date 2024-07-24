def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def divide(x,y):
    return x/y
def multiply(x,y):
    return x*y
def exponentation(x,y):
    return x**y

print("Please choose an operation: -\n" 
      "1. add \n" 
      "2. subtract \n" 
      "3. divide \n" 
      "4. multiply \n" 
      "5. exponentation")

operation = int(input("Input which operation you would like to chose(1-5): "))
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

if operation == 1:
    print(num1, "+", num2 , "=", add(num1, num2 ))

elif operation == 2:
    print(num1, "-", num2 , "=", subtract(num1, num2 ))

elif operation == 3:
    if num2 == 0:
        print("Cannot divide by 0")
    else:
        print(num1, "/", num2 , "=", divide(num1, num2 ))
    
elif operation == 4:
    print(num1, "*", num2 , "=", multiply(num1, num2 ))

elif operation == 5:
    print(num1, "**", num2 , "=", exponentation(num1, num2 ))

else: 
    print("Invalid input")