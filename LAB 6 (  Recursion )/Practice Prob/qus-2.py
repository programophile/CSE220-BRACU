def bunnyEars(n):
    if n==0:
        return 0
    elif n%2==0:
        return 3+ bunnyEars(n-1)
    elif n%2!=0:
        return 2+bunnyEars(n-1)
print(bunnyEars(2))