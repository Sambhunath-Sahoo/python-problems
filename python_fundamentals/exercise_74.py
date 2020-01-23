def greatest(x, y):
    return x if x>y else y

a = int(input("value for a is :"))
b = int(input("value for b is :"))

print(f"{greatest(a,b)} is greatest")