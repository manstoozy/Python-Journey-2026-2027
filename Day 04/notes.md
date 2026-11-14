## Day 04 — Input, Output and String Formatting

## Part 1 — Input and output

Input means receiving information from the user.

Output means displaying information to the user.

**Python uses two common built-in functions:**

| Function | Purpose |
|--------|--------|
| `input()` | Receives user information |
| `print()` | Displays information |

**Example:**

# user input

name = input("Enter your name: ")

# display output

print("Welcome,", name)

**Output:**

Enter your name: Sibusiso

Welcome, Sibusiso

## Part 2 — Understanding input()

**Remember:** input() returns a string by default.

**Example:**

age = input("Enter your age: ")

print(type(age))

**If you enter 21, the output is:**

<class 'str'>

To perform calculations, convert the input.

# user input

age = int(input("Enter your age: "))

height = float(input("Enter your height: "))

# display data types

print(type(age))

print(type(height))

**Output:**

Enter your age: 21

Enter your height: 1.75

<class 'int'>

<class 'float'>

## Part 3 — The print() function

You've already used print(), but it has some useful features.

**1. Printing multiple values**

name = "Sibusiso"

age = 21

print("Name:", name, "Age:", age)

**Output:**

Name: Sibusiso Age: 21

**2. Using sep**

sep controls what appears between multiple values.

print("Python", "C++", "Java", sep=" | ")

**Output:**

Python | C++ | Java

**3. Using end**

By default, print() moves to a new line after displaying information. end changes what it prints at the end.

print("Hello", end=" ")

print("World")

**Output:**

Hello World

## Part 4 — Escape characters

Escape characters help you control how text appears.

| Character | Meaning |
|--------|--------|
| `\n` | New line |
| `\t` | Tab space |
| `\\` | Backslash |
| `\"` | Double quotation mark |

**Example:** New line \n

print("Hello\nWorld")

**Output:**
Hello

World

**Example:** Tab \t

print("Name:\tSibusiso")

print("Course:\tComputer Systems Engineering")

**Output:**

**Name:**   Sibusiso

**Course:** Computer Systems Engineering

## Part 5 — String formatting using f-strings

An f-string allows you to insert variables directly into a string.

You place the letter f before the opening quotation mark and put variables inside curly brackets {}.

**Example:**

# variables

name = "Sibusiso"

age = 21

course = "Computer Systems Engineering"

# display information

print(f"My name is {name}.")

print(f"I am {age} years old.")

print(f"I study {course}.")

**Output:**

My name is Sibusiso.

I am 21 years old.

I study Computer Systems Engineering.

Formatting decimal numbers

You can also control the number of decimal places.

average = 78.56789

print(f"Average: {average:.2f}")

**Output:**

**Average:** 78.57

.2f means display two decimal places.

## Part 6 — Practical examples

**Example 1:** Personal information program

# user inputs

name = input("Enter your name: ")

age = int(input("Enter your age: "))

university = input("Enter your university: ")

course = input("Enter your course: ")

# display the results

print("\n=======Student Information=======")

print(f"Name: {name}")

print(f"Age: {age}")

print(f"University: {university}")

print(f"Course: {course}")
