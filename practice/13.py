nums = [5, 12, 7, 3, 14, 9]
even_sum = 0
for n in nums:
    if n % 2 != 0:
        continue
    even_sum += n
print("Even sum:", even_sum)  # Output: 26 (12 + 14)