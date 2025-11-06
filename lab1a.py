import math


try:
        # Accept input from the user
        num = int(input("Enter a positive integer: "))
        
        # Check if the number is positive
        if num < 0:
            print("The number must be a positive integer.")
            
        
        # Check if the number is a perfect square
        sqrt_num = math.isqrt(num)  # Integer square root
        if sqrt_num * sqrt_num == num:
            print(f"{num} is a perfect square.")
        else:
            print(f"{num} is NOT a perfect square.")
    
except ValueError:
        print("Invalid input! Please enter a valid positive integer.")


