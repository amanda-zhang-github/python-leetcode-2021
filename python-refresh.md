# Python Refresh
### Variable
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

### Set
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
