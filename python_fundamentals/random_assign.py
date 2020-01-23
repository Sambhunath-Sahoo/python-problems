import random

#num = range(1,11)

#for i in num:
#    print(i)

#num = random.randint(1,50)
#print(num)

#for i in range(1,51):
#    print(i,end = " ")
num = list(range(1,51))
print(f"total numbers are :{num}")


i = 0
group1 = []
group2 = []
group3 = []
group4 = []
group5 = []
while i<5:
    group1.append(random.randint(1,50))
    group2.append(random.randint(1,50))
    group3.append(random.randint(1,50))
    group4.append(random.randint(1,50))
    group5.append(random.randint(1,50))
    i += 1
print("\n")
print(f"group 1 num are: {group1}")
print(f"group 2 num are: {group2}")
print(f"group 3 num are: {group3}")
print(f"group 4 num are: {group4}")
print(f"group 5 num are: {group5}")