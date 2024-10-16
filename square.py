import math

# Function to check if a number is a perfect square
def is_perfect_square(num):
    if num < 0:
        return False
    sqrt_num = int(math.sqrt(num))
    return sqrt_num * sqrt_num == num

# Input a number from the user
num = int(input("Enter a number: "))

# Check if the number is a perfect square
if is_perfect_square(num):
    print(f"{num} is a perfect square.")
else:
    print(f"{num} is not a perfect square.")
