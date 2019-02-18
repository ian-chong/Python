def say_hello():
    print ('Hello')

say_hello()

def say_hello_to(first_name):
    print(f"Hello {first_name}!")

say_hello_to("John")

def say_hello_too(first_name, last_name):
    print(f"Hello {first_name} {last_name}!")

def multiply(x,y):
    magic=x*y
    print(magic)
multiply(9,6)

def some_function():
    return 4

a = some_function()
print(a)

def format_name(first_name, last_name):
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    return (first_name, last_name)

name = format_name("john", "lee")
print (name)

x = 10

def does_something():
  x = 2
  print(x)

does_something()

x = x+2
print(x)

x = 1

for i in range(0,5):
    x = i
    print(x)

print(x)

def print_bob(n):
    if n == 0: # Base / Terminating Condition
        return None
    else:
        print("bob")
        print_bob(n-1) # Call itself and move towards terminating condition

print_bob(9)

def factorial(n):
    if n < 0:
        return -1
    else:
        fact = 1
        for i in range(1, n+1):
            fact *= i
        return fact
print (factorial(6))

def recursive_factorial(n):
    if n < 0:
        return -1
    elif n < 2:
        return 1
    else:
        return n * recursive_factorial(n-1)
print (recursive_factorial(5))