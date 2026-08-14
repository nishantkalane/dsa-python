# Pattern Printing — Notes

> Topic-level notes for understanding and solving pattern problems.
> Individual problems, mistakes, dates, and revisions are documented
> in their respective `.py` files and trackers.
>
> **Update this file only when you discover a genuinely new general rule — not after every pattern.**

---

## 1. Core Mental Model

Most pattern problems can be understood through this thinking chain:

```
Rows
  ↓
What appears in each row
  ↓
How the number of elements changes
  ↓
How values change
  ↓
Translate the observation into loops
```

**Basic Loop Structure**

```python
for i in range(n):          # Rows
    for j in range(...):    # Elements in the row
        print(...)
    print()                 # Move to next row
```

| Statement | Behaviour |
|---|---|
| Outer loop | Controls rows |
| Inner loop | Controls content / columns |
| `print(..., end=" ")` | Continue on same line |
| `print()` | Move to next line |

---

## 2. Start With the Pattern, Not the Code

Before writing a single loop, observe the pattern and answer these four steps in order.

**Step 1 — How many rows?**
This determines the outer loop: `for i in range(n)`

**Step 2 — How many elements are in each row?**
This determines what goes inside the inner loop.

**Step 3 — What changes between rows?**

Look for:
- Increasing or decreasing elements
- Increasing or decreasing numbers
- Increasing or decreasing spaces
- Values that reset each row vs values that continue across rows

**Step 4 — Can the pattern be split into smaller parts?**

Complex patterns are almost always made of simpler ones combined together.

```
Diamond      = Upper Pyramid  +  Lower Inverted Pyramid
Half Diamond = Increasing Triangle  +  Decreasing Triangle
```

---

## 3. `range()` — The Main Shape Controller

`range()` is the primary tool for controlling how many elements appear per row.

**Fixed — same count every row**

```python
for j in range(n):
```
```
* * * *
* * * *
* * * *
* * * *
```

---

**Increasing — more elements each row**

```python
for j in range(i + 1):
```
```
*
* *
* * *
* * * *
* * * * *
```

Row 0 → 1 element · Row 1 → 2 elements · Row `i` → `i + 1` elements

---

**Decreasing — fewer elements each row**

```python
for j in range(i, n):
```
```
* * * * *
* * * *
* * *
* *
*
```

Row 0 → n elements · Row 1 → n−1 elements · Row `i` → `n − i` elements

---

**Off-by-one — one element too many or too few**

When the shape is almost right but slightly off, adjust the boundary:

```python
range(i, n - 1)    # one fewer element vs range(i, n)
range(i + 1 + 1)   # one more element vs range(i + 1)
```

> When a pattern is almost correct, inspect the `range()` boundaries first.
> A difference of one changes the shape significantly.

---

## 4. Number Patterns

When numbers appear instead of stars, separate two independent questions:

1. **How many values per row?** → inner loop controls this
2. **How do the values change?** → a counter variable like `p` controls this

---

**Variable resets every row** → `1 / 1 2 / 1 2 3 / ...`

Initialize `p` **inside** the outer loop so it resets to 1 for each new row.

```python
for i in range(n):
    p = 1                      # ← inside = resets each row
    for j in range(i + 1):
        print(p, end=" ")
        p += 1
    print()
```

```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

---

**Variable continues across rows** → `1 / 2 2 / 3 3 3 / ...`

Initialize `p` **outside** the outer loop so it keeps its value between rows.

```python
p = 1                          # ← outside = continues across rows
for i in range(n):
    for j in range(i + 1):
        print(p, end=" ")
    p += 1
    print()
```

```
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
```

---

## 5. Where Should the Increment Go?

The position of `p += 1` decides what triggers the change.

**Inside inner loop → value changes after every element**

```python
for j in range(n):
    print(p, end=" ")
    p += 1
```

Output: `1 2 3 4 5`

---

**Outside inner loop, inside outer loop → value changes after every row**

```python
for j in range(i + 1):
    print(p, end=" ")
p += 1
```

Output per row: `3 3 3` → then next row gets `4 4 4 4`

---

| Increment location | What changes |
|---|---|
| Inside inner loop | After every single element |
| Outside inner loop (inside outer) | After every complete row |

---

## 6. Spaces and Centered Patterns

A pyramid is not just stars — it is **spaces + stars on the same row**, both changing as `i` changes.

```
    *              row 0: spaces = n-1, stars = 1
   * * *           row 1: spaces = n-2, stars = 3
  * * * * *        row 2: spaces = n-3, stars = 5
 * * * * * * *     row 3: spaces = n-4, stars = 7
* * * * * * * * *  row 4: spaces = 0,   stars = 9
```

Pattern: as `i` increases → **spaces decrease, stars increase by 2**.

```python
for i in range(n):
    for j in range(n - i - 1):    # decreasing spaces
        print(" ", end=" ")
    for j in range(2 * i + 1):    # increasing stars
        print("*", end=" ")
    print()
```

> Keep the character width consistent — mixing `" "` and `"  "` in the same pattern
> breaks alignment and the shape looks wrong.

**Reverse pyramid** — same idea, but spaces increase and stars decrease:

```
* * * * * * * * *  row 0: spaces = 0,   stars = 2n-1
 * * * * * * *     row 1: spaces = 1,   stars = 2n-3
  * * * * *        row 2: spaces = 2,   stars = 2n-5
   * * *           row 3: spaces = 3,   stars = 3
    *              row 4: spaces = n-1, stars = 1
```

---

## 7. Building Complex Patterns

Never look at a complex pattern as one problem. Break it into known parts.

**Diamond = Upper Pyramid + Lower Inverted Pyramid**

```
    *         ← Pyramid starts
   * * *
  * * * * *
   * * *      ← Inverted pyramid starts
    *
