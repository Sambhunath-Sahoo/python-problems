#list_ methode with range
number = list(range(1,11))
#print(num)

#pop methode
#poped_item = num.pop()
#print(poped_item)
#print(num)

#index mehode
#print(num.index(2,1,5))

def negative_list(number):
    negative = []
    for i in number:
        negative.append(-i)
        return negative

print(negative_list(number))
print(negative)