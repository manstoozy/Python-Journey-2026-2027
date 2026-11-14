# user inputs
exercise = input("Enter exercise name: ")
reps = int(input("Enter repetitions per set: "))
sets = int(input("Enter number of sets: "))

# calculate total repetitions
total = reps * sets

# display the results
print("\n=======Gym Workout Summary=======")
print("Exercise:", exercise)
print("Repetitions per set:", reps)
print("Number of sets:", sets)
print("Total repetitions:", total)