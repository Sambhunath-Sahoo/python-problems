def list_counter(l):
    count = 0
    for i in l:
        if type(i) == list:
            count += 1
    return count

lis = [[12],3,5,6,7,[3],4,[3]]
print(list_counter(lis))