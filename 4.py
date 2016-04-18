from math import *
c=0
for i in range(2,101):
    for j in range(2,int(sqrt(i)+1)):
        if i%j==0:break
    else:
        print(i,end=' ')
        c+=1
        if c%5==0:print()
