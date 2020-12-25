JSON is a syntax for storing and exchanging data.

JSON is text, written with JavaScript object notation.  

Python has a built-in package called `json`, which can be used to work with JSON data.

### Parse JSON - Convert from JSON to Python
If we have a JSON string, we can parse it by using the `json.loads()` method.

```
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
```

### Convert from Python to JSON
If you have a Python object, you can convert it into a JSON string by using the `json.dumps()` method.

```
import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
```

We can convert Python objects of the following types, into JSON strings:

- dict
- list
- tuple
- string
- int
- float
- True
- False
- None

When we convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent

|Python|JSON|
|-------|-----------|
|dict	|Object|
|list|	Array|
|tuple|	Array|
|str|	String|
|int|	Number|
|float|	Number|
|True|	true|
|False|	false|
|None|	null|

Convert a Python object containing all the legal data types:
```
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))
```
o/p:
```
{"name": "John", "age": 30, "married": true, "divorced": false, "children": ["Ann","Billy"], "pets": null, "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}]}
```


The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.

The `json.dumps() `method has parameters to make it easier to read the result

`json.dumps(x, indent=4)`

o/p:
```
{
    "name": "John",
    "age": 30,
    "married": true,
    "divorced": false,
    "children": [
        "Ann",
        "Billy"
    ],
    "pets": null,
    "cars": [
        {
            "model": "BMW 230",
            "mpg": 27.5
        },
        {
            "model": "Ford Edge",
            "mpg": 24.1
        }
    ]
}
```

You can also define the separators, default value is (", ", ": "), which means using a comma and a space to separate each object, and a colon and a space to separate keys from values
`json.dumps(x, indent=4, separators=(". ", " = "))`

Use the `sort_keys` parameter to specify if the result should be sorted or not:
`json.dumps(x, indent=4, sort_keys=True)`

