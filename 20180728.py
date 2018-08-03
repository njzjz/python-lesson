#找到100-1000之间的所有素数，每行一个存于文件primenumber.txt中
import math
def isprimenumber(n):
    i,w=2,True
    while i<=int(math.sqrt(n)):
        if n%i==0:
            w=False
            break
        else:
            i+=1
    return w

with open("primenumber.txt",'w') as f:
    for i in range(100,1001):
        if isprimenumber(i):
            print(i,file=f)
