
# 16. Positive, Negative or Zero
n = int(input("Enter number: "))
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")


# 17. Even or Odd
n = int(input("Enter number: "))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")


# 18. Largest of Two Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Largest =", a)
else:
    print("Largest =", b)


# 19. Largest of Three Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a > b and a > c:
    print("Largest =", a)
elif b > c:
    print("Largest =", b)
else:
    print("Largest =", c)


# 20. Smallest of Three Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a < b and a < c:
    print("Smallest =", a)
elif b < c:
    print("Smallest =", b)
else:
    print("Smallest =", c)


# 21. Voting Eligibility
age = int(input("Enter age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


# 22. Leap Year
year = int(input("Enter year: "))
if year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")


# 23. Vowel or Consonant
ch = input("Enter character: ")
if ch in "aeiouAEIOU":
    print("Vowel")
else:
    print("Consonant")


# 24. Divisible by 5
n = int(input("Enter number: "))
if n % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")


# 25. Simple Calculator
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter +, -, *, /: ")

if op == "+":
    print("Answer =", a + b)
elif op == "-":
    print("Answer =", a - b)
elif op == "*":
    print("Answer =", a * b)
elif op == "/":
    print("Answer =", a / b)
else:
    print("Invalid operator")

