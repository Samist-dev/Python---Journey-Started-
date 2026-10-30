# I am gonna implement 3 functions in this file and 
# the name of the functions are square(n) is_even(n) and greet(name,greeting="Hello"). 



def square(n):
    return n*n

def is_even(n):
    if n%2==0:
        return True
    else:
        return False

def greet(name,greeting="Hello"):
    return f"{greeting} {name}"


x = square(5)
y = is_even(4)
z = greet("")



print(x)
print(y)
print(z)