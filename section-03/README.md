CONDITIONAL STATEMENTS IN PYTHON
===========================================================================
Conditional statements allow you to execute certain pieces of code based on specific conditions. The primary conditional statements in Python are `if`, `elif`, and `else`.

1. **if statement**: The `if` statement evaluates a condition (an expression that returns `True` or `False`). If the condition is `True`, the code block under the `if` statement is executed.

```python
age = 18
if age >= 18:
    print("You are eligible to vote.")
```

2. **elif statement**: The `elif` (short for "else if") statement allows you to check multiple conditions. If the condition for the `if` statement is `False`, the `elif` statement is evaluated.

```python
age = 16
if age >= 18:
    print("You are eligible to vote.")
elif age >= 16:
    print("You are eligible for a learner's permit.")
```

3. **else statement**: The `else` statement is executed if all preceding conditions are `False`.

```python
age = 15
if age >= 18:
    print("You are eligible to vote.")
elif age >= 16:
    print("You are eligible for a learner's permit.")
else:
    print("You are not eligible for any permits.")
```

4. **Nested if statements**: You can also nest `if` statements within each other.

```python
age = 20
if age >= 18:
    print("You are eligible to vote.")
    if age >= 21:
        print("You are also eligible to drink alcohol.")
```

5. **Ternary operator**: Python also supports a shorthand way to write conditional statements using the ternary operator.

```python
age = 18
status = "Eligible to vote." if age >= 18 else "Not eligible to vote."
print(status)
```

In summary, conditional statements are a fundamental part of programming in Python, allowing you to control the flow of your code based on specific conditions.
