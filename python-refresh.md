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

- Merge Iterators
- Split Iterators
- Convert Inputs
- Produce New Values
- Filtering
- Group Data
- Combine Inputs

### Merge Iterator
For a list of iterable containers, we can merge do the merge vertically or horizontally.

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

zip_longest([1, 2], ['a', 'edf', {1: 'amanda'}], fillvalue=dict())
# -> (1, 'a'), (2, 'edf'), ({}, {1: 'amanda'})
```








