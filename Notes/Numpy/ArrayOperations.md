## Array Indexing

### Accessing array elements:
The indexes in NumPy arrays start with 0, meaning that the first element has index 0, and the second has index 1 etc.

`arr[1]` to access second element


### Access 2-D Arrays
To access elements from 2-D arrays we can use comma separated integers representing the dimension and the index of the element
```
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st dim: ', arr[0, 1])
```

### Access 3-D Arrays
To access elements from 3-D arrays we can use comma separated integers representing the dimensions and the index of the element
```
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2]) #6
```

### Negative Indexing
use negative indexing to access an array from end
```
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[1, -1]) #10
```

## Slicing Arrays
`[start:end]` or `[start:end:step]`

If we don't pass start its considered 0
If we don't pass end its considered length of array in that dimension
If we don't pass step its considered 1


- The result *includes* the start index, but *excludes* the end index.
- use the negative sign to refer to an index from end.

Ex - Return every other element from the entire array
```
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[::2])
```
o/p:

```
[1 3 5 7]
```

### Slicing 2-D arrays
```
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4]) #choose second array and 2 to 4 elements in that array (index 1-3)
```
o/p:
```
[7 8 9]
```
Ex-From both elements, return index 2
```
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 2]) #choose both array 0 and 1 and then 2nd element in the both arrays
```
o/p:
`[3 8]`

From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:

```
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 1:4]) #choose both the arrays and then slice elements 2 to 4 from both array
```
o/p:
```
[[2 3 4]
 [7 8 9]]
```

## Data Types in Numpy
NumPy has some extra data types, and refer to data types with one character, like i for integers, u for unsigned integers etc

- Data types
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )

- The NumPy array object has a property called `dtype` that returns the data type of the array:
Get the data type of an array - `arr.dtype`

- We can create arrays with a defined data types
`arr = np.array([1, 2, 3, 4], dtype='S')`
- For `i`, `u`, `f`, `S` and `U` we can define size as well.
`arr = np.array([1, 2, 3, 4], dtype='i4')` 4bytes integer

- A non integer string like 'a' can not be converted to integer (will raise an error)
`arr = np.array(['a', '2', '3'], dtype='i')`

> ValueError: In Python ValueError is raised when the type of passed argument to a function is unexpected/incorrect.

### Converting Data Type on Existing Arrays
The best way to change the data type of an existing array, is to make a copy of the array with the `astype()` method. It creates a copy of array and allow us to specify type

```
arr = np.array([1.1, 2.1, 3.1]) 
newArr = arr.astype('i') #[1,2,3] type= i32
```
or 
```
arr = np.array([1.1, 2.1, 3.1])
newArr = arr.astype(int) #[1,2,3] type = i64
```
change to boolean
```
arr = np.array([1, 0, 3])
newArr = arr.astype(bool) #[True,False,True] type = bool
```


## Numpy copy vs view
- The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array
- The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy
- The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view

```
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy() #copy of arr
x = arr.view() #view of arr
```

### Check if array own it's data (copy or view)
Every NumPy array has the attribute base that returns None if the array owns the data.
Otherwise, the base  attribute refers to the original object

```
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()
print(x.base) #None
print(y.base) #[1,2,3,4,5]
```

## Shape of Array
NumPy arrays have an attribute called `shape` that returns a tuple with each index having the number of corresponding elements.

```
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape) #(2,4) means matrix of 2x4(2 dimension with each dimension having 4 elements)
```

## Array Reshaping
- changing the shape of array
- By reshaping we can add or remove dimensions or change number of elements in each dimension.

### Reshape From 1-D to 2-D

```
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newArr = arr.reshape(4, 3)
```
o/p:
```
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]
```
### Reshape From 1-D to 3-D
```
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newArr = arr.reshape(2, 3, 2)
```
o/p:
```
[[[ 1  2]
  [ 3  4]
  [ 5  6]]

 [[ 7  8]
  [ 9 10]
  [11 12]]]
```
Can we reshape in any shape ?
Yes
We can reshape an 8 elements 1D array into 4 elements in 2 rows 2D array but we cannot reshape it into a 3 elements 3 rows 2D array as that would require 3x3 = 9 elements
Try converting 1D array with 8 elements to a 2D array with 3 elements in each dimension will raise an error

>Reshaping returns view of array

#### unknown dimension
we don't have to specify an exact no of dimension in the reshape method
Pass -1 as the value, and NumPy will calculate this number for us.
```
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newArr = arr.reshape(2, 2, -1)
```
o/p
```
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
```
> We can not pass -1 to more than one dimension.
#### Flattening the arrays
convert multi dimensional array into 1D array
we can use `reshape(-1)` to do this
  
