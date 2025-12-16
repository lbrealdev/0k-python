# https://github.com/prettytable/prettytable
# https://pypi.org/project/prettytable/

from prettytable import PrettyTable


result = [
    {
        "Coin": "Akash",
        "Price": "$2.10",
        "Max. supply": "20931",
        "Circulating supply": "103405",
    },
    {
        "Coin": "Bitcoin",
        "Price": "$113096.71",
        "Max. supply": "21000000",
        "Circulating supply": "19901015",
    },
]

# Instance a table
table = PrettyTable()

# Table tile
table.title = "test table (add_row)"

# Table fields style
table.header_style = "upper"

fields = []
if result and isinstance(result[0], dict):
    fields = list(result[0].keys())

# Add table field names
table.field_names = fields

# print(table, end="\n\n")

for coin in result:
    table.add_row(
        [
            coin.get(fields[0], "N/A"),
            coin.get(fields[1], "N/A"),
            coin.get(fields[2], "N/A"),
            coin.get(fields[3], "N/A"),
        ]
    )

# Debug table using `.add_row()` method.
print(table.get_string(sortby="Price"), end="\n\n")

# Cleanup result list with `.clear()` method.
result.clear()

table.title = "test table (add_rows)"

for coin in result:
    table.add_rows(
        [
            [
                f"{coin.get(fields[0], "N/A")}",
                f"{coin.get(fields[1], "N/A")}",
                f"{coin.get(fields[2], "N/A")}",
                f"{coin.get(fields[3], "N/A")}",
            ]
        ]
    )

# Debug table using `.add_rows()` method.
print(table.get_string(sortby="Price"))

# for coin in result[0]:
#     print(coin.upper())

# for coin in result:
#     result.pop(0)
#     keys = list(coin.keys())
#     print(keys)

# for coin in result:
#     for key, value in coin.items():
#         print(f"{key} = {value}")
