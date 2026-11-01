#list
tea = ["green", "black", "oolong", "white"]

print(tea) # this will return the list of tea varieties.
print(tea[0]) # this will return 'green' because it is the first item in the list.
print(tea[-1]) # this will return 'white' because it is the last item
print (tea[1:3]) # this will return ['black', 'oolong'] because it will return the items from index 1 to index 3 (not inclusive of index 3).


tea[3] = "herbal" # this will change the item at index 3 from 'white' to 'herbal'.
print(tea) 
tea[1:2] = "earl" # this will change the item at index 1 from 'black' to 'earl' but it look like ['green', 'e', 'a', 'r', 'l', 'oolong', 'herbal'] because it treat the string as a list of characters.
print(tea)

tea[3:4] = ["oolong", "white"] # this will change the item at index 3 from 'herbal' to 'oolong' and add 'white' at index 4.
print(tea) 


for item in tea:
    print(item, end = " ") # this will print all the items in the list on the same line separated by a space.



print(tea)

if "green" in tea:
    print("\nGreen tea is available.") # this will print 'Green tea is available.' because 'green' is present in the list 'tea'.    



tea.append("matcha") # this will add 'matcha' to the end of the list 'tea'.
print(tea)

tea.pop() # this will remove the last item from the list 'tea'.
print(tea)

tea.remove("green") # this will remove 'green' from the list 'tea'.
print(tea)

tea.insert(0, "chamomile") # this will add 'chamomile' to the beginning of the list 'tea'.
print(tea)


tea_varieties = tea.copy() # this will create a copy of the list 'tea' and assign it to the variable 'tea_varieties'.
print(tea_varieties)

squared_numbers = [x**2 for x in range(10)] # this will create a list of squared numbers from 0 to 9.
print(squared_numbers)