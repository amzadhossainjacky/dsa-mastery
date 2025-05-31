""" try:
    # Start: Get input number
    n = int(input("Input a number: "))
    
    # Initialize i to 2
    i = 2

    # Start loop: while i <= n - 1
    while i <= n - 1:
        # If n is divisible by i
        if n % i == 0:
            print(f"{n} is not a prime number")
            break
        i += 1
    else:
        # If loop completes without break, it's prime
        print(f"{n} is a prime number")

except ValueError as e:
    print("Invalid input")
    print(f"Error details: {e}") """

try:
    # Get input number
    n = int(input("Input a number: "))

    if n <= 1:
        print(f"{n} is not a prime number")
    else:
        # Use for loop from 2 to n - 1
        for i in range(2, n):
            if n % i == 0:
                print(f"{n} is not a prime number")
                break
        else:
            # The else belongs to the for loop, not the if
            print(f"{n} is a prime number")

except ValueError as e:
    print("Invalid input")
    print(f"Error details: {e}")