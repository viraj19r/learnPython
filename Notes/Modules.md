Module is like a code library
A file containing a set of functions which we want to include in our application.

To create a module we just have to save our code with `.py` extension
Now we can use the module created, by using the `import` statement:

like if we create a module named `myModule.py`

When using a function from a module,we use the syntax: `module_name.function_name`.

- The module can contain all types of variables and we can access the variables after importing the module or assign them to new variable
- We can create an **alias** when we import a module, by using the `as` keyword:
   Ex : Create an alias for `myModule` called `mx`:
   `import myModule as mx`


## Built-in Modules

Import and use the `platform` module:
```
import platform

x = platform.system()
print(x)
```
o/p : 
`windows`

### `dir()` function
This function is used to list all the function and variable names in a module
```
import platform

x = dir(platform)
print(x)
```
- This function can be used on all modules,also the ones we create


## Import from modules
You can choose to import only parts from a module, by using the `from` keyword.

`from module1 import person` (import only person function from module1)











