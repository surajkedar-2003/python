#this file include basic set operations in python

setone = {1, 2, 3, 4, 5}
settwo = {4, 5, 6, 7, 8}

print("Set One:", setone)
print("Set Two:", settwo)


#union of two sets
union_set = setone.union(settwo)
print("Union of Sets:", union_set)

#intersection of two sets
intersection_set = setone.intersection(settwo)
print("Intersection of Sets:", intersection_set)

#difference of two sets
difference_set = setone.difference(settwo)
print("Difference of Sets:", difference_set)

# we can also use the '|' operator for union, '&' for intersection, and '-' for difference
union_set_operator = setone | settwo
intersection_set_operator = setone & settwo
difference_set_operator = setone - settwo

print("Union using operator:", union_set_operator)
print("Intersection using operator:", intersection_set_operator)
print("Difference using operator:", difference_set_operator)


#this will remove the elements of the second set from the first set and return a new set
print(setone - {1, 2, 3, 4, 5})  # this will return an empty set and output will be set() not {}

#because {} is used to create an empty dictionary in python, not an empty set. To create an empty set, we use the set() function.