# Getting number from the user
num1 = int(input("Enter a number: "))
is_prime = True  # Assume the number is prime initially

# Loop to check for any factors between 2 and num1-1
for x in range(2, num1):
    if num1 % x == 0:
        is_prime = False  # Found a factor, so it's not prime
        break  # Exit the loop immediately

# Printing the final result based on the flag
if is_prime and num1 > 1:
    print(f"{num1} is prime 🎉")
else:
    print(f"{num1} is NOT prime ❌")