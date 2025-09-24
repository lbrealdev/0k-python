# Virtualenv for linux

Virtualenv python on linux.

### Use

Create a virtualenv:
```
virtualenv $new_project
```

Set different python version for create virtualenv:
```
virtualenv -p `which python3` $new_project

virtualenv --p=/usr/local/bin/python3 $new_project

python3 -m virtualenv $new_project
```

Activate venv:
```
source $new_project/bin/activate
```

Deactivate venv:
```
deactivate
```

Upgrade pip in virtualenv
```
./bin/python -m pip install --upgrade pip
```

### Work with Python interpreters vscode

Select and activate an environment:
```
Ctrl+Shift+P
```

# Virutalenv for windows

### Install

```
pip install virtualenv

pip install virtualenvwrapper-win
```

### Create virtualenv

#### Execute virtualenv or mkvirtualenv, but creating with mkvirtualenv will create your env in `C:\Users\Username\Evns\`. With virtualenv will create your env in your current directory.

```
virtualenv testspy


mkvirtualenv testpy
```

### Activate Windows

```
activate.bat

or

.\Scripts\activate
```

### Deactivate Windows

```
deactivate.bat

or

.\Scripts\deactivate.bat
```

For check your env execute:

```
pip list

pip        20.0.2
setuptools 45.2.0
wheel      0.34.2
```
You can see the difference of your packages list Python installed on virtualenv with packages Python installed in your system.


Source: [python.org](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
