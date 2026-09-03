1. `itertools.permutations`
2. `itertools.combinations`
3. `itertools.product`
4. `itertools.accumulate`
5. `itertools.groupby`
6. `functools.lru_cache` ⭐ very important for DP
7. `functools.reduce`
8. `cmp_to_key` later

---

# 6.1 `itertools` 🔧

Think of `itertools` as a **toolbox for generating and processing sequences**.

The three most important combinatorics tools are:

| Function | Simple meaning |
|---|---|
| `permutations()` | All possible **orders** |
| `combinations()` | All possible **selections** |
| `product()` | All possible **choices with repetition** |

## 1. `permutations()` 🔄

Suppose:

```python
from itertools import permutations

print(list(permutations("abc")))
```

Output:

```text
[('a', 'b', 'c'),
 ('a', 'c', 'b'),
 ('b', 'a', 'c'),
 ('b', 'c', 'a'),
 ('c', 'a', 'b'),
 ('c', 'b', 'a')]
```

Why 6?

For `abc`:

```text
abc
acb
bac
bca
cab
cba
```

**Order matters.**

`abc` and `acb` are different permutations.



### Think:

> "Give me every possible arrangement."

For DSA, you'll see this in problems involving:
- arranging elements
- generating all possible orders
- brute force/backtracking

---

# 2. `combinations()` 🎯

Now suppose:

```python
from itertools import combinations

print(list(combinations([1, 2, 3, 4], 2)))
```

Output:

```text
[(1, 2),
 (1, 3),
 (1, 4),
 (2, 3),
 (2, 4),
 (3, 4)]
```

Here we are **selecting 2 elements**.

Notice:

```text
(1, 2)
```

and

```text
(2, 1)
```

are NOT both present.

Why?

Because **order does not matter**.

Selecting:

```text
1 and 2
```

is the same selection as:

```text
2 and 1
```



### Think:

> "Give me every possible group of these elements."

### Quick difference

```text
Permutation → arrangement → order matters
Combination → selection → order doesn't matter
```

This distinction is **very important for DSA**.

---

# 3. `product()` 🧩

This one is slightly different.

```python
from itertools import product

print(list(product([0, 1], repeat=3)))
```

Output:

```text
[(0, 0, 0),
 (0, 0, 1),
 (0, 1, 0),
 (0, 1, 1),
 (1, 0, 0),
 (1, 0, 1),
 (1, 1, 0),
 (1, 1, 1)]
```

We're basically creating **all possible 3-position choices**, where each position can independently be `0` or `1`.

So:

```text
000
001
010
011
100
101
110
111
```

That's exactly all possible **3-bit binary strings**.

There are:

```text
2 × 2 × 2 = 8
```

possibilities.

### Think:

> "For every position, give me every possible choice."

---

# 4. `accumulate()` ➕

This one is much easier.

```python
from itertools import accumulate

print(list(accumulate([1, 2, 3, 4])))
```

Output:

```text
[1, 3, 6, 10]
```

Why?

It creates **running results**:

```text
1
1 + 2 = 3
1 + 2 + 3 = 6
1 + 2 + 3 + 4 = 10
```

So:

```text
[1, 2, 3, 4]
       ↓
[1, 3, 6, 10]
```

This is basically a **prefix sum**.

You'll encounter this concept frequently in DSA.

---

# 5. `groupby()` 👥

This one needs one important warning:

> `groupby()` groups **consecutive** equal elements.

Example:

```python
from itertools import groupby

for key, group in groupby("aaabbc"):
    print(key, list(group))
```

Output:

```text
a ['a', 'a', 'a']
b ['b', 'b']
c ['c']
```

Think:

```text
aaabbc
^^^ ^^ ^
 a   b c
```

It sees a run of `a`s, then a run of `b`s, then a run of `c`s.

But:

```python
groupby("aabbaa")
```

does **not** produce one group of all `a`s.

It produces:

```text
a aa
b bb
a aa
```

because the final `aa` is separated from the first `aa`.

That's an important interview detail.

---

# 6.2 `functools` 🛠️

Now we move to another toolbox.

For DSA, the **star of this section is `lru_cache`**.

---

# 6. `lru_cache` ⭐⭐⭐

