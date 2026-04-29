# Prompt user to enter password
#  and validate the field and the user input

password = 'Roy'

while True:
    passwordInput = input("Enter your password (q to quit): ")
    
    if passwordInput == "":
        print("You did not enter a password!")
        continue