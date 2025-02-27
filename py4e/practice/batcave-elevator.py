name = input("Please identify yourself! ")
print(f"Hello, Master {name.capitalize()}.")
print("Welcome to the Bat Cave!\n")

ground_floor = "operations"
first_floor = "weapons"
second_floor = "transport"
third_floor = "suit"

which_floor = input("Please enter the floor you wish to go: ")

if which_floor == f"{ground_floor}":
    print(f"{ground_floor.capitalize()} room it is.")
    print(f"Welcome to the {ground_floor.capitalize()} room.")
    print("Let's find some bad guys!")
elif which_floor == f"{first_floor}":
    print(f"{first_floor.capitalize()} room it is.")
    print(f"Welcome to the {first_floor.capitalize()} room.")
    print("Welcome to the candy land!")
elif which_floor == f"{second_floor}":
    print(f"{second_floor.capitalize()} room it is.")
    print(f"Welcome to the {second_floor.capitalize()} room.")
    print("Let's chase some bad guys!")
elif which_floor == f"{third_floor}":
    print(f"{third_floor.capitalize()} room it is.")
    print(f"Welcome to the {third_floor.capitalize()} room.")
    print(f"Sweet Dreams! Master {name.capitalize()}.")
else:
    print("Error! Please enter the valid floor name")