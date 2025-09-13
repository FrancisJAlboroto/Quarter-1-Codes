import string
first, middle, last = input("Enter your full name (First,Middle,Last): ").split(",")
print(f"{last.strip().capitalize()}, {first.strip().capitalize()} {middle.strip()[0].upper()}.")

