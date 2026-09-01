Today, your goal should be to understand **what each tool is for and recognize it when you see it later**.

Think of `collections` as Python giving you some **specialized containers** that solve common DSA situations more conveniently.

# 3. `collections` Module

```python
from collections import Counter, defaultdict, deque
```

The three you should focus on first are:

```text
Counter     → counting
defaultdict → grouping / automatic dictionary values
deque       → queue
```

`OrderedDict` and `namedtuple` can be understood lightly for now.

---

# 3.1 Counter

## What is it?

`Counter` is basically a dictionary specially designed for **counting things**.

Instead of writing:

```python
freq = {}

for x in "banana":
    freq[x] = freq.get(x, 0) + 1
```

you can write:

```python
from collections import Counter

freq = Counter("banana")
print(freq)
```

Output:

```text
{'a': 3, 'n': 2, 'b': 1}
```

Think:

```text
Counter = automatic frequency dictionary
```

### Useful operations

```python
freq["a"]          # 3
freq["x"]          # 0
freq.most_common(2)
```

`most_common(2)` means:

> Give me the 2 most frequent elements.

```python
Counter("banana").most_common(2)
```

gives something like:

```text
[('a', 3), ('n', 2)]
```

### Counter arithmetic

```python
a = Counter("aabb")
b = Counter("ab")

a + b
```

adds the counts.

```text
a → a:2, b:2
b → a:1, b:1

result → a:3, b:3
```

### 🧠 Remember

> **Counter = dictionary for counting.**

This is the **most important `collections` tool for you to learn first.**

---

# 3.2 defaultdict

A `defaultdict` is basically a dictionary that **automatically creates a default value when a key doesn't exist**.

Normal dictionary:

```python
groups = {}

groups["a"].append("apple")
```

❌ Error, because `"a"` doesn't exist yet.

With `defaultdict`:

```python
from collections import defaultdict

groups = defaultdict(list)

groups["a"].append("apple")
groups["a"].append("ant")

print(groups)
```

Result:

```text
{'a': ['apple', 'ant']}
```

You didn't have to create:

```python
groups["a"] = []
```

Python did it automatically.

---

## Why is this useful?

Especially for **grouping** and later **graphs**.

Example:

```python
graph = defaultdict(list)

graph["A"].append("B")
graph["A"].append("C")
```

Now:

```text
A → [B, C]
```

This becomes extremely useful when you start learning graphs.

### 🧠 Remember

```text
defaultdict(list)
        ↓
missing key → automatically gets []
```

And:

```text
defaultdict(int)
        ↓
missing key → automatically gets 0
```

So:

```python
count = defaultdict(int)
```

is useful for counting.

---

# 3.3 deque

This one is **very important later for DSA**.

`deque` means:

> **double-ended queue**

It allows you to efficiently add/remove from **both ends**.

```python
from collections import deque

q = deque()
```

You can do:

```python
q.append(10)       # add to right
q.append(20)

q.appendleft(5)    # add to left

q.pop()            # remove from right
q.popleft()        # remove from left
```

Think:

```text
appendleft ← [ 5 | 10 | 20 ] → append
popleft   ←                 → pop
```

---

## Why not use a list as a queue?

You might do:

```python
queue = [1, 2, 3]

queue.pop(0)
```

It works, but removing the first element from a list is **O(n)** because the remaining elements have to shift.

With:

```python
q = deque([1, 2, 3])
q.popleft()
```

it's **O(1)**.

Therefore:

> **Use `deque` when you need a queue.**

Later, when you learn **BFS**, `deque` will become one of your standard tools.

### 🧠 Remember

```text
deque
 ↓
fast at both ends
 ↓
queue / BFS
```

---

# 3.4 OrderedDict

You don't need to study this deeply yet.

Modern Python dictionaries already preserve insertion order:

```python
d = {
    "a": 1,
    "b": 2
}
```

`OrderedDict` is useful when you need to **actively manipulate the order**.

For example:

```python
from collections import OrderedDict

od = OrderedDict([
    ("a", 1),
    ("b", 2),
    ("c", 3)
])

od.move_to_end("a")
```

Now `a` moves to the end.

```text
Before:
a → b → c

After:
b → c → a
```

This is useful in things like **LRU Cache**.

For now:

> **OrderedDict = dictionary with special order manipulation.**

Don't spend much time on it yet.

---

# 3.5 namedtuple

A `namedtuple` gives names to the fields of a tuple.

Normal tuple:

```python
point = (3, 4)

print(point[0])
print(point[1])
```

With `namedtuple`:

```python
from collections import namedtuple

Point = namedtuple("Point", "x y")

p = Point(3, 4)

print(p.x)
print(p.y)
```

Much easier to understand:

```text
p.x → 3
p.y → 4
```

Think:

```text
tuple:
(3, 4)

namedtuple:
x = 3
y = 4
```

Useful for small fixed records such as:

```text
Point
Edge
Coordinates
Interval
```

For now:

> **namedtuple = tuple with meaningful field names.**

---

# 🧠 Your Priority Order

You absolutely **do not need to master all five today**.

Learn them in this order:

### ⭐⭐⭐ Very important

```text
1. Counter
2. defaultdict
3. deque
```

### ⭐ Know the basic idea

```text
4. OrderedDict
5. namedtuple
```

---

# One-Line Mental Models

Write these in your notes:

```text
Counter
→ count occurrences

defaultdict
→ dictionary with automatic default values

deque
→ queue with fast operations at both ends

OrderedDict
→ dictionary with special order manipulation

namedtuple
→ tuple with named fields
```

And the three connections worth remembering for your future DSA journey:

```text
Counter
   ↓
Frequency / counting problems

defaultdict
   ↓
Grouping / graphs / adjacency lists

deque
   ↓
Queue / BFS / sliding window
```

**For today, don't touch the sliding-window `deque` example or nested `defaultdict` yet.** Those are applications of the basics, not basics themselves. First make these three mental models solid.