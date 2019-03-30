#©2016 ZENG Jinzhe. All rights reserved.
import random
print("欢迎进入游戏！")
input("按回车键开始游戏！")
x1=1
x2=1
print("您是玩家A，电脑为玩家B！")
n=[j for j in range(51)]
y2=0
def printmap():
    print("\n"*25)
    for i in range(1,50):
        if i==x1:
            n[i]="A"
        elif i==x2:
            n[i]="B"
        elif i==5 or i==15 or i==25 or i==35 or i==45:
            n[i]="R"
        else:
            n[i]="#"
    for i in range(1,12):
        print(n[i],end="")
    print("")
    for i in range(13,19):
        print(" "*9,n[i])
    for i in range(31,20,-1):
        print(n[i],end="")
    print("")
    for i in range(32,38):
        print(n[i])
    for i in range(39,50):
        print(n[i],end="")
    print("")
while x1<50 and x2<50:
    printmap()
    if y2!=0:
        print("玩家B掷出了点数",y2,z2)
    input("轮到你掷点，按回车键掷出点数！")
    y1=random.randint(1,6)
    x1+=y1
    if x1==5 or x1==15 or x1==25 or x1==35 or x1==45:
        r=random.randint(1,6)
        if r==1:
            x1-=4
            z1="，因为英语挂科，退4步！"
        elif r==2:
            x1-=2
            z1="，因为未写英语作业被查到，退2步！"
        elif r==3:
            x1+=3
            z1="，因为高数满分，进3步！"
        elif r==4:
            x1+=y1
            z1="，因为GPA4.3，再进"+str(y1)+"步！"
        elif r==5:
            x1=1
            z1="，因为考试作弊被发现，返回原点！"
        else:
            c=x1
            x1=x2
            x2=c
            z1="，$%^&*$##%，和玩家B互换位置！"
    else:
        z1="，前进"+str(y1)+"步。"
    if x1<50 and x2<50:
        printmap()
        print("玩家A掷出了点数",y1,z1)
        input("轮到玩家B掷点，请按回车键确认！")
        y2=random.randint(1,6)
        x2+=y2
        if x2==5 or x2==15 or x2==25 or x2==35 or x2==45:
            r=random.randint(1,6)
            if r==1:
                x2-=4
                z2="，因为英语挂科，退4步！"
            elif r==2:
                x2-=2
                z2="，因为未写英语作业被查到，退2步！"
            elif r==3:
                x2+=3
                z2="，因为高数满分，进3步！"
            elif r==4:
                x2+=y1
                z2+="，因为GPA4.3，再进"+str(y1)+"步！"
            elif r==5:
                x2=1
                z2="，因为考试作弊被发现，返回原点！"
            else:
                c=x2
                x2=x1
                x1=c
                z2="，$%^&*$##%，和玩家B互换位置！"
        else:
            z2="，前进"+str(y2)+"步。"
else:
    if x1>50:
        x1=50
        printmap()
        print("玩家A掷出了点数",y1,z1,"\n玩家A获得胜利！")
    else:
        x2=50
        printmap()
        print("玩家A掷出了点数",y2,z2,"\n玩家A获得胜利！")
    input("游戏结束。")
