#作出20180801.txt的图像
import numpy as np
import matplotlib.pyplot as plt
data=np.loadtxt("20180801.txt")
plt.plot(data[:,0],data[:,1])
plt.xlabel("Energy(eV)")
plt.ylabel("DOS")
plt.savefig("20180801.svg")
