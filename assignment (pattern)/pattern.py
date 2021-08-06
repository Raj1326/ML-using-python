print("1\n")
for i in range(1,6):
    print("*" *i)
print("2\n")
for i in range(6):
    print("*"*(5-i))
print("3\n")
for i in range(1,6):
    print(" " * (5-i) + "*" *i)
print("4\n")
for i in range(6):
    print( " " *i + "*" * (5-i) )
print("5\n")
for i in range(1,10):
    if(i<6):
        print(" " * (5-i) + "*" *i)
    else:
        print( " " *(i-5) + "*" * (5-(i-5)))
print("6\n")
for i in range(1,6):
    print(" " * (5-i) + "*" *i + "*" *(i-1))
print("6 Alternate\n")
j = 6
num = 6
for i in range(0, num + 1):
    print('{}{}'.format(' ' * j, ' *' * i))
    j -= 1
print("7\n")
for i in range(1,10):
    if(i<6):
        print(" " * (5-i) + "*" *i + "*" *(i-1) + " " * (5-i) )
    else:
        print( " " *(i-5) + "*" * (5-(i-5)) + "*" * (5-(i-5)-1))
print("8\n")
for i in range(1,10):
    if i==1 or i==9:
        print("*"*9)
    elif(i<5):
        print("*" * (5-i) + " " *i + " " *(i-1) + "*" * (5-i))
    else:
        print("*" *(i-4) + " " * (5-(i-5)-1) + " " * (5-(i-5)-2) +"*" *(i-4))

print("8 corrected\n")
for i in range(1,10):
    if i==1 or i==9:
        print("*"*9)
    elif i>1 and i<6:
        print("*" * (6-i) + " " *(2*i-3) + "*" * (6-i))
    else:
        print("*" *(i-4) + " " * (17-2*i) +"*" *(i-4))
        
print("9\n")
k=0
for i in range(1,6):
    print(" " * (6-i-1),end ="")
    k =(k*10)+i
    print(k)
    
print("10\n")
k="1"
for i in range(1,6):
    print(" " * (6-i-1),end ="")
    if(i!=1):
        print(k+ str(i) + k[::-1])
        k = k+ str(i)
    else:
        print(k)
print("11\n")
k="1"
for i in range(1,6):
    print(" " * (6-i-1),end ="")
    if(i!=1):
        print( str(i) +k + str(i))
        k = str(i) +k + str(i)
    else:
        print(k)
    