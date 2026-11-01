# def divide(a, b):
#     return a / b

# def calculate():
#     return divide(10, 0)

# calculate()

#we get a traceback with the error message

import traceback

try:
    10/0
except ZeroDivisionError:
    traceback.print_exc()
