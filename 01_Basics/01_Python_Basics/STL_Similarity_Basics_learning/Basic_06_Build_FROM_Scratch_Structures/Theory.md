Yes. This is an important transition in your DSA journey. Up to now, we mostly used Python's ready-made structures. **Here you start building the structures yourself.** 🧱

We'll learn this section **one structure at a time**, and I don't want you memorizing the code. The goal is to understand what each structure is doing internally.

The order will be:

1. **Singly Linked List** ⭐⭐⭐
2. **Binary Search Tree (BST)** ⭐⭐⭐
3. **Trie** ⭐⭐
4. **Union-Find / Disjoint Set** ⭐⭐⭐

Let's start with the **Singly Linked List**.

---

# 7.1 Singly Linked List

## First: what problem does a linked list solve?

You already know a Python list:

```python
nums = [10, 20, 30, 40]
```

You can imagine it as:

```text
[10][20][30][40]
```

A linked list is different.

Instead of each element simply sitting next to the next element, **each element stores a connection to the next element**.

```text
[10 | next] → [20 | next] → [30 | next] → [40 | None]
```

Each box is called a **node**.

---

# 1. What is a Node?

A node contains two things:

```text
┌───────────────┐
│ value | next  │
└───────────────┘
```

For example:

```text
10 | ●────────→ next node
```

So we create a class:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

Let's understand this **word by word**.

---

## `class ListNode:`

We're creating our own type called `ListNode`.

Just like Python already has:

```python
list
str
dict
```

we are creating:

```python
ListNode
```

---

## `__init__`

```python
def __init__(self, val=0, next=None):
```

This is the constructor.

Whenever we create:

```python
node = ListNode(10)
```

Python runs `__init__`.

We give it:

```text
val = 10
next = None
```

---

## `self.val = val`

```python
self.val = val
```

means:

> Store the value inside this node.

So:

```python
node = ListNode(10)
```

gives:

```text
node
 ↓
┌─────────────┐
│ 10 | None   │
└─────────────┘
```

---

## `self.next = next`

This stores the connection to the next node.

Initially:

```python
node = ListNode(10)
```

means:

```text
┌─────────────┐
│ 10 | None   │
└─────────────┘
```

because we haven't connected it to anything yet.

---

# 2. Creating a Linked List

Let's manually create:

```text
10 → 20 → 30 → None
```

Code:

```python
node1 = ListNode(10)
node2 = ListNode(20)
node3 = ListNode(30)

node1.next = node2
node2.next = node3
```

Now:

```text
node1
  ↓
[10 | ●] ──→ [20 | ●] ──→ [30 | None]
               node2          node3
```

And this is the key idea:

> **A linked list is a chain of nodes.**

---

# 3. What is `head`?

You'll constantly see:

```python
head
```

in linked-list problems.

`head` simply means:

> **The first node of the linked list.**

For our list:

```text
head
 ↓
[10] → [20] → [30] → None
```

So:

```python
head = node1
```

Now `head` gives us access to the entire chain.

Why?

Because:

```text
head
 ↓
10 → 20 → 30 → None
```

From 10 we can reach 20, from 20 we can reach 30.

---

# 4. Traversing a Linked List

Suppose:

```python
head = node1
```

We can walk through it:

```python
while head:
    print(head.val)
    head = head.next
```

Output:

```text
10
20
30
```

The important line is:

```python
head = head.next
```

It means:

> Move to the next node.

Think of yourself walking through a chain:

```text
10 → 20 → 30 → None
↑
you
```

Then:

```text
10 → 20 → 30 → None
     ↑
    you
```

Then:

```text
10 → 20 → 30 → None
          ↑
         you
```

Then:

```text
None
```

Stop.

---

# 5. Reversing a Linked List ⭐⭐⭐

This is one of the **classic DSA problems**.

Original:

```text
1 → 2 → 3 → 4 → None
```

We want:

```text
4 → 3 → 2 → 1 → None
```

The tricky part is that we're changing the arrows.

---

## The three-pointer idea

We use:

```text
prev
head
nxt
```

Initially:

```text
prev = None

head
 ↓
1 → 2 → 3 → 4 → None
```

Our job is essentially:

```text
1 → 2
```

change into:

```text
1 ← 2
```

But before changing the arrow, we must **remember where 2 was**.

That's why we need `nxt`.

