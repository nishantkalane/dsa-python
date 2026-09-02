# Dictionary (`dict`)

> **Dictionary = key → value**

Think of it like a real dictionary:

```text
word → meaning
```

In Python:

```python
student = {
    "name": "Nishant",
    "age": 21
}
```

Here:

```text
"name" → "Nishant"
"age"  → 21
```

A dictionary is a **hash map**, similar to `unordered_map` in C++ and `HashMap` in Java.

---

## 1. Creating a Dictionary

```python
student = {
    "name": "Nishant",
    "age": 21
}
```

Access a value using its key:

```python
print(student["name"])
# Nishant
```

Add or change a value:

```python
student["city"] = "Pune"
student["age"] = 22
```

---

## 2. Most Important Operations

```python
d[key]              # access
d[key] = value      # add/change
d.get(key, default) # safely get value
d.pop(key)          # remove
key in d            # check if key exists
len(d)              # number of key-value pairs
```

Example:

```python
freq = {}

freq["a"] = 1
freq["a"] += 1

print(freq["a"])    # 2
```

---

# 3. Frequency Counting ⭐

This is **very important for DSA**.

Suppose:

```python
"banana"
```

We want to count:

```text
b → 1
a → 3
n → 2
```

Code:

```python
freq = {}

for ch in "banana":
    freq[ch] = freq.get(ch, 0) + 1

print(freq)
```

Result:

```text
{'b': 1, 'a': 3, 'n': 2}
```

### Understand `get()`

```python
freq.get(ch, 0)
```

means:

> "Give me the current count of `ch`. If it doesn't exist, give me `0`."

So for the first `b`:

```text
b doesn't exist → 0
0 + 1 → 1
```

Next time `a` appears:

```text
a already exists → current count
current count + 1
```

This pattern appears **everywhere in DSA**.

---

# 4. Looping Through a Dictionary

### Keys

```python
for key in d:
    print(key)
```

### Values

```python
for value in d.values():
    print(value)
```

### Key + Value ⭐

```python
for key, value in d.items():
    print(key, value)
```

Think:

```text
.items()
   ↓
(key, value)
```

---

# 5. Grouping with `setdefault()`

Suppose:

```python
words = ["cat", "car", "dog"]
```

We want:

```text
c → cat, car
d → dog
```

Code:

```python
groups = {}

for word in words:
    groups.setdefault(word[0], []).append(word)
```

Result:

```python
{
    'c': ['cat', 'car'],
    'd': ['dog']
}
```

Don't worry too much about `setdefault()` yet.

Understand the idea:

> **Use a key to create groups of related values.**

You can think:

```text
first letter → words starting with that letter
```

---

# 6. Dictionary vs List vs Tuple

Keep this simple:

```text
LIST
index → value

TUPLE
fixed group of values

DICT
key → value
```

Example:

```python
nums = [10, 20, 30]

point = (3, 4)

student = {
    "name": "Nishant",
    "age": 21
}
```

---

# 7. Complexity You Should Know

For a dictionary, basic lookup/addition/removal are **O(1) average**:

```text
d[key]          → O(1) average
d[key] = value  → O(1) average
key in d        → O(1) average
d.pop(key)      → O(1) average
```

This is why dictionaries are extremely useful in DSA.

Instead of searching through an entire list:

```text
O(n)
```

a dictionary can usually find something by key in:

```text
O(1) average
```

---

# 🧠 What You Actually Need to Remember

For your current Python DSA basics, make these automatic:

```python
d = {}                    # create

d[key] = value            # add/change

d[key]                    # access

d.get(key, default)       # safely access

key in d                  # check

d.pop(key)                # remove

for k, v in d.items():    # loop

len(d)                    # size
```

And especially remember this DSA pattern:

```python
freq = {}

for x in arr:
    freq[x] = freq.get(x, 0) + 1
```

### 🧠 Mental model

> **List:** "Give me the item at this position."  
> **Tuple:** "These values belong together and won't change."  
> **Dictionary:** "Give me the value associated with this key."

For DSA, the **frequency-counting pattern** is the first dictionary pattern you should make muscle memory. 🔑