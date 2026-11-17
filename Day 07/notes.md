## Day 07 — Python for Loops

 Repetition using for loop

**By the end of Day 07, you'll understand:**
- What a for loop is.
- How to use the range() function.
- How to loop through strings.
- The difference between for and while loops.
- How to use loops in practical programs.
  
# 1. What is a for loop?

A for loop is used to repeat a block of code for each item in a sequence.

**For example, instead of writing:**

print(1)
print(2)
print(3)
print(4)
print(5)

**You can use:**

for number in range(1, 6):    

    print(number)

**Output:**

1
2
3
4
5

Much shorter!

# 2. Understanding range()

The range() function generates a sequence of numbers.

It is commonly used with for loops.

**There are three ways to use it:**

# A. range(stop)

for number in range(5):    

    print(number)



**Output:**

0
1
2
3
4

It starts at 0 and stops before 5.

# B. range(start, stop)

for number in range(1, 6):   

    print(number)

**Output:**

1
2
3
4
5

It starts at 1 and stops before 6.

# C. range(start, stop, step)

The step determines how much the number increases or decreases each time.

for number in range(2, 11, 2):   

    print(number)

**Output:**

2
4
6
8
10

**Here:**
- Start = 2
- Stop = 11
- Step = 2
  
**Remember:** the stop value is not included.

# 3. Counting backwards

You can also use a negative step to count backwards.

for number in range(10, 0, -1):    

    print(number)

**Output:**

10
9
8
7
6
5
4
3
2
1

The -1 tells Python to decrease the number by 1 each time.

# 4. Looping through strings

A for loop can also go through each character in a word.

**Example:**

word = "PYTHON"

for letter in word:   

    print(letter)

**Output:**

P
Y
T
H
O
N

Python takes one character at a time and displays it.

# 5. Using a for loop with calculations

Let's calculate the total of numbers from 1 to 5.

    # starting total

total = 0

    # calculate the sum
    
for number in range(1, 6):    

total = total + number

    # display the result
    
print("Total:", total)

**Output:**

Total: 15

# 6. Difference between for and while loops

Both loops repeat code, but they are commonly used in different situations.

| For Loop | While Loop |
|-----------|-----------|
| Used to iterate through a sequence | Repeats while a condition is true |
| Often used when the number of repetitions is known | Often used when repetitions depend on a condition |
| Can use `range()` | Uses a condition |
| Automatically moves to the next item | You often update the variable yourself |

## Example of a `for` Loop

```python
for number in range(1, 6):
    print(number)
```

## Example of a `while` Loop

```python
number = 1

while number <= 5:
    print(number)
    number += 1
```

## Both Produce the Same Output

```text
1
2
3
4
5
```

---

# 7. Practical Examples

## Example 1 – Multiplication Table

```python
# User input
number = int(input("Enter a number: "))

# Display multiplication table
print("\n======= Multiplication Table =======")

for count in range(1, 11):
    print(number, "x", count, "=", number * count)
```

### Sample Output

If the user enters **5**:

```text
======= Multiplication Table =======
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
```

---

## Example 2 – Gym Workout Counter

```python
# Workout details
exercise = input("Enter exercise name: ")
sets = int(input("Enter number of sets: "))

# Display workout sets
print("\n======= Workout Tracker =======")

for count in range(1, sets + 1):
    print("Set", count, "-", exercise)

print("Workout completed!")
```

### Sample Output

If the user enters **Push-ups** and **3** sets:

```text
======= Workout Tracker =======
Set 1 - Push-ups
Set 2 - Push-ups
Set 3 - Push-ups
Workout completed!
```

---

## Important Note About `range()`

```python
range(start, stop)
```

The `stop` value is **not included** in the sequence.

Example:

```python
for number in range(1, 6):
    print(number)
```

Output:

```text
1
2
3
4
5
```

Notice that **6 is not included**.

Therefore:

```python
range(1, sets + 1)
```

is used to ensure the final set is included.

Example:

```python
range(1, 4)
```

Produces:

```text
1
2
3
```

This is why `sets + 1` is needed when counting from 1 up to the total number of sets.

# Day 07 Exercises

Try these independently before asking for the solutions.

---

## Exercise 1 – Counting Numbers

Use a `for` loop to display numbers from **1 to 20**.

### Expected Output

```text
1
2
3
...
20
```

---

## Exercise 2 – Even Numbers

Use a `for` loop to display even numbers from **2 to 30**.

### Expected Output

```text
2
4
6
...
30
```

---

## Exercise 3 – Multiplication Table

Ask the user to enter a number.

Use a `for` loop to display its multiplication table from **1 to 12**.

### Example

```text
Enter a number: 5

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 12 = 60
```

---

## Exercise 4 – Sum of Numbers

Use a `for` loop to calculate the sum of numbers from **1 to 100**.

### Expected Output

```text
The sum is: 5050
```

---

## Exercise 5 – Factorial Calculator

Ask the user to enter a positive whole number.

Calculate its factorial using a `for` loop.

### Example

```text
Enter a number: 5
Factorial: 120
```

### Hint

Factorial means multiplying a number by every positive whole number below it.

```text
5! = 5 × 4 × 3 × 2 × 1 = 120
```


