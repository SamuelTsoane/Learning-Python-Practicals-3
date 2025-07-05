#Control Statements

num = -1

if num > 0:
    print("This number is positive")
elif num == 0:
    print("This number is zero")
else:
    print("This number is negative")
    
num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second numbedr"))

if num1 > num2:
    print(num1, "is greater then" , num2)
elif num2 > num1:
    print(num2, "is greater then" , num1)
else:
    print("Both numbers are equal")