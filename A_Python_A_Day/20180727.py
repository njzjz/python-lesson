#计算1-100之间的所有奇数和、偶数和、总计和
sum_odd = 0
sum_even = 0
sum_all = 0
for i in range(1,101):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i
sum_all = sum_odd + sum_even
print("奇数和为：", sum_odd)
print("偶数和为：", sum_even)
print("总计和为：", sum_all)
