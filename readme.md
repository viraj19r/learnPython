# Notes


>Python is a general-purpose, versatile, and powerful programming language. It’s a great first >language because it’s concise and easy to read. Whatever you want to do, Python can do it. >From web development to machine learning to data science, Python is the language for you.

>Python is a dynamic, interpreted (bytecode-compiled) language. There are no type declarations >of variables, parameters, functions, or methods in source code. This makes the code short and >flexible, and you lose the compile-time type checking of the source code. Python tracks the >types of all values at runtime and flags code that does not make sense as it runs.


## Python Keywords and Identifiers

- keywords - reserved words in python
- identifiers - names given to functions,variables,class,etc.

 We cannot use a keyword as a variable name, function name or any other identifier. They are  used to define the syntax and structure of the Python language.

 All the keywords except `True`, `False` and `None` are in lowercase.


 - Rules to write identifiers
    1. Identifiers can be a combination of letters in lowercase (a to z) or uppercase (A to Z) or digits (0 to 9) or an underscore `_`. Names like `myClass`, `var_1` and `print_this_to_screen`, all are valid example.
    2. An identifier cannot start with a digit. `1variable` is invalid, but `variable1` is a valid name.
    3. Keywords cannot be used as identifiers.
    4. We cannot use special symbols like !, @, #, $, % etc. in our identifier.
    5. An identifier can be of any length.

 - Python is a case-sensitive language. This means, Variable and variable are not the same.
 - Always give the identifiers a name that makes sense. While `c = 10` is a valid name, writing `count = 10` would make more sense, and it would be easier to figure out what it represents when you look at your code after a long gap.
 - Multiple words can be separated using an underscore, like `this_is_a_long_variable`.


## Python Statement
Instructions that a Python interpreter can execute are called statements. For example, `a = 1` is an assignment statement. `if` statement, `for` statement, `while` statement, etc.

  ### Multi-line statement
  - In Python, the end of a statement is marked by a newline character. But we can make a statement extend over multiple lines with the line continuation character`(\)` .
  For example:
  ```
  a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9 
  ```

  - This is an explicit line continuation. In Python, line continuation is implied inside parentheses ( ), brackets [ ], and braces { }. For instance, we can implement the above multi-line statement as:
  ```
  a = (1 + 2 + 3 +
    4 + 5 + 6 +
    7 + 8 + 9)
  ```
  - Here, the surrounding parentheses ( ) do the line continuation implicitly. Same is the case with [ ] and { }. For example:
  ```
  colors = ['red',
          'blue',
          'green']  
  ```
  - We can also put multiple statements in a single line using semicolons, as follows:
   
   `a = 1; b = 2; c = 3`
 

        
## Python Indentation
Most of the programming languages like C, C++, and Java use braces { } to define a block of code. Python, however, uses indentation.

A code block (body of a function, loop, etc.) starts with indentation and ends with the first un-indented line. The amount of indentation is up to us, but it must be consistent throughout that block.

Generally, four white spaces are used for indentation and are preferred over tabs.
 Here is an example.
 ```
 for i in range(1,11):
    print(i)
    if i == 5:
        break
```

Indentation can be ignored in line continuation, but it's always a good idea to indent. It makes the code more readable. For example:
```
if True:
    print('Hello')
    a = 5
```    
and

`if True: print('Hello'); a = 5`

both are valid and do the same thing, but the former style is clearer.

- Incorrect indentation will result in `IndentationError`.

