We can import a module named `datetime` to work with dates as objects.

```
import datetime

x = datetime.datetime.now()
print(x)
```

## Creating Date Objects
To create a date, we can use the `datetime()` class (constructor) of the `datetime` module.

The `datetime()` class requires three parameters to create a date: year, month, day

```
import datetime

x = datetime.datetime(2020, 5, 17)
```

The `datetime()` class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone), but they are optional, and has a default value of `0`, (`None` for timezone)

## The strftime() Method
- The method is called `strftime()`, and takes one parameter, `format`, to specify the format of the returned string

```
Display the name of the month:

import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))
```

- [Reference to all legal format codes](https://www.w3schools.com/python/python_datetime.asp)















