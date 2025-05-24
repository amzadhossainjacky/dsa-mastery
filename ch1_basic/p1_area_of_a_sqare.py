
#Problem: Area of a square 

try:
    # Define a variable and input from user
    straight_side = int(input("Input straight side of square: "))

    # Calculate the area of square
    area_of_a_square = straight_side * straight_side

    # Print the results
    print(f"Area of a square: {area_of_a_square}")
except ValueError as e:
    print(f"Error details: {e}")