---

# Step 1

```python
nxt = head.next
```

Currently:

```text
head
 ↓
1 → 2 → 3 → 4
```

We save:

```text
nxt
 ↓
2 → 3 → 4
```

---

# Step 2

```python
head.next = prev
```

Initially:

```text
prev = None
```

So:

```text
1 → None
```

Now we've reversed the first link.

---

# Step 3

```python
prev = head
```

Now:

```text
prev
 ↓
1 → None
```

---

# Step 4

```python
head = nxt
```

Move forward:

```text
prev       head
 ↓           ↓
1 → None    2 → 3 → 4
```

And repeat.

---

# The complete code

```python
def reverse_linked_list(head):
    prev = None

    while head:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt

    return prev
```

The four lines inside the loop are the **heart of linked-list reversal**:

```python
nxt = head.next
head.next = prev
prev = head
head = nxt
```

Remember the mental sentence:

> **Save → Reverse → Move prev → Move head**

```text
SAVE
nxt = head.next

REVERSE
head.next = prev

MOVE PREV
prev = head

MOVE HEAD
head = nxt
```

At the end:

```text
prev
 ↓
4 → 3 → 2 → 1 → None
```

That's why we return:

```python
return prev
```

The old `head` has reached `None`, while `prev` is now the **new head**.

---

# 6. Detecting a Cycle 🔄

Now imagine someone accidentally creates:

```text
1 → 2 → 3 → 4
        ↑     |
        └─────┘
```

There is no `None`.

The list loops forever.

This is called a **cycle**.

We need to detect it.

---

# Floyd's Cycle Detection

The clever idea is to use **two pointers**:

```text
slow
fast
```

- `slow` moves **1 step**
- `fast` moves **2 steps**

```python
slow = slow.next
fast = fast.next.next
```

Think of a race track.

If the track has no loop:

```text
slow → → → → None
fast → → → → None
```

Eventually `fast` reaches the end.

If there is a loop:

```text
       ┌──────────┐
       ↓          │
1 → 2 → 3 → 4 → 5 ┘
```

Fast and slow are running around the same circle.

Eventually:

```text
slow
  ↓
  3

fast
  ↓
  3
```

They meet.

That's the trick.

---

## Code

```python
def has_cycle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            return True

    return False
```

### Why:

```python
slow = fast = head
```

Both start at the beginning.

```text
slow
 ↓
1 → 2 → 3 → 4

fast
 ↓
1 → 2 → 3 → 4
```

Then:

```python
slow = slow.next
```

moves one.

```python
fast = fast.next.next
```

moves two.

If they meet:

```python
if slow is fast:
```

we found a cycle.

Notice **`is`**, not `==`.

Here we care whether they are literally the **same node object**.

---

# 🧠 Singly Linked List: What you need to remember

For now, don't memorize every line.

Understand these four things:

```text
NODE
[value | next]

HEAD
first node

TRAVERSAL
current = current.next

REVERSE
save → reverse → move → move

CYCLE
slow = 1 step
fast = 2 steps
meeting = cycle
```

### Complexity

| Operation | Linked List |
|---|---:|
| Access by index | O(n) |
| Search | O(n) |
| Insert at known node | O(1) |
| Delete at known node | O(1) |
| Traverse | O(n) |
| Reverse | O(n) |
| Cycle detection | O(n) |

The big difference from Python lists:

```text
Python list:
nums[5] → directly jump to index 5

Linked list:
head → next → next → next → next → ...
```

So linked lists are **not good at random access**.

---

## 🎯 Your first practice

Before moving to BST, let's make sure the linked-list foundation is solid.

Create these nodes:

```text
10 → 20 → 30 → 40 → None
```

using:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

Then write code to **traverse the list and print**:

```text
10
20
30
40
```

Don't reverse it yet.

Send me what you write, and we'll build from there.



BST


Absolutely. Let's make **BST a proper learning topic**, not just a few functions to memorize. You should come out of this knowing what a BST is, how to build one from scratch in Python, how every operation works, and when you'd use it in DSA.

# 🌳 Binary Search Tree (BST)

## 1. What is a Tree?

Before BST, understand a normal tree.

A tree is a collection of **nodes connected in a hierarchy**.

Example:

```text
              8
            /   \
           3     10
          / \      \
         1   6      14
```

Unlike a linked list:

