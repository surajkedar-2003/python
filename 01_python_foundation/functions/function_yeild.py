#generate even number using yeild

def even_generator(limit):
    for i in range(2, limit+1, 2):
        yield i


for num in even_generator(10):
    print(num)


# In Python,  yield returns a value one at a time without terminating the function. It is used to create a generator.


# def numbers():
#   return 1
#   return 2
#   return 3
# 
# print(numbers())  # Output: 1


# Once return executes, the function terminates.

#Example using yield


# def numbers():
#     yield 1
#     yield 2
#     yield 3
# 
# for num in numbers():
#     print(num)

# Output:

# 1
# 2
# 3

# Each time the generator is asked for the next value, execution resumes from where it previously paused.

#Why does yield exist?

# - Memory efficiency: Generates values when needed instead of storing all values in memory.
# - Lazy evaluation: Produces values only when requested.
# - Pauses execution: Remembers its current position and local variables, then resumes later.

# For example, if you need to process one million numbers, `yield` lets you generate them one at a time instead of creating a list containing all one million numbers.

# Remember:

# - return → Returns a value and ends the function.
# - yield → Produces a value and pauses the function.