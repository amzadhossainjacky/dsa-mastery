
#problems: Minimum of two numbers

try:

    # Define first number and second number
    first_number = int(input(f"Given first number: "))
    second_number = int(input(f"Given second number: "))

    #Check which one is smaller
    if first_number < second_number:
        print(f"{first_number} is less than {second_number}")
    elif first_number > second_number:
        print(f"{second_number} is less than {first_number}")
    else:
        print("Both numbers are equal.")

except ValueError as e:
    print("Invalid input.")
    print(f"Error details: {e}")