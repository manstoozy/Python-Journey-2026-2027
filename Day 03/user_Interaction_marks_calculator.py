# user inputs
test1 = float(input("Enter Test 1 marks: "))
test2 = float(input("Enter Test 2 marks: "))
test3 = float(input("Enter Test 3 marks: "))

# calculate marks avarage
avarage = (test1 + test2 + test3) / 3

# display the results
print("\n=======Final Year Mark=======")
print("Avarage:", round(avarage, 2))

# compare results
print("Passed:", avarage >= 50)
print("Passed with Distinction:", avarage >= 75)
