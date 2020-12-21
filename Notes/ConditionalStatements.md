## If statements

```
a = 33
b = 200
if b > a:
  print("b is greater than a")
```

- Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. If statement, without indentation will raise an error

## Elif

The `elif` keyword is pythons way of saying "if the previous conditions were not true, then try this condition".

```
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
```

## Else

The `else` keyword catches anything which isn't caught by the preceding conditions.

```
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
```
- we can also have `else` without `elif`

## Short Hand If
If we have only one statement to execute, we can put it on the same line as the if statement.
`if a > b: print("a is greater than b")`

## Short Hand If ... Else

If we have only one statement to execute, one for if, and one for else, we can put it all on the same line:
```
a = 2
b = 330
print("A") if a > b else print("B")
```
*This technique is known as **Ternary Operators**, or **Conditional Expressions**.*

- We can also have multiple else statements on the same line
```
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
```
o/p - `=`

- You can have `if` statements inside `if` statements, this is called nested `if` statements.
```
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
```
### The pass Statement
`if` statements cannot be empty, but if you for some reason have an `if` statement with no content, put in the `pass` statement to avoid getting an error.
```
a = 33
b = 200

if b > a:
  pass
```


