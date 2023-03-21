# Defines the main part of the program
def main():
    # Asks the user's name
    name = input("What's your name? ").strip().title()
    # Greets the user together with their name
    hello(f"{name}!")


# Defines the hello() function
def hello(name="World!"):
    print("Hello,", name)


main()
