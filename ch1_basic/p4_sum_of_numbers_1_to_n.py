
# Problem: Sum of numbers 1 to N

try:
    #Get the number from user input
    input_number = int(input(f"Input number: "))
    initial_number = 1
    sum_of_numbers = 0
    i=1

    # Check if the number is valid
    if(input_number >=1):
        # Calculate the sum from 1 to input_number
        """ for i in range(1, input_number + 1):
            sum_of_numbers = sum_of_numbers + initial_number
            initial_number  = initial_number +1 """
        while i <= input_number:
            sum_of_numbers+=initial_number
            initial_number+=1

            i = i+1
            
        # Example: for 3 → 1 + 2 + 3 = 6
        print(f"Sum of the numbers: {sum_of_numbers}")

    else: 
        print("Given number is not equal or greater than 1")

except ValueError as e:
    print("Invalid input")
    print(f"Error details: {e}")

    
