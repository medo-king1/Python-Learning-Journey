# Getting password from the user
password = input("Enter your password: ")

# Flags to check password criteria
is_upper = False
is_has_digit = False

# Loop through each character in the password
for char in password:
    # Check if the character is uppercase
    if char.isupper():
        is_upper = True
        
    # Check if the character is a digit
    if char.isdigit():
        is_has_digit = True

# Checking if the password meets all conditions (Upper + Digit + Length)
if is_upper and is_has_digit and len(password) >= 8:
    print("----------------------------------------")
    print("Your password is strong! 💪🎉")
else:
    print("----------------------------------------")
    print("Weak password! Make sure it has 8+ characters, an uppercase letter, and a number. ❌")