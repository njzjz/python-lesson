x=input("Please input something:")
n=0
for i in x:
    if not i.isalpha():n=n+1
if n>0:print("All are NOT characters.")
else:print("All are characters.")
