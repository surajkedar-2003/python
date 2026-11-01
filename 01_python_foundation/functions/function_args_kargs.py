
# functions with multiple arguments using *args

def sum_all(*args): # at place of args we can write anythings but * is important. but writing args is good practice
    print(*args) # it gives me all arguments given to this.
    print(args) # it print tuples

    for i in args:
        print(i * 2)

    return sum(args) # this method is inbuilt method for sum.

print(sum_all(1, 2, 3))

#functions using **kwargs - this is called keyword arguments

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")


print_kwargs(name="shaktiman")
print_kwargs(name="shaktiman", power="lazer")
print_kwargs(name="shaktiman", power="lazer", enemy="Dr. Jackaal")

