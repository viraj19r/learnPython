Python has two primitive loop commands:

`while` loops
`for` loops
 ## While loop

 With the `while` loop we can execute a set of statements as long as a condition is true.
Ex:
Print i as long as i is less than 6:
```
i = 1
while i < 6:
  print(i)
  i += 1
```
- if we don't increment the `i` then the loop will continue forever.

- The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1

### break Statement
With the `break` statement we can stop the loop even if the while condition is true
```
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
```

### continue Statement
With the continue statement we can stop the current iteration, and continue with the next:
```
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
```

## For loop

A `for` loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string)

The `for` loop does not require an indexing variable to set beforehand.

```
for x in "banana":
  print(x)
```
### break statement
```
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break     #exit the loop when x is banana
```
### continue statement
With the `continue` statement we can stop the current iteration of the loop, and continue with the next

```fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
```

### The range() Function
To loop through a set of code a specified number of times, we can use the `range()` function,
The `range()` function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
```
for x in range(6):
  print(x)
```

- Note that `range(6)` is not the values of 0 to 6, but the values 0 to 5.

The `range()` function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: `range(2, 6)`, which means values from 2 to 6 (but not including 6)

`for x in range(2, 6):`

The `range()` function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: `range(2, 30, 3)`

```
Increment the sequence with 3 (default is 1):

for x in range(2, 30, 3):   #increment with a difference of 3
  print(x)
```  

### Else in For Loop
The else keyword in a for loop specifies a block of code to be executed when the loop is finished
```
for x in range(6):
  print(x)
else:
  print("Finally finished!")
```


`for` loops cannot be empty, but if you for some reason have a `for` loop with no content, put in the `pass` statement to avoid getting an error.
```
for x in [0, 1, 2]:
  pass
```






