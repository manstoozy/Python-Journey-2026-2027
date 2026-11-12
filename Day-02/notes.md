## Day 02 — Variables and Data Types

Today we're learning how Python stores information and how to work with different types of data.

## Part 1 — Understanding variables

A **variable** is a named container used to store information in a program.

Think of it as a labelled box.

**For example:**

name = "Sibusiso"

age = 21

course = "Computer Systems Engineering"

**Here:**
- name stores "Sibusiso".
- age stores 21.
- course stores "Computer Systems Engineering".
  
The **=** symbol is called the **assignment operator**. It assigns a value to a variable.

**Displaying variables**

name = "Sibusiso"

age = 21

print(name)

print(age)

**Output:**

Sibusiso

21

**You can also combine text and variables:**

name = "Sibusiso"

course = "Computer Systems Engineering"

print("My name is", name)

print("My course is", course)

**Output:**

My name is Sibusiso

My course is Computer Systems Engineering

## Part 2 — Rules for naming variables

Python has rules when naming variables.

**Correct naming**           
- name
- student_age
- myCourse
- age2	

**Remember:**

- Variable names cannot start with numbers. 
- They cannot contain spaces.
- They cannot use Python reserved keywords such as **if, for, and class**.
- Python is case-sensitive: **age** and **Age** are different variables

## Part 3 — Python data types
A data type tells Python what kind of value is being stored.

**There are four important beginner data types:**

**1. String (str) (Text)**

name = "Sibusiso"

university = "VUT"

**2. Integer (int) (Whole numbers)**

age = 21

year = 2026

**3. Float (float) (Decimal numbers)**

height = 1.75

price = 99.50

**4. Boolean (bool) (True or False)**

is_student = True

has_passed = False

## Part 4 — Checking data types with type()

Python provides a built-in function called type().

It tells us the data type of a value or variable.

**Example:**

name = "Sibusiso"

age = 21

height = 1.75

is_student = True

print(type(name))

print(type(age))

print(type(height))

print(type(is_student))

**Output:**

<class 'str'>

<class 'int'>

<class 'float'>

<class 'bool'>



