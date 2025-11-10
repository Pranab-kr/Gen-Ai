LOOPS IN PYTHON
================================================================

Loops are used in programming to repeat a block of code multiple times until a certain condition is met. In Python, there are two primary types of loops: `for` loops and `while` loops.


FOR LOOPS
================================================
A `for` loop is used to iterate over a sequence (like a list, tuple, dictionary, set, or string) or other iterable objects. The syntax of a `for` loop is as follows:
```python
for item in iterable:
    # do something with item
```
Example:
```pythonpython
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```
Output:
```apple
banana
cherry
```
WHILE LOOPS
============================
A `while` loop repeatedly executes a block of code as long as a specified condition is true. The syntax of a `while` loop is as follows:
```python
while condition:
    # do something
```
Example:
```python
count = 0
while count < 5:
    print(count)
    count += 1
```
Output:
```0
1
2
3
4
```
BREAK AND CONTINUE STATEMENTS
================================================
- The `break` statement is used to exit a loop prematurely when a certain condition is met.
- The `continue` statement is used to skip the current iteration of a loop and move to the next iteration.
Example using `break`:
```python
for number in range(10):
    if number == 5:
        break
    print(number)
```
Output:
```0
1
2
3
4
```
Example using `continue`:
```python
for number in range(10):
    if number % 2 == 0:
        continue
    print(number)
```
Output:
```1
3
5
7
9
```
