# Understanding Stacks in Python

A **stack** is a fundamental data structure in computer science that follows the **Last-In, First-Out (LIFO)** principle. This means the last element added to the stack will be the first one to be removed. Imagine a stack of plates: you add plates to the top and also remove from the top.

---

## Table of Contents

- [Stack Data Structure - Notes](#stack-data-structure---notes)
      - [1. **Introduction to Stack**](#1-introduction-to-stack)
      - [2. **Basic Operations**](#2-basic-operations)
      - [3. **Real-Life Examples**](#3-real-life-examples)
      - [4. **Python Implementation Using List**](#4-python-implementation-using-list)
      - [5. **Common Stack Use Cases**](#5-common-stack-use-cases)
      - [6. **Stack in Real-World Applications**](#6-stack-in-real-world-applications)
    - [Stack Operations with Examples](#stack-operations-with-examples)
    - [1. **Push Operation**](#1-push-operation)
    - [2. **Push Multiple Elements**](#2-push-multiple-elements)
    - [3. **Pop Operation**](#3-pop-operation)
    - [4. **Check if Stack is Empty**](#4-check-if-stack-is-empty)
    - [5. **Peek at the Top Element**](#5-peek-at-the-top-element)
    - [**Summary of Stack Operations**](#summary-of-stack-operations)
- [Understanding Stacks in Python](#understanding-stacks-in-python)
  - [Table of Contents](#table-of-contents)
  - [1. Introduction to Stacks](#1-introduction-to-stacks)
  - [2. Stack Operations](#2-stack-operations)
  - [3. Implementing Stacks in Python](#3-implementing-stacks-in-python)
    - [Using a List](#using-a-list)
    - [Using `collections.deque`](#using-collectionsdeque)
    - [Creating a Custom Stack Class](#creating-a-custom-stack-class)
  - [4. Practical Examples](#4-practical-examples)
    - [Reversing a String](#reversing-a-string)
    - [Checking for Balanced Parentheses](#checking-for-balanced-parentheses)
  - [5. Summary](#5-summary)
  - [6. References](#6-references)

---

## 1. Introduction to Stacks

A stack is a linear data structure that allows adding and removing elements in a particular order.
The principal operations are:

- **Push**: Add an element to the top of the stack.
- **Pop**: Remove the element from the top of the stack.

**Characteristics:**

- **LIFO (Last-In, First-Out)**: The last element pushed onto the stack is the first one popped off.
- Used in various applications like function call management, undo mechanisms, and parsing expressions.

---

## 2. Stack Operations

The fundamental operations performed on a stack:

- **Push**: Insert an element on top of the stack.
- **Pop**: Remove and return the top element of the stack.
- **Peek/Top**: Return the top element without removing it.
- **isEmpty**: Check if the stack is empty.
- **Size**: Return the number of elements in the stack.

---

## 3. Implementing Stacks in Python

Python doesn't have a built-in stack data type, but you can implement a stack using lists or the `deque` class from the `collections` module.

### Using a List

Python lists can serve as stacks since they support adding and removing elements from the end.

```python
# Initialize an empty stack
stack = []

# Push operation
stack.append(item)

# Pop operation
item = stack.pop()

# Peek operation
top_item = stack[-1] if stack else None

# Check if the stack is empty
is_empty = len(stack) == 0

# Get the size of the stack
size = len(stack)
```

**Note:** While lists are efficient for stack operations, they can be less efficient than `deque` for large data sets due to memory allocation.

### Using `collections.deque`

The `deque` (double-ended queue) is optimized for adding and removing elements from both ends.

```python
from collections import deque

# Initialize an empty stack
stack = deque()

# Push operation
stack.append(item)

# Pop operation
item = stack.pop()

# Peek operation
top_item = stack[-1] if stack else None

# Check if the stack is empty
is_empty = len(stack) == 0

# Get the size of the stack
size = len(stack)
```

### Creating a Custom Stack Class

Creating a custom class allows for more control and readability.

```python
class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return not self.items
    
    def push(self, item):
        self.items.append(item)
        print(f"Pushed {item} onto the stack.")
    
    def pop(self):
        if self.isEmpty():
            print("Stack is empty. Cannot pop.")
            return None
        item = self.items.pop()
        print(f"Popped {item} from the stack.")
        return item
    
    def peek(self):
        if self.isEmpty():
            print("Stack is empty. Nothing to peek.")
            return None
        return self.items[-1]
    
    def size(self):
        return len(self.items)
```

**Example Usage:**

```python
stack = Stack()
stack.push(1)
stack.push(2)
print(f"Top element is {stack.peek()}")
stack.pop()
print(f"Stack size is {stack.size()}")
```

**Output:**

```
Pushed 1 onto the stack.
Pushed 2 onto the stack.
Top element is 2
Popped 2 from the stack.
Stack size is 1
```

---

## 4. Practical Examples

### Reversing a String

You can use a stack to reverse a string by pushing each character onto the stack and then popping them off.

```python
def reverse_string(s):
    stack = []
    for char in s:
        stack.append(char)
    reversed_s = ''
    while stack:
        reversed_s += stack.pop()
    return reversed_s

print(reverse_string("Hello, World!"))  # Output: !dlroW ,olleH
```

### Checking for Balanced Parentheses

Stacks are useful for checking if an expression has balanced parentheses.

```python
def is_balanced(expression):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in expression:
        if char in '([{':
            stack.append(char)
            print(f"Pushed {char} onto the stack.")
        elif char in ')]}':
            if not stack or stack.pop() != pairs[char]:
                print(f"Unbalanced at character {char}")
                return False
            print(f"Popped matching opening brace for {char}")
    if stack:
        print("Unbalanced - Stack is not empty at the end.")
        return False
    return True

expr = "{[()()]}"
print(f"Expression '{expr}' is balanced: {is_balanced(expr)}")
```

**Output:**

```
Pushed { onto the stack.
Pushed [ onto the stack.
Pushed ( onto the stack.
Popped matching opening brace for )
Pushed ( onto the stack.
Popped matching opening brace for )
Popped matching opening brace for ]
Popped matching opening brace for }
Expression '{[()()]}' is balanced: True
```

---

## 5. Summary

- **Stack**: A linear data structure following LIFO.
- **Primary Operations**: `push()`, `pop()`, `peek()`, `isEmpty()`, `size()`.
- **Implementation in Python**:
  - **List**: Simple but can be less efficient for large datasets.
  - **`deque`**: Optimized for frequent additions/removals.
  - **Custom Class**: Offers more control and clarity.
- **Use Cases**:
  - Reversing data.
  - Undo mechanisms.
  - Syntax parsing.
  - Function call management.

---

## 6. References

- [Python Documentation on Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Collections — Container Datatypes](https://docs.python.org/3/library/collections.html#collections.deque)
- [Real Python: Stacks and Queues](https://realpython.com/queue-in-python/)

