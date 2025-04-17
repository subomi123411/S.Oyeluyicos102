x = 0
for i in range(1,6):
    if i % 2 == 0:
        x += i
        print(f"x1 is {x}")
    else:
        x -= i
        print(x)