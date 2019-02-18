def some_decorator(my_func): # this is a decorator function
    def wrapped_func():
        print("Execute this first before my_func")

        my_func()

        print("Execute this after my_func")

    return wrapped_func # decorator functions always return a function without calling it e.g. `wrapped_func()`

@some_decorator # adds functionality to `my_function`
def my_function():
    print("Hello World")

my_function()
