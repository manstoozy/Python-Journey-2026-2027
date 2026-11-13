## Day 03 — Python Operators & Expressions

## Part 1 — What are operators?

An operator is a symbol or keyword that performs an operation on values or variables.

**For example:**

x = 20

y = 10

result = x + y

print(result)

**Output:**

30

**Here:**
- x and y are operands (values).
- **+** is the operator.
- x + y is an expression.
- **result** stores the answer.

## Part 2 — Arithmetic operators

Arithmetic operators are used to perform mathematical calculations.

| Operator | Name | Example | Answer |
|--------|--------|--------|--------|
| `+` | Addition | `10 + 5` | 15 |
| `-` | Subtraction | `10 - 5` | 5 |
| `*` | Multiplication | `10 * 5` | 50 |
| `/` | Division | `10 / 5` | 2.0 |
| `%` | Modulus | `10 % 3` | 1 |
| `**` | Exponentiation | `2 ** 3` | 8 |
| `//` | Floor division | `10 // 3` | 3 |

**Understand the two special operators**

**1. Modulus %**

Returns the remainder after division.

x = 10

y = 3

print(x % y)

**Output:**

1

Why? 3 goes into 10 three times, leaving a remainder of 1.

**2. Floor division //**

Returns the quotient rounded down to the nearest whole number.

print(10 // 3)

**Output:**

3

## Part 3 — Comparison operators

Comparison operators compare two values.

**They return a Boolean result:** True or False.

| Operator | Meaning | Example | Result |
|--------|--------|--------|--------|
| `==` | Equal to | `10 == 10` | True |
| `!=` | Not equal to | `10 != 5` | True |
| `>` | Greater than | `10 > 5` | True |
| `<` | Less than | `10 < 5` | False |
| `>=` | Greater than or equal to | `10 >= 10` | True |
| `<=` | Less than or equal to | `5 <= 10` | True |

**Example:**

age = 21

print(age == 21)

print(age > 18)

print(age < 18)

**Output:**

True

True

False

**Important difference:**
- **=** assigns a value.
- **==** checks whether two values are equal.

## Part 4 — Logical operators

Logical operators combine or reverse conditions.

**Python has three main logical operators:**

| Operator | Meaning |
|--------|--------|
| `and` | Both conditions must be True |
| `or` | At least one condition must be True |
| `not` | Reverses the result |

**1. AND**

age = 21

is_student = True

print(age >= 18 **and** is_student == True)

**Output:**

True

Both conditions are True.

**2. OR**

age = 17
has_permission = True

print(age >= 18 **or** has_permission == True)

**Output:**

True

At least one condition is True.

**3. NOT**
   
is_student = True

print(**not** is_student)

**Output:**

False

not reverses True into False.

## Part 5 — Assignment operators

Assignment operators assign or update values stored in variables.

| Operator | Example | Equivalent to |
|--------|--------|--------|
| `=` | `x = 10` | Assign 10 |
| `+=` | `x += 5` | `x = x + 5` |
| `-=` | `x -= 5` | `x = x - 5` |
| `*=` | `x *= 5` | `x = x * 5` |
| `/=` | `x /= 5` | `x = x / 5` |

**Example:**

x = 10

x += 5

print(x)

**Output:**

15

## Part 6 — Operator precedence

Operator precedence determines which calculation Python performs first.

**For example:**

result = 10 + 5 * 2

print(result)

**Output:**

20

Why not 30?

Because multiplication happens before addition.

**You can use brackets to change the order:**

result = (10 + 5) * 2

print(result)

**Output:**

30

**Remember this basic order:**
1. Brackets ()
2. Exponents **
3. Multiplication, division, floor division and modulus
4. Addition and subtraction
