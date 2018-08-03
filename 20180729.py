#用幂级数展开式计算e的值，要求最后一项的值小于10的-6次方
import math
n,e,a=0,0,1
while a>=1e-6:
    a=1/math.factorial(n)
    e+=a
    n+=1
print(e,a)
