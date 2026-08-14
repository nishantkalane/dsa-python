# Python Basics for DSA

> A quick reference for the Python concepts required to solve Data Structures and Algorithms problems.

---

## 1. Variables and Data Types

```python
name = "Nishant"
age = 22
height = 1.85
is_student = True
```

**Common Data Types**

| Type  | Example          |
|-------|-------------------|
| int   | 10                |
| float | 10.5              |
| str   | "hello"           |
| bool  | True / False      |
| list  | [1, 2, 3]         |
| tuple | (1, 2, 3)         |
| set   | {1, 2, 3}         |
| dict  | {"a": 1, "b": 2}  |

Check the type:

```python
x = 10
print(type(x))
```

---

## 2. Input and Output

**Input**

```python
n = int(input())
name = input()
```

Multiple integers:

```python
a, b = map(int, input().split())
```

List of integers:

```python
arr = list(map(int, input().split()))
```

Example:

```
Input:
5
1 2 3 4 5
```

```python
n = int(input())
arr = list(map(int, input().split()))
```

**Output**

```python
print("Hello")
print(n)
```

Print without moving to a new line:

```python
print("*", end=" ")
```

---

## 3. Operators

**Arithmetic**

```python
+       # addition
-       # subtraction
*       # multiplication
/       # division
//      # integer division
%       # remainder
**      # power
```

Example:

```python
print(10 // 3)   # 3
print(10 % 3)    # 1
```

**Important for DSA**

`%` is frequently used for:
- Digit extraction
- Checking even/odd
- Cyclic operations
- Hashing
- Modular arithmetic

```python
digit = n % 10
```

`//` is frequently used for:
- Removing the last digit
- Integer division

```python
n = n // 10
```

**Comparison Operators**

```python
==    # equal
!=    # not equal
>     # greater
<     # smaller
>=    # greater or equal
<=    # smaller or equal
```

**Logical Operators**

```python
and
or
not
```

Example:

```python
if age >= 18 and age <= 60:
    print("Valid")
```

---

## 4. Conditional Statements

```python
if condition:
    # code
elif another_condition:
    # code
else:
    # code
```

Example:

```python
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")
```

**Ternary Expression**

```python
result = "Even" if n % 2 == 0 else "Odd"
```

---

## 5. Loops

**For Loop**

```python
for i in range(5):
    print(i)
```

Output: `0 1 2 3 4`

**Range**

```python
range(stop)
range(start, stop)
range(start, stop, step)
```

Examples:

```python
range(5)          # 0 to 4
range(1, 6)       # 1 to 5
range(1, 10, 2)   # 1, 3, 5, 7, 9
```

Reverse:

```python
for i in range(5, 0, -1):
    print(i)
```

**While Loop**

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

Useful when the number of iterations is not known beforehand. Common in:
- Two pointers
- Sliding window
- Binary search
- Linked lists
- Recursion-related problems

**break** — stops the loop.

```python
for i in range(10):
    if i == 5:
        break
```

**continue** — skips the current iteration.

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

---

## 6. Functions

```python
def add(a, b):
    return a + b
```

Calling:

```python
result = add(5, 3)
```

Function with no return:

```python
def greet():
    print("Hello")
```

Default argument:

```python
def power(a, b=2):
    return a ** b
```

**Why functions matter in DSA**

Most DSA problems are easier to structure as:

```python
def solve():
    # logic

if __name__ == "__main__":
    solve()
```

---

## 7. Lists

Lists are the main Python structure used for arrays in DSA.

```python
arr = [10, 20, 30, 40]
```

Access:

```python
arr[0]      # first element
arr[-1]     # last element
```

Modify:

```python
arr[1] = 25
```

Add / Insert / Remove:

```python
arr.append(50)
arr.insert(1, 15)
arr.remove(30)
arr.pop()
arr.pop(1)
```

Length:

```python
len(arr)
```

---

## 8. List Traversal

By value:

```python
for x in arr:
    print(x)
```

By index:

```python
for i in range(len(arr)):
    print(arr[i])
```

Index and value together:

```python
for i, value in enumerate(arr):
    print(i, value)
```

This is very useful in DSA.

---

## 9. List Slicing

```python
arr = [10, 20, 30, 40, 50]

arr[1:4]    # [20, 30, 40]
arr[:3]     # [10, 20, 30]
arr[2:]     # [30, 40, 50]
arr[:]      # copy
```

