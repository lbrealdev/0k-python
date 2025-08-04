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


max_ = store_arguments(max)

print(max_(42, 99, 298))
print(max_("Hello", "Goodbye", "Au Revoir"))
print(max_("Hello", "Goodbye", "Au Revoir", key=lambda x: len(x)))

print(max_.__closure__[0].cell_contents)
