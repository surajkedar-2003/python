try:
    num = int(input("enter a number: "))
    print(100/num)
except:
    print("something went wrong")
finally:
    print("Program execution completed")


#file not found error
try:
    with open("missing.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File does not exist")


#zero division error
try:
    result = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero")


#multiple exceptions

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

except ValueError:
    print("Please enter numeric values")

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Result:", result)



#raise keywoard is used to raise an exception explicitly in Python. It allows you to create custom error messages and handle specific conditions in your code. When the raise statement is executed, it interrupts the normal flow of the program and raises the specified exception.

age = -5

if age < 0:
    raise ValueError("Age cannot be negative")

