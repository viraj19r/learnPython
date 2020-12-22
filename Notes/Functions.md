# Functions
- A function is a block of code which only runs when it is called
- We can pass data, known as **parameters**, into a function
- A function can return data as a result

In Python a function is defined using the `def` keyword
```
def my_function():
  print("Hello from a function")
```
To call a function, use the function name followed by parenthesis

`my_function()`

### Arguments

Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name

```
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
```

- *Arguments* are often shortened to *args* in Python documentations.

### Parameters or Arguments?

The terms parameter and argument can be used for the same thing: information that are passed into a function.

- From a function's perspective:

  - A parameter is the variable listed inside the parentheses in the function definition.

  - An argument is the value that is sent to the function when it is called.


- By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.

### Arbitrary Arguments, *args
If we do not know how many arguments that will be passed into your function, add a `*` before the parameter name in the function definition.
This way the function will receive a *tuple* of arguments, and can access the items accordingly
```
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
```
- Arbitrary Arguments are often shortened to `*args` in Python documentations.

### Keyword Arguments
We can also send arguments with the key = value syntax.
This way the order of the arguments does not matter.

```
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
```

` The phrase *Keyword Arguments* are often shortened to *kwargs* in Python documentations.

### Arbitrary Keyword Arguments, **kwargs

If you do not know how many keyword arguments that will be passed into your function, add two asterisk: `**` before the parameter name in the function definition.

This way the function will receive a *dictionary* of arguments, and can access the items accordingly
```
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
```

- Arbitrary Keyword Arguments are often shortened to `**kwargs` in Python documentations.

### Default Parameter Value
If we call the function without argument, it uses the default value
```
def my_function(country = "Norway"):
  print("I am from " + country)
my_function()
my_function("India")
```
- We can send any data types of argument to a function (string, number, list, dictionary etc), and it will be treated as the same data type inside the function

E.g. if we send a List as an argument, it will still be a List when it reaches the function

### Return value

To let a function return a value, use the `return` statement:
```
def my_function(x):
  return 5 * x
```

- function definitions cannot be empty, but if for some reason we have a function definition with no content, put in the `pass` statement to avoid getting an error.

## Recursion

Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

We should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming

```
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

tri_recursion(6)
```

o/p -
```
1
3
6
10
15
21
```


## Lambda Function

A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.

Syntax:
`lambda arguments : expression`

Ex:
```
x = lambda a : a + 10
print(x(5))
```
```
x = lambda a, b : a * b
print(x(5, 6))
```



- The power of lambda is better shown when we use them as an anonymous function inside another function.

```
def myFunc(n):
  return lambda a : a * n
```
Now we can use this function two write program to double or triple the number as
```
def myFunc(n):
  return lambda a : a * n

myDoubler = myFunc(2)
myTripler = myFunc(3)

print(myDoubler(11))
print(myTripler(11))
```
o/p:
```
22
33
```

- We use lambda functions when an anonymous function is required for a short period of time.



