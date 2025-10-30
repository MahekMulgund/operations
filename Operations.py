# Program to perform addition, subtraction, multiplication, and division of two numbers
# Taking input from the user
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))

# Performing operations
sum_result = n1 + n2
diff_result = n1 - n2
prod_result = n1 * n2

# Handling division by zero
if n2 != 0:
    div_result = n1 / n2
else:
    div_result = "Undefined (division by zero is not allowed)"

# Displaying the results
print("\nResults:")
print(f"Addition: {n1} + {n2} = {sum_result}")
print(f"Subtraction: {n1} - {n2} = {diff_result}")
print(f"Multiplication: {n1} * {n2} = {prod_result}")
print(f"Division: {n1} / {n2} = {div_result}")
