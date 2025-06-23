# Example from this blog:
# https://www.thepythoncodingstack.com/p/demystifying-python-decorators


# Outer function
def store_arguments(func):
    data = []

    # Inner function
    def inner(*args, **kwargs):
        data.append((args, kwargs))
        func(*args, **kwargs)

    return inner


print_ = store_arguments(print)

print_("I love python")
print_(42, 99, 298)
print_(10, 19, 598, sep=":")

print(print_.__closure__[0].cell_contents)
