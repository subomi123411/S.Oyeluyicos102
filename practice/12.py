for i in range(3):
    for j in range(5):
        if j == 2:
            break
        print(f"1st value is {i}-{j}")
    print(f"2nd value is {j}-{j}")  # Output below