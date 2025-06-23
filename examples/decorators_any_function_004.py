# Example from this blog:
# https://www.thepythoncodingstack.com/p/demystifying-python-decorators

# A decorator is a function that accepts another function as an argument and returns yet another function.
# The function it returns is a decorated version of the function you pass as an argument.

# There are three functions involved in this definition, so it can get a bit complex.
# The decorator, such as store_arguments(), is a function. Its argument and its return value are also functions.
# These two functions perform similar tasks to each other. However, the function the decorator returns is a
# decorated version of the function you pass as an argument to the decorator.

# Outer function
def store_arguments(func):
    data = []

    # Inner function
    def inner(*args, **kwargs):
        data.append((args, kwargs))
        value = func(*args, **kwargs)
        return value

    return inner

def my_special_function(name, repeat):
    return name.upper() * repeat


my_special_function = store_arguments(my_special_function)

print(my_special_function("James", 3))
print(my_special_function("Bob", 2))

print(
    my_special_function.__closure__[0].cell_contents
)
