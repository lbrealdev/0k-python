# Example from this blog:
# https://www.thepythoncodingstack.com/p/demystifying-python-decorators


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
