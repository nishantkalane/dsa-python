# Basic Maths — Notes
## Page 1
![Handwritten Notes - Page 1](../../handwritten_notes/11.jpeg)

## Page 2
![Handwritten Notes - Page 2](../../handwritten_notes/12.jpeg)
---

## 1. Core Mental Model

Most Basic Maths problems are about recognizing **what mathematical operation is being repeated**.

```text
Read the number
      ↓
Identify the property / operation
      ↓
Can I process digit-by-digit?
      ↓
Can I reduce the search space?
      ↓
Choose the simplest efficient approach
```

### Main Categories

| Pattern | Typical Problems |
|---|---|
| **Digit Manipulation** | Extract, Count, Reverse digits |
| **Digit Properties** | Armstrong number |
| **Divisor / Factor Properties** | Print divisors |
| **Prime Properties** | Prime check |
| **GCD / HCF** | Common factors, Euclidean Algorithm |

> **First question:** Am I processing digits, checking factors, or finding a mathematical relationship between numbers?

---

## 2. Digit Manipulation

When a problem asks you to work with **individual digits**, think:

```text
             N
             ↓
        % 10 → Last digit
             ↓
        // 10 → Remove digit
             ↓
          Repeat
```

### Extract the last digit

```python
digit = n % 10
```

Example:

```text
1234 % 10 → 4
```

### Remove the last digit

```python
n = n // 10
```

Example:

```text
1234 // 10 → 123
```

### The basic digit-processing loop

```python
while n > 0:
    digit = n % 10
    n = n // 10
```

Each iteration removes **one digit**.

Therefore:

```text
Number of iterations = Number of digits
                    = O(log N)
```

> **Golden rule:** `% 10` → extract. `// 10` → remove.

---

## 3. Counting Digits

There are two common approaches.

### Loop Method

```text
count = 0
while n > 0:
    count += 1
    n //= 10
```

Useful when you are **already processing digits**.

### Log Method

For `N > 0`:

```text
digits = floor(log₁₀(N)) + 1
```

Example:

```text
N = 1234

floor(log₁₀(1234)) + 1
= 3 + 1
= 4
```

```text
Loop method → O(log N)
Log method  → O(1)
```

> `log10(0)` is undefined, so handle `0` separately when necessary.

---

## 4. Building a Number From Digits

When extracting digits and wanting to **construct a new number**, use:

```text
new_number = new_number × 10 + digit
```

### Reverse Number

```text
N = 1234

digit = 4 → rev = 4
digit = 3 → rev = 43
digit = 2 → rev = 432
digit = 1 → rev = 4321
```

Mental model:

```text
Old number
     ↓
Extract digit
     ↓
Shift existing result left ×10
     ↓
Add new digit
```

> **Remember:** `rev = rev*10 + digit`

### Why `×10`?

Multiplying by 10 shifts every existing digit one position left:

```text
43 × 10 = 430
430 + 2 = 432
```

---

## 5. Digit-Based Number Properties

Some problems require extracting **every digit** and applying a rule to it.

General structure:

```text
Original N
    ↓
Extract digit
    ↓
Apply operation to digit
    ↓
Add / combine result
    ↓
Remove digit
    ↓
Repeat
```

### Armstrong Number

A number is Armstrong when:

```text
Sum of (each digit ^ number of digits)
=
Original number
```

Example:

```text
371

Number of digits = 3

3³ + 7³ + 1³
= 27 + 343 + 1
= 371
```

### Recognition Pattern

```text
Need individual digits?
        ↓
Need number of digits?
        ↓
Raise every digit to that power
        ↓
Compare sum with original
```

> **Key:** Armstrong power = **length of the number**.

---

## 6. Divisors — Pair Observation

A divisor problem should immediately trigger:

```text
Can I stop at √N?
```

If:

```text
N % i == 0
```

then both are divisors:

```text
i
N // i
```

Example:

```text
36

1 × 36
2 × 18
3 × 12
4 × 9
6 × 6
```

Once we reach `6 = √36`, all divisor pairs have been found.

### √N Approach

```python
i = 1

while i * i <= n:
    if n % i == 0:
        add i
        add n // i
    i += 1
```

### Perfect Square Trap

For:

```text
36
```

when:

```text
i = 6
n // i = 6
```

Do **not** add `6` twice.

```python
if i != n // i:
    add n // i
```

> **Core observation:** Divisors come in pairs, so checking beyond `√N` repeats work.

---

## 7. Prime Number Pattern

A prime number has exactly:

```text
2 divisors
→ 1 and itself
```

Instead of checking all numbers up to `N`, use the divisor-pair observation.

```text
Check i from 1 to √N
        ↓
If N % i == 0
        ↓
Found divisor pair
        ↓
Not prime if another divisor exists
```

### Important Boundary

Use:

```python
while i * i <= n:
```

not:

```python
while i * i < n:
```

because `√N` itself may be a divisor.

Example:

```text
N = 49
√49 = 7

7 × 7 = 49
```

### Prime Recognition

```text
N < 2 → Not prime

N has exactly 2 divisors → Prime
```

> **Prime = no divisor between 2 and √N.**

---

## 8. GCD / HCF

### Meaning

GCD/HCF = **Greatest Common Divisor**

It is the largest number that divides both numbers.

Example:

```text
9 → 1, 3, 9
12 → 1, 2, 3, 4, 6, 12

Common → 1, 3
GCD = 3
```

### Basic Search

