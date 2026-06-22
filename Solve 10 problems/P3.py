#Getting the number
num = int(input("Enter a number : "))

#make total variable
total = 0

#loop
for n in range(1, num + 1):
    total += n

#print total
print(f"The sum of first {num} numbers is: {total}")