name = input("enter your name :")
i = 0
repeated_var = " "
 
while i<= len(name)-1:
    if name[i] not in repeated_var:
        repeated_var += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i += 1
    