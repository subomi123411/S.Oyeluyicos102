s = "unbelievable"
part1 = s[:4]       # "unbe"
part2 = s[-3:]      # "ble"
middle = s[4:8]     # "liev"
combined = part1 + middle + part2
print("Combined:", combined)  # Output: "unbelievable"
print("Char at -1:", combined[-1])  # Output: "e"