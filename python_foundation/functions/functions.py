def square(number):
    return number ** 2

result = square(4)
print(result)


#sum of two numbers
def sum(num1, num2):
    return num1 + num2

sum_result = sum(4, 5)
print(sum_result)


#area and circumference using same function
def area_and_circumference(radius):
    area = 3.14 * radius * radius
    circumference = 2 * 3.14 * radius
    return round(area, 2), circumference

print(area_and_circumference(3))