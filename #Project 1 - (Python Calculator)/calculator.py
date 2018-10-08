#Python Calculator 
import time
numOne = float(input("Enter a number: "))

mathOperator = input("Enter a operator: ")

numTwo = float(input("Enter a number: "))

if mathOperator == "+":
	print(numOne + numTwo)

elif mathOperator == "-":
	print(numOne - numTwo)
elif mathOperator == "*":
	print(numOne * numTwo)
elif mathOperator == "/":
	print(numOne / numTwo)
else:
	print("Invalid operator")

time.sleep(60)