print("Hello World!")
# 1. Print Hello World
print("Hello World")

# 2. Add two numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Addition =", a + b)

# 3. Subtract two numbers
print("Subtraction =", a - b)

# 4. Multiply two numbers
print("Multiplication =", a * b)

# 5. Divide two numbers
print("Division =", a / b)

# 6. Find remainder using %
print("Remainder =", a % b)

# 7. Find square of a number
n = float(input("Enter a number: "))
print("Square =", n ** 2)

# 8. Find cube of a number
print("Cube =", n ** 3)

# 9. Calculate area of a circle
r = float(input("Enter radius: "))
print("Area of circle =", 3.14 * r * r)

# 10. Calculate simple interest
p = float(input("Enter principal: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time: "))
print("Simple Interest =", (p * rate * time) / 100)

# 11. Convert Celsius to Fahrenheit
c = float(input("Enter Celsius: "))
print("Fahrenheit =", (c * 9/5) + 32)

# 12. Swap two numbers
x = input("Enter first value: ")
y = input("Enter second value: ")
x, y = y, x
print("After swap:", x, y)

# 13. Find average of three numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
print("Average =", (a + b + c) / 3)

# 14. Calculate total and percentage of marks
m1 = float(input("Enter marks 1: "))
m2 = float(input("Enter marks 2: "))
m3 = float(input("Enter marks 3: "))
total = m1 + m2 + m3
print("Total =", total)
print("Percentage =", total / 3)

# 15. Convert days into years, months, and days
days = int(input("Enter days: "))
years = days // 365
months = (days % 365) // 30
remaining_days = (days % 365) % 30
print("Years =", years)
print("Months =", months)
print("Days =", remaining_days)
