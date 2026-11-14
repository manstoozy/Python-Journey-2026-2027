# user inputs
item = input("Enter item name: ")
price = float(input("Enter item price: R"))
quantity = int(input("Enter quantity purchased: "))

# calculate total cost
total = price * quantity

# display the results
print("\n=======Shopping Summary=======")
print("Item:", item)
print(f"Price: R{price:.2f}")
print("Quantity:", quantity)
print(f"Total Cost: R{total:.2f}")