## Python Comments
 In Python, we use the hash (#) symbol to start writing a comment.
```
#This is a comment
#print out Hello
print('Hello')
```

 ### Multi-line comments
We can have comments that extend up to multiple lines. One way is to use the hash(#) symbol at the beginning of each line. For example:
```
#This is a long comment
#and it extends
#to multiple lines
```
Another way of doing this is to use triple quotes, either ''' or """.

These triple quotes are generally used for multi-line strings. But they can be used as a multi-line comment as well. Unless they are not docstrings, they do not generate any extra code.
```
"""This is also a
perfect example of
multi-line comments"""
```

## Docstring in python(documentation string in python)

A docstring is short for documentation string.

Python docstrings (documentation strings) are the string literals that appear right after the definition of a function, method, class, or module.

Triple quotes are used while writing docstrings. For example:
```
def double(num):
    """Function to double the value"""
    return 2*num
```
Docstrings appear right after the definition of a function, class, or a module. This separates docstrings from multiline comments using triple quotes.

The docstrings are associated with the object as their` __doc__ `attribute.

So, we can access the docstrings of the above function with the following lines of code:
```
def double(num):
    """Function to double the value"""
    return 2*num
print(double.__doc__)
```
Output

`Function to double the value`

## Python Variables
A variable is a named location used to store data in the memory. It is helpful to think of variables as a container that holds data that can be changed later in the program. 


`number = 10`
`number = 1.1`

- Assigning multiple values to multiple variables

```
a, b, c = 5, 3.2, "Hello"

print (a)
print (b)
print (c)
```
- If we want to assign the same value to multiple variables at once, we can do this as:

```
x = y = z = "same"

print (x)
print (y)
print (z)
```
### Constants
A constant is a type of variable whose value cannot be changed. It is helpful to think of constants as containers that hold information which cannot be changed later.

In Python, constants are usually declared and assigned in a module. Here, the module is a new file containing variables, functions, etc which is imported to the main file. Inside the module, constants are written in all capital letters and underscores separating the words.

Create a constant.py:

```
PI = 3.14
GRAVITY = 9.8
```
Create a main.py:

```
import constant

print(constant.PI)
print(constant.GRAVITY)
```


In the above program, we create a constant.py module file. Then, we assign the constant value to `PI` and `GRAVITY`. After that, we create a main.py file and import the `constant` module. Finally, we print the constant value.

- In reality, we don't use constants in Python. Naming them in all capital letters is a convention to separate them from variables, however, it does not actually prevent reassignment.


 ## Literals
Literal is a raw data given in a variable or constant. In Python, there are various types of literals they are as follows:

  ### Numeric Literals
Numeric Literals are immutable (unchangeable). Numeric literals can belong to 3 different numerical types: `Integer`, `Float`, and `Complex`.


```
a = 0b1010 #Binary Literals
b = 100 #Decimal Literal 
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal

#Float Literal
float_1 = 10.5 
float_2 = 1.5e2

#Complex Literal 
x = 3.14j

print(a, b, c, d)
print(float_1, float_2)
print(x, x.imag, x.real)
```
   ### Strings
   A string literal is a sequence of characters surrounded by quotes. We can use both single, double, or triple quotes for a string. And, a character literal is a single character surrounded by single or double quotes.
```
strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\u00dcnic\u00f6de"
raw_str = r"raw \n string"
```

In the above program, This is Python is a string literal and C is a character literal.

The value in triple-quotes """ assigned to the multiline_str is a multi-line string literal.

The string u"\u00dcnic\u00f6de" is a Unicode literal which supports characters other than English. In this case, \u00dc represents Ü and \u00f6 represents ö.

r"raw \n string" is a raw string literal.

### Boolean literals
A Boolean literal can have any of the two values: True or False.
```
x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10
```
In the above program, we use boolean literal True and False. In Python, True represents the value as 1 and False as 0. The value of x is True because 1 is equal to True. And, the value of y is False because 1 is not equal to False.


- Python contains one special literal i.e. None. We use it to specify that the field has not been created.
  ```
  drink = "Available"
  food = None
  ```
## Literal Collections

  There are four different literal collections List literals, Tuple literals, Dict literals, and Set literals.
```
fruits = ["apple", "mango", "orange"] #list

numbers = (1, 2, 3) #tuple

alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} #dictionary

vowels = {'a', 'e', 'i' , 'o', 'u'} #set
```

- We can use the `type()` function to know which class a variable or a value belongs to. Similarly, the `isinstance()` function is used to check if an object belongs to a particular class.

## Python type conversion and type casting

The process of converting the value of one data type (integer, string, float, etc.) to another data type is called type conversion. Python has two types of type conversion.

1. Implicit Type Conversion
2. Explicit Type Conversion


### Implicit Type Conversion

In Implicit type conversion, Python automatically converts one data type to another data type. This process doesn't need any user involvement.

Let's see an example where Python promotes the conversion of the lower data type (integer) to the higher data type (float) to avoid data loss.

```
num_int = 123   #integer
num_flo = 1.23  #float

num_new = num_int + num_flo  #float
```
Addition of string(higher) data type and integer(lower) datatype

```
num_int = 123        #number
num_str = "456"   #string
print(num_int+num_str)  #Type error
``` 

### Explicit Type Conversion

In Explicit Type Conversion, users convert the data type of an object to required data type. We use the predefined functions like int(), float(), str(), etc to perform explicit type conversion.

This type of conversion is also called typecasting because the user casts (changes) the data type of the objects.

Syntax :

`<required_datatype>(expression)`
Typecasting can be done by assigning the required data type function to the expression.

```
num_int = 123 #int
num_str = "456"  #string

num_str = int(num_str)   #int

num_sum = num_int + num_str  #int
```
- In Type Casting, loss of data may occur as we enforce the object to a specific data type.

## Python output using `print()` function

We use the print() function to output data to the standard output device (screen)
Ex:-
`print('This sentence is output to the screen')`
```
a = 5
print('The value of a is', a)
```

In the second print() statement, we can notice that space was added between the string and the value of variable a. This is by default, but we can change it.

The actual syntax of the print() function is:
```
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```
Here, objects is the value(s) to be printed.

The sep separator is used between the values. It defaults into a space character.

After all values are printed, end is printed. It defaults into a new line.

The file is the object where the values are printed and its default value is sys.stdout (screen). Here is an example to illustrate this.
```
print(1, 2, 3, 4)
print(1, 2, 3, 4, sep='*')
print(1, 2, 3, 4, sep='#', end='&')
```
output: 
```
1 2 3 4
1*2*3*4
1#2#3#4&
```
### Output formatting
Sometimes we would like to format our output to make it look attractive. This can be done by using the `str.format()` method. This method is visible to any string object.
```
>>> x = 5; y = 10
>>> print('The value of x is {} and y is {}'.format(x,y))
The value of x is 5 and y is 10
```
Here, the curly braces `{}` are used as placeholders. We can specify the order in which they are printed by using numbers (tuple index).
```
print('I love {0} and {1}'.format('bread','butter'))
print('I love {1} and {0}'.format('bread','butter'))
```
output :
```
I love bread and butter
I love butter and bread
```

We can even use keyword arguments to format the string.
```
>>> print('Hello {name}, {greeting}'.format(greeting = 'Good morning', name = 'John'))
Hello John, Good morning
```

We can also format strings like the old sprintf() style used in C programming language. We use the % operator to accomplish this.

```
>>> x = 12.3456789
>>> print('The value of x is %3.2f' %x)
The value of x is 12.35
>>> print('The value of x is %3.4f' %x)
The value of x is 12.3457
```

## Python Input

To allow flexibility, we might want to take the input from the user. In Python, we have the input() function to allow this. The syntax for input() is:

```
input([prompt])
```
where prompt is the string we wish to display on the screen. It is optional.

```
>>> num = input('Enter a number: ')
Enter a number: 10
>>> num
'10'
```

Here, we can see that the entered value 10 is a string, not a number. To convert this into a number we can use int() or float() functions.
```
>>> int('10')
10
>>> float('10')
10.0
```


This same operation can be performed using the eval() function. But eval takes it further. It can evaluate even expressions, provided the input is a string
```
>>> int('2+3')
Traceback (most recent call last):
  File "<string>", line 301, in runcode
  File "<interactive input>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '2+3'
>>> eval('2+3')
5
```
## Python Import

When our program grows bigger, it is a good idea to break it into different modules.

A module is a file containing Python definitions and statements. Python modules have a filename and end with the extension .py.

Definitions inside a module can be imported to another module or the interactive interpreter in Python. We use the import keyword to do this.

`import math`
```
import math
print(math.pi)
```
O/P - 3.14159263


Now all the definitions inside math module are available in our scope. We can also import some specific attributes and functions only, using the from keyword. For example:
```
>>> from math import pi
>>> pi
3.141592653589793
```

While importing a module, Python looks at several places defined in sys.path. It is a list of directory locations.
```
>>> import sys
>>> sys.path
['', 
 'C:\\Python33\\Lib\\idlelib', 
 'C:\\Windows\\system32\\python33.zip', 
 'C:\\Python33\\DLLs', 
 'C:\\Python33\\lib', 
 'C:\\Python33', 
 'C:\\Python33\\lib\\site-packages']
```
We can also add our own location to this list.


## Operators in Python

Operators are special symbols in Python that carry out arithmetic or logical computation. The value that the operator operates on is called the operand.

### Arithmetic Operator
```
+ - addition
- - subtraction
/ - division
* - multiplication
% - modulus
// - quotient
** - power(2**2 - 2^2)
```
### Comparison Operator

```
> - greater than
< - less than
== - equal to
!= - not equal to
>= - greater than equal to
<= - less than equal to
```

### Logical Operator
```
and - true if both true - x and y
or - true if either of one is true - x or y
not - true if false(complement) - not x
```

### Bitwise Operators 








### Assignment Operator


## Special Operators
Python language offers some special types of operators like the identity operator or the membership operator.

### Identity Operators
`is` and `is not` are the identity operators in Python. They are used to check if two values (or variables) are located on the same part of the memory. Two variables that are equal does not imply that they are identical.

```
is - true if the operands are identical(refers to same object) - x is True
is not - true if the operands are not identical(do not refer to same object) - x is not True
```

```
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

# Output: False
print(x1 is not y1)

# Output: True
print(x2 is y2)

# Output: False
print(x3 is y3)
```

### Membership operators
`in` and `not in` are the membership operators in Python. They are used to test whether a value or variable is found in a sequence (string, list, tuple, set and dictionary).

- In a dictionary we can only test for presence of key, not the value.
```
in - true if value/variable is found in the sequence - 5 in x
not in - true if value/variable is not found in the sequence - 5 not in x.
```
```
x = 'Hello world'
y = {1:'a',2:'b'}

# Output: True
print('H' in x)

# Output: True
print('hello' not in x)

# Output: True
print(1 in y)

# Output: False
print('a' in y)
```


## [Python Namespace and Scope](https://www.programiz.com/python-programming/namespace)


