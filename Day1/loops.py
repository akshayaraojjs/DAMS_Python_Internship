# 1. Basic for Loop

# Iterating through a list
fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    print(fruit)

# With index using enumerate()
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# 2. Basic while Loop

# Simple while loop
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1

# While loop with user input
password = ""
while password != "secret123":
    password = input("Enter the password: ")
print("Access granted!")

# 3. Range-based for Loops

# Using range() function
print("Counting from 0 to 4:")
for i in range(5):
    print(i)

# Output: 0, 1, 2, 3, 4

print("\nCounting from 2 to 6:")
for i in range(2, 7):
    print(i)

print("\nCounting even numbers from 0 to 10:")
for i in range(0, 11, 2):
    print(i)

print("\nCounting backwards:")
for i in range(5, 0, -1):
    print(i)

# 4. Loop Control Statements

# break statement
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in numbers:
    if num > 5:
        break
    print(num)

# continue statement
for num in numbers:
    if num % 2 == 0:  # Skip even numbers
        continue
    print(num)

# pass statement (placeholder)
for num in numbers:
    if num == 5:
        pass  # Do nothing, just a placeholder
    else:
        print(num)

# else clause with loops
for num in numbers:
    if num == 10:
        break
else:
    print("10 was not found in the list")

# 5. Nested Loops

# Multiplication table
print("Multiplication Table:")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} × {j} = {i * j}", end="\t")
    print()  # New line after each row

# Pattern printing
print("\nPattern:")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()