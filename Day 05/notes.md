## Day 05 — Python: Conditional Statements (if, elif, else)

Today we're learning how to make Python programs make decisions based on conditions.

**By the end of Day 05, you should be able to:**
- Use if, elif and else.
- Compare values using comparison operators.
- Combine conditions using and, or and not.
- Build simple decision-making programs.
  
# 1. What are conditional statements?
Conditional statements allow a program to execute different instructions depending on whether a condition is True or False.

**For example:**

age = 20

if age >= 18:

    print("You are an adult.")

**Output:***

You are an adult.

**Because 20 >= 18 is true**, Python executes the indented print() statement.

# 2. The if statement

An if statement executes code only when its condition is true.

marks = 75

if marks >= 50:

    print("You passed!")

**If the mark is below 50**, nothing will be displayed because the condition is false.

# 3. The if-else statement

Use else when you want the program to do something if the condition is false.

marks = 40

if marks >= 50:

    print("You passed!")

else:

    print("You failed.")

**Output:**

You failed.

# 4. The if-elif-else statement

Use elif when you have multiple conditions to check.

**Example:** Student grading system.

marks = 85

if marks >= 75:

    print("Distinction")

elif marks >= 50:    

    print("Passed")

else:
    
    print("Failed")

**Output:**

Distinction

Python checks the conditions from top to bottom. Once one is true, it executes that block and skips the remaining conditions.

# 5. Comparison operators

These operators help Python compare values.

| Operator | Meaning | Example |
|:---:|---|:---:|
| `==` | Equal to | `10 == 10` |
| `!=` | Not equal to | `10 != 5` |
| `>` | Greater than | `10 > 5` |
| `<` | Less than | `5 < 10` |
| `>=` | Greater than or equal to | `10 >= 10` |
| `<=` | Less than or equal to | `5 <= 10` |

**Remember: =** assigns a value, while **==** compares two values.

# 6. Logical operators

Logical operators allow you to combine conditions.

| Operator | Meaning |
|---|---|
| `and` | Both conditions must be true |
| `or` | At least one condition must be true |
| `not` | Reverses the result |

**Example using and:**

age = 21

has_ticket = True

if age >= 18 and has_ticket == True:   

    print("You can enter.")
    
else:    
    
    print("Entry denied.")

**Output:**

You can enter.

# 7. Combining conditions with and and or

**Example using or:**

A student qualifies if they score at least 75 in Test 1 or Test 2.

test1 = 80

test2 = 60

if test1 >= 75 or test2 >= 75:   

    print("You qualify!")

else:   

    print("You do not qualify.")

**Output:**

You qualify!

# 8. Day 05 exercises

Try these independently. Use the concepts we've covered today.

**Exercise 1 — Even or odd**

Ask the user to enter a number.
- If the number is divisible by 2, display Even number.
- Otherwise, display Odd number.
  
**Hint:** Use the modulus operator %.

**Exercise 2 — Positive, negative or zero**

Ask the user to enter a number.
- Greater than 0: Positive.
- Less than 0: Negative.
- Equal to 0: Zero.
  
**Exercise 3 — Student grading system**

Ask the user to enter their name and marks.

**Display:**
- 75–100: Distinction
- 50–74: Pass
- 0–49: Fail
  
**Exercise 4 — Age eligibility checker**

Ask the user to enter their age.
- Below 13: Child
- 13–19: Teenager
- 20 and above: Adult
  
**Exercise 5 — Simple login system**

Ask the user to enter a username and password.

Use these sample credentials:
- Username: admin
- Password: 12345
  
If both are correct, display Login successful.

Otherwise, display Invalid username or password.
