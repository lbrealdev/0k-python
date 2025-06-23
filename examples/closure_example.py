# Example from this blog:
# https://www.thepythoncodingstack.com/p/demystifying-python-decorators


def print_with_memory():
    data = []

    def inner(some_obj):
        data.append(some_obj)
        print(some_obj)

    # Return the function by using
    # just its name without parentheses.
    return inner


print_ = print_with_memory()

print_("I love python")
print_("... and also writing code in python")
