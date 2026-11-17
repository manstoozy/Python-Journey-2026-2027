number = int(input("Enter a positive whole number: "))

factorial = 1

for count in range(1, number + 1):
    factorial *= count

print("Factorial:", factorial)