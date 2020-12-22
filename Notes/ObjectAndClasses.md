- Python is an object oriented programming language.
- Almost everything in Python is an object, with its properties and methods.
- A Class is like an object constructor, or a "blueprint" for creating objects


- Create a class
```
 class MyClass:
  x = 5
```
- Create objects
```
p1 = MyClass()
```

## The `__init__()` Function
All classes have a function called` __init__()`, which is always executed when the class is being initiated.
Use the `__init__()` function to assign values to object properties, or other operations that are necessary to do when the object is being created.
```
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
```
- The `__init__()` function is called automatically every time the class is being used to create a new object.


## Object Methods
Methods in objects are functions that belong to the object
Methods in objects are functions that belong to the object
```
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
```


## The self Parameter

- The `self` parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
- It does not have to be named `self`, we can name it whatever we want
- But it has to be the first parameter of any function in the class

Use the words `mysillyobject` and `abc` instead of self:

```
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
```
## Modify object properties 

`p1.age = 40`
`del p1.age`   delete object properties
`del p1`   delete object


- Use `pass` statement when class is empty
```
class Person:
  pass
```

## Python Inheritance

Inheritance allows us to define a class that inherits all the methods and properties from another class.
- **Parent class** is the class being inherited from, also called base class.
- **Child class** is the class that inherits from another class, also called derived class.

Now create a parent class(syntax is same as of a normal class)
```
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()
```


Create child class and inherit all the properties of the parent class

```
class Student(Person):  #to use inheritance we simply put the parent class name in parenthesis
  pass
```
Use the `pass` when there is no property or method in child class

Now,Use the Student class to create an object, and then execute the printname method
```
x = Student("Mike", "Olsen")
x.printname()
```

### Add the `__init__()` Function

Add the `__init__()` function to the Student class:
```
class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.
```

When we add the `__init__()` function, the child class will no longer inherit the parent's `__init__()` function.
The child's `__init__() `function overrides the inheritance of the parent's `__init__()` function
To keep the inheritance of the parent's `__init__()` function, add a call to the parent's `__init__()` function

```
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
```

#### Use the `super()` Function
Python also has a `super()` function that will make the child class inherit all the methods and properties from its parent:
```
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
```
- By using the `super()` function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent

#### Add properties and methods
Add a property called `graduationyear` to the `Student` class:
```
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019
```
In the example below, the year `2019` should be a variable, and passed into the Student class when creating student objects. To do so, add another parameter in the `__init__()` function

```
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
```
Add a method called welcome to the Student class:
```
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
```
- If we add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.














