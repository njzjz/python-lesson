#作出总能量和势能的图像
import numpy as np
import matplotlib.pyplot as plt
energies=[]
with open("20180802.txt") as f:
    for line in f:
        if "---------------- Step" in line:
            lines=[x.split() for x in (line,next(f),next(f))]
            energies.append([float(x) for x in (lines[0][2],lines[1][2],lines[2][2])])
energies=np.array(energies)
plt.plot(energies[:,0],energies[:,1],label="Total Energy (kcal/mol)")
plt.plot(energies[:,0],energies[:,2],label="Potential Energy (kcal/mol)")
plt.xlabel("Step")
plt.legend()
plt.savefig("20180802.svg")
