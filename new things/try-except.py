#try / except --

try:
    num1 = int(input("Enter a number : "))
    num2 = int(input("Enter second number : "))
    print(num1/num2)
except ZeroDivisionError:
    print("ZeroDivisionError !")
except ValueError:
    print("ValueError")
except:
    print("Something wrong")