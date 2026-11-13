# user inputs
pushups = int(input("Enter number of push-ups per set: "))
sets = int(input("Enter number of sets completed: "))

# calculate total push-ups
total = pushups * sets

# display the results
print("\n=======Gym Workout Summary=======")
print("Push-ups per set:", pushups)
print("Number of sets:", sets)
print("Total push-ups:", total)