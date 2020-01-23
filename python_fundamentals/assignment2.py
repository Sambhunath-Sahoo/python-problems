


num = input("input a number :")
even_sum = 0
odd_sum = 0
i = 0
while i <= len(num)-1:
    if (int(num[i])%2 != 0):
        odd_sum += int(num[i])
   
    i += 1
        
print(odd_sum)