```text
10 → 20 → 30 → 40
```

a tree can **branch**.

---

# 2. What is a Binary Tree?

A **binary tree** is a tree where each node can have **at most two children**.

Those two children are called:

```text
left child
right child
```

Example:

```text
        8
       / \
      3   10
```

A node can have:

```text
0 children → leaf
1 child
2 children
```

It cannot have 3 children in a binary tree.

---

# 3. What is a Binary Search Tree?

A **Binary Search Tree** is a binary tree with an additional ordering rule.

### The rule:

For every node:

```text
LEFT SUBTREE < NODE < RIGHT SUBTREE
```

Example:

```text
             8
           /   \
          3     10
         / \      \
        1   6      14
```

For node `8`:

```text
Left side:  1, 3, 6
Right side: 10, 14
```

Therefore:

```text
1, 3, 6 < 8 < 10, 14
```

For node `3`:

```text
1 < 3 < 6
```

So the rule applies **recursively to every node**.

---

# 4. Why is it called "Search" Tree?

Because the ordering allows us to eliminate half of the possibilities as we search.

Suppose:

```text
             8
           /   \
          3     10
         / \      \
        1   6      14
```

We want to find `6`.

Start at `8`:

```text
6 < 8
```

So we know:

> 6 must be somewhere on the left.

We don't need to inspect `10` or `14`.

Move to `3`:

```text
6 > 3
```

So:

> 6 must be on the right.

Move to `6`.

Found it.

```text
8
↓
3
↓
6 ✓
```

This is the basic search idea.

---

# 5. Important BST Terminology

You should know these.

### Root

The first/top node.

```text
        8
       / \
      3   10
```

`8` is the **root**.

---

### Parent

A node directly above another node.

```text
    8
   /
  3
```

`8` is the parent of `3`.

---

### Child

A node directly below another node.

`3` is the child of `8`.

---

### Leaf

A node with **no children**.

```text
        8
       / \
      3   10
     / \
    1   6
```

Leaves:

```text
1, 6, 10
```

---

### Subtree

Any node and everything underneath it.

For example, the subtree rooted at `3`:

```text
      3
     / \
    1   6
```

---

### Height

The longest path from a node down to a leaf.

We'll implement this later.

---

# 6. Creating a BST Node

Just like our linked list had:

```python
class ListNode:
```

a BST has:

```python
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

A node contains:

```text
        [value]
        /     \
      left   right
```

So:

```python
self.val
```

stores the value.

```python
self.left
```

stores the left child.

```python
self.right
```

stores the right child.

---

# 7. Creating a BST Manually

Let's create:

```text
        8
       / \
      3   10
```

Code:

```python
root = TreeNode(8)

root.left = TreeNode(3)
root.right = TreeNode(10)
```

Now:

```text
root
 ↓
    8
   / \
  3   10
```

We call `root` the starting point of the tree.

This is similar to:

```text
Linked List → head
BST          → root
```

---

# 8. Building a BST Using Insert ⭐⭐⭐

Normally we don't manually connect every node.

We create an `insert()` function.

Suppose we start with:

```text
8
```

and want to insert:

```text
3
```

Compare:

```text
3 < 8
```

Go left.

Since left is empty:

```text
    8
   /
  3
```

Now insert `10`:

```text
10 > 8
```

Go right:

```text
    8
   / \
  3   10
```

Now insert `6`:

```text
6 < 8
```

go left.

At `3`:

```text
6 > 3
```

go right.

Result:

```text
    8
   / \
  3   10
   \
    6
```

---

# 9. Insert Code

```python
def insert(root, val):
    if root is None:
        return TreeNode(val)

    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)

    return root
```

Let's understand this carefully.

---

## `if root is None`

```python
if root is None:
    return TreeNode(val)
```

We've reached an empty position.

Example:

```text
      3
       \
        None
```

We're trying to insert `6`.

We've found the correct position.

Create:

```text
      3
       \
        6
