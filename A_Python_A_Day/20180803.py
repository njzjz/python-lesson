#读取20180803.txt结构并计算库仑矩阵
import numpy as np
nuclearcharge={"H":1,"He":2,"Li":3,"Be":4,"B":5,"C":6,"N":7,"O":8,"F":9,"Ne":10}
element,x,y,z=np.loadtxt("20180803.txt",skiprows=2,dtype="a2,f,f,f",unpack=True)
crd=np.array([x,y,z]).T
element=element.astype(str)
m=np.array([[nuclearcharge[element[i]]**2.4/2 if i==j else nuclearcharge[element[i]]*nuclearcharge[element[j]]/np.linalg.norm(crd[i]-crd[j]) for j in range(len(crd))] for i in range(len(crd))])
np.savetxt("20180803_m.txt",m)
