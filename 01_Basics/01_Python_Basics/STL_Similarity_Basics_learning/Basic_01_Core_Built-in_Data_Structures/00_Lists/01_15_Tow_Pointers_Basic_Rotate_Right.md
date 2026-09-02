## Rotate Right

**Idea:** Rotate an array right by `k` means moving the last `k` elements to the beginning while keeping their order.

```text
[1, 2, 3, 4, 5]  → rotate right by 2 →  [4, 5, 1, 2, 3]
```

### Pattern

```text
[1, 2, 3 | 4, 5]
              ↑
           last k

        ↓

[4, 5 | 1, 2, 3]
```

### Code

```python
def rotate_right(arr, k):
    k %= len(arr)

    if k:
        return arr[-k:] + arr[:-k]
    else:
        return arr


print(rotate_right([1, 2, 3, 4, 5], 2))
# [4, 5, 1, 2, 3]
```

### Key Python concepts

- `len(arr)` → number of elements
- `k % len(arr)` → handles `k` larger than the array length
- `arr[-k:]` → last `k` elements
- `arr[:-k]` → everything before the last `k` elements
- `+` → joins two lists
- `return` → gives the result back

**Mental model:**  
> **Rotate right = take the last `k` elements + put the remaining elements after them.**

**Note:** This version creates a new list, so it is **not in-place**.