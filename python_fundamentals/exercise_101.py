def even_odd(l):
    odd = []
    even = []
    for i in l:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)

    print(even)
    print(odd)

      
nums = [1,2,3,4,5,6,7,8,9]

print(even_odd(nums))