```

---

## `if val < root.val`

```python
if val < root.val:
```

The new value is smaller.

Therefore:

```text
go LEFT
```

---

## Recursive call

```python
root.left = insert(root.left, val)
```

This means:

> "Go into the left subtree and try inserting there."

Similarly:

```python
root.right = insert(root.right, val)
```

means:

> "Go into the right subtree."

---

# 10. Why do we assign the result?

This line is important:

```python
root.left = insert(root.left, val)
```

Suppose:

```text
8
/
None
```

We insert `3`.

`insert(None, 3)` creates:

```text
3
```

But we need to attach it:

```text
8
/
3
```

That's why:

```python
root.left = ...
```

connects the newly created node to the tree.

This is one of those lines you should **understand**, not blindly memorize.

---

# 11. Building a Complete BST

We can do:

```python
root = None

root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 10)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 14)
```

Result:

```text
             8
           /   \
          3     10
         / \      \
        1   6      14
```

---

# 12. Tree Traversals ⭐⭐⭐

This is one of the most important parts.

There are three basic DFS traversals:

```text
Inorder
Preorder
Postorder
```

The difference is **when you process the current node**.

---

# 13. Inorder ⭐⭐⭐

Pattern:

```text
LEFT → NODE → RIGHT
```

For:

```text
        8
       / \
      3   10
     / \
    1   6
```

Visit:

```text
1 → 3 → 6 → 8 → 10
```

### Code

```python
def inorder(root, result):
    if root:
        inorder(root.left, result)
        result.append(root.val)
        inorder(root.right, result)
```

Use:

```python
result = []

inorder(root, result)

print(result)
```

Output:

```text
[1, 3, 6, 8, 10]
```

### ⭐ Critical BST fact

> **Inorder traversal of a BST produces values in sorted order.**

Remember this.

---

# 14. Preorder

Pattern:

```text
NODE → LEFT → RIGHT
```

For our tree:

```text
        8
       / \
      3   10
     / \
    1   6
```

Output:

```text
8 → 3 → 1 → 6 → 10
```

Code:

```python
def preorder(root, result):
    if root:
        result.append(root.val)
        preorder(root.left, result)
        preorder(root.right, result)
```

---

# 15. Postorder

Pattern:

```text
LEFT → RIGHT → NODE
```

Output:

```text
1 → 6 → 3 → 14 → 10 → 8
```

Code:

```python
def postorder(root, result):
    if root:
        postorder(root.left, result)
        postorder(root.right, result)
        result.append(root.val)
```

---

# 16. Easy Way to Remember Traversals

Focus on the position of **NODE**.

```text
INORDER

LEFT → NODE → RIGHT
        ↑
       NODE in middle


PREORDER

NODE → LEFT → RIGHT
↑
NODE first


POSTORDER

LEFT → RIGHT → NODE
                 ↑
              NODE last
```

Don't memorize the names blindly.

Think:

```text
PRE  = node comes BEFORE children
IN   = node comes IN BETWEEN children
POST = node comes AFTER children
```

---

# 17. Searching in a BST ⭐⭐⭐

Suppose:

```text
        8
       / \
      3   10
     / \
    1   6
```

Search for `6`.

At `8`:

```text
6 < 8 → left
```

At `3`:

```text
6 > 3 → right
```

At `6`:

```text
6 == 6 → found
```

Code:

```python
def search(root, val):
    if root is None or root.val == val:
        return root

    if val < root.val:
        return search(root.left, val)
    else:
        return search(root.right, val)
```

---

# 18. What if the value doesn't exist?

Search for `7`.

```text
8
↓
3
↓
6
↓
right
↓
None
```

We eventually reach:

```python
root is None
```

Therefore:

```python
return None
```

So:

```python
result = search(root, 7)

if result:
    print("Found")
else:
    print("Not found")
```

---

# 19. Find Minimum

In a BST:

> **The smallest value is the leftmost node.**

Example:

```text
             8
           /   \
          3     10
         / \
        1   6
```

Keep going left:

```text
8 → 3 → 1
```

So minimum = `1`.

Code:

```python
def find_min(root):
    while root.left:
        root = root.left

    return root
```

---

# 20. Find Maximum

The opposite:

> **The largest value is the rightmost node.**

```text
8 → 10 → 14
```

So maximum = `14`.

```python
def find_max(root):
    while root.right:
        root = root.right

    return root
```

---

# 21. Height of BST

Consider:

```text
        8
       / \
      3   10
     /
    1
```

Height depends on the definition being used.

The version you're learning uses:

```python
def height(root):
    if root is None:
        return 0

    return 1 + max(
        height(root.left),
        height(root.right)
    )
