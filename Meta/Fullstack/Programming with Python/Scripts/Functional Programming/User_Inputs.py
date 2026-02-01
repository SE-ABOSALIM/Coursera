name = input("What is your name? ")
surname = input("What is your surname? ")
email = input("What is your email? ")
phoneNumber = input("What is your phone number? ")

print(f'Hello {name} {surname}',
      f'Welcome to our system you need to verify your {email} email address',
      f'Also check if your {phoneNumber} phone number is correct.', sep='\n') # Separate by \n to go to new line