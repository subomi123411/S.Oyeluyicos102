numbers = [7, 3, 9]
if numbers[0] < numbers[1]:
    numbers[0], numbers[1] = numbers[1], numbers[0]
if numbers[1] > numbers[2]:
    numbers[1], numbers[2] = numbers[2], numbers[1]
if numbers[0] > numbers[2]:
    numbers[0], numbers[2] = numbers[2], numbers[0]
print(numbers)  # Output: [3, 7, 9]