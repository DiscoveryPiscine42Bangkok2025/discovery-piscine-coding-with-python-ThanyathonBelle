num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
mul = num1 * num2
print(num1, "x", num2, "=", mul)
if mul < 0:
    print("The result is negative.")
elif mul > 0:
    print("The result is positive.")
else:
    print("The result is positive and negative.")