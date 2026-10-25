#tuple - defination: A tuple is an ordered, immutable collection of elements in Python.
watches = ("Rolex", "Casio", "Titan", "Fossil", "Seiko")

#Accessing elements in a tuple
print(watches[0])  # Output: Rolex

print(watches[-1])  # Output: Seiko

print(watches[2:4])  # Output: ('Titan', 'Fossil')

print(len(watches))  # Output: 5

digital_watches = ("Casio", "Timex", "Seiko")
analog_watches = ("Rolex", "Titan", "Fossil")

#Concatenation of tuples
all_watches = digital_watches + analog_watches
print(all_watches)  # Output: ('Casio', 'Timex', 'Seiko', 'Rolex', 'Titan', 'Fossil')

(casio, timex, seiko) = digital_watches
print(casio)  # Output: Casio

print(type(watches))  # Output: <class 'tuple'>

nested = ("tuple", ("ordered", "immutable", "collection"))
print(nested)  # Output: ('tuple', ('ordered', 'immutable', 'collection'))
