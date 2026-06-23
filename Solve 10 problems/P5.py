# Getting text from the user
txt = input("Enter a text: ")

reversed_txt = ""

# Reverse the string by prepending characters
for char in txt:
    reversed_txt = char + reversed_txt

print("---------------------------")
print(f"Reversed text (Loop): {reversed_txt}")

# -------------------------------------------------
# Reverse the string using Slicing method
text = input("Enter text: ")

# Printing the reversed text directly
print(f"Reversed text (Slicing): {text[::-1]}")