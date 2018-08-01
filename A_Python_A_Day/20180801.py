#作出20180801.txt的图像
import numpy as np
import matplotlib.pyplot as pl
data=np.loadtxt("20180801.txt")
pl.plot(data[:,0],data[:,1])
pl.xlabel("Energy(eV)")
pl.ylabel("DOS")
pl.savefig("20180801.svg")
