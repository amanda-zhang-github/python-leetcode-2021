# Python Refresh

## Contents
 - [Variable](#variable) 
 - [Set](#set) 
 - [Itertools](#itertools)

<a name="variable">

### Variable

</a>
- Variable is case sensitive, `a` and `A` are different variables
- Assign multiple variables: 

  ```
  x, y, z = 1, 2, 3   # many values to many variables
  x = y = x = 1       # single value to many variables
  x, y, x = [1, 2, 3] # unpack a collection
  ```
  
- Global variables can be created/used outside and inside a method
  If you create a variable inside a method, that variable is **local**.
  To create/change value of a global variable, you have to use the keyword `global`.

<a name="set">

### Set

</a>

Set items are **unordered**, **unique** and **immutable**.

#### Create a set
- Set can be created in 2 ways: `Set(<iter>)` and `{item1, item2, ...}`.
  - `Set(<iter>)` takes any iterable variable, string is iterable, so `set('abc') = {'a', 'b', 'c'}`
  - `{item1, item2, ...}` item type must be immutable, so item can be tuple but not list
  - `{}` means empty dict, so the only way to create an empty set is by `set()`.
- Immutable item means: 
  - If you try to create a set with mutable item (such as a list), exception will be thrown.
  - You can add/remove item into the set, but not changing the item that is in the set.
- Set can have items of different types, `{a, 'abc', 0.0, None}`.

#### Set Operation
- union: `a.union(b)` or `a | b`
- intersection: `a.intersection(b)` or `a & b`
- difference: `a.difference(b)` or `a - b`
- symmetric difference: `a.symmetric_difference(b)` or `a ^ b`
- is disjoint: `a.isdisjoint(b)` or check if `a & b` is empty
- is subset: `a.issubset(b)` or `a <= b`
- is super set: `a.issuper(b)` or `a >= b`

#### Set Modification
- add
- remove vs discard vs pop
  - remove throws exception if item doesn't exist
  - discard doesn't throw exception
  - pop removes a random item and throws exception is the set is empty
- clear

#### Set vs Frozenset
Frozenset is immutable, therefore you can't add/remove items. Recall that set items must be immutable, so frozenset is useful when you want to create a set of set (or other case that requires an immutable variable).

<a name="itertools">

## [itertools](https://pymotw.com/3/itertools/index.html): module for working with sequential data

</a>

Benefits:

- Simple functions hooked together to express more complicated use case
- Less memory consumption as data is not produced from the iterator until it is needed, so all data doesn't need to be stored in memory at the same time

Iterator functions can be grouped into the following categories:

- [Merge](#merge)
- [Split](#split)
- [Duplicate](#duplicate)
- [Convert Inputs](#convert)
- [Filter](#filter)
- [Group](#group)
- [Combine](#combine)
- [Generate Iterables](#generate)

<a name="merge">

### Merge

</a>

For a list of iterable containers, we can do the merge vertically or horizontally.

#### Vertical Merge (水平合并)
`chain()` takes several iterators as arguments and returns a single iterator that produces the contents of all inputs

```
from itertools import *
chain([1, 2, 3], ['a', 'b', 'c'])
# -> 1, 2, 3, 'a', 'b', 'c'
```
`chain.from_iterable()` takes in an iterable argument, each element in the argument is also iterable, and flattens the argument.

```
# string is iterable
chain.from_iterable(['abc', 'def'])
# -> 'a', 'b', 'c', 'd', 'e', 'f'
```

#### Horizontal Merge (垂直合并)
`zip()` and `zip_longest()` both return an iterator that contains the **elements** of **several** iterators into tuples.

- `zip` stops when the first iterator is exhausted
- `zip_longest` will process all the inputs and substitutes `None` for any missing values.
- `zip_longest` can take an extra parameter `fillvalue`, which is used to specify a different substitute value

```
zip([1, 2, 3], ['a', 'f', 'edf'])
# -> (1, 'a'), (2, 'f'), (3, 'edf')

zip_longest([1, 2, 3], ['a', 'f', 'edf', '456'])
# -> (1, 'a'), (2, 'f'), (3, 'edf'), (None, '456')

zip_longest(
    [{'name': 'amanda', 'gender': 'female'}, {'name': 'tim', 'gender': 'male'}],
    [{'membership': True}], 
    fillvalue={'membership': False}
)
# output:
# ({'name': 'amanda', 'gender': 'female'}, {'membership': True})
# ({'name': 'tim', 'gender': 'male'}, {'membership': False})
```
<a name="split">

### Split

</a>

#### List slicing 
`L[start:stop:step]` returns the portion of the list from `start` to `stop`(excluded) at a step size `step`.

- Step size is optional, and `L[start:end] = L[start:end:1]`.
- Start and end are also optional, but need to have `:` in between, `L[:] = L[0:len(L)]`.

#### Slice with Negative Indices
- the right of the last element is labeled as index 0
- the right of the second last element is index 1
- the right of the first element is index len - 1
- the left of the first element is index len

```
L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
#   |    |    |    |    |    |    |    |    |   |
#   0    1    2    3    4    5    6    7    8   9   positve index
#  -9   -8   -7   -6   -5   -4   -3   -2   -1   0   nagetive index
                                     
L[2:7]    # -> ['c', 'd', 'e', 'f', 'g']
L[-7:-2]  # -> ['c', 'd', ' e', 'f', 'g']
L[2:-1]   # -> ['c', 'd', 'e', 'f', 'g', 'h']
```
Negative index is treated the same as the positive index. I think the reason to use positve and nagetive index together is to simplify the notation, for example `L[2:-1]` is cleaner than `L[2:len(L)-1]`.

Note that negative index doesn't change the direction of slicing, nagetive step size does!

```
L[-7:-2:2]   # -> ['c', 'e', 'g']
L[-7:-2:-2]  # -> ['g', 'e', 'c']
```
Slice with negative step size -1 can be used to reserve a list:

```
L[::-1]   # -> ['i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
```

#### Copy vs Clone a List
This part was confusing to me, so I think I need to write it down. 

- Slicing can be used to modify, insert, delete elements into specific position.
  - modify： `L[1:4] = [1, 2, 3] -> L = ['a', 1, 2, 3, 'e', 'f', 'g', 'h', 'i']`
    - insert: `L[1:1] =  [1, 2] -> L = [1, 2, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']`
    - delete: `L[:5] = [] -> ['f', 'g', 'h', 'i']`
- Assignment together with list slicing generates a **shallow copy** of the sliced part.

	```
	L_new = L[:]
	print(L_new is L)   # False
	```
我困惑的点在于modify sliced part will modify the original list, 但是assign sliced list to a new list generates a shallow copy. 我猜想是assign这个过程把clone变成了copy，且这应该是一个跟slicing有关的特殊操作，因为一般的assign都是clone。

Slicing result is iterable, so if we only use it as a way to specify how to loop a list, here is an iterator version `islice(iterable, start, stop, step)`, which uses less memory. `islice` takes the same parameters as the `slice` operator. Ulike in `slice`, the stop parameter in `islice` is madatory.

<a name="duplicate">

### Duplicate

</a>
`tee(iterator, n)` returns n iterators and they refer to the same underlying interator. Therefore, once the new ones are generated, the original iterator should not be used. Otherwise, the generated iterator will also change. 

```
r = islice(count(), 5)
i1, i2 = tee(r, 2)

for i in r:
    print(i)
    if (i > 2):
        break;
# -> 1, 2, 3

print('i1:', list(i1))  # -> 4
print('i2:', list(i2))  # -> 4
```
But using one generated iterator will not affect another generated iterator.

```
r = islice(count(), 5)
i1, i2 = tee(r, 2)
print('i1:', list(i1))  # -> 1, 2, 3, 4
print('i2:', list(i2))  # -> 1, 2, 3, 4
```
**It can be used to feed the same set of data into multiple algorithms to be processed in parallel.**

<a name="convert">

### Convert Input

</a>

Convert means apply a function on the values in the input iterators and return a new iterator.

- `map(func, iterable(s))`

  ```
  map(lambda x: x*2, [1, 2, 3])
  map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6])
  ```
- `starmap(func, iterator)`

  ```
  starmap(lambda x, y: x + y, [(1, 4) , (2, 5), (3, 6)])
  ```
Difference between `map` and `starmap`: `map` can take multiple iterators, where the number of iterators equals to the number of func's parameters; `starmap` takes single iterator, and each value in the iterator can be a tuple of multiple elements.

<a name="filter">

### Filter

</a>

| Function | Condition |
| ------ | ------ |
| `dropwhile(predicate, iterable)` | drop item until the first item evaluated as False |
| `takewhile(predicate, iterable)` | take item until the first item evaluated as False |
| `filter(predicate, iterable)` | take all item which are evaluated as True |
| `filerFalse(predicate or None, iterable)` | take all item which are evaluated as False |
| `compress(iter, selector(boolean value iterable))` | take all item which the selector is True or 1|

<a name="group">

### Group

</a>
`groupby(iterable, key_func)` returns an iterator that produces sets of values organized by a common key.

<a name="combine">

### Combine (排列组合)

</a>

- `accumulate(iterable, func)` returns the cumulative result of the function at each step

  ```
  accumulate('abc')                               # -> a, ab, abc
  accumulate([1, 2, 3, 4, 5], lambda x,y : x * y) # -> 1, 2, 6, 24, 120
  ```
  If no func gets passed, the default action is addition.
  
- `product` returns Cartesian product of the input iterables.
	- `product(iterable, repeat=1)` repeat the single iterable n times
	
	  ```
	  product([1, 2], repeat=3)
	  # -> 
	  # (1, 1, 1), (1, 1, 2), (1, 2, 1), (1, 2, 2)
	  # (2, 1, 1), (2, 1, 2), (2, 2, 1), (2, 2, 2)
	  ```
	  
	- `product(iterables)`
	
		```
		product([1, 2], ['a', 'b', 'c'])
		# -> (1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c')
		```
- permutation
  - `permutation(iterable)` generates n! permutations, where n is length of the input sequence
  - `permutations('iterable', l)` generates permutations of length l  
- `combination` / `combinations_with_replacement`
  - `combination(iterable)` generates all unique combination of length n
  - `combination(iterable, l)` generates all possible combination of length l

<a name="generate">

### Generate Iterables

</a>

| Function | |
| ------ | ------ |
| `count(start, step)` | Returns an iterator that produces consecutive numbers, **indefinitely**. Start and step are both optional, start defaults to 0, step defaults to 1 |
| `cycle(iterable)` | Returns an iterator that repeats the input iterable indefinitely |
| `repeat(val, num)` | Returns an iterator that produces the input value for given number of times. If the number is not specified, repeat indefinitely |