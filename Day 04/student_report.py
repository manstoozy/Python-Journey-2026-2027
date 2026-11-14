# user inputs
test1 = float(input("Enter Test 1 marks: "))
test2 = float(input("Enter Test 2 marks: "))
test3 = float(input("Enter Test 3 marks: "))

# calculate marks
total = test1 + test2 + test3
average = total / 3

# display the results
print("\n=======Student Marks Report=======")
print("Total Marks:", total)
print(f"Average: {average:.2f}")

# compare results
print("Passed:", average >= 50)
print("Passed with Distinction:", average >= 75)