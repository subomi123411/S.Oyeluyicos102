n = 50
while n > 1:
    if n % 2 == 0:
        n //= 2
    else:
        n -= 1
        print(n)