```

Here:

```text
empty tree → height 0
one node   → height 1
```

For:

```text
    8
   /
  3
 /
1
```

height = `3`.

---

# 22. Why Recursion Works So Well Here

This is an important DSA lesson.

A tree contains **smaller trees inside it**.

For:

```text
        8
       / \
      3   10
```

the left side:

```text
    3
```

is itself a tree.

The right side:

```text
    10
```

is itself a tree.

So when we write:

```python
height(root.left)
```

we're simply asking:

> "What's the height of the smaller tree on the left?"

That's why tree problems naturally lend themselves to recursion.

---

# 23. Balanced vs Skewed BST ⭐⭐⭐

This is important for understanding complexity.

### Balanced

```text
          8
        /   \
       4     12
      / \    / \
     2   6  10 14
```

The tree is reasonably balanced.

Searching can be very fast.

### Skewed

If we insert:

```text
1
2
3
4
5
6
```

we get:

```text
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
```

That's basically a linked list wearing a tree costume. 🌲➡️📏

---

# 24. BST Complexity

For a **balanced BST**:

| Operation | Average/Typical |
|---|---:|
| Search | O(log n) |
| Insert | O(log n) |
| Find min/max | O(log n) |
| Traversal | O(n) |
| Height | O(n) |

Worst case, if the tree is skewed:

| Operation | Worst case |
|---|---:|
| Search | O(n) |
| Insert | O(n) |
| Find min/max | O(n) |

Why `O(log n)` when balanced?

Because each decision takes you into roughly half the remaining tree:

```text
100 nodes
 ↓
50
 ↓
25
 ↓
12
 ↓
6
...
```

That's the same basic reason binary search is fast.

---

# 25. What about Duplicate Values?

Your current implementation says:

```python
if val < root.val:
    ...
else:
    ...
```

So duplicates go to the **right**.

For example, inserting:

```text
5, 5
```

gives:

```text
5
 \
  5
```

Different BST implementations may use different duplicate rules.

For now:

> **Use the rule in your implementation and be consistent.**

Don't worry about advanced duplicate handling yet.

---

# 26. Complete Basic BST Code

This is the version you should eventually be able to write yourself:

```python
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert(root, val):
    if root is None:
        return TreeNode(val)

    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)

    return root


def search(root, val):
    if root is None or root.val == val:
        return root

    if val < root.val:
        return search(root.left, val)
    else:
        return search(root.right, val)


def inorder(root, result):
    if root:
        inorder(root.left, result)
        result.append(root.val)
        inorder(root.right, result)


def height(root):
    if root is None:
        return 0

    return 1 + max(
        height(root.left),
        height(root.right)
    )
```

Build it:

```python
root = None

for value in [8, 3, 10, 1, 6, 14]:
    root = insert(root, value)
```

Then:

```python
result = []
inorder(root, result)

print(result)
print(search(root, 6).val)
print(height(root))
```

Output:

```text
[1, 3, 6, 8, 10, 14]
6
3
```

---

# 🧠 What YOU need to know for DSA

Don't try to memorize that entire code block.

Your BST checklist should be:

### Must understand ⭐⭐⭐

```text
✓ What is a binary tree?
✓ What makes it a BST?
✓ TreeNode
✓ root / left / right
✓ BST ordering rule
✓ Insert
✓ Search
✓ Inorder traversal
✓ Preorder traversal
✓ Postorder traversal
✓ Height
✓ Balanced vs skewed
✓ BST complexity
```

### Especially important

These three ideas should become automatic:

```text
1. BST:
   left < node < right

2. Inorder:
   left → node → right
   gives sorted order in BST

3. Search:
   smaller → left
   larger  → right
```

### Not necessary yet

```text
❌ AVL trees
❌ Red-Black trees
❌ B-Trees
❌ Splay trees
❌ Advanced deletion cases
```

One caveat: **BST deletion is an important standard operation**, but given your current learning stage, I would postpone its implementation until you've become comfortable with the above. When we return to BST problems, deletion will be worth learning.

---

## 🎯 How I suggest we learn it from here

Don't just paste the complete code into PyCharm.

We'll build it progressively:

**Step 1:** Create `TreeNode` and manually make a 3-node tree.

**Step 2:** Build a BST using `insert()`.

**Step 3:** You trace the recursion for each inserted number.

**Step 4:** Learn the three traversals.

**Step 5:** Implement search.

**Step 6:** Implement min/max and height.

**Step 7:** Do 3-5 tiny BST problems.

That will make the structure stick much better than reading the whole implementation once.



TRIE:
Yes. Let's simplify it a lot. For your **beginner DSA stage**, you do **not** need all the Trie theory right now.

## 🌳 Trie: Learn only these things

### 1. What is a Trie?

Just remember:

> **Trie = a tree used to store words character by character.**

Example:

```text
cat
car
```

share:

```text
c → a
```

then split:

```text
     c
     |
     a
    / \
   t   r
