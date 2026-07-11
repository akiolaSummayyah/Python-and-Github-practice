
import math
print("Welcome to my calculator!")
num1=float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
operation=input("Choose Operation(+ - * / ** sqrt):")
if operation=="+":
    result=num1 + num2
elif operation=="-":
    result=num1-num2
elif operation== "*":
    result=num1 * num2
elif operation=="/":
    result=num1 /num2
elif operation=="**":
    result=num1 ** num2
elif operation=="sqrt":
    result=math.sqrt(num1)
else:
    print("Invalid operation!")
print("Answer:", result)
word=input("Enter a word:")
print(word * 5)