## Array Iterating
Iterating - going through the elements one by one
we can iterate through a `for` loop
```
arr = np.array([1, 2, 3])

for x in arr:
  print(x)
```
> If we iterate on a n-D array it will go through n-1th dimension one by one.

- iterating 2D array
```
arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  for y in x:
    print(y)
```

- iterating 3D array
```
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  print(x)  #produce 2d arrays


for x in arr:
  for y in x:
    for z in y:
      print(z)  #iterate through each element/scalars

```

### Iterating Arrays Using nditer()

The function `nditer()` is a helping function that can be used from very basic to very advanced iterations. It solves some basic issues which we face in iteration

#### Iterating on Each Scalar Element
In basic `for` loops, iterating through each scalar of an array we need to use n `for` loops which can be difficult to write for arrays with very high dimensionality

```
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)  #1 2 3 4 5 6 7 8
```

#### Iterating Array With Different Data Types
We can use `op_dtypes` argument and pass it the expected datatype to change the datatype of elements while iterating.

NumPy does not change the data type of the element in-place (where the element is in array) so it needs some other space to perform this action, that extra space is called buffer, and in order to enable it in `nditer()` we pass `flags=['buffered']`

```
arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)
```
o/p:
```
b'1'
b'2'
b'3'
```
#### Iterating With Different Step Size
Iterate through every scalar element of the 2D array skipping 1 element:
```
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
  print(x) # 1 3 5 7
```

#### Enumerated Iteration Using ndenumerate()
Enumeration means mentioning sequence number of somethings one by one.
Sometimes we require corresponding index of the element while iterating, the `ndenumerate()` method can be used for those use cases
So basically by this method we can get the index of each element while iterating    
Enumerate on 1D array
```
arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
  print(idx, x)
```
o/p:
```
(0,) 1
(1,) 2
(2,) 3
```
Enumerate on 2D array
```
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr):
  print(idx, x)
```
o/p:
```
(0, 0) 1
(0, 1) 2
(0, 2) 3
(0, 3) 4
(1, 0) 5
(1, 1) 6
(1, 2) 7
(1, 3) 8
```


## Joining Array
We pass a sequence of arrays that we want to join to the `concatenate()` function, along with the axis. If axis is not explicitly passed, it is taken as 0
```
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))
```
- joining 2D arrays along rows(axis=1)
```
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)
```
o/p:
```
[[1 2 5 6]
 [3 4 7 8]]
```
### Joining array using stack functions
Stacking is same as concatenation, the only difference is that stacking is done along a new axis.
We can concatenate two 1-D arrays along the second axis which would result in putting them one over the other, ie. stacking
We pass a sequence of arrays that we want to join to the `stack() `method along with the axis. If axis is not explicitly passed it is taken as 0.
```
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)

print(arr)
```
o/p:
```
[[1 4]
 [2 5]
 [3 6]]
```
#### Stacking Along Rows(horizontal)
NumPy provides a helper function: `hstack()` to stack along rows.
```
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.hstack((arr1, arr2))
print(arr) #[1,2,3,4,5,6]
```
#### Stacking Along Columns(vertical)
NumPy provides a helper function: `vstack()`  to stack along columns.
```
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.vstack((arr1, arr2))
print(arr)
```
o/p:
```
[[1 2 3]
 [4 5 6]]
```
#### Stacking Along Height (depth)
NumPy provides a helper function: `dstack()` to stack along height, which is the same as depth.
```
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.dstack((arr1, arr2))
print(arr)
```
o/p:
```
[[[1 4]
  [2 5]
  [3 6]]]
```


## Splitting Array
We use `array_split()` for splitting arrays, we pass it the array we want to split and the number of splits

```
arr = np.array([1, 2, 3, 4, 5, 6])
newArr = np.array_split(arr, 3)
print(newArr)
```
o/p:
`[array([1, 2]), array([3, 4]), array([5, 6])]`
> The return value is an array containing three arrays

> If the array has less elements than required then it will adjust the end accordingly 

> We also have the method split() available but it will not adjust the elements when elements are less in source array for splitting like in example above, array_split() worked properly but split() would fail

split 2D arrays
```
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newArr = np.array_split(arr, 3)

print(newArr)
```
o/p:
```
[array([[1, 2],[3, 4]]),
 array([[5, 6],[7, 8]]),
 array([[ 9, 10],[11, 12]])]
```
- we can specify axis
```
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newArr = np.array_split(arr, 3, axis=1)
print(newArr)
```
o/p:
```
[array([[ 1],
       [ 4],
       [ 7],
       [10],
       [13],
       [16]]), array([[ 2],
       [ 5],
       [ 8],
       [11],
       [14],
       [17]]), array([[ 3],
       [ 6],
       [ 9],
       [12],
       [15],
       [18]])]
```
- An alternate solution is using` hsplit()` opposite of `hstack()`
produce same result as above
```
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newArr = np.hsplit(arr, 3)
```
> Similar alternates to `vstack()` and `dstack()` are available as `vsplit()` and `dsplit()`



