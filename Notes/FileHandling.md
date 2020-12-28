- File handling is an important part of any web application.

Python has several functions for creating, reading, updating, and deleting files.

The key function for working with files in Python is the `open()` function.
The `open()` function takes two parameters; `filename, and mode`.

There are four different methods (modes) for opening a file:

`"r"` - Read - Default value. Opens a file for reading, error if the file does not exist

`"a"` - Append - Opens a file for appending, creates the file if it does not exist

`"w"` - Write - Opens a file for writing, creates the file if it does not exist

`"x"` - Create - Creates the specified file, returns an error if the file exists


- In addition we can specify if the file should be handled as binary or text mode
`"t"` - Text - Default value. Text mode
`"b"` - Binary - Binary mode (e.g. images)

To open a file for reading it is enough to specify the name of the file:

`f = open("demofile.txt")`
or
`f = open("demofile.txt", "rt")`
Because `"r"` for read and `"t"` for text are the default values, we do not need to specify them.

- If the file does not exist, we get an error

The `open()` function returns a file object, which has a `read()` method for reading the content of the file:

Example:
```
f = open("demofile.txt", "r")
print(f.read())
```
- If the file is located in a different location then we have to specify the file path

`f = open("D:\\myfiles\welcome.txt", "r")`

- By default the `read()` method returns the whole text, but we can also specify how many characters you want to return
```
f = open("demofile.txt", "r")
print(f.read(5))
```
- we can return one line by using `readline()` method and by calling two times, we can read first two lines and 

```
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())
```

- By looping through the line, we can read the whole file line by line
```
f = open("demofile.txt", "r")
for x in f:
  print(x)
```
- It is a good practice to always close the file when we are done with the file
```
f = open("demofile.txt", "r")
print(f.readline())
f.close()
```                                                                 
- To write to an existing file, we must add a parameter to the `open()` function:
`"a"` - Append - will append to the end of the file

`"w"` - Write - will overwrite any existing content
```
f = open("demofile2.txt", "a")   #append the file
f.write("Now the file has more content!")
f.close()
```
```
f = open("demofile3.txt", "w")   #overwrite the content
f.write("Woops! I have deleted the content!")
f.close()
```

### Create a New File
To create a new file in Python, we use the `open()` method, with one of the following parameters:

`"x"` - Create - will create a file, returns an error if the file exist

`"a"` - Append - will create a file if the specified file does not exist

`"w"` - Write - will create a file if the specified file does not exist

`f = open("myfile.txt", "x")`
`f = open("myfile.txt", "w")`

### Delete a File
To delete a file, we must import the OS module, and run its `os.remove()` function
```
import os
os.remove("demofile.txt")
```
To avoid getting error, we might first check if the file exist before we try to delete
```
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
```
To delete an entire folder, use the `os.rmdir()` method:
```
import os
os.rmdir("myfolder")
```
we can only remove only empty folder




