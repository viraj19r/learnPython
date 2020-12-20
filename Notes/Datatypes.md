Python has the following data types built-in by default

| type     | data                       |
| -------- | -------------------------- |
| Text     | string                     |
| Numeric  | int,float,complex          |
| Sequence | list,tuple,range           |
| Mapping  | dict                       |
| Set      | set,frozen set             |
| Boolean  | bool                       |
| Binary   | bytes,bytearray,memoryview |


### Getting the Data Type
We can get the data type of any object by using the `type()` function:
```
x = 5
print(type(x))
```
O/P :
`<class 'int'>`


### Setting the Specific Data Type
We can use the built in constructor function like `int(), float(),str(),complex(),list(),tuple(),range(),dict(),set(),etc ` (function are available for all data types)


### Python Random Number 
Python does not have a `random()` function to make a random number, but Python has a built-in module called `random` that can be used to make random numbers

```
import random

print(random.randrange(1, 10))

```

-----------------------------------------------------------------------
## String
- string in python are surrounded by either single or double quotation marks
- You can assign a multiline string to a variable by using three quotes(either single or double)
- we can access string letters like as array elements(a[0] = first letter)
- To get the length of a string we use length function `len()`
- we use `in` or `not in` to check whether a substring is contained in the string.

  ### string slicing

  Specify the start index and the end index, separated by a colon, to return a part of the string.
   ```
  b = "Hello, World!"
  print(b[2:5])
   ```

   slice from start
   ```
   b = "Hello, World!"
   print(b[:5])
   ```
   slice to the end
   ```
   b = "Hello, World!"
   print(b[2:])
   ```
   Use negative indexes to start the slice from the end of the string
   ```
   b = "Hello, World!"
   print(b[-5:-2])
   ```
   O/P:
   `orl`

  ### modify string
  The `upper()` method returns the string in upper case
  The `lower()` method returns the string in lower case
  ```
  a = "Hello, World!"
  print(a.upper())
  ```
 
  remove whitespace using `strip()`
  ```
  a = " Hello, World! "
  print(a.strip()) # returns "Hello, World!"
  ```
  The `replace() `method replaces a string with another string:
   ```
  a = "Hello, World!"
  print(a.replace("H", "J"))
  ```
  The `split()` method splits the string into substrings if it finds instances of the separator:
  ```
  a = "Hello, World!"
  print(a.split(",")) # returns ['Hello', ' World!']
  ```
  ### string concatenation
  To concatenate, or combine, two strings we can use the + operator.

  ### String Format
  In python we cannot combine numbers and string like this
  ```
  age = 36
  txt = "My name is John, I am " + age
  print(txt)
  ```
  The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
  ```
  age = 36
  txt = "My name is John, and I am {}"
  print(txt.format(age))
  ``` 
  The format() method takes unlimited number of arguments, and are placed into the respective placeholders
  ```
  quantity = 3
  itemno = 567
  price = 49.95
  myorder = "I want {} pieces of item {} for {} dollars."
  print(myorder.format(quantity, itemno, price))
  ```
  We can use index numbers {0} to be sure the arguments are placed in the correct placeholders
  ```
  quantity = 3
  itemno = 567
  price = 49.95
  myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
  print(myorder.format(quantity, itemno, price))
  ```

  ### Escape characters 
  To insert characters that are illegal in a string, use an escape character.

  An escape character is a backslash `\` followed by the character you want to insert
  Ex: `\'`, `\\`(backslash), `\n`(new line),etc

  ### [String Methods](https://www.w3schools.com/python/python_strings_methods.asp)

## Boolean(True or False)

 The `bool()` function allows you to evaluate any value, and give you `True` or `False` in return.
- Almost any value is evaluated to `True` if it has some sort of content.

- Any string is `True`, except empty strings.

- Any number is `True`, except `0`.

- Any `list`, `tuple`, `set`, and `dictionary` are `True`, except empty ones.
  
- There are not many values that evaluate to False, except empty values, such as `()`, `[]`, `{}`, `""`, the number `0`, and the value None. And of course the value False evaluates to False.
- One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a `__len__` function that returns `0` or `False`

   ```
    def __len__(self):
    return 0

    myobj = myclass()
    print(bool(myobj))
   ```

Python also has many built-in functions that return a boolean value, like the `isinstance()` function, which can be used to determine if an object is of a certain data type:

```
x = 200
print(isinstance(x, int))
```
O/P :
`True`

-----------------------------------------------------------------
## Python List

Lists are used to store multiple items in a single variable.

