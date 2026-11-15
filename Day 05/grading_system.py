# user inputs
name = input("Enter student name: ")
marks = float(input("Enter student marks: "))

# check student performance
if marks >= 75 and marks <= 100:
    result = "Distinction"
elif marks >= 50 and marks < 75:
    result = "Pass"
elif marks >= 0 and marks < 50:
    result = "Fail"
else:
    result = "Invalid marks"

# display the results
print("\n======= Student Report =======")
print("Name:", name)
print("Marks:", marks)
print("Result:", result)