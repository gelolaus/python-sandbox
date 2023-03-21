# Asks the user's name
name = input("What's your name? ").strip().title()

# Splits the user's name into first name and last name
first_name, last_name = name.split(" ")

# Greets the user together with their name
print(f"Hey, {first_name}!")
