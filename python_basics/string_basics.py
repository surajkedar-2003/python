name = 'suraj kedar'
print(name)

first_char = name[0]
print(first_char)

last_char = name[-1] # when we use negative indexing, it starts counting from the end of the string. So, -1 will give us the last character of the string.
print(last_char)

slice_first_name = name[0:5] # this is not inclusive of 5th index, so it will return 'suraj'
print(slice_first_name)


number_list = '0123456789'
print(number_list)

print(number_list[0:5]) # this will return '01234'
print(number_list[5:]) # this will return '56789' because we have not specified the end index, so it will return all the characters from 5th index to the end of the string.
print(number_list[:5]) # this will return '01234' because we have not specified the start index, so it will return all the characters from the start of the string to the 5th index.
print(number_list[::2]) # this will return '02468' because we have specified the step as 2, so it will return every second character from the string.
print(number_list[1::2]) # this will return '13579' because we have specified the start index as 1 and the step as 2, so it will return every second character from the string starting from the 1st index.
print(number_list[::-1]) # this will return '9876543210' because we have specified the step as -1, so it will return the string in reverse order.
print(number_list[:]) # this will return '0123456789' because we have not specified the start index, end index and step, so it will return the whole string.
print(number_list[::]) # this will return '0123456789' because we have not specified the start index, end index and step, so it will return the whole string.
print(number_list[1:8:2]) # this will return '1357' because we have specified the start index as 1, end index as 8 and step as 2, so it will return every second character from the string starting from the 1st index to the 8th index.
print(number_list[8:1:-2]) # this will return '8642' because we have specified the start index as 8, end index as 1 and step as -2, so it will return every second character from the string starting from the 8th index to the 1st index in reverse order.
print(number_list[1:4])


print(name.lower()) # this will return 'suraj kedar' because it will convert all the characters in the string to lowercase.
print(name.upper()) # this will return 'SURAJ KEDAR' because it will convert all the characters in the string to uppercase.

temp = "   github temp   "

print(temp.strip()) # this will return 'github temp' because it will remove all the leading and trailing whitespaces from the string.

print(temp.replace("temp", "test")) # this will return '   github test   ' because it will replace the substring 'temp' with 'test' in the string.

chai = "Lemon, Ginger, Masala, Black, Green"
print(chai.split(", ")) # this will return a list of the items in the string, separated by the specified delimiter.


print(name.find("kedar")) # this will return 6 because it will return the index of the first occurrence of the substring 'kedar' in the string. If the substring is not found, it will return -1.


chai_variety = ["Lemon", "Ginger", "Masala", "Black", "Green"]
print(chai_variety) # this will return the list of chai varieties.
print(", ".join(chai_variety)) # this will return a string of the items in the list, separated by the specified delimiter.

print('kedar' in name) # this will return True because the substring 'kedar' is present in the string 'name'.
print('kedar' not in name) # this will return False because the substring 'kedar' is present in the string 'name'.

