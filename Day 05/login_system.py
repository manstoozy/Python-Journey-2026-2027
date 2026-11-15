# correct login details
correct_username = "admin"
correct_password = "12345"

# user inputs
username = input("Enter username: ")
password = input("Enter password: ")

# check login details
if username == correct_username and password == correct_password:
    print("Login successful")
else:
    print("Invalid username or password")