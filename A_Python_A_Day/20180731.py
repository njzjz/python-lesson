#统计20180731.txt单词个数和出现最多的单词
from collections import Counter
with open("20180731.txt") as f:
    s="".join(f.readlines()).replace(","," ").replace("."," ").split()
    c=Counter(s).most_common(1)[0]
    print(len(s),c)
