#for loop

for i in range(5):
    print(i)


for i in range(1, 11):
    print(i)


#The range() function
#range() generates a sequence of integers, commonly used when you want to repeat something a specific number of times.

for i in range(2, 20, 2): #start, stop, step
    print(i)

for char in "python":
    print(char)


colors = ("red", "blue", "green")

for color in colors:
    print(color)



#while loop

i=0
while i<5:
    print("Hello")
    i = i + 1


#enumerate() - this is give both key and values
colors = ["red", "blue", "orange", "black", "white"]

for index, item in enumerate(colors):
    print(index, item)



#Python allows an else block after a loop. The else executes if the loop finishes normally, without being terminated by break.

for i in range(3):
    print(i)
else:
    print("Loop completed")


#zip function in python - The zip() function combines elements from two or more iterables, such as lists or tuples, pairing elements based on their positions.

names = ["Alice", "Bob", "Charlie"]
ages = [22, 25, 28]

for name, age in zip(names, ages):
    print(name, age)