- Lists are created using square brackets
`thisList = ["apple", "banana", "cherry"]`
- List items are ordered, changeable, and allow duplicate values.
- When we say that lists are **ordered**, it means that the items have a defined order, and that order will not change.If you add new items to a list, the new items will be placed at the **end** of the list.
- The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
- To determine how many items a list has, use the `len()` function:
   `print(len(thisList))`
- List items can be of any data type. A list can contain different data types.
 ` list1 = ["abc", 34, True, 40, "male"]`
- type = object
- It is also possible to use the `list()` constructor when creating a new list.
`thisList = list(("apple", "banana", "cherry")) # note the double round-brackets`


### Python Collections (Arrays)
There are four collection data types in the Python programming language:

- List is a collection which is ordered and changeable. Allows duplicate members.
- Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
- Set is a collection which is unordered and un-indexed. No duplicate members.
- Dictionary is a collection which is unordered and changeable. No duplicate members.
When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.

### Accessing list items

we can access using indexing   
- negative indexing means start from end(-1 = last item, -2 = second last item)
- We can specify a range of indexes by specifying where to start and where to end the range.
```
thisList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thisList[2:5])
```
### change items
To change the value of a specific item, refer to the index number:
```
thisList = ["apple", "banana", "cherry"]
thisList[1] = "blackcurrant"
print(thisList)
```
To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values
```
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
```

- The `insert()` method inserts an item at the specified index:
```
thislist.insert(2, "watermelon")
print(thislist)
```
- To add an item to the end of the list, use the `append()` method:
- To append elements from another list to the current list, use the `extend()` method.
```
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
```
- The `extend()` method does not have to append lists, we can add any iterable object (tuples, sets, dictionaries etc.).
- The `remove()` method removes the specified item.
- The `pop()` method removes the specified index.
- If we do not specify the index, the `pop()` method removes the last item.
- The `del` keyword also removes the specified index
`del thislist[0]`
- The `del` keyword can also delete the list completely.
`del thislist`
- The `clear()` method empties the list.The list still remains, but it has no content.
- we can loop through the list using `for` and `while` loops
- **List Comprehension** offers the shortest syntax for looping through lists.A short hand `for` loop that will print all items in a list:
```
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
```

code without list comprehension
```
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)
```
Now code with list comprehension
```
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]
```

**syntax for list comprehension :**
`newlist = [expression for item in iterable if condition == True]`
The return value is a new list, leaving the old list unchanged.
The condition is like a filter that only accepts the items that valuate to `True`.

The iterable can be any iterable object, like a list, tuple, set etc.

we can use the `range()` function

`newlist = [x for x in range(10)]`

The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list
`newlist = [x.upper() for x in fruits]`

Set all values in the new list to 'hello':

`newlist = ['hello' for x in fruits]`

The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
```
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)
```
O/P:
`['apple', 'orange', 'cherry', 'kiwi', 'mango']`

### sorting the list
List objects have a `sort()` method that will sort the list alphanumerically, ascending, by default
`list.sort()`

- descending sort
`list.sort(reverse=True)`

- customize sort function
You can also customize your own function by using the keyword argument `key = function`.
```
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
```

- By default the `sort()` function is case sensitive

### Reverse a list
- reverse the order of the list using the `reverse()` function

### Copy a list
We cannot copy a list simply by typing `list2 = list1`, because: `list2` will only be a reference to `list1`, and changes made in `list1` will automatically also be made in `list2`.

So we will use the built-in `copy()` method

`newlist = mylist.copy()`

Another way to make a copy is to use the built-in method `list()`.

`newlist = list(mylist)`

### Join two lists
- we can join by appending each item of one list to other
- using addition `list3 = list1 + list2
- using `extend()` method
-------------------------------------------------------------------
## Tuple 

- store multiple items in single variable
- ordered and unchangeable(cannot add or remove or change once created), allow duplicate values

`thisTuple = ("apple","mango","cherry")`


- To determine no of items in a tuple, use `len()`.
- To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple
```
thistuple = ("apple",)

thistuple = ("apple") #Not a tuple
```
- tuple items can be any data type
- tuple can contain different data types
- type of tuple is also object
- It is also possible to use the `tuple()` constructor to make a tuple.
```
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
```
- we can access the tuple with same methods we used with lists

### changing tuples

- Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
```
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
```
- delete the tuple using `del` keyword
`del thistuple`

- unpacking a tuple
```
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits
```

- The number of variables must match the number of values in the tuple, if not, you must use an asterix to collect the remaining values as a list
```
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits
```


- join two tuples
`tuple3 = tuple2 + tuple 1`
- multiply tuples
```
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
```
o/p :
`('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')`

- `count()` -Returns the number of times a specified value occurs in a tuple
- `index()` -Searches the tuple for a specified value and returns the position of where it was found
 