## Searching array
we can search for an array and return the index of array that get matched
To search an array, use the `where()`method.
```
arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4) #(array([3, 5, 6]),)
```

```
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 0)  #(array([1, 3, 5, 7]),)
```
### Search Sorted
There is a method called `searchsorted()` which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order
> The `searchsorted()` method is assumed to be used on sorted arrays.
```
arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)   # x outputs 1
```
The number 7 should be inserted on index 1 to remain the sort order.The method starts the search from the left and returns the first index where the number 7 is no longer larger than the next value.

- By default the left most index is returned, but we can give `side='right'` to return the right most index instead.

```
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7, side='right') #x outputs 2
```

- To search for more than one value, use an array with the specified values.
```
arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6]) 
```
The return value is an array: `[1 2 3]` containing the three indexes where 2, 4, 6 would be inserted in the original array to maintain the order.

 
## Sorting Arrays
Numpy ndarray object has a function called `sort()`  to sort specified arrays
`arr = np.array([3, 2, 0, 1])` # [0,1,2,3]

> This method returns a copy of the array, leaving the original array unchanged


we can also sort array of strings or any other data type
```
arr = np.array(['banana', 'cherry', 'apple'])
np.sort(arr)#['apple' 'banana' 'cherry']
```

sort a boolean array
```
arr = np.array([True, False, True])
np.sort(arr)# [False True True]
```

- If we sort 2D array both arrays will be sorted
```
arr = np.array([[3, 2, 4], [5, 0, 1]])
np.sort(arr)
```
o/p:
```
[[2 3 4]
 [0 1 5]]
```

## Filtering Array
Getting some elements out of a existing array and creating a new array out of them is called filtering
In NumPy, we filter an array using a *boolean index list*.
A boolean index list is a list of booleans corresponding to indexes in the array.

If the value at an index is `True` that element is contained in the filtered array, if the value at that index is `False` that element is excluded from the filtered array

```(not use this approach)
import numpy as np

arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newArr = arr[x]

print(newArr)
```
The example above will return `[41, 43]`
Because the new filter contains only the values where the filter array had the value `True`.

### Creating the Filter Array(not use this)
In the example above we hard-coded the `True` and `False` values, but the common use is to create a filter array based on conditions.
create a filter array that will return only values greater than 42
```
import numpy as np

arr = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)
```
### Creating Filter Directly From Array
We can directly substitute the array instead of the iterable variable in our condition and it will work just as we expect it to

```
import numpy as np

arr = np.array([41, 42, 43, 44])

filter_arr = arr > 42

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)
```

## Random Number
Random number does NOT mean a different number every time. Random means something that can not be predicted logically.

NumPy offers the `random` module to work with random numbers.
- Generate a random integer from 0 to 100:
```
from numpy import random

x = random.randint(100)

print(x)
```
- The random module's `rand()` method returns a random float between 0 and 1
```
from numpy import random
x = random.rand()
print(x)
```
- we can also generate random arrays by above two methods
The `randint()` method takes a `size` parameter where you can specify the shape of an array.


Generate a 1-D array containing 5 random integers from 0 to 100:
```
from numpy import random

x=random.randint(100, size=(5))

print(x)
```

Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:
```
from numpy import random

x = random.randint(100, size=(3, 5))
```

- The `rand()` method also allows us to specify the shape of the array.
`x = random.rand(5)`
`x = random.rand(3, 5)`

### Generate Random Number From Array
The `choice()` method allows you to generate a random value based on an array of values.
The `choice()` method takes an array as a parameter and randomly returns one of the values.

```
from numpy import random

x = random.choice([3, 5, 7, 9])
```

The `choice()` method also allows us to return an array of values.

Add a `size` parameter to specify the shape of the array

`x = random.choice([3, 5, 7, 9], size=(3, 5))`
o/p like:
```
[[9 3 5 5 7] 
 [7 5 3 3 9] 
 [7 5 9 9 7]]
```

- [Random number in more detail](https://www.w3schools.com/python/numpy_random.asp)


## Numpy ufuncs
ufuncs stands for "Universal Functions" and they are NumPy functions that operates on the ndarray object
they include all type of mathematical operation on arrays

- [ufuncs in detail](https://www.w3schools.com/python/numpy_ufunc.asp)