```

---

### 2. Learn `TrieNode`

Know this:

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
```

Understand only:

```text
children → stores next characters
is_end   → tells us a word ends here
```

---

### 3. Learn `Trie`

```python
class Trie:
    def __init__(self):
        self.root = TrieNode()
```

Just understand:

```text
root = starting point
```

---

### 4. Learn `insert()` ⭐⭐⭐

You should be able to understand/write:

```python
def insert(self, word):
    node = self.root

    for ch in word:
        if ch not in node.children:
            node.children[ch] = TrieNode()

        node = node.children[ch]

    node.is_end = True
```

Don't worry about advanced variations.

---

### 5. Learn `search()` ⭐⭐⭐

```python
def search(self, word):
    node = self.root

    for ch in word:
        if ch not in node.children:
            return False

        node = node.children[ch]

    return node.is_end
```

Understand:

```text
character exists → continue
character missing → False
finished word → check is_end
```

---

### 6. Learn `startsWith()` ⭐⭐

```python
def starts_with(self, prefix):
    node = self.root

    for ch in prefix:
        if ch not in node.children:
            return False

        node = node.children[ch]

    return True
```

Just remember:

```text
search()      → complete word?
startsWith()  → prefix exists?
```

---

# 🎯 That's ALL for Trie right now

Your checklist:

```text
TRIE
──────────────
[ ] Trie concept
[ ] TrieNode
[ ] children
[ ] is_end
[ ] root
[ ] insert()
[ ] search()
[ ] startsWith()
```

### Don't learn yet ❌

```text
❌ Delete from Trie
❌ Autocomplete implementation
❌ Wildcard search
❌ Compressed Trie
❌ Ternary Search Tree
❌ Advanced Trie problems
```

Once you can **create a Trie + insert + search + startsWith**, move on.

That's the right level for you right now.


Union Find :
Absolutely. Let's keep **Union-Find (Disjoint Set Union / DSU)** to only what you actually need for DSA. No mathematical jungle. 🌱

# Union-Find / DSU

### 1. What is it?

Union-Find is a data structure used to **manage groups of connected elements**.

It mainly answers:

> **"Are these two elements in the same group?"**

and allows:

> **"Join these two groups."**

### 2. The only 2 operations you need

```text
find(x)    → tells which group x belongs to
union(a,b) → joins the groups of a and b
```

Example:

```text
Initially:

0   1   2   3   4

Each is its own group.
```

After:

```python
union(0, 1)
union(1, 2)
```

You get:

```text
0 ─ 1 ─ 2     3     4
   Group 1   Group 2 Group 3
```

So:

```text
find(0) == find(2) → True
find(0) == find(3) → False
```

---

# 3. Basic implementation

This is the version you should learn:

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a != root_b:
            self.parent[root_b] = root_a
```

Don't worry if `find()` looks strange initially. The important idea is:

```python
self.parent[x]
```

stores **who x points to**.

---

# 4. How to use it

```python
uf = UnionFind(5)

uf.union(0, 1)
uf.union(1, 2)

print(uf.find(0) == uf.find(2))
print(uf.find(0) == uf.find(3))
```

Output:

```text
True
False
```

---

# 5. One optimization you should know

The line:

```python
self.parent[x] = self.find(self.parent[x])
```

is called **path compression**.

You don't need to master the theory yet. Just remember:

> **Path compression makes future `find()` operations faster by directly connecting nodes to their group representative.**

### Your Union-Find checklist

```text
UNION-FIND
[✓] What is Union-Find?
[✓] parent array
[✓] find()
[✓] union()
[✓] Path compression
[ ] Union by rank/size → learn later
[ ] Advanced DSU problems → later
```

For your current DSA stage, **this is enough**. You can move on from Union-Find without learning its advanced variations.