Reverse:

```python
arr[::-1]
```

Every second element:

```python
arr[::2]
```

---

## 10. Useful List Operations

```python
arr.append(x)
arr.pop()
arr.sort()
arr.reverse()
arr.count(x)
arr.index(x)
```

Sorting:

```python
arr.sort()               # ascending, modifies original
arr.sort(reverse=True)   # descending
new_arr = sorted(arr)    # returns a new sorted list
```

**Important:** `arr.sort()` modifies the original list. `sorted(arr)` returns a new sorted list without changing the original.

---

## 11. Strings

```python
s = "hello"
```

Access: `s[0]`, `s[-1]`
Length: `len(s)`
Slice: `s[1:4]`
Reverse: `s[::-1]`

Useful methods:

```python
s.lower()
s.upper()
s.strip()
s.split()
s.replace()
s.count()
s.find()
```

Example:

```python
s = "hello world"
words = s.split()
```

---

## 12. String Traversal

```python
for ch in s:
    print(ch)
```

With index:

```python
for i in range(len(s)):
    print(s[i])
```

---

## 13. Tuples

Tuples are ordered and immutable.

```python
point = (10, 20)
print(point[0])
```

Tuple unpacking:

```python
a, b = point
```

Useful when returning multiple values:

```python
def get_values():
    return 10, 20

a, b = get_values()
```

---

## 14. Sets

Sets store unique elements.

```python
s = {1, 2, 3, 3}
print(s)   # {1, 2, 3}
```

Common operations:

```python
s.add(5)
s.remove(2)

if x in s:
    print("Found")
```

Sets are extremely useful for:
- Removing duplicates
- Fast membership checking
- Hashing problems

Typical lookup `x in s` — average time O(1).

---

## 15. Dictionaries

Dictionaries store key-value pairs.

```python
freq = {"a": 2, "b": 3}
```

Access: `freq["a"]`
Add/update: `freq["c"] = 5`
Check key:

```python
if "a" in freq:
    print("Found")
```

**Frequency Counting** — one of the most important patterns in DSA:

```python
freq = {}
for x in arr:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1
```

Shorter version:

```python
freq = {}
for x in arr:
    freq[x] = freq.get(x, 0) + 1
```

Example:

```python
arr = [1, 2, 2, 3, 3, 3]
freq = {}
for x in arr:
    freq[x] = freq.get(x, 0) + 1

print(freq)   # {1: 1, 2: 2, 3: 3}
```

---

## 16. List Comprehension

Normal way:

```python
squares = []
for i in range(5):
    squares.append(i * i)
```

List comprehension:

```python
squares = [i * i for i in range(5)]
```

With condition:

```python
even = [x for x in arr if x % 2 == 0]
```

Don't use comprehensions when they make the logic difficult to understand.

---

## 17. Built-in Functions Useful in DSA

```python
len(arr)
sum(arr)
min(arr)
max(arr)
sorted(arr)
reversed(arr)
abs(x)
```

Examples:

```python
total = sum(arr)
largest = max(arr)
smallest = min(arr)
```

---

## 18. Important Built-ins

**enumerate()** — get index and value:

```python
for i, value in enumerate(arr):
    print(i, value)
```

**zip()** — traverse multiple sequences together:

```python
a = [1, 2, 3]
b = [4, 5, 6]
for x, y in zip(a, b):
    print(x, y)
```

**any()** — True if at least one element is true:

```python
any(x > 10 for x in arr)
```

**all()** — True if every element is true:

```python
all(x > 0 for x in arr)
```

---

## 19. Mutable vs Immutable

**Mutable** (can be changed after creation): `list`, `set`, `dict`

**Immutable** (cannot be changed after creation): `int`, `float`, `str`, `tuple`, `bool`

Example:

```python
arr = [1, 2, 3]
arr[0] = 10   # works because lists are mutable
```

---

## 20. References and Copying

Be careful:

```python
a = [1, 2, 3]
b = a
b[0] = 100
print(a)   # a also changes — both refer to the same list
```

Create a real copy:

```python
b = a.copy()
# or
b = a[:]
```

---

## 21. Nested Lists

Useful for matrices and 2D arrays.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

Access:

```python
matrix[0][1]
```

Traversal:

```python
for row in matrix:
    for value in row:
        print(value)
```

---

## 22. Important DSA Input Patterns

Single integer:

