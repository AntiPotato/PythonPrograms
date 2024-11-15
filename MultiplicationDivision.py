print("This is a program to show the multiplication and division of two numbers.")

first_num = int(input("Enter the first number:"))
second_num = int(input("Enter the second number:"))

print("You entered", first_num, "as the first number and", second_num, "as the second number")
print("Multiplication of the two numbers, i.e.,",first_num, "*", second_num, "is", first_num * second_num)
if(second_num != 0):
	print("Division of the two numbers, i.e.,", first_num, "/", second_num, "is", first_num / second_num)
else:
	print("Division is undefined when the second number is 0")

