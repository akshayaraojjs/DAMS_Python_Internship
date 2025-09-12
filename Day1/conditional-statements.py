# 1. Basic if Statement

# Simple if statement
age = 18
if age >= 18:
    print("You are an adult")

# Output: You are an adult

# 2. if-else Statement

# if-else statement
temperature = 25
if temperature > 30:
    print("It's hot outside!")
else:
    print("The weather is pleasant")

# Output: The weather is pleasant

# 3. if-elif-else Statement

# if-elif-else statement
score = 85

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"Your grade is: {grade}")
# Output: Your grade is: B

# 4. Nested if Statements

# Nested if statements
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("You can drive legally")
    else:
        print("You're old enough but need a license")
else:
    print("You're too young to drive")

# Output: You can drive legally

# 5. Conditional Expressions (Ternary Operator)

# Ternary operator
x = 10
y = 20

# Traditional way
if x > y:
    result = x
else:
    result = y

# Using ternary operator
result = x if x > y else y
print(f"The larger number is: {result}")
# Output: The larger number is: 20

# Another example
is_even = "Even" if x % 2 == 0 else "Odd"
print(f"{x} is {is_even}")
# Output: 10 is Even

# 6. Multiple Conditions with Logical Operators

# Using and, or, not operators
age = 25
income = 50000
has_good_credit = True

# AND operator
if age >= 21 and income > 30000:
    print("You qualify for the premium account")

# OR operator
if age >= 65 or income < 20000:
    print("You qualify for discounts")

# NOT operator
if not has_good_credit:
    print("Credit application denied")
else:
    print("Credit application approved")

# Combined conditions
if (age >= 18 and has_good_credit) or income > 75000:
    print("Loan approved!")

# 7. Membership Operators (in, not in)

# Using 'in' and 'not in' operators
fruits = ['apple', 'banana', 'orange']

if 'apple' in fruits:
    print("Apple is available")

if 'grape' not in fruits:
    print("Grape is not available")

# With strings
text = "Hello World"
if 'World' in text:
    print("Found 'World' in the text")