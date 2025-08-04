# Python: working with list
# https://docs.python.org/3/tutorial/introduction.html#lists
# https://docs.python.org/3/tutorial/datastructures.html#more-on-lists

data = [
    {
        "Coin": "Akash",
        "Price": "2.10",
        "Max. supply": "20931",
        "Circulating supply": "103405"
    },
    {
        "Coin": "Bitcoin",
        "Price": "113096.71",
        "Max. supply": "21000000",
        "Circulating supply": "19901015"
    }
]

# New empty lists
key_fields = []
value_fields = []

# Add value to list '1'
key_fields.append(1)
value_fields.append(9)

# Add values to the list:
if data:
    keys = list(data[0].keys())
    values = list(data[0].values())

    for key in keys:
        key_fields.append(key)

    for value in values:
        value_fields.append(value)

# Debug original lists:
print(f"Original list (keys): {key_fields}")
print(f"Original list (values): {value_fields}", end="\n\n")

# Remove item from lists by index.
key_fields.pop(0)
value_fields.pop(0)

# Debug modified lists:
print(f"Modified list (keys): {key_fields}")
print(f"Modified list (values): {value_fields}", end="\n\n")

# Remove all items from list.
key_fields.clear()
value_fields.clear()

# Debug empty list:
print(f"Empty list (keys): {key_fields}")
print(f"Empty list (values): {value_fields}", end="\n\n")

# Add new value to empty lists.
key_fields.append("one")
value_fields.append("five")

# Add new value by index.
key_fields.insert(0, "two")
value_fields.insert(0, "six")

# Reverse list.
key_fields.reverse()
value_fields.reverse()

# Debug lists:
print(f"Reversed list (keys): {key_fields}")
print(f"Reversed list (values): {value_fields}", end="\n\n")

# Remove first item from lists.
key_fields.remove("two")
value_fields.remove("five")

# Debug removed list:
print(f"Removed first item (keys): {key_fields}")
print(f"Removed first item (values): {value_fields}")
