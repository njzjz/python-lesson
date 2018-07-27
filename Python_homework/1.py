#1.输入三角形的边长，输出其面积
import math
a,b,c=3,4,5
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("area=",area)
