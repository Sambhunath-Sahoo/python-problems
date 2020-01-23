def big(a, b, c):
    bigger = big(a, b)
    return big(bigger,c)

print(big(34,5,6))