# Getting numbers from the user
nums = input("Enter numbers and press space between them: ")

# Splitting the string and converting each item to an integer in one line
split_numbers = [int(num) for num in nums.split()]

# Calculating the average using sum() and len()
average = sum(split_numbers) / len(split_numbers)

print("---------------------------")
print(f"The average is: {average}")