This is extremely useful when you start learning **Dynamic Programming**.

Consider Fibonacci.

Without caching:

```python
def fib(n):
    if n < 2:
        return n

    return fib(n - 1) + fib(n - 2)
```

If you calculate:

```python
fib(5)
```

the function repeatedly calculates the same values.

For example:

```text
fib(5)
├── fib(4)
│   ├── fib(3)
│   └── fib(2)
└── fib(3)   ← calculated again
```

That's wasteful.

### `lru_cache` remembers previous answers.

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n

    return fib(n - 1) + fib(n - 2)

print(fib(50))
```

The important part is:

```python
@lru_cache(maxsize=None)
```

Think of it as:

> **"If you've already calculated this input, remember the answer and reuse it."**

So:

```text
fib(10) → calculate → remember
fib(10) → already remembered → return immediately
```

This is called **memoization**.

### Very important DSA connection

When you eventually learn DP, you'll encounter:

```text
Recursion
    ↓
Repeated calculations
    ↓
Memoization
    ↓
Dynamic Programming
```

`lru_cache` gives you a very convenient way to implement memoization.

---

# 7. `reduce()` ➗

`reduce()` repeatedly combines values into **one final value**.

Example:

```python
from functools import reduce

product_of_all = reduce(
    lambda a, b: a * b,
    [1, 2, 3, 4]
)

print(product_of_all)
```

Output:

```text
24
```

What's happening?

```text
1 × 2 = 2
2 × 3 = 6
6 × 4 = 24
```

So:

```text
[1, 2, 3, 4]
       ↓
     reduce
       ↓
      24
```

### Another example

```python
reduce(lambda a, b: a + b, [1, 2, 3, 4])
```

becomes:

```text
1 + 2 = 3
3 + 3 = 6
6 + 4 = 10
```

Result:

```text
10
```

For DSA, though, **you don't need to heavily practice `reduce()` right now**. A normal loop is often clearer.

---

# 8. `cmp_to_key()` 🧠

This is the least important one for you right now.

Suppose you have:

```python
def compare(a, b):
    return a - b
```

and:

```python
from functools import cmp_to_key

nums = [3, 1, 2]

print(sorted(nums, key=cmp_to_key(compare)))
```

Output:

```text
[1, 2, 3]
```

`cmp_to_key()` lets Python's `sorted()` use an old-style **comparison function**.

You can think:

```text
compare(a, b)
      ↓
Should a come before b?
      ↓
cmp_to_key()
      ↓
sorted()
```

We'll come back to this when you encounter custom sorting problems. **Don't spend much time on it now.**

---

# 🧠 Your DSA cheat sheet

Write this in your notes:

```text
ITERTOOLS
---------

permutations() → all possible orders
combinations() → all possible selections
product()      → all possible choices
accumulate()   → running/prefix results
groupby()      → consecutive equal groups


FUNCTOOLS
---------

lru_cache()    → remember previous function results
                 → memoization → very useful for DP

reduce()       → repeatedly combine values into one result

cmp_to_key()   → use custom comparison function with sorted()
```

## The most important mental picture

```text
PERMUTATION
"Arrange them"
ABC
ACB
BAC
...

COMBINATION
"Choose them"
AB
AC
BC
...

PRODUCT
"Choose for every position"
000
001
010
011
...

ACCUMULATE
"Keep a running result"
1  → 1
2  → 3
3  → 6
4  → 10

LRU_CACHE
"Have I solved this input before?"
       ↓
   YES → reuse answer
   NO  → calculate + remember
```

### What I want you to actually practice

Don't jump into complicated problems yet. Let's build muscle memory with **8 tiny exercises**, one function at a time:

1. Generate all permutations of `"abc"`.
2. Generate all 2-element combinations from `[1,2,3,4]`.
3. Generate all 3-bit binary combinations.
4. Generate prefix sums using `accumulate()`.
5. Use `groupby()` on `"aaabbc"`.
6. Write Fibonacci with `lru_cache`.
7. Use `reduce()` to multiply `[1,2,3,4,5]`.
8. Use `cmp_to_key()` for a custom sort.

**Start with #1 only.** Send me your code, and I'll check it before we move to #2.