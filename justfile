# justfile for python

# Alias

alias run := run-python-example

@setup:
    pre-commit install

[working-directory: 'examples']
@run-python-example target:
    python3 {{ target }}
