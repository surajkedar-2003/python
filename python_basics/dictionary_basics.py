watches_types = {"casio": "digital", "seiko": "automatic", "rolex": "luxury", "timex": "affordable"}
print(watches_types["casio"])  # Output: digital

for watch in watches_types:
    print(watch, watches_types[watch])

#we can also use the items() method to iterate over the key-value pairs in the dictionary
for key, value in watches_types.items():
    print(key, value)


print(len(watches_types))  # Output: 4

watches_types["fossil"] = "fashion"  # Adding a new key-value pair
print(watches_types)

watches_types.pop("fossil")  # Removing a key-value pair
print(watches_types)

watches_types.popitem()  # This will remove and return an arbitrary key-value pair from the dictionary
print(watches_types)

del watches_types["rolex"]  # This will remove the key "rolex" and its associated value from the dictionary
print(watches_types)

copy_of_watches_types = watches_types.copy()  # Creating a shallow copy of the dictionary
print(copy_of_watches_types)


watch_shop = {
    "digital" : {"casio": 100, "timex": 50},
    "automatic" : {"seiko": 200},
    "luxury" : {"rolex": 1000, "omega": 800, "tag heuer": 600},
}

print(watch_shop)
print(watch_shop["luxury"]["rolex"])  # Output: 1000

squared_numbers = {x: x**2 for x in range(6)}  # Dictionary comprehension to create a dictionary of squared numbers
print(squared_numbers)

squared_numbers.clear()  # This will remove all items from the dictionary
print(squared_numbers)  # Output: {}

keys = ["java", "python", "c++"]
default_value = "programming language"

new_dict = dict.fromkeys(keys, default_value)  # Creating a new dictionary with keys from the list and a default value
print(new_dict)  # Output: {'java': 'programming language', 'python': 'programming language', 'c++': 'programming language'}

new_dict_2 = dict.fromkeys(keys, keys) # Creating a new dictionary with keys from the list and the list itself as the value
print(new_dict_2)  # Output: {'java': ['java', 'python', 'c++'], 'python': ['java', 'python', 'c++'], 'c++': ['java', 'python', 'c++']}