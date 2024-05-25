num1 = float(input("enter the first num : "))
oprate = input("choose the oprator(+, -, *, /)")
num2 = float(input("enter the sacend num : "))

if oprate == "+":
    result = num1 + num2
elif oprate == "-":
    result = num1 - num2
elif oprate == "*":
    result = num1 * num2
elif oprate == "/":
    result = num1 / num2
else:
    result = "out of order"

print(f"RESULT:{result}")
