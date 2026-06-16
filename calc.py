# calculator project
#--------------------------------------------------------#

# *TODO*: Upgrade inputs from int to float to support decimal numbers later

# input first number
num1 = int(input('Enter first number : '))

# input operator
op = input('Enter operator +,-,*,/ : ')

# input second number
num2 = int(input('Enter second number : '))
# conditions , input result
if op == "+":
    print(f" Result is :{num1 + num2}")

elif op == "-":
    print(f" Result is :{num1 - num2}")

elif op == "*" :
    print(f" Result is :{num1 * num2}")

elif op == "/" :
    print(f" Result is :{num1 / num2}")

else:
    print("Error")