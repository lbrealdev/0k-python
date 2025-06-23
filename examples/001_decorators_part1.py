# Example from this blog:
# https://www.thepythoncodingstack.com/p/demystifying-python-decorators


# A closure allows a function to access variables that aren't in its local scope or in the global scope.
# A closure has access to the enclosing scope and, therefore, to variables defined in the enclosing (outer)
# function when creating the closure.

# A closure permits some data to persist when you call a function.
# Therefore, each call of the function can "communicate" with previous and future calls of the same function.

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

print(print_.__closure__[0].cell_contents)
