# Appendix B: Top 20 Python Errors (and How to Fix Them)

Every Python developer - from complete beginner to seasoned professional - has seen these errors. The difference between a beginner and an expert isn't that experts don't get errors; it's that experts read the error message, nod, and fix it in thirty seconds. By the end of this appendix, you'll do the same.

---

## 1. SyntaxError: invalid syntax

**We've ALL seen this one.** It means Python can't even understand your code enough to run it.

```python
# This causes the error
if x == 5
    print("hello")
```

```
SyntaxError: invalid syntax
```

**What it means:** You have a typo or missing punctuation. Python's parser choked.

**Common causes:** Missing colon after `if`, `for`, `while`, `def`, or `class`. Mismatched parentheses. Using `=` instead of `==`.

**Fix:** Add the missing colon:
```python
if x == 5:
    print("hello")
```

---

## 2. IndentationError: unexpected indent

```python
x = 5
    y = 10  # This line is randomly indented
```

**What it means:** A line is indented when it shouldn't be, or indented to the wrong level.

**Fix:** Make sure indentation is consistent. Use 4 spaces per level (never mix tabs and spaces). Most editors have a "convert tabs to spaces" setting - turn it on.

---

## 3. NameError: name 'variable' is not defined

```python
print(message)  # 'message' was never created
```

**What it means:** You're trying to use a variable or function that doesn't exist yet.

**Common causes:** Typo in the variable name. Using a variable before assigning it. Forgetting to import a module.

**Fix:** Check spelling carefully. Make sure the variable is assigned before you use it. Variable names are case-sensitive (`Name` is not `name`).

---

## 4. TypeError: unsupported operand type(s)

```python
result = "age: " + 25
```

```
TypeError: can only concatenate str (not "int") to str
```

**What it means:** You're trying to combine two types that don't work together.

**Fix:** Convert to the same type:
```python
result = "age: " + str(25)
# Or better, use an f-string:
result = f"age: {25}"
```

---

## 5. TypeError: function() takes X positional arguments but Y were given

```python
def greet(name):
    print(f"Hello, {name}")

greet("Alice", "Bob")  # Too many arguments
```

**What it means:** You called a function with the wrong number of arguments.

**Fix:** Check the function definition and match the number of arguments. If you forgot `self` in a class method, that's often the culprit.

---

## 6. IndexError: list index out of range

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[3])  # Only indices 0, 1, 2 exist
```

**What it means:** You're trying to access a list position that doesn't exist.

**Fix:** Remember that list indices start at 0. A list with 3 items has indices 0, 1, and 2. Use `len(fruits) - 1` for the last index, or just `fruits[-1]`.

---

## 7. KeyError: 'key'

```python
user = {"name": "Alice", "age": 30}
print(user["email"])  # 'email' doesn't exist
```

**What it means:** You're trying to access a dictionary key that doesn't exist.

**Fix:** Use `.get()` for safe access:
```python
email = user.get("email", "not provided")
```
Or check first: `if "email" in user:`

---

## 8. ValueError: invalid literal for int()

```python
number = int("hello")
```

**What it means:** You tried to convert a string to a number, but the string isn't a valid number.

**Fix:** Validate input before converting, or use try/except:
```python
try:
    number = int(user_input)
except ValueError:
    print("Please enter a valid number.")
```

---

## 9. AttributeError: 'type' object has no attribute 'method'

```python
name = "Alice"
name.push("!")  # Strings don't have a 'push' method
```

**What it means:** You're calling a method that doesn't exist on that type.

**Fix:** Check the documentation for available methods. For strings, it's `name + "!"` or `name.replace(...)`. For lists, `append()` not `push()`.

---

## 10. FileNotFoundError: No such file or directory

```python
with open("data.txt") as f:
    content = f.read()
