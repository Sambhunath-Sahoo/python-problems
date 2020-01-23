def reverse_list(l):
    element = []
    for i in l:
        element.append(i[::-1])
    return element

lis = ['sambhu','vishal','abhay']
print(reverse_list(lis))