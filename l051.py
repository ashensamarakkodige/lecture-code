number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

if number1 < number2:
    print("min=", number1, "max=", number2)
elif number1 == number2:
    print("Both number 1 and 2 are equal. The number is:", number1)  # or number2
else:
    print("min=", number2, "max=", number1)
