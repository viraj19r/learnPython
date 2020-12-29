
Numpy(Numerical python) is a python library used for working with arrays  

In python we have lists which can be used to serve the purpose of array but they are slow to process.
NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.

The array object in NumPy is called `ndarray`, it provides a lot of supporting functions that make working with `ndarray` very easy

## Install Numpy
If we have already installed PIP and python then Numpy can be easily installed
`pip install numpy`
then import Numpy and use
```
import numpy
arr = numpy.array([1, 2, 3, 4, 5])
```

- NumPy is usually imported under the `np` alias.
```
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
```
- checking numpy version
```
import numpy as np
print(np.__version__)
```
## Create a NumPy ndarray Object
We can create a NumPy `ndarray` object by using the `array()` function.
```
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
```
- To create an `ndarray`, we can pass a list, tuple or any array-like object into the `array()` method, and it will be converted into an `ndarray`
 use tuple to create a Numpy array
`arr = np.array((1, 2, 3, 4, 5))`

## Dimensions in Array
A dimension in arrays is one level of array depth (nested arrays).


### 0-D Arrays
0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.

```
import numpy as np
arr = np.array(42)
```


### 1-D Arrays
An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.
These are the most common and basic arrays.


`arr = np.array([1, 2, 3, 4, 5])`
### 2-D Arrays
An array that has 1-D arrays as its elements is called a 2-D array.
These are often used to represent matrix or 2nd order tensors.
`arr = np.array([[1, 2, 3], [4, 5, 6]])`

> NumPy has a whole sub module dedicated towards matrix operations called `numpy.mat`

### 3-D arrays
An array that has 2-D arrays (matrices) as its elements is called 3-D array.
These are often used to represent a 3rd order tensor
`arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])`



- NumPy Arrays provides the `ndim` attribute that returns an integer that tells us how many dimensions the array have.
```
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
```

### Higher Dimensional Arrays
An array can have any number of dimensions.

When the array is created, you can define the number of dimensions by using the `ndmin` argument
```
import numpy as np
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)
```
o/p:
```
[[[[[1 2 3 4]]]]]
number of dimensions : 5
```


