 # Get input
expression = (input("Expression: "))
#turn into variables
x, y, z = expression.split(" ")
# change variables to float
new_x = float(x)
new_z = float(z)
# Get result
if y == "+":
    result = new_x + new_z
if y == "-":
    result = new_x - new_z
if y == "*":
    result = new_x * new_z
if y == "/":
    result = new_x / new_z

print(round(result, 2))