#Numbers
num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))
num3 = float(input("Enter third number : "))

#If condition
if num1 > num2 and num1 > num3:
    print(f"Number {num1} is the largest - First number")
elif num2 > num1 and num2 > num3:
    print(f"Number {num2} is the largest - second number")
else:
    print(f"Number {num3} is the largest - third number")