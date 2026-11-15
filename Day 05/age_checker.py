# user input
age = int(input("Enter your age: "))

# check age category
if age < 13:
    category = "Child"
elif age <= 19:
    category = "Teenager"
else:
    category = "Adult"

# display the results
print("\n======= Age Category =======")
print("Age:", age)
print("Category:", category)