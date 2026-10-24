x = 2
y = 3
z = 4

print(x+y)

#we should avoid this type of operation of both different data types.
print(40 + 2.23)

#below int() methods tell the pvm to convert the float value to int value before performing the addition operation.
print(40 + int(2.23))

#python automatically checks the data type of both the operands if they are string then it will perform the concatenation operation.
#operator overloading is the concept of using the same operator for different data types.
print('suraj' + 'kedar')

print(40 ** 2) #exponentiation operator

print(40 // 2) #floor division operator - different between floor division and normal division is that floor division will return the integer value of the result whereas normal division will return the float value of the result.

print(2 ** 1000) #this will return the value of 2 raised to the power of 1000. Python can handle very large integers without any issues.

result = 1/3.0

print(result)

repr = repr(result) #repr() method returns a string representation of the object. It is used to get the string representation of an object that can be used to recreate the object.
print(repr)

str = str(result) #str() method returns a string representation of the object. It is used to get the string representation of an object that can be used to display the object.
print(str)

#difference between repr() and str() is that repr() is used for debugging and development, whereas str() is used for creating output for end users. The output of repr() is more detailed and unambiguous, whereas the output of str() is more user-friendly and readable.


5.0 != 5.0 #this will return False because both the values are equal.
print(5.0 != 5.0)


print(1 == 2 < 3) #this will return false because 1 is not equal to 2 and 2 is less than 3.


import math

print(math.floor(3.5)) #this will return 3 because floor() method returns the largest integer less than or equal to the given number.

print(math.floor(-3.5)) #this will return -4 because floor() method returns the largest integer less than or equal to the given number.


#trunc() - it return the integer part of the given number. It is different from floor() method because it does not consider the sign of the number. It simply returns the integer part of the number.
print(math.trunc(3.5))  #this returns 3 because trunc() method returns the integer part of the given number.
print(math.trunc(-3.5))  #this returns -3 because trunc() method returns the integer part of the given number.


#complex number
print((2 + 3j) * 3)


#octals and hexadecimals and binary
print(0o10) #octal representation of 8

print(0x10) #hexadecimal representation of 16

print(0b10) #binary representation of 2

#converting decimal to octal, hexadecimal and binary

print(oct(8)) #oct() method returns the octal representation of the given number.
print(hex(16)) #hex() method returns the hexadecimal representation of the given number.
print(bin(2)) #bin() method returns the binary representation of the given number.

#other way to convert decimal to octal, hexadecimal and binary is by using int() method.
print(int('64', 8))  # converts decimal string to octal
print(int('64', 16))  # converts decimal string to hexadecimal
print(int('100', 2))  # converts binary string to decimal


#
print(0.1 + 0.1 + 0.1 - 0.3) # this returns 5.551115123125783e-17 because of the floating point arithmetic issue in python. It is not a bug in python but a limitation of the way floating point numbers are represented in computer memory. It is a common issue in all programming languages that use floating point arithmetic.

#for solving this issue we can use the decimal module in python. The decimal module provides support for fast correctly-rounded decimal floating point arithmetic. It offers several advantages over the float datatype.
from decimal import Decimal
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')) # this returns 0.0 because the decimal module provides support for fast correctly-rounded decimal floating point arithmetic.