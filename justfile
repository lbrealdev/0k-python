# justfile for python

# Alias

alias run := run-python-example

@fmt:
    ruff format .

@setup:
    pre-commit install

[working-directory: 'examples']
@run-python-example target:
    python3 {{ target }}
