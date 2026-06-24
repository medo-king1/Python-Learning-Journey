# Getting words from the user and splitting them into a list
words_list = input("Enter words separated by spaces: ").split()

# Empty list to store unique words
unique_words = []

# Loop through each word in the original list
for word in words_list:
    # Check if the word is NOT already in the new list
    if word not in unique_words:
        unique_words.append(word)

# Printing the final list without duplicates
print("----------------------------------------")
print(f"Unique Words: {unique_words}")