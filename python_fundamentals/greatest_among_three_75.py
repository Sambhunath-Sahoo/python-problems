def greatest(a, b, c):
    if a>b and b>c:
        return a
    elif b>c:
        return b
    else:
        return c

print(greatest(4,56,5))            
    