The GCD cannot be greater than:

```text
min(n1, n2)
```

So possible candidates are:

```text
1 → min(n1,n2)
```

Better:

```text
Start from min(n1,n2)
        ↓
Move downward
        ↓
First common divisor = GCD
```

Why?

```text
Starting from largest possible value
+
First valid divisor
=
Largest common divisor
```

---

## 9. Euclidean Algorithm — Optimal GCD Pattern

The most important GCD pattern to remember:

```text
GCD(a, b) = GCD(b, a % b)
```

Repeatedly replace the larger number with the remainder.

Example:

```text
GCD(20, 15)

20 % 15 = 5
→ GCD(15, 5)

15 % 5 = 0
→ GCD(5, 0)

Answer = 5
```

### Algorithm

```text
while both numbers are non-zero:
    larger → larger % smaller

when one becomes 0:
    other number = GCD
```

### Why it works

The common divisors of:

```text
(a, b)
```

are the same as those of:

```text
(b, a % b)
```

So the problem keeps shrinking without changing the answer.

### Complexity

```text
Brute force → O(min(a,b))
Euclidean    → O(log(min(a,b)))
```

> **GCD question? Think Euclidean Algorithm first.**

---

## 10. Basic Maths Building Blocks

| Building Block | Key Idea |
|---|---|
| Extract digit | `n % 10` |
| Remove digit | `n // 10` |
| Process all digits | `while n > 0` |
| Count digits | `log10(n)+1` |
| Build reverse | `rev*10 + digit` |
| Armstrong | `Σ digit^digits` |
| Divisor check | `n % i == 0` |
| Divisor pairs | `i` and `n//i` |
| √N optimization | `i*i <= n` |
| Prime | Exactly 2 divisors |
| Basic GCD | Search up to `min(a,b)` |
| Optimal GCD | `gcd(a,b)=gcd(b,a%b)` |

---

## 11. Complexity Patterns

The most useful complexity recognition:

```text
Digit-by-digit processing
        ↓
One digit removed each iteration
        ↓
O(log N)
```

```text
Check every number from 1 → N
        ↓
O(N)
```

```text
Check factors only until √N
        ↓
O(√N)
```

```text
Euclidean Algorithm
        ↓
O(log(min(a,b)))
```

### Quick Table

| Technique | Time | Space |
|---|---:|---:|
| Digit loop | O(log N) | O(1) |
| Digit count using log | O(1) | O(1) |
| Reverse number | O(log N) | O(1) |
| Armstrong | O(log N) | O(1) |
| Divisors, linear | O(N) | O(K) |
| Divisors, √N | O(√N + K log K)* | O(K) |
| Prime, linear | O(N) | O(1) |
| Prime, √N | O(√N) | O(1) |
| GCD, brute force | O(min(a,b)) | O(1) |
| GCD, Euclidean | O(log(min(a,b))) | O(1) |

`K` = number of divisors.
`*` Sorting is responsible for the `K log K` part.

---

## 12. Common Mistakes to Watch For

### Digit Problems

- Using `/ 10` instead of `// 10` when integer division is required.
- Forgetting that `% 10` gives the **last digit**.
- Forgetting to save the original number when it is needed later.
- Using the wrong power for Armstrong numbers.

### Divisor / Prime Problems

- Checking all the way to `N` when √N optimization is possible.
- Using `i*i < n` instead of `i*i <= n`.
- Counting the square-root divisor twice.
- Forgetting that `1` is a divisor but prime numbers must have exactly two divisors.
- Treating `1` as prime.

### GCD Problems

- Searching beyond `min(n1,n2)`.
- Forgetting to include the minimum boundary.
- Using `&` instead of logical `and` in Python.
- Using brute force when the Euclidean Algorithm is expected.

---

## 13. Problem-Solving Checklist

Before solving a Basic Maths problem:

- [ ] Is this a **digit manipulation** problem?
- [ ] Do I need `% 10` to extract a digit?
- [ ] Do I need `// 10` to remove a digit?
- [ ] Do I need to preserve the original number?
- [ ] Am I building a new number using `result*10 + digit`?
- [ ] Is there a mathematical property of the number?
- [ ] Can I use divisor pairs?
- [ ] Can I reduce the search to `√N`?
- [ ] Is this a prime-number problem?
- [ ] Is this a GCD/HCF problem?
- [ ] Can I use the Euclidean Algorithm?
- [ ] Can the approach be reduced from `O(N)` to `O(√N)` or `O(log N)`?

---

## 14. Quick Revision Summary

### Digit Manipulation

```text
%10   → Extract last digit
//10  → Remove last digit
```

```text
while n > 0
    ↓
process one digit
    ↓
n //= 10
```

### Number Construction

```text
rev = rev*10 + digit
```

### Armstrong

```text
Σ(digit ^ number_of_digits) == original
```

### Divisors

```text
if n % i == 0:
    i and n//i are divisors
```

```text
Check only while:
i*i <= n
```

### Prime

```text
Exactly 2 divisors
```

```text
Check only up to √N
```

### GCD

```text
GCD(a,b) = GCD(b,a%b)
```

```text
Repeat remainder
        ↓
one becomes 0
        ↓
remaining number = GCD
```

### Complexity

```text
Digit processing → O(log N)
√N search        → O(√N)
Euclidean GCD    → O(log N)
```

> **The goal is not to memorize separate solutions.**
>
> The goal is to recognize the **mathematical building block** behind a new problem.

---
