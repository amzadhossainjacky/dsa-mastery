
# Problem: Is the number is odd and even

try:
    # Get the number from user input
    given_number = int(input(f"Input number: "))

    #check the number is odd or even
    if(given_number % 2 == 0):
        print(f"{given_number} is even")
    else:
        print(f"{given_number} is odd")

except ValueError as e:
    print("invalid input")
    print(f"Error details: {e}")

