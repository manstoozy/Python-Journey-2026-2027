## Day 06 — Python while Loops

# 1. What is a loop?

A loop allows a program to execute the same block of code repeatedly while a particular condition is true.

**For example, imagine you want Python to display:**

Hello
Hello
Hello
Hello
Hello

You could write five print() statements, but that would be repetitive.

Instead, you can use a loop.

# 2. The while loop

A while loop executes a block of code as long as its condition is true.

**Syntax:**

while condition:

    # code to execute

Let's look at an example.

number = 1

while number <= 5:    

    print(number)    

number = number + 1

**Output:**

1
2
3
4
5

# 3. Understanding the code step by step

Let's break it down.

**Step 1 — Create a variable**

number = 1

We start counting from 1.

**Step 2 — Set the condition**

while number <= 5:

Python checks whether number is less than or equal to 5.

**Step 3 — Display the number**

print(number)

This displays the current value.

**Step 4 — Increase the number**

number = number + 1

This increases the number by 1 every time the loop runs.

It is also possible to write:

number += 1

Both statements do the same thing.

# 5. Important: Infinite loops

An infinite loop happens when a loop never stops because its condition remains true.

**Example:**

number = 1

while number <= 5:    

    print(number)

What's wrong?

We forgot to increase number.

Therefore, the condition number <= 5 will always be true.

**Remember:** Always make sure your loop has a way to reach its stopping condition.

# 6. Using a while loop with user input

You can also use loops together with input().

**Example:** Display numbers until the user reaches 5.

number = 1

while number <= 5:    

    print("Number:", number)    
    
number += 1

**Output:**

Number: 1
Number: 2
Number: 3
Number: 4
Number: 5

# 7. Practical example — Countdown timer

    # starting number
    
count = 5
    
    # countdown
    
while count >= 1:  

    print(count)    
    
    count -= 1
    
    # display message
    
print("Happy New Year!")

**Output:**

5
4
3
2
1
Happy New Year!


Notice that we use count -= 1 to decrease the number by one.

## Day 06 Exercises

Try these independently before looking for solutions.

# Exercise 1 — Counting numbers

Use a while loop to display numbers from 1 to 10.

**Expected output:**

1
2
3
4
5
6
7
8
9
10

# Exercise 2 — Even numbers

Use a while loop to display even numbers from 2 to 20.

**Expected output:**

2
4
6
8
10
12
14
16
18
20


# Exercise 3 — Countdown

Use a while loop to count backwards from 10 to 1.

After the countdown, display:

Time's up!

# Exercise 4 — Multiplication table

Ask the user to enter a number.

Use a while loop to display its multiplication table from 1 to 10.

**Example:**

Enter a number: 5

======= Multiplication Table =======

5 x 1 = 5

5 x 2 = 10

5 x 3 = 15

...

5 x 10 = 50

# Exercise 5 — Sum of numbers

Use a while loop to calculate the sum of numbers from 1 to 10.

Expected output:

The sum is: 55
