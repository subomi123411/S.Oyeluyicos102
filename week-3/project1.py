# Get user input
name1 = input("Enter the first name: ")
age1 = int(input("Enter the first age: "))

name2 = input("Enter the second name: ")
age2 = int(input("Enter the second age: "))

# Swap the ages
age1, age2 = age2, age1

print("\nAfter swapping:")
print(f"{name1}'s age is now {age1} years old")
print(f"{name2}'s age is now {age2} years old")