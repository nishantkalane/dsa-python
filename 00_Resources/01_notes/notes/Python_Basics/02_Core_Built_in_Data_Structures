# 2. Python Built-in Data Structures

## 2.1 List

**List = ordered, mutable collection.** Similar to `vector` (C++) / `ArrayList` (Java).

```python
nums = [1, 2, 3, 4, 5]
```

### Essential Operations

```python
nums[i]          # access
nums[i] = x      # change
nums.append(x)   # add at end
nums.pop()       # remove last
nums.pop(i)      # remove by index
nums.remove(x)   # remove by value
len(nums)        # size
x in nums        # check
nums[a:b]        # slicing
nums[::-1]       # reversed copy
```

### Complexity

```text
nums[i]      → O(1)
append()     → O(1) amortized
pop()        → O(1)
insert(0,x)  → O(n)
pop(0)       → O(n)
x in nums    → O(n)
```

**Remember:** Fast index access, but inserting/removing at the front requires shifting elements.

---

## 2.2 Tuple

**Tuple = ordered, immutable sequence.**

```python
point = (3, 4)
```

Unlike lists, tuples cannot be changed.

```python
x, y = point       # unpacking

a, b = b, a        # swap
```

### Useful in DSA

Tuples can represent fixed combinations such as:

```python
(row, col)
(x, y)
```

They can be used as **set elements and dictionary keys** because they are immutable.

```python
visited = set()
visited.add((1, 2))

grid = {(0, 0): "start"}
```

**Remember:**

```text
List  → mutable
Tuple → immutable
```

---

## 2.3 Dictionary (`dict`)

**Dictionary = key → value.** Similar to `unordered_map` (C++) / `HashMap` (Java).

```python
student = {
    "name": "Nishant",
    "age": 21
}
```

### Essential Operations

```python
d[key]               # access
d[key] = value       # add/change
d.get(key, default)  # safe access
d.pop(key)           # remove
key in d             # check
len(d)               # size

for k, v in d.items():
    print(k, v)
```

Python `dict` preserves **insertion order**.

### Frequency Counting ⭐

```python
freq = {}

for x in arr:
    freq[x] = freq.get(x, 0) + 1
```

Example:

```text
"banana" → {'b': 1, 'a': 3, 'n': 2}
```

### Grouping

```python
groups = {}

for word in words:
    groups.setdefault(word[0], []).append(word)
```

**Mental model:**

```text
frequency → count occurrences
grouping  → key → list of related values
```

Basic dictionary lookup/addition/removal: **O(1) average**.

---

## 2.4 Set / `frozenset`

**Set = unordered collection of unique values.** Similar to `unordered_set` (C++) / `HashSet` (Java).

```python
s = {1, 2, 3}
s = set()          # empty set
```

⚠️ `{}` creates an empty **dictionary**, not a set.

### Essential Operations

```python
s.add(x)
s.remove(x)
x in s
len(s)
```

Membership is **O(1) average**.

### Set Algebra

```python
a = {1, 2, 3}
b = {2, 3, 4}

a | b    # union        → {1,2,3,4}
a & b    # intersection → {2,3}
a - b    # difference   → {1}
```

### Remove Duplicates

```python
unique = set([3, 1, 3, 2, 1])
```

Gives unique values, but **do not rely on the order**.

To preserve first-occurrence order:

```python
unique = list(dict.fromkeys([3, 1, 3, 2, 1]))
# [3, 1, 2]
```

### Detect Duplicates

```python
def has_duplicate(nums):
    return len(nums) != len(set(nums))
```

### `frozenset`

Immutable version of a set:

```python
fs = frozenset([1, 2, 3])
```

```text
set       → mutable
frozenset → immutable
```

---

## 🧠 Quick Comparison

| Structure | Ordered | Mutable | Duplicates | Main Use |
|---|---|---|---|---|
| `list` | ✅ | ✅ | ✅ | General sequence |
| `tuple` | ✅ | ❌ | ✅ | Fixed group of values |
| `dict` | ✅* | ✅ | Keys ❌ | Key → value / lookup |
| `set` | ❌ | ✅ | ❌ | Unique values / fast membership |
| `frozenset` | ❌ | ❌ | ❌ | Immutable set |

\* `dict` preserves **insertion order** in modern Python.

### 🧠 One-line Mental Models

```text
List   → ordered things that can change
Tuple  → ordered things that cannot change
Dict   → key → value
Set    → unique things
```

These four mental models are enough to start using Python's core data structures in DSA.