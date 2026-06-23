# Getting numbers from the user
nums = input("Enter numbers separated by space: ")
split_num = nums.split()

# Initializing counters
positive_nums = 0
negative_nums = 0
zero_nums = 0

# Loop through the split strings, convert to int, and check conditions
for num in split_num:
    int_num = int(num)
    if int_num > 0:
        positive_nums += 1
    elif int_num < 0:
        negative_nums += 1  # Fixed the += operator
    else:
        zero_nums += 1

# Printing the final counts
print("---------------------------")
print(f"Positive numbers: {positive_nums}")
print(f"Negative numbers: {negative_nums}")  # Fixed the printed variable
print(f"Zero numbers: {zero_nums}")