```

**What it means:** The file you're trying to open doesn't exist at that path.

**Fix:** Check the file path. Use `os.path.exists("data.txt")` to verify. Remember that the path is relative to where you RUN the script, not where the script file lives.

---

## 11. ModuleNotFoundError: No module named 'module'

```python
import pandas  # Not installed
```

**What it means:** The module isn't installed or doesn't exist.

**Fix:** Install it with pip:
```bash
pip install pandas
```
If it IS installed, check you're using the right Python environment (virtual environments are a common gotcha).

---

## 12. ZeroDivisionError: division by zero

```python
average = total / count  # count is 0
```

**What it means:** Exactly what it says - you divided by zero.

**Fix:** Check for zero before dividing:
```python
average = total / count if count != 0 else 0
```

---

## 13. TypeError: 'NoneType' object is not subscriptable

```python
result = some_function()
print(result[0])  # some_function() returned None
```

**What it means:** You're trying to index or slice something that is `None`.

**Common cause:** A function that doesn't explicitly return a value returns `None` by default. Methods like `list.sort()` and `list.append()` return `None` (they modify the list in place).

**Fix:**
```python
# Wrong: sort() returns None
sorted_list = my_list.sort()

# Right: sort in place, then use the list
my_list.sort()
sorted_list = my_list

# Or: use sorted() which returns a new list
sorted_list = sorted(my_list)
```

---

## 14. RecursionError: maximum recursion depth exceeded

```python
def countdown(n):
    print(n)
    countdown(n - 1)  # No base case!

countdown(10)
```

**What it means:** A function calls itself forever without stopping.

**Fix:** Add a base case:
```python
def countdown(n):
    if n <= 0:     # Base case
        return
    print(n)
    countdown(n - 1)
```

---

## 15. TypeError: 'int' object is not iterable

```python
for digit in 12345:
    print(digit)
```

**What it means:** You're trying to loop over something that isn't a sequence (like a number).

**Fix:** Convert to an iterable:
```python
for digit in str(12345):
    print(digit)

# Or use range for counting:
for i in range(5):
    print(i)
```

---

## 16. UnboundLocalError: local variable referenced before assignment

```python
count = 10

def increment():
    count = count + 1  # Python sees 'count =' and treats it as local
    return count
```

**What it means:** Inside a function, Python sees an assignment to `count` and treats it as a local variable, but you're trying to read it before the assignment happens.

**Fix:** Use the `global` keyword (sparingly) or pass the value as a parameter:
```python
def increment(count):
    return count + 1

count = increment(count)
```

---

## 17. StopIteration

```python
my_iter = iter([1, 2, 3])
next(my_iter)  # 1
next(my_iter)  # 2
next(my_iter)  # 3
next(my_iter)  # StopIteration!
```

**What it means:** You called `next()` on an iterator that has no more items.

**Fix:** Use a for loop instead (it handles StopIteration automatically), or provide a default:
```python
value = next(my_iter, None)  # Returns None instead of raising error
```

---

## 18. ImportError: cannot import name 'X' from 'Y'

```python
from math import squareroot  # Wrong name
```

**What it means:** The name you're trying to import doesn't exist in that module.

**Fix:** Check the correct name. For math, it's `sqrt`, not `squareroot`:
```python
from math import sqrt
```

---

## 19. PermissionError: Permission denied

```python
with open("/etc/passwd", "w") as f:  # Can't write to system files
    f.write("oops")
```

**What it means:** You don't have permission to read or write that file.

**Fix:** Check file permissions. On Windows, make sure the file isn't open in another program. Write to locations you own (your home directory, your project folder).

---

## 20. JSONDecodeError: Expecting value

```python
import json
data = json.loads("")  # Empty string isn't valid JSON
```

**What it means:** You tried to parse something as JSON, but it's not valid JSON.

**Common causes:** Empty string, HTML instead of JSON (API returned an error page), file path instead of file contents.

**Fix:** Validate before parsing:
```python
import json

text = response.read()
if text:
    try:
        data = json.loads(text)
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
        print(f"Received: {text[:100]}")
```

---

## How to Read Any Error Message

Every Python error message follows this pattern:

```
Traceback (most recent call last):
  File "script.py", line 15, in main
    result = process(data)
  File "script.py", line 8, in process
    return data[key]
KeyError: 'missing_key'
```

Read it from **bottom to top**:
1. **Last line** = the actual error (KeyError: 'missing_key')
2. **Line above** = the exact code that failed (`return data[key]`)
3. **File and line number** = where to look (`script.py, line 8`)
4. **The chain** = how you got there (main called process)

The error message is your friend. Read it carefully, and it will tell you exactly what went wrong and where.