```

**Half Diamond = Increasing Triangle + Decreasing Triangle**

```
*             ← Increasing starts
* *
* * *
* *           ← Decreasing starts
*
```

**Strategy every time:**

```
Identify Part 1
      ↓
Identify Part 2
      ↓
Solve each part independently
      ↓
Combine them
      ↓
Check the joining row — is it printed twice?
```

---

## 8. Avoiding the Duplicate Middle Row

When two patterns are combined, the last row of Part 1 and the first row of Part 2 are usually the same row. If you print both parts fully, it appears twice.

**Example — Combining for a Diamond (n = 5)**

```
Part 1 (Pyramid)      Part 2 (Inverted Pyramid)
    *                 * * * * * * * * *
   * * *              * * * * * * *
  * * * * *           * * * * *
 * * * * * * *        * * *
* * * * * * * * *     *
```

Widest row `* * * * * * * * *` appears at the end of Part 1 AND start of Part 2 → printed twice.

**Fix:** Run Part 1 with `range(n - 1)` to skip its last row, then Part 2 fully with `range(n)`.

```python
# Part 1 — pyramid, skip last row
for i in range(n - 1):
    ...

# Part 2 — inverted pyramid, full
for i in range(n):
    ...
```

> This applies to Diamond and Half Diamond both.

---

## 9. Pattern Building Blocks Reference

| Block | Key Idea | Inner range |
|---|---|---|
| Rectangle | Fixed elements per row | `range(n)` |
| Increasing triangle | More elements each row | `range(i + 1)` |
| Decreasing triangle | Fewer elements each row | `range(i, n)` |
| Increasing number pattern | Value increases across the row | `range(i + 1)` + `p` inside |
| Repeated row number | Same value across whole row | `range(i + 1)` + `p` outside |
| Decreasing number pattern | Fewer elements + values grow | `range(i, n)` + `p` |
| Pyramid | Spaces decrease + stars increase | Two inner loops |
| Reverse pyramid | Stars decrease + spaces increase | Two inner loops |
| Diamond | Pyramid + Reverse pyramid | Combined with seam fix |
| Half diamond | Increasing + Decreasing triangle | Combined with seam fix |

```
Rect.       Incr. Tri.   Decr. Tri.     Pyramid        Rev. Pyramid
* * * *     *            * * * * *          *            * * * * *
* * * *     * *          * * * *          * * *            * * *
* * * *     * * *        * * *          * * * * *            *
* * * *     * * * *      * *
            * * * * *    *
```

> The goal is not to memorize 10 separate codes.
> The goal is to **recognize which building blocks a new pattern is made from**.

---

## 10. Problem-Solving Checklist

Use this every time you see a new pattern before touching the keyboard.

- [ ] How many rows? → outer loop
- [ ] How many elements per row? → inner loop
- [ ] Increasing or decreasing?
- [ ] Printing stars / numbers / spaces / something else?
- [ ] Does the variable reset every row or continue across rows?
- [ ] Does the value change every element or every row?
- [ ] What is the exact inner `range()`?
- [ ] Can this split into two simpler patterns?
- [ ] After combining — is the middle row printed twice?
- [ ] Final check: extra column? Missing column? Wrong spacing?

---

## 11. Common Mistakes to Watch For

- Wrong `range()` boundary — off by one
- Hardcoded value instead of using a variable
- Variable initialized in the wrong scope (inside vs outside outer loop)
- Increment `p += 1` placed in the wrong loop (per element vs per row)
- Forgetting to reset a variable that should restart each row
- Accidentally continuing a variable that should reset
- Duplicate middle row when combining two patterns
- Inconsistent space width in centered patterns breaking alignment
- Calling `print()` before the full row is complete
- Function name and function call not matching
- Writing `=` instead of `==` in:

```python
if __name__ == "__main__":
```

---

## 12. Quick Revision Summary

**Loop**
```
Outer loop   → Rows
Inner loop   → Elements in each row
```

**range()**
```
range(n)       → Fixed count per row
range(i + 1)   → Increasing count
range(i, n)    → Decreasing count
```

**Variable scope**
```
p inside outer loop   → Resets every row
p outside outer loop  → Continues across rows
```

**Increment placement**
```
p += 1 inside inner loop  → Changes every element
p += 1 outside inner loop → Changes every row
```

**Spaces**
```
spaces = n - i - 1   (decreasing)
stars  = 2 * i + 1   (increasing)
```

**Combining**
```
Part 1 with range(n - 1)   → skip last row
Part 2 with range(n)       → full
→ middle row printed exactly once
```

> **Understand the pattern first. Write the loops second.**

---

## File System for This Topic

```
pattern_01_rectangle.py   → What happened in THIS problem
notes_patterns.md         → What can I reuse in FUTURE problems
mistakes.md               → What mistakes keep happening to ME
journal/                  → How is my learning journey going
Google Sheets             → What have I solved and what needs revision
```
'''
Just for my reference to add notes: 


The way to use it going forward:

- **Section 9 (Building Blocks)** — add new blocks to the table as you learn them
- **Section 11 (Common Mistakes)** — add any new mistake you make that isn't already listed
- **Section 12 (Quick Revision Summary)** — add any new shorthand rule that you want to remember fast
- **Sections 1–8** — these are fundamentals, they won't change much. Only touch them if a new pattern teaches you something genuinely different that doesn't fit anywhere else

The individual `.py` files handle the problem-specific stuff. This file stays at the topic level — rules you can reuse, not notes about one specific problem.

So the workflow is:

```
Solve new pattern
      ↓
Document it in pattern_XX.py
      ↓
Ask: did I learn a new general rule?
      ↓
Yes → add one line to notes_patterns.md
No  → leave it alone
```

'''