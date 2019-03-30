#请输出100以内的素数，每行输出5个数据
#     2   3   5   7  11
#  13  17  19  23  29
#  31  37  41  43  47
#  53  59  61  67  71
#  73  79  83  89  97 
from math import sqrt
c=0
for i in range(2,101):
    for j in range(2,int(sqrt(i))+1):
        if i%j==0:
            break
    else:
        print(i,end=' ')
        c+=1
        if c%5==0:
            print()