```python
n = int(input())
```

Two integers:

```python
n, k = map(int, input().split())
```

Array:

```python
arr = list(map(int, input().split()))
```

Multiple test cases:

```python
t = int(input())
for _ in range(t):
    # solve each test case
```

---

## 23. Common DSA Patterns in Python

Traversing an array:

```python
for i in range(len(arr)):
    # use arr[i]
```

Reverse traversal:

```python
for i in range(len(arr) - 1, -1, -1):
    # use arr[i]
```

Find maximum:

```python
maximum = arr[0]
for x in arr:
    if x > maximum:
        maximum = x
```

Count elements:

```python
count = 0
for x in arr:
    if x == target:
        count += 1
```

Two variables (left/right) — important for two pointers, binary search, sliding window:

```python
left = 0
right = len(arr) - 1
```

---

## 24. Time Complexity Awareness

Python code should not only be correct — it should also be efficient.

| Operation      | Average Complexity |
|----------------|---------------------|
| arr[i]         | O(1)                |
| arr.append(x)  | O(1)                |
| arr.pop()      | O(1)                |
| x in list      | O(n)                |
| x in set       | O(1)                |
| x in dict      | O(1)                |
| arr.sort()     | O(n log n)          |
| len(arr)       | O(1)                |

Common complexity patterns:

```python
for x in arr:
    ...
```
Usually O(n)

```python
for i in range(n):
    for j in range(n):
        ...
```
Usually O(n²)

Repeatedly dividing by 2 → O(log n)
Sorting → O(n log n)

---

## 25. Python Shortcuts Worth Knowing

Swap variables:

```python
a, b = b, a
```

Reverse a list:

```python
arr.reverse()
# or
arr[::-1]
```

Check even/odd:

```python
if n % 2 == 0:
    ...
if n % 2 != 0:
    ...
```

Maximum of two values:

```python
max(a, b)
```

Absolute difference:

```python
abs(a - b)
```

---

## 26. Common Mistakes

`=` vs `==`:

```python
x = 5       # assignment
x == 5      # comparison
```

Integer division:

```python
10 / 3      # 3.333...
10 // 3     # 3
```

Off-by-one errors — remember `range(n)` means `0` to `n-1`.

Index error:

```python
arr = [1, 2, 3]
arr[3]      # Error — valid indexes are 0, 1, 2
```

Modifying a list while iterating — avoid:

```python
for x in arr:
    arr.remove(x)
```

Use a safer approach depending on the problem.

---

## 27. Python Concepts to Master Before DSA

- [ ] Variables and data types
- [ ] Input and output
- [ ] Arithmetic and logical operators
- [ ] if / elif / else
- [ ] for loops
- [ ] while loops
- [ ] break and continue
- [ ] Functions
- [ ] Lists
- [ ] Strings
- [ ] Tuples
- [ ] Sets
- [ ] Dictionaries
- [ ] List slicing
- [ ] List comprehension
- [ ] enumerate()
- [ ] zip()
- [ ] map()
- [ ] sum(), min(), max(), sorted()
- [ ] Mutable vs immutable
- [ ] Basic time complexity
- [ ] Common DSA input patterns

---

## 28. DSA Python Template

Basic starting point for problems:

```python
def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    # Write solution here


if __name__ == "__main__":
    solve()
```

For multiple test cases:

```python
def solve():
    # solve one test case
    pass


t = int(input())
for _ in range(t):
    solve()
```

---

## 29. Quick Revision

**Input**
```python
int(input())
list(map(int, input().split()))
```

**Loop**
```python
for i in range(n):
while condition:
```

**Array**
```python
arr[i]
arr.append(x)
arr.pop()
len(arr)
```

**String**
```python
s[i]
s.split()
s[::-1]
```

**Hashing**
```python
set()
dict()
```

**Frequency**
```python
freq[x] = freq.get(x, 0) + 1
```

**Useful**
```python
enumerate()
zip()
sum()
min()
max()
sorted()
```

**Complexity**
```
Single loop       → O(n)
Nested loop       → O(n²)
Binary search     → O(log n)
Sorting           → O(n log n)
Hash lookup       → O(1) average
```

---

## Goal

The purpose of this file is **not** to learn Python completely. The goal is to know enough Python that the language does not become a barrier while solving DSA problems.

> Learn Python → Practice Patterns → Solve DSA → Analyze Complexity → Repeat.