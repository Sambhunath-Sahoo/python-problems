def reverse_list(l):
    element = []
    for i in range(1,len(l)):
        element.append(i**2)
    return element

lis = [1,2,3,4,5]
print(reverse_list(lis))