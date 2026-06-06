# topic: User input and output in python

# Taking user input

name = input("Enter your name: ")
age = input("Enter your age: ")

print("\n--- User Information ---")
print("Name:", name)
print("Age:", age)

# Type Conversion

age = int(age)

print("\nNext year you will be:", age + 1)

# Multiple Inputs

city = input("\nEnter your city: ")
profession = input("Enter your profession: ")

print("\n--- Profile Summary ---")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
print(f"Profession: {profession}")

# Simple Calculator

num1 = float(input("\nEnter first number: "))
num2 = float(input("Enter second number: "))

print("\nResults:")
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)