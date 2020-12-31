username = input("What is your username?\n")
password = input("What is your password?\n")

print(f'{username}, your password {"*" * len(password)} is {len(password)} letters long')