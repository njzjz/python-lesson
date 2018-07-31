#计算20180730.txt的mae和rmse
import numpy as np
data=np.loadtxt("20180730.txt")
error=np.abs(data[:,0]-data[:,1])
mae=np.sum(error)/len(error)
rmse=np.sqrt(np.sum(np.square(error))/len(error))
print(mae,rmse)
