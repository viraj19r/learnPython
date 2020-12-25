PIP is a package manager for Python packages, or modules.


### What is a Package?
A package contains all the files we need for a module.

Modules are Python code libraries we can include in our project


### Install PIP
If you do not have PIP installed, you can download and install it from this page:` https://pypi.org/project/pip/`

After installing PIP

### Download a Package
Open the command line interface and tell PIP to download the package we want.

Navigate your command line to the location of Python's script directory, and type command

Example:
`pip install camelcase`

Now we have downloaded and installed our first package

### Using a Package
Once the package is installed, it is ready to use.
Import the "camelcase" package into project

```
import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))
```
This capitalize the first letter of each word

- [find more packages](https://pypi.org/)


Use the `uninstall` command to remove a package:
`pip uninstall camelcase`

- Use the `list` command to list all the packages installed on system